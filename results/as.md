| Algorithm                                      |   Precision |   Recall |   F1-measure |
|:-----------------------------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM                        |       0.636 |    0.66  |        0.648 |
| MicroTokenizer_with_DAG                        |       0.46  |    0.625 |        0.53  |
| tokenizer_MicroTokenizer_with_join_model       |       0.681 |    0.685 |        0.683 |
| tokenizer_MicroTokenizer_with_CRF              |       0.732 |    0.74  |        0.736 |
| tokenizer_MicroTokenizer_with_custom_model     |       0.884 |    0.844 |        0.864 |
| tokenizer_MicroTokenizer_with_custom_CRF_model |       0.934 |    0.943 |        0.938 |
| jieba                                          |       0.74  |    0.737 |        0.738 |
| thulac                                         |       0.732 |    0.745 |        0.738 |
| nlpir                                          |       0.485 |    0.651 |        0.556 |
| ltp                                            |       0.794 |    0.809 |        0.801 |