import os
import subprocess

current_dir_path = os.path.dirname(os.path.abspath(__file__))


def do_evaluate(corpus, tokenizer_name):
    evaluate_cmd = os.path.join(current_dir_path, "data/icwb2-data/scripts/score")
    training_file = os.path.join(current_dir_path, "data/icwb2-data/testing/{}_test.utf8".format(corpus))

    gold_file = os.path.join(current_dir_path, "data/icwb2-data/gold/{}_test_gold.utf8".format(corpus))
    alternative_gold_file = os.path.join(current_dir_path, "data/icwb2-data/gold/{}_testing_gold.utf8".format(corpus))
    if not os.path.exists(gold_file):  # for fix some gold corpus such as AS uising testing in file name instead of test
        gold_file = alternative_gold_file

    test_file = os.path.join(current_dir_path, "workspace/{}-{}.txt".format(corpus, tokenizer_name))
    score_file = os.path.join(current_dir_path, "score/{}-{}.txt".format(corpus, tokenizer_name))

    command = ['perl', evaluate_cmd, training_file, gold_file, test_file, '>', score_file]
    command_string = " ".join(command)
    subprocess.run(command_string, shell=True)

    return score_file


if __name__ == "__main__":
    do_evaluate('msr', 'jieba')