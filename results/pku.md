| Algorithm                            | Precision   | Recall    | F1-measure   |
|:-------------------------------------|:------------|:----------|:-------------|
| jieba                                | 0.853       | 0.787     | 0.818        |
| thulac                               | 0.922       | 0.923     | 0.923        |
| nlpir                                | 0.940       | 0.943     | 0.941        |
| ltp                                  | **0.960**   | **0.946** | **0.953**    |
| MicroTokenizer_with_HMM              | 0.742       | 0.732     | 0.737        |
| MicroTokenizer_with_DAG              | 0.884       | 0.911     | 0.897        |
| MicroTokenizer_with_join_model       | 0.867       | 0.808     | 0.837        |
| MicroTokenizer_with_CRF              | 0.909       | 0.909     | 0.909        |
| MicroTokenizer_with_custom_model     | 0.890       | 0.833     | 0.861        |
| MicroTokenizer_with_custom_CRF_model | 0.909       | 0.909     | 0.909        |