#!/bin/env python
# -*- coding: utf-8 -*-


def parse_score(score_file):
    with open(score_file, 'r') as fd:
        lines = fd.readlines()
        raw_last_line = lines[-1]

        last_line = raw_last_line.strip()

        raw_metrics = last_line.split()

        metrics = {
            "RECALL": raw_metrics[8],
            "PRECISION": raw_metrics[9],
            "F1-MEASURE": raw_metrics[10]
        }

    return metrics


if __name__ == "__main__":
    score = parse_score("score_microtokenizer.ut8")
    print(score)

