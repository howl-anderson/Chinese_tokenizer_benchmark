| Algorithm                            | Precision   | Recall    | F1-measure   |
|:-------------------------------------|:------------|:----------|:-------------|
| jieba                                | 0.748       | 0.735     | 0.742        |
| thulac                               | 0.730       | 0.745     | 0.738        |
| nlpir                                | 0.452       | 0.620     | 0.523        |
| ltp                                  | 0.783       | 0.801     | 0.792        |
| MicroTokenizer_with_HMM              | 0.593       | 0.577     | 0.585        |
| MicroTokenizer_with_DAG              | 0.422       | 0.604     | 0.497        |
| MicroTokenizer_with_join_model       | 0.628       | 0.602     | 0.615        |
| MicroTokenizer_with_CRF              | 0.721       | 0.732     | 0.726        |
| MicroTokenizer_with_custom_model     | **0.870**   | **0.835** | **0.852**    |
| MicroTokenizer_with_custom_CRF_model | 0.721       | 0.732     | 0.726        |