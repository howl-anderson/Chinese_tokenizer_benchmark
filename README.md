# 中文分词软件基准测试
## 评测目标
本项目只测试各个常见分词软件在分词效果上的表现,着总比较各个分词方法和理论的实际效果.分词工具的速度等因素不在考虑范围内.
## 分词软件
本文选择了4个相对常见的分词工具，分别是：哈工大LTP、中科院计算所NLPIR、清华大学THULAC和jieba。

1. LTP https://github.com/HIT-SCIR/ltp
2. NLPIR https://github.com/NLPIR-team/NLPIR
3. THULAC https://github.com/thunlp/THULAC
4. jieba https://github.com/yanyiwu/cppjieba

##测试数据集
SIGHAN Bakeoff 2005 MSR PKU AS and CityU at http://sighan.cs.uchicago.edu/bakeoff2005/

本数据集是 `ACL SIGHAN` 于 2005 年组织的中文分词比赛所用的数据集，也是学术界测试分词工具的标准数据集.

## 测试方法
用SIGHAN Bakeoff 2005比赛中所自带的score脚本、test gold数据和training words数据对4个工具进行准确性测试，具体使用方法可参考：http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip 中的readme文件。

##测试结果
## AS

| Algorithm               |   Precision |   Recall |   F1-measure |
|:------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM |       0.636 |    0.66  |        0.648 |
| jieba                   |       0.74  |    0.737 |        0.738 |
| thulac                  |       0.732 |    0.745 |        0.738 |
| nlpir                   |       0.485 |    0.651 |        0.556 |
| ltp                     |       0.794 |    0.809 |        0.801 |

## CityU

| Algorithm               |   Precision |   Recall |   F1-measure |
|:------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM |       0.613 |    0.646 |        0.629 |
| jieba                   |       0.748 |    0.735 |        0.742 |
| thulac                  |       0.73  |    0.745 |        0.738 |
| nlpir                   |       0.452 |    0.62  |        0.523 |
| ltp                     |       0.783 |    0.801 |        0.792 |

## MSR

| Algorithm               |   Precision |   Recall |   F1-measure |
|:------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM |       0.732 |    0.787 |        0.758 |
| jieba                   |       0.817 |    0.812 |        0.815 |
| thulac                  |       0.834 |    0.879 |        0.856 |
| nlpir                   |       0.869 |    0.914 |        0.891 |
| ltp                     |       0.868 |    0.899 |        0.883 |

## PKU 

| Algorithm               |   Precision |   Recall |   F1-measure |
|:------------------------|------------:|---------:|-------------:|
| MicroTokenizer_with_HMM |       0.742 |    0.774 |        0.758 |
| jieba                   |       0.853 |    0.787 |        0.818 |
| thulac                  |       0.922 |    0.923 |        0.923 |
| nlpir                   |       0.94  |    0.943 |        0.941 |
| ltp                     |       0.96  |    0.946 |        0.953 |

## 测试结论
1、一个好的分词工具不应该只能在一个数据集上得到不错的指标，而应该在各个数据集都有很不错的表现。从这一点来看，thulac和ltp都表现非常不错。

2、因为分词是个基础部件，分词速度对于一个分词工具来说也至关重要。从这一点来看，thulac和jieba表现的不错。

3、大家都知道，基本的分词依赖模型，但真正想用分词工具来解决应用层面上的问题，都需要借助于词库，本文测试的4个工具均支持用户自定义词库。

4、特别需要强调的一点是，哈工大的ltp支持分词模型的在线训练，即在系统自带模型的基础上可以不断地增加训练数据，来得到更加丰富、更加个性化的分词模型。

# Acknowledge & Credit
* [中文分词工具测评](http://rsarxiv.github.io/2016/11/29/%E4%B8%AD%E6%96%87%E5%88%86%E8%AF%8D%E5%B7%A5%E5%85%B7%E6%B5%8B%E8%AF%84/)
* 