import os

import MicroTokenizer
from MicroTokenizer.tokenizer import Tokenizer


def tokenizer_MicroTokenizer_with_HMM(input_file, output_file, delim="  ", corpus=None):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(MicroTokenizer.cut_by_HMM(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_MicroTokenizer_with_DAG(input_file, output_file, delim="  ", corpus=None):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(MicroTokenizer.cut_by_DAG(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_MicroTokenizer_with_joint_model(input_file, output_file, delim="  ", corpus=None):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(MicroTokenizer.cut_by_joint_model(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_MicroTokenizer_with_CRF(input_file, output_file, delim="  ", corpus=None):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(MicroTokenizer.cut_by_CRF(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_MicroTokenizer_with_custom_joint_model(input_file, output_file, delim="  ", corpus=None):
    output_dir = os.path.join("MicroTokenizer_model", corpus)

    tokenizer = Tokenizer(output_dir)

    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(tokenizer.cut_by_joint_model(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_MicroTokenizer_with_custom_CRF_model(input_file, output_file, delim="  ", corpus=None):
    output_dir = os.path.join("MicroTokenizer_model", corpus)

    tokenizer = Tokenizer(output_dir)

    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(tokenizer.cut_by_CRF(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_MicroTokenizer_with_max_match_forward(input_file, output_file, delim="  ", corpus=None):
    output_dir = os.path.join("MicroTokenizer_model", corpus)

    tokenizer = Tokenizer(output_dir)

    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(tokenizer.cut_by_max_match_forward(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_MicroTokenizer_with_max_match_backward(input_file, output_file, delim="  ", corpus=None):
    output_dir = os.path.join("MicroTokenizer_model", corpus)

    tokenizer = Tokenizer(output_dir)

    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(tokenizer.cut_by_max_match_backward(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_MicroTokenizer_with_max_match_bidirectional(input_file, output_file, delim="  ", corpus=None):
    output_dir = os.path.join("MicroTokenizer_model", corpus)

    tokenizer = Tokenizer(output_dir)

    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()

            if not line:
                # empty line get empty result
                result = ""
            else:
                result = delim.join(tokenizer.cut_by_max_match_bidirectional(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)