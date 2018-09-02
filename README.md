# 中文分词软件基准测试

## 评测目标
本项目测试各个常见分词软件在分词效果上的表现，比较各个分词方法和理论的实际效果，对分词速度也做了简单的考核。

## 分词软件
本文选择了4个相对常见的分词工具，分别是：哈工大的 `LTP`、中科院计算所的 `NLPIR`、清华大学的 `THULAC`, [Sun Junyi](https://github.com/fxsjy) 的 `jieba` 和 [Xiaoquan Kong](https://github.com/howl-anderson) 的 `MicroTokenizer`。

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
### 模型性能

#### MSR
| Algorithm                                   | Precision   | Recall    | F1-measure   |
|:--------------------------------------------|:------------|:----------|:-------------|
| jieba                                       | 0.817       | 0.812     | 0.815        |
| thulac                                      | 0.834       | 0.878     | 0.856        |
| nlpir                                       | 0.869       | **0.914** | **0.891**    |
| ltp                                         | 0.868       | 0.899     | 0.883        |
| MicroTokenizer_with_HMM                     | 0.694       | 0.734     | 0.713        |
| MicroTokenizer_with_DAG                     | 0.802       | 0.892     | 0.845        |
| MicroTokenizer_with_joint_model             | 0.811       | 0.813     | 0.812        |
| MicroTokenizer_with_CRF                     | 0.789       | 0.774     | 0.781        |
| MicroTokenizer_with_custom_joint_model      | **0.904**   | 0.870     | 0.886        |
| MicroTokenizer_with_custom_CRF_model        | 0.789       | 0.774     | 0.781        |
| MicroTokenizer_with_max_match_forward       | 0.800       | 0.890     | 0.843        |
| MicroTokenizer_with_max_match_backward      | 0.801       | 0.892     | 0.844        |
| MicroTokenizer_with_max_match_bidirectional | 0.800       | 0.890     | 0.843        |

#### AS
| Algorithm                                   | Precision   | Recall    | F1-measure   |
|:--------------------------------------------|:------------|:----------|:-------------|
| jieba                                       | 0.740       | 0.737     | 0.738        |
| thulac                                      | 0.732       | 0.745     | 0.738        |
| nlpir                                       | 0.485       | 0.651     | 0.556        |
| ltp                                         | 0.794       | 0.809     | 0.801        |
| MicroTokenizer_with_HMM                     | 0.639       | 0.632     | 0.635        |
| MicroTokenizer_with_DAG                     | 0.448       | 0.633     | 0.524        |
| MicroTokenizer_with_joint_model             | 0.670       | 0.654     | 0.662        |
| MicroTokenizer_with_CRF                     | 0.643       | 0.580     | 0.609        |
| MicroTokenizer_with_custom_joint_model      | **0.884**   | **0.844** | **0.864**    |
| MicroTokenizer_with_custom_CRF_model        | 0.643       | 0.580     | 0.609        |
| MicroTokenizer_with_max_match_forward       | 0.448       | 0.633     | 0.525        |
| MicroTokenizer_with_max_match_backward      | 0.447       | 0.633     | 0.524        |
| MicroTokenizer_with_max_match_bidirectional | 0.448       | 0.633     | 0.525        |

#### PKU
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

#### CityU
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


### 分词速度
#### 测试结果
| Algorithm                      | Time Cost (seconds)   |
|:-------------------------------|:----------------------|
| jieba                          | 4.629725              |
| thulac                         | 24.443029             |
| nlpir                          | **2.9404**            |
| ltp                            | 7.118068              |
| MicroTokenizer_with_HMM        | 35.199929             |
| MicroTokenizer_with_DAG        | 11.520658             |
| MicroTokenizer_with_join_model | 56.950306             |
| MicroTokenizer_with_CRF        | 4.108395              |
#### 测试硬件
| 指标           |                                     参数 |
|:---------------|-----------------------------------------:|
| CPU            | Intel(R) Core(TM) i7-7660U CPU @ 2.50GHz |
| memory         |                                      16G |
| OS             |                    macOS 10.13.6 (17G65) |
| Python version |                                    3.6.5 |

#### 测试语料
| Key      |          Value |
|:---------|---------------:|
| 小说名   | 《平凡的世界》 |
| 行数     |          11145 |
| 文件大小 |           2.3M |


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