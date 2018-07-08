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
            result = delim.join(jieba.cut(line, cut_all=False, HMM=True))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


if __name__ == "__main__":
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir_path, "utils/icwb2-data/testing/msr_test.utf8")
    output_file = os.path.join(current_dir_path, "workspace/msr_jieba.txt")

    tokenizor_jieba(input_file, output_file)