import os

import MicroTokenizer
from MicroTokenizer.tokenizer import Tokenizer
import jieba
import thulac
import pynlpir
from pyltp import Segmentor

pynlpir.open()

current_dir_path = os.path.dirname(os.path.abspath(__file__))

segmentor = Segmentor()
segmentor.load(os.path.join(current_dir_path, "data/ltp_data_v3.4.0/cws.model"))


def tokenizer_jieba(input_file, output_file, delim="  ", corpus=None):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()
            result = delim.join(jieba.cut(line, cut_all=False, HMM=True))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


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


def tokenizer_MicroTokenizer_with_join_model(input_file, output_file, delim="  ", corpus=None):
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


def tokenizer_MicroTokenizer_with_custom_model(input_file, output_file, delim="  ", corpus=None):
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


def tokenizer_thulac(input_file, output_file, delim=" ", corpus=None):
    thu1 = thulac.thulac(seg_only=True)   # 只进行分词，不进行词性标注
    thu1.cut_f(input_file, output_file)   # 对input.txt文件内容进行分词，输出到output.txt


def tokenizer_nlpir(input_file, output_file, delim=" ", corpus=None):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()
            result = delim.join(pynlpir.segment(line, pos_tagging=False))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)


def tokenizer_ltp(input_file, output_file, delim=" ", corpus=None):
    with open(input_file, 'r') as fp, open(output_file, 'w') as output_fd:
        output_lines = []
        for raw_line in fp:
            line = raw_line.strip()
            result = delim.join(segmentor.segment(line))

            result_with_new_line = result + "\n"

            output_lines.append(result_with_new_line)

        output_fd.writelines(output_lines)