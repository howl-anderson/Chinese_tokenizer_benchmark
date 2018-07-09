import os

from tabulate import tabulate

from tokenizers import tokenizer_jieba, tokenizer_MicroTokenizer_with_HMM, tokenizer_thulac, tokenizer_nlpir, tokenizer_ltp
from evaluate import do_evaluate
from score import parse_score

current_dir_path = os.path.dirname(os.path.abspath(__file__))

tokenizer_registry = {
    'MicroTokenizer_with_HMM': tokenizer_MicroTokenizer_with_HMM,
    'jieba': tokenizer_jieba,
    'thulac': tokenizer_thulac,
    'nlpir': tokenizer_nlpir,
    'ltp': tokenizer_ltp
}

# TODO: likely to be over-design
corpus_registry = {
    "MSR": 'msr',
    "AS": 'as',
    "PKU": 'pku',
    "CityU": "cityu"
}


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

    tokenizer(input_file, output_file)

    return output_file


if __name__ == "__main__":
    all_corpus_list = corpus_registry.values()
    all_tokenizer_list = tokenizer_registry.keys()

    table_header = ["Algorithm", "Precision", "Recall", "F1-measure"]

    for corpus in all_corpus_list:
        table = []
        for tokenizer in all_tokenizer_list:
            print("working on {}+{}".format(corpus, tokenizer))
            get_token_file(corpus, tokenizer)

            score_file = do_evaluate(corpus, tokenizer)

            score = parse_score(score_file)

            print(score)

            table.append(
                [tokenizer, score['PRECISION'], score['RECALL'], score['F1-MEASURE']]
            )

        table_content_string = tabulate(table, headers=table_header, tablefmt="pipe")

        result_file = os.path.join(current_dir_path, 'results', '{}.md'.format(corpus))

        with open(result_file, 'w') as fd:
            fd.write(table_content_string)
