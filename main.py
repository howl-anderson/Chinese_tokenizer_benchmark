#!/usr/bin/env python

import os
from collections import defaultdict

from tabulate import tabulate
from joblib import Parallel, delayed

from config import tokenizer_registry, corpus_registry
from evaluate import do_evaluate
from score import parse_score

current_dir_path = os.path.dirname(os.path.abspath(__file__))


def get_train_data_file(corpus_name="msr"):
    # corpus_name = corpus_registry[corpus]

    corpus_file = "{}_training.utf8".format(corpus_name)

    return os.path.join(current_dir_path, "data/icwb2-data/training/{}".format(corpus_file))


def get_input_data_file(corpus_name="msr"):
    # corpus_name = corpus_registry[corpus]

    corpus_file = "{}_test.utf8".format(corpus_name)

    return os.path.join(current_dir_path, "data/icwb2-data/testing/{}".format(corpus_file))


def get_output_data_file(corpus_name="msr", tokenizor_name=""):
    # corpus_name = corpus_registry[corpus]

    return os.path.join(current_dir_path, "workspace/{}-{}.txt".format(corpus_name, tokenizor_name))


def get_token_file(corpus_type, tokenizer_name):
    input_file = get_input_data_file(corpus_type)
    output_file = get_output_data_file(corpus_type, tokenizer_name)

    tokenizer = tokenizer_registry[tokenizer_name]

    tokenizer(input_file, output_file, corpus=corpus_type)

    return output_file


def test_tokenizer_on_corpus(corpus, tokenizer):
    print("working on {}+{}".format(corpus, tokenizer))
    get_token_file(corpus, tokenizer)

    score_file = do_evaluate(corpus, tokenizer)

    score = parse_score(score_file)

    print("{} on {}: {}".format(tokenizer, corpus, score))

    return corpus, tokenizer, score['PRECISION'], score['RECALL'], score['F1-MEASURE']


if __name__ == "__main__":
    all_corpus_list = corpus_registry.values()
    all_tokenizer_list = tokenizer_registry.keys()

    table_header = ["Algorithm", "Precision", "Recall", "F1-measure"]

    raw_table = Parallel(n_jobs=-1)(
        delayed(test_tokenizer_on_corpus)(corpus, tokenizer)
        for tokenizer in all_tokenizer_list
        for corpus in all_corpus_list
    )

    # re group result
    all_table = defaultdict(list)
    for (corpus, *item) in raw_table:
        all_table[corpus].append(item)

    for corpus, table in all_table.items():
        table_content_string = tabulate(table, headers=table_header, tablefmt="pipe")

        result_file = os.path.join(current_dir_path, 'results', '{}.md'.format(corpus))

        with open(result_file, 'w') as fd:
            fd.write(table_content_string)
