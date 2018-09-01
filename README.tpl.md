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
{% for item in test_result %}
#### {{ item.title }}
{{ item.markdown_table }}
{% endfor %}

### 分词速度
#### 测试结果
{{ speed }}
#### 测试硬件
{{ sysinfo }}
#### 测试语料
{{ big_corpus }}

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