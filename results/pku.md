| Algorithm                                      |   Precision |   Recall |   F1-measure |
|:-----------------------------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM                        |       0.742 |    0.774 |        0.758 |
| MicroTokenizer_with_DAG                        |       0.806 |    0.785 |        0.795 |
| tokenizer_MicroTokenizer_with_join_model       |       0.82  |    0.754 |        0.786 |
| tokenizer_MicroTokenizer_with_CRF              |       0.909 |    0.909 |        0.909 |
| tokenizer_MicroTokenizer_with_custom_model     |       0.89  |    0.833 |        0.861 |
| tokenizer_MicroTokenizer_with_custom_CRF_model |       0.925 |    0.906 |        0.915 |
| jieba                                          |       0.853 |    0.787 |        0.818 |
| thulac                                         |       0.922 |    0.923 |        0.923 |
| nlpir                                          |       0.94  |    0.944 |        0.942 |
| ltp                                            |       0.96  |    0.946 |        0.953 |