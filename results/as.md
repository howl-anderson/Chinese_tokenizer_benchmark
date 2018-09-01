| Algorithm                            | Precision   | Recall    | F1-measure   |
|:-------------------------------------|:------------|:----------|:-------------|
| jieba                                | 0.740       | 0.737     | 0.738        |
| thulac                               | 0.732       | 0.745     | 0.738        |
| nlpir                                | 0.485       | 0.651     | 0.556        |
| ltp                                  | 0.794       | 0.809     | 0.801        |
| MicroTokenizer_with_HMM              | 0.639       | 0.632     | 0.635        |
| MicroTokenizer_with_DAG              | 0.448       | 0.633     | 0.524        |
| MicroTokenizer_with_join_model       | 0.670       | 0.654     | 0.662        |
| MicroTokenizer_with_CRF              | 0.732       | 0.740     | 0.736        |
| MicroTokenizer_with_custom_model     | **0.884**   | **0.844** | **0.864**    |
| MicroTokenizer_with_custom_CRF_model | 0.732       | 0.740     | 0.736        |