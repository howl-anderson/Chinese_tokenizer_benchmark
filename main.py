import os

import jieba
import MicroTokenizer


def tokenizor_jieba(input_file, output_file, delim="  "):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()
            result = delim.join(jieba.cut(line, cut_all=False, HMM=True))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizor_MicroTokenizer_with_HMM(input_file, output_file, delim="  "):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()
            result = delim.join(MicroTokenizer.cut_by_HMM(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def get_input_data_file(corpus="msr"):
    if corpus == "msr":
        corpus_file = "msr_test.utf8"
    if corpus == "xx":
        pass
    # TOOD: more if is here

    return os.path.join(current_dir_path, "utils/icwb2-data/testing/{}".format(corpus_file))


def get_output_data_file(corpus="msr", tokenizor_name=""):
    return os.path.join(current_dir_path, "workspace/{}_{}.txt".format(corpus, tokenizor_name))


if __name__ == "__main__":
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir_path, "utils/icwb2-data/testing/msr_test.utf8")
    output_file = os.path.join(current_dir_path, "workspace/msr_microtokenizer.txt")

    tokenizor_MicroTokenizer_with_HMM(input_file, output_file)