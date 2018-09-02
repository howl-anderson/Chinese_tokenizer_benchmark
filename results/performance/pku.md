| Algorithm                                   | Precision   | Recall    | F1-measure   |
|:--------------------------------------------|:------------|:----------|:-------------|
| jieba                                       | 0.853       | 0.787     | 0.818        |
| thulac                                      | 0.922       | 0.923     | 0.923        |
| nlpir                                       | 0.940       | 0.943     | 0.941        |
| ltp                                         | **0.960**   | **0.946** | **0.953**    |
| MicroTokenizer_with_HMM                     | 0.742       | 0.732     | 0.737        |
| MicroTokenizer_with_DAG                     | 0.884       | 0.911     | 0.897        |
| MicroTokenizer_with_joint_model             | 0.867       | 0.808     | 0.837        |
| MicroTokenizer_with_CRF                     | 0.852       | 0.791     | 0.821        |
| MicroTokenizer_with_custom_joint_model      | 0.890       | 0.833     | 0.861        |
| MicroTokenizer_with_custom_CRF_model        | 0.852       | 0.791     | 0.821        |
| MicroTokenizer_with_max_match_forward       | 0.882       | 0.910     | 0.896        |
| MicroTokenizer_with_max_match_backward      | 0.882       | 0.910     | 0.896        |
| MicroTokenizer_with_max_match_bidirectional | 0.883       | 0.910     | 0.896        |