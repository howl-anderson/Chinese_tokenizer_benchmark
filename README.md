# 中文分词软件基准测试

## 评测目标
本项目只测试各个常见分词软件在分词效果上的表现，着重比较各个分词方法和理论的实际效果，分词工具的速度等因素不在考虑范围内。

## 分词软件
本文选择了4个相对常见的分词工具，分别是：哈工大 `LTP`、中科院计算所 `NLPIR`、清华大学 `THULAC`, `jieba` 和本人自己开发的 `MicroTokenizer`。

1. LTP @ https://github.com/HIT-SCIR/pyltp
2. NLPIR @ https://github.com/tsroten/pynlpir
3. THULAC @ https://github.com/thunlp/THULAC-Python
4. jieba @ https://github.com/fxsjy/jieba
5. MicroTokenizer @ https://github.com/howl-anderson/MicroTokenizer

## 测试数据集
SIGHAN Bakeoff 2005 的 `MSR`、`PKU`、`AS` and `CityU` at http://sighan.cs.uchicago.edu/bakeoff2005/

本数据集是 `ACL SIGHAN` 于 2005 年组织的中文分词比赛所用的数据集，也是学术界测试分词工具的标准数据集。

## 测试方法
用 SIGHAN Bakeoff 2005 比赛中所自带的 score 脚本、test gold 数据和 training words 数据 5 个工具进行准确性测试，具体使用方法可参考：http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip 中的readme文件。

## 测试过程
### 安装依赖
```bash
pip install -r ./requirements.txt
```

如果 Mac OS 下安装 `pyltp` 出现 `MACOSX_DEPLOYMENT_TARGET` 相关的问题，请参考 [pyltp 安装](https://github.com/HIT-SCIR/pyltp#%E5%AE%89%E8%A3%85) 和 `install_pyltp_under_macos.bash`


### 下载许可证和模型文件
```bash
bash ./install_model_or_license.bash
```

如果遇到 `Error: unable to fetch newest license.` 那么可能是 Python 3 的 SSL 的问题，参考 [pynlpir update error](https://github.com/tsroten/pynlpir/issues/108) 或者 [How to make Python use CA certificates from Mac OS TrustStore?](https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore) 进行解决。

### 训练模型
```bash
python ./train_MicroTokenizer.py
```

### 执行测试程序
```bash
python ./main.py
```

### 渲染可视化结果
```bash
python ./render_readme.py
```

渲染结果为 `README.md`

## MicroTokenizer 模型说明
这里简单介绍各个 MicroTokenizer 模型的情况，具体信息请访问 [MicroTokenizer 文档](https://github.com/howl-anderson/MicroTokenizer)

### MicroTokenizer_with_HMM
使用人民日报的数据，模型为 HMM

### MicroTokenizer_with_DAG
使用人民日报的数据，模型为 DAG

### tokenizer_MicroTokenizer_with_join_model
使用人民日报的数据，模型为 HMM 和 DAG 联合模型

### tokenizer_MicroTokenizer_with_custom_model
使用 SIGHAN Bakeoff 2005 的训练数据，模型为 HMM 和 DAG 联合模型

## 测试结果

### MSR
| Algorithm                                      |   Precision |   Recall |   F1-measure |
|:-----------------------------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM                        |       0.732 |    0.787 |        0.758 |
| MicroTokenizer_with_DAG                        |       0.801 |    0.81  |        0.805 |
| tokenizer_MicroTokenizer_with_join_model       |       0.822 |    0.781 |        0.801 |
| tokenizer_MicroTokenizer_with_CRF              |       0.828 |    0.868 |        0.847 |
| tokenizer_MicroTokenizer_with_custom_model     |       0.904 |    0.87  |        0.886 |
| tokenizer_MicroTokenizer_with_custom_CRF_model |       0.946 |    0.941 |        0.943 |
| jieba                                          |       0.817 |    0.812 |        0.815 |
| thulac                                         |       0.834 |    0.878 |        0.856 |
| nlpir                                          |       0.869 |    0.914 |        0.891 |
| ltp                                            |       0.868 |    0.899 |        0.883 |

### AS
| Algorithm                                      |   Precision |   Recall |   F1-measure |
|:-----------------------------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM                        |       0.636 |    0.66  |        0.648 |
| MicroTokenizer_with_DAG                        |       0.46  |    0.625 |        0.53  |
| tokenizer_MicroTokenizer_with_join_model       |       0.681 |    0.685 |        0.683 |
| tokenizer_MicroTokenizer_with_CRF              |       0.732 |    0.74  |        0.736 |
| tokenizer_MicroTokenizer_with_custom_model     |       0.884 |    0.844 |        0.864 |
| tokenizer_MicroTokenizer_with_custom_CRF_model |       0.934 |    0.943 |        0.938 |
| jieba                                          |       0.74  |    0.737 |        0.738 |
| thulac                                         |       0.732 |    0.745 |        0.738 |
| nlpir                                          |       0.485 |    0.651 |        0.556 |
| ltp                                            |       0.794 |    0.809 |        0.801 |

### PKU
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

### CityU
| Algorithm                                      |   Precision |   Recall |   F1-measure |
|:-----------------------------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM                        |       0.613 |    0.645 |        0.629 |
| MicroTokenizer_with_DAG                        |       0.425 |    0.593 |        0.495 |
| tokenizer_MicroTokenizer_with_join_model       |       0.651 |    0.665 |        0.658 |
| tokenizer_MicroTokenizer_with_CRF              |       0.721 |    0.732 |        0.726 |
| tokenizer_MicroTokenizer_with_custom_model     |       0.87  |    0.835 |        0.852 |
| tokenizer_MicroTokenizer_with_custom_CRF_model |       0.925 |    0.922 |        0.923 |
| jieba                                          |       0.748 |    0.735 |        0.742 |
| thulac                                         |       0.73  |    0.745 |        0.738 |
| nlpir                                          |       0.452 |    0.622 |        0.524 |
| ltp                                            |       0.783 |    0.801 |        0.792 |


## Roadmap
* [TODO] 添加 HanLP 作为待评测中文分词器
* [TODO] 添加 Stanford core NLP 作为待评测中文分词器
* [TODO] 添加 FudanNLP 作为待评测中文分词器

## 测试结论
1. `thulac` 和 `ltp` 性能突出, 但都是不是可以商业免费使用的(如果我没理解错的话)。
2. 比较流行的工具中 `jieba` 能商用,但性能上和以上顶级分词工具还有不少差距。
3. `MicroTokenizer` 只使用人民日报或者 SIGHAN Bakeoff 2005 提供的语料，但是其 `CRF` 模型能力非常优秀，在添加允许用户添加自定义词典的特性后，将是非常有前景的中文分词工具。

# Acknowledge & Credit
* 文本部分目前大量参考了 [中文分词工具测评](http://rsarxiv.github.io/2016/11/29/%E4%B8%AD%E6%96%87%E5%88%86%E8%AF%8D%E5%B7%A5%E5%85%B7%E6%B5%8B%E8%AF%84/) 的组织方式和表达。