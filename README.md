# Graph-Drawing-Language-Interpreter

一个简单的函数绘图语言解释器

## 环境要求

1. python 3.5.7及以上版本
2. numpy
3. matplotlib

## 使用方法

- 在graphic.txt中编写函数绘图语言。
- 运行final.py

## 解释器项目结构

### 词法分析器（scanner）

词法分析器由三个文件构成，分别是scanner_token.py、scannerprocess.py和testscanner.py

- scanner_token.py文件中给出了token的定义和可能出现的所有token类型，对于一些特殊token 类型，如sin, cos等，使用numpy对应的矩阵运算方法进行构造。
- scannerprocess.py主要实现词法分析过程，其核心在于GetToken方法的设计。其设计的核心原 理在于对于每一类字符的正规式的构造，并依据正规式给出对应类型的识别方法。
- testscanner.py负责对scanner进行测试，输入graphic.txt文件，输出由scanner检测到的记号流构成的记号表，通过测试scanner，为后续创建语法树打基础。

### 语法分析（Parser）

语法分析器由parser_node.py、parserprocess.py和testparser.py构成。

- parser_node.py中给出了语法树节点 ExprNode 的构造方法，在确定每一个运算符的种类后，对 于双目运算符，给该节点分配左右子树，对于函数类型，给该节点分配函数指针和middle内容。构造GetValue方法，针对每一个节点给出其结果的运算方式，将其存储在矩阵中，为后续过程实 现画图提供方便。
- parserprocess.py中主要实现了语法分析的过程，其中语法树的构造，语法的识别，报错信息的提 示等功能，是整个函数绘图语言解释器的核心部分，也是最难的部分。 实现该部分的核心思路在于针对不同的语句提供一种构造语法树的方法，针对每一种语句，如 OriginStatement，ScaleStatement，ForStatement构建其语法分析过程，并使得程序可以在读 到错误语法是给出对应行号的报错。
- testparser.py主要功能是测试语法分析的过程是否正确，输入graphic.txt文件，输出构造出的语法树结构，方便进行下一步操作。

### 语义分析（semantic）

由于该解释器基于python环境，且在语法分析过程中已经构造了GetValue方法，因此在语义分析阶段，我们仅需关注画图部分的内容。由于在语法分析器中，Statement方法并未给出画图过程，因此在semantic类中，应重载该方法，在保留基本功能的同时，在For语句执行后进行绘图操作。



## 可能的运行结果

根据项目内现有的graphic.txt中的内容，绘制出的图保存在result.jpg文件中。

## 更详细的说明
[概述&词法分析](https://www.bbbbchan.com/2020/01/10/%e7%ae%80%e5%8d%95%e5%87%bd%e6%95%b0%e7%bb%98%e5%9b%be%e8%af%ad%e8%a8%80%e8%a7%a3%e9%87%8a%e5%99%a8-python%e5%ae%9e%e7%8e%b0-%e6%a6%82%e8%bf%b0%e8%af%8d%e6%b3%95%e5%88%86%e6%9e%90%e7%af%87/)

[语法分析](https://www.bbbbchan.com/2020/01/10/%e7%ae%80%e5%8d%95%e5%87%bd%e6%95%b0%e7%bb%98%e5%9b%be%e8%af%ad%e8%a8%80%e8%a7%a3%e9%87%8a%e5%99%a8-python%e5%ae%9e%e7%8e%b0-%e8%af%ad%e6%b3%95%e5%88%86%e6%9e%90%e7%af%87/)

[语义分析&实现](https://www.bbbbchan.com/2020/01/10/%e7%ae%80%e5%8d%95%e5%87%bd%e6%95%b0%e7%bb%98%e5%9b%be%e8%af%ad%e8%a8%80%e8%a7%a3%e9%87%8a%e5%99%a8-python%e5%ae%9e%e7%8e%b0-%e8%af%ad%e4%b9%89%e5%88%86%e6%9e%90%e5%ae%9e%e7%8e%b0%e7%af%87/)

