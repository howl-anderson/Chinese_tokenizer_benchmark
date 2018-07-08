#!/usr/bin/env bash

perl utils/icwb2-data/scripts/score utils/icwb2-data/gold/msr_training_words.utf8 \
    utils/icwb2-data/gold/msr_test_gold.utf8 workspace/msr_jieba.txt > score_jieba.ut8