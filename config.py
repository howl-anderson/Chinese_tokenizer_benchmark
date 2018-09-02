from tokenizers_collection.config import tokenizer_registry as collection_tokenizer_registry


from tokenizers import (
    tokenizer_MicroTokenizer_with_HMM,
    tokenizer_MicroTokenizer_with_DAG,
    tokenizer_MicroTokenizer_with_joint_model,
    tokenizer_MicroTokenizer_with_CRF,
    tokenizer_MicroTokenizer_with_custom_join_model,
    tokenizer_MicroTokenizer_with_custom_CRF_model,
)


def make_func_accept_corpus_kwarg(func):
    def decorator(*args, **kwargs):
        kwargs.pop('corpus', None)
        return func(*args, **kwargs)

    return decorator


tokenizer_registry = {
    k: make_func_accept_corpus_kwarg(v)
    for k, v in collection_tokenizer_registry.items()
}


tokenizer_registry.update(
    {
        'MicroTokenizer_with_HMM': tokenizer_MicroTokenizer_with_HMM,
        'MicroTokenizer_with_DAG': tokenizer_MicroTokenizer_with_DAG,
        'MicroTokenizer_with_joint_model': tokenizer_MicroTokenizer_with_joint_model,
        'MicroTokenizer_with_CRF': tokenizer_MicroTokenizer_with_CRF,
        'MicroTokenizer_with_custom_join_model': tokenizer_MicroTokenizer_with_custom_join_model,
        'MicroTokenizer_with_custom_CRF_model': tokenizer_MicroTokenizer_with_custom_CRF_model,
    }
)

# TODO: likely to be over-design
corpus_registry = {
    "MSR": 'msr',
    "AS": 'as',
    "PKU": 'pku',
    "CityU": "cityu"
}