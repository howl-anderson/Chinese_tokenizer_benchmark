| Algorithm                            | Precision   | Recall    | F1-measure   |
|:-------------------------------------|:------------|:----------|:-------------|
| jieba                                | 0.817       | 0.812     | 0.815        |
| thulac                               | 0.834       | 0.878     | 0.856        |
| nlpir                                | 0.869       | **0.914** | **0.891**    |
| ltp                                  | 0.868       | 0.899     | 0.883        |
| MicroTokenizer_with_HMM              | 0.694       | 0.734     | 0.713        |
| MicroTokenizer_with_DAG              | 0.802       | 0.892     | 0.845        |
| MicroTokenizer_with_join_model       | 0.811       | 0.813     | 0.812        |
| MicroTokenizer_with_CRF              | 0.828       | 0.868     | 0.847        |
| MicroTokenizer_with_custom_model     | **0.904**   | 0.870     | 0.886        |
| MicroTokenizer_with_custom_CRF_model | 0.828       | 0.868     | 0.847        |