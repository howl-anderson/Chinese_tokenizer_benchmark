#!/usr/bin/env bash

pynlpir update  # download the latest license

wget -c http://ospm9rsnd.bkt.clouddn.com/model/ltp_data_v3.4.0.zip -O ./data/raw_data/ltp_data_v3.4.0.zip
unzip ./data/raw_data/ltp_data_v3.4.0.zip -d ./data
