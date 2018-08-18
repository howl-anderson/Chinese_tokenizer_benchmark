from tokenizers import (
    tokenizer_MicroTokenizer_with_HMM,
    tokenizer_MicroTokenizer_with_DAG,
    tokenizer_MicroTokenizer_with_join_model,
    tokenizer_MicroTokenizer_with_CRF,
    tokenizer_MicroTokenizer_with_custom_model,
    tokenizer_MicroTokenizer_with_custom_CRF_model,
    tokenizer_jieba,
    tokenizer_thulac,
    tokenizer_nlpir,
    tokenizer_ltp
)

tokenizer_registry = {
    'MicroTokenizer_with_HMM': tokenizer_MicroTokenizer_with_HMM,
    'MicroTokenizer_with_DAG': tokenizer_MicroTokenizer_with_DAG,
    'tokenizer_MicroTokenizer_with_join_model': tokenizer_MicroTokenizer_with_join_model,
    'tokenizer_MicroTokenizer_with_CRF': tokenizer_MicroTokenizer_with_CRF,
    'tokenizer_MicroTokenizer_with_custom_model': tokenizer_MicroTokenizer_with_custom_model,
    'tokenizer_MicroTokenizer_with_custom_CRF_model': tokenizer_MicroTokenizer_with_custom_CRF_model,
    'jieba': tokenizer_jieba,
    'thulac': tokenizer_thulac,
    'nlpir': tokenizer_nlpir,
    'ltp': tokenizer_ltp
}

# TODO: likely to be over-design
corpus_registry = {
    "MSR": 'msr',
    "AS": 'as',
    "PKU": 'pku',
    "CityU": "cityu"
}