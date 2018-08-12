#!/usr/bin/env python

import os

from MicroTokenizer.train.train import train
from main import get_train_data_file
from config import corpus_registry

for corpus in corpus_registry.values():
    input_file_list = [get_train_data_file(corpus)]
    output_dir = os.path.join("MicroTokenizer_model", corpus)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    train(input_file_list, output_dir)
