# 中文分词软件基准测试
## 评测目标
本项目只测试各个常见分词软件在分词效果上的表现,着总比较各个分词方法和理论的实际效果.分词工具的速度等因素不在考虑范围内.
## 分词软件
本文选择了4个相对常见的分词工具，分别是：哈工大 `LTP`、中科院计算所 `NLPIR`、清华大学 `THULAC` , `jieba` 和本人自己开发的 `MicroTokenizer` with HMM。

1. LTP @ https://github.com/HIT-SCIR/pyltp
2. NLPIR @ https://github.com/tsroten/pynlpir
3. THULAC @ https://github.com/thunlp/THULAC-Python
4. jieba @ https://github.com/fxsjy/jieba
5. MicroTokenizer @ https://github.com/howl-anderson/MicroTokenizer

## 测试数据集
SIGHAN Bakeoff 2005 `MSR` `PKU` `AS` and `CityU` at http://sighan.cs.uchicago.edu/bakeoff2005/

本数据集是 `ACL SIGHAN` 于 2005 年组织的中文分词比赛所用的数据集，也是学术界测试分词工具的标准数据集.

## 测试方法
用 SIGHAN Bakeoff 2005 比赛中所自带的 score 脚本、test gold数据和training words数据对4个工具进行准确性测试，具体使用方法可参考：http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip 中的readme文件。

## 测试结果
{% for item in test_result %}
### {{ item.title }}
{{ item.markdown_table }}
{% endfor %}

## 测试结论
1. `thulac` 和 `ltp` 性能突出, 但都是不是可以商业免费使用的(如果我没理解错的话)。
2. 比较流行的工具中 `jieba` 能商用,但性能上和以上顶级分词工具还有不少差距.
3. `MicroTokenizer` with HMM, 只使用 HMM 和人民日报的语料,却有着相对不错的效果,总体看来中文分词做起来不是很难,即使比较简单的模型,也能收获不错的性能,但达到优秀的性能,还是需要大量语料和模型改进的.

# Acknowledge & Credit
* 文本部分目前大量参考了 [中文分词工具测评](http://rsarxiv.github.io/2016/11/29/%E4%B8%AD%E6%96%87%E5%88%86%E8%AF%8D%E5%B7%A5%E5%85%B7%E6%B5%8B%E8%AF%84/) 的组织方式和表达.