| Algorithm                            | Precision   | Recall    | F1-measure   |
|:-------------------------------------|:------------|:----------|:-------------|
| jieba                                | 0.740       | 0.737     | 0.738        |
| thulac                               | 0.732       | 0.745     | 0.738        |
| nlpir                                | 0.485       | 0.651     | 0.556        |
| ltp                                  | 0.794       | 0.809     | 0.801        |
| MicroTokenizer_with_HMM              | 0.636       | 0.660     | 0.648        |
| MicroTokenizer_with_DAG              | 0.460       | 0.625     | 0.530        |
| MicroTokenizer_with_join_model       | 0.681       | 0.685     | 0.683        |
| MicroTokenizer_with_CRF              | 0.732       | 0.740     | 0.736        |
| MicroTokenizer_with_custom_model     | **0.884**   | **0.844** | **0.864**    |
| MicroTokenizer_with_custom_CRF_model | 0.732       | 0.740     | 0.736        |