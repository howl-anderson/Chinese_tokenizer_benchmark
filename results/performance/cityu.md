| Algorithm                                   | Precision   | Recall    | F1-measure   |
|:--------------------------------------------|:------------|:----------|:-------------|
| jieba                                       | 0.748       | 0.735     | 0.742        |
| thulac                                      | 0.730       | 0.745     | 0.738        |
| nlpir                                       | 0.452       | 0.620     | 0.523        |
| ltp                                         | 0.783       | 0.801     | 0.792        |
| MicroTokenizer_with_HMM                     | 0.592       | 0.576     | 0.584        |
| MicroTokenizer_with_DAG                     | 0.422       | 0.604     | 0.497        |
| MicroTokenizer_with_joint_model             | 0.627       | 0.601     | 0.614        |
| MicroTokenizer_with_CRF                     | 0.654       | 0.602     | 0.627        |
| MicroTokenizer_with_custom_joint_model      | **0.870**   | **0.835** | **0.852**    |
| MicroTokenizer_with_custom_CRF_model        | 0.654       | 0.602     | 0.627        |
| MicroTokenizer_with_max_match_forward       | 0.421       | 0.603     | 0.496        |
| MicroTokenizer_with_max_match_backward      | 0.422       | 0.604     | 0.497        |
| MicroTokenizer_with_max_match_bidirectional | 0.421       | 0.603     | 0.496        |