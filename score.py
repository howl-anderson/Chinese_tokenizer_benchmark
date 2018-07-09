#!/bin/env python
# -*- coding: utf-8 -*-


def parse_score(score_file):
    with open(score_file, 'r') as fd:
        lines = fd.readlines()
        last_line = lines[-1]
        print(last_line)
