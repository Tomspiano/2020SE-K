:point_right: 这里先附上[Github Repo地址](https://github.com/Tomspiano/2020SE-K/tree/master/181800331/01)和[作业地址](https://edu.cnblogs.com/campus/fzu/FZU_SE_KClass/homework/11118) :point_left:

# 需求

**题目：论文查重**

描述如下：

设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。

> 原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
>
> 抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。

要求输入输出采用文件输入输出，规范如下：

- 从**命令行参数**给出：论文原文的文件的**绝对路径**。
- 从**命令行参数**给出：抄袭版论文的文件的**绝对路径**。
- 从**命令行参数**给出：输出的答案文件的**绝对路径**。



# 解决方案

## 1. 计算模块接口的设计与实现过程

**代码的总设计结构如下：**

![code_structure](blog.assets/code_structure.png)

- #### 读取文本

  先处理从命令行读取到的参数，即文本路径。读取文件时注意使用`utf-8`编码。

- #### 文本预处理

  首先，生成停用词表`get_stopwords()`，这里引用了[goto456的中文停用词表](https://github.com/goto456/stopwords/blob/master/cn_stopwords.txt)。注意一下，在测试须知里提到**不允许读写其他文件！！**于是只能手动生成停用词表:no_mouth:（运行[`process.py`](https://github.com/Tomspiano/2020SE-K/blob/master/181800331/01/release/dcheck/process.py)，从输出的文件中获得相应列表）。

  接着，先对文本分段，再用[`jieba`](https://github.com/fxsjy/jieba)分词。这里使用了搜索引擎模式`jieba.lcut_for_search`，因为考虑到无法针对测试集自定义词典，而论文中的专有名词较多，精确模式在这种情况下分词效果可能不够好。

  最后，从得到的分词列表中过滤掉出现在停用词表中的词。分段、分词、过滤均封装在函数`segment()`中。

  以上函数均在[`process.py`](https://github.com/Tomspiano/2020SE-K/blob/master/181800331/01/release/dcheck/process.py)中定义。

- #### 相似度模型

  我设计的模型是**[Jaccard index](https://blog.csdn.net/qq_34333481/article/details/84024513) + [Cosine similarity](http://www.ruanyifeng.com/blog/2013/03/cosine_similarity.html)**。之所以选择这个组合，是因为一开始我联想到在CV目标检测中有个[IoU](https://blog.csdn.net/gaoyu1253401563/article/details/86484851)（其实就是Jaccard index），用来衡量锚框（anchor box）与真实边界框（ground-truth bounding box）之间的相似度。而查重也是度量两篇文章之间的相似度，它们之间的相似度与使用到相同词的个数正相关。Jaccard index计算公式：

  $$J(\mathcal{A},\mathcal{B}) = \frac{\left|\mathcal{A} \cap \mathcal{B}\right|}{\left| \mathcal{A} \cup \mathcal{B}\right|}.$$

  但是只用Jaccard index显然不够，我们还能进行更精细的度量。Jaccard index只衡量了两个文本之间用词的重叠度，而忽略了词语在文本中出现的频率——**[词频TF](https://www.ruanyifeng.com/blog/2013/03/tf-idf.html)**。设想，若一个文本通篇讲半导体芯片，另一个文本只是科普性文章，顺带提到了半导体芯片，那么它们的Jaccard index有可能较大。因此，我对两个文本分别计算了共同出现词的词频：

  $$词频(TF)=\frac{某个词在文章中的出现次数}{文章的总词数},$$

  并依此写出词频向量，利用Cosine similarity衡量它们的相似度：

  $$\cos<\vec a, \vec b>=\frac{\vec a \cdot \vec b}{\| \vec a \|  \| \vec b \|}.$$

  *尝试画图。。。*

  ![similarity_model](blog.assets/similarity_model.png)

  最后，定义相似度：

  $$Sim = J(\mathcal{A},\mathcal{B}) \times \cos<\vec a, \vec b>.$$

  *注：相似度计算封装在函数[`get_sim()`](https://github.com/Tomspiano/2020SE-K/blob/master/181800331/01/release/dcheck/compare.py)中。*

  ---

  这里用词集合代替词空间或许会更准确。毕竟语言太复杂，我在此没有对其定义[基](https://baike.baidu.com/item/%E5%9F%BA/16246650#viewPageContent)。

- #### 输出

  和读取文本一样，注意使用`utf-8`编码。

## 2. 计算模块接口部分的性能改进

使用的性能分析工具为[gprof2dot](https://github.com/jrfonseca/gprof2dot)。

依次执行如下命令：

```bash
python -m cProfile -o profile.pstats main.py ..\sample\sim_0.8\orig.txt ..\sample\sim_0.8\orig_0.8_mix.txt ..\output\mix.txt
python -m gprof2dot -f pstats profile.pstats -o profile.dot
dot -Tpng -o ..\blog.assets\profile_result.png profile.dot
```

得到

![profile_result](blog.assets/profile_result.png)

简化版则执行：

```bash
python -m gprof2dot -f pstats profile.pstats -o profile_simple.dot -n20 -s
dot -Tpng -o ..\blog.assets\profile_result_simple.png profile_simple.dot
```

得到

![profile_result_simple](blog.assets/profile_result_simple.png)

这里可以看到调用`jieba`进行分词的部分耗时最多，具体如下：

```bash
python -c "import pstats; p=pstats.Stats('profile.pstats'); p.strip_dirs(); p.sort_stats('cumulative').print_stats(0.005)"
```

![cumulative](blog.assets/cumulative.png)

如果要改进的话，看看[源码](https://github.com/fxsjy/jieba)？开发者最近的commit都和[PaddlePaddle](https://www.paddlepaddle.org.cn/)深度学习相关，可神经网络的速度难以改进，除非换一个模型（扯远了这里没用到paddle模式）。还有一个思路是从Python的特性入手，应用一些[trick](https://www.cnblogs.com/taceywong/p/5773220.html)。自以为如果trick会降低可读性，那我可能不会采用。“Readability counts.”

*这里挖个坑，回头看看[Decorators](https://www.runoob.com/w3cnote/python-func-decorators.html)怎么用。。。*

## 3. 计算模块部分[单元测试展示](https://github.com/Tomspiano/2020SE-K/tree/master/181800331/01/release/test)

测试分为三个部分，具体如下。

- 对样例的测试

  ![test_sim](blog.assets/test_sim.png)

- 对个人数据的测试

  ![test_report](blog.assets/test_report.png)

- 对异常的测试

  这部分看[下面](#4-计算模块部分异常处理说明)。

- 最后是测试执行文件

  ![main_test](blog.assets/main_test.png)

  其中目录结构如下：

  ![directory](blog.assets/directory.png)

  使用[coverage](https://coverage.readthedocs.io/en/coverage-5.3/index.html)得到的测试覆盖率：

  ```bash
  coverage run main_test.py
  coverage html -i -d report
  ```

  ![report](blog.assets/report.png)

  实际上，测试覆盖率应该为$100\%$。代码没有被测试到是因为它们在`main`函数中，没有单独执行文件的话是不会运行的。

  `test_*.py`：

  ![test](blog.assets/test.png)

  `process.py`：这是预处理，用来手动生成停用词表，不用进行测试。

  ![get_stopwords](blog.assets/get_stopwords.png)

  ![process](blog.assets/process.png)

  `main.py`：用`os.system()`传参导致这部分没有测试到。但是从下面的异常处理中可知，这段代码可执行。
  
  ![main](blog.assets/main.png)
  
  ---

  糟心的是样例测试输出结果：

  ![output](blog.assets/output.png)
  
  个人数据的结果就不放了，文档选得不太好，没多大意义。倒是这个样例！我有点方！！和各位大佬相比低了很多！！！刚拿到测试样例我还觉得这没有现实意义，有的文章一看就知道是合成的，句子就不是个句子。这样的测试数据不考察NLP中的语义关联问题，换句话说，上下文对于模型没有任何意义。但是，`orig_0.8_add.txt`和`orig_0.8_del.txt`的测试结果也太低了！只改动了$20\%$，结果却远低于$80\%$。这要是有标准答案不得被:hammer:
  
  但是仔细想想，这个结果也是可以接受的。`jieba`是根据词频来分词的，文章经过增减，分出来的词变化可能很大。例如：
  
  > 原：国庆\放假\我\想\出去\玩
  >
  > 增：国家\庆典\放假\我\想\出去\玩（相似度：0.62）
  >
  > 删：国\假\我\想\出去\玩（相似度：0.50）
  
  相似度也很低！这个例子同时也说明了上下文的重要性。
  
  ![理直气壮](blog.assets/理直气壮.jpg)

## 4. 计算模块部分异常处理说明

- 命令行参数输入格式错误

  在`main.py`中使用`assert`：

  ![test_command2](blog.assets/test_command2.png)

  对应的单元测试样例：

  ![test_command](blog.assets/test_command.png)

- 命令行参数给出的文件路径不存在
  - 输入文件路径
  
    在`main.py`中使用`assert`：
  
    ![test_input_path2](blog.assets/test_input_path2.png)
  
    对应的单元测试样例：
  
    ![test_input_path](blog.assets/test_input_path.png)
  
  - 输出文件路径
  
    在`main.py`中使用`try...except...`：
  
    ![test_output_path2](blog.assets/test_output_path2.png)
  
    对应的单元测试样例：
  
    ![test_output_path](blog.assets/test_output_path.png)
  
- 测试`main.py`能否正常执行

  ![test_work](blog.assets/test_work.png)

- 两篇完全不相同的文章相似度应接近0.00

  ![test_noise](blog.assets/test_noise.png)

- 两篇完全相同的文章相似度应为1.00

  ![test_same](blog.assets/test_same.png)

- 有一个文档是空白的，相似度应为0.00

  ![test_blank](blog.assets/test_blank.png)

- 两个文档都是空白的，无法计算Jaccard index，相似度为1.00

  ![test_blank2](blog.assets/test_blank2.png)

  

# PSP2.1

| Personal Software Process Stages     | Estimate (min) | Actual (min) |
| :----------------------------------- | :------------- | :-------- |
| **Planning**                         | **60** | **30** |
| · Estimate                           | 60 | 30 |
| **Development**                      | **960** | **2360** |
| · Analysis                           | 180 | 1440 |
| · Design Spec                        | 90 | 60 |
| · Design Review                      | 30 | 30 |
| · Coding Standard                    | 30 | 20 |
| · Design                             | 180 | 150 |
| · Coding                             | 90 | 300          |
| · Code Review                        | 60 | 120          |
| · Test                               | 300 | 240 |
| **Reporting**                       | **210** | **240** |
| · Test Report                        | 90 | 180 |
| · Size Measurement                   | 60 | 30 |
| · Postmortem & Process Improvement Plan | 60 | 30 |
| **TOTAL**                            | **1230** | **2630** |



---

## 写在后面

- 一开始看到题目是“论文查重”的OS：这是要训练一个神经网络模型？？？找数据集好麻烦:confused:。深入思考后发觉不对，测试就只输入两个文件，还没有给测试文章的主题范围，数据集难以建立。后来想用gensim里的模型，得到的结果却不是很理想，要么很接近$1$，要么很接近$0$（到现在还没整明白为啥:no_mouth:）。Deadline马上要到了，最后只好自己手写一个:pensive:。这次走了很多弯路，主要是因为**对需求的分析不够到位**。接触了很多新技术，学习时间比预估的长很多。
- 谈谈我是怎么填PSP表的吧。这个模板已经很详细了，如果我自己设计可能就只有加粗的大框架。整体来看时间分配为**鸡蛋型**，开发最多，接下来依次为报告、计划。开发就不说了，注意**为设计文档、复审和测试留时间**。计划的话就**尽量快**，一开始不可能面面俱到。先动手，之后逢山开路遇水搭桥。至于报告，本着**开源精神**就认真一点啦，希望各位多提意见多交流~
- **收获：**
  - 性能分析：[cProfile](https://docs.python.org/3.9/library/profile.html) + [gprof2dot](https://github.com/jrfonseca/gprof2dot) + [Graphviz](https://graphviz.org)
  - 单元测试：[unittest](https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest) + [coverage](https://coverage.readthedocs.io/en/coverage-5.3/index.html)
  - Python：在程序里接受命令行参数
- **遗憾：**没有和其他模型进行对比分析
- **TODO：**学习Decorator

![给我冲](blog.assets/给我冲.jpg)