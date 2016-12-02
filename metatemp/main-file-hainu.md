## 主文件的设计安排

### 开题报告的主文件

真正在写论文的时候，三篇各自的报告可能采用各自的不同的格式，但是很大的可能是它们仍然还共享很多的设置，特别是与页面无关的一些设置。这个时候我们还是得慢慢地把这些东西调整起来。上面的只是一个示例。头文件不只是加载其中的一个类，而是各情况都有包含。而且这还仅仅只是和成头文件而已。真正的情况下，除了头文件，还有各个文件的生成的选项。因为主文件要负责生成论文中的各个部分。比如开题报告的正式内容的结构应该是这样的：

照理来说，元数据应该是统一的，比如什么样的导师，又有什么样的课题。但是目前却做不到这样的整合的程度。只好一步一步来了。

首先是选择文类并定义一系列的元数据字段

```{.nwcode title="hnureport.tex/示例"}
\documentclass{hnureport}

\author{任呈祥}
\title{开题报告示例模板}
\studentnumber{14081200210004}
\institution{海南大学}
\supervisor{段玉聪（教授）}[]

\profession{14计算机科学与技术}
\degreetype{工学硕士（？）}
\domain{----}

\graduatedate{==}
\studenttopic{（Keywords：面向服务、形式化方法、UD与OD）}
\plannedfirstdraft{2015.10.1}
\plannedmanuscript{2015.10.31}
```

然后是确定文件的结构

```{.nwcode title="hnureport.tex/示例"}
\usepackage{lipsum}
\begin{document}
% 制造封面
\pagestyle{empty}
\makecover

\clearpage
\AddToShipoutPicture{\BackgroundPic}
\makeheader

<<hnureport.tex的内容>>

\end{document}
``` 

#### 正式开题报告的格式

[11-06-2015 15:05:26 CST]从现在来看我们知道当时的设计肯定是考虑错误了。因为开题报告的主文件的内容显然是在开题的时候才确定而不是我们上研究生的时候就确定了的。甚至是开题报告的格式也存在很多的困难。所以为了应对这样的变化，我们得把开题报告的主文件内容放在第四章里面去。比如说开题的题目，显然也应该是放在第四章里面的。现在马上要交开题报告了，所以我们暂时将主文件中的各个字段放在此处。以后修改的时候讲。

```{.nwcode title="hnureport.tex"}
\documentclass{hnureport}

\author{任呈祥}
\title{面向服务体系结构下基于价值的过设计与欠设计的问题研究}
\studentnumber{14081200210004}
\institution{海南大学}
\supervisor{段玉聪}[]

\profession{14计算机科学与技术}
\degreetype{工学硕士}
\domain{---}

\graphicspath{{pictures/}}

\graduatedate{2017年5月}
\studenttopic{面向服务、形式化方法、UD与OD}
\plannedfirstdraft{2015年10月}
\plannedmanuscript{2015年12月}
```

然后是确定文件的结构

```{.nwcode title="hnureport.tex"}
\usepackage{lipsum}
\begin{document}
% 制造封面
\pagestyle{empty}
\makecover

\clearpage
\AddToShipoutPicture{\BackgroundPic}
\makeheader

<<hnureport.tex的内容>>

\end{document}
```


### 开题报告主文件的正文

而hnureport.tex的内容现在假设只是一个lipsum

```{.nwcode title="hnureport.tex的内容（示例）"}
%\lipsum[1-5]
```


[11-05-2015 15:52:40 CST]现在开题报告的内容是正式的开题报告格式了

```{.nwcode title="hnureport.tex的内容"}
<<正式开题报告的结构>>
```


#### 确定文件的内容

主体内容已经说了包括里面的四个部分，研究来源等等。但是具体的情况下有待确定。这种方法可能还需要修改。自己决定哪些内容添加到开题报告里面还得调查一下。

按照相关的要求，开题报告包含有四个部分，研究来源、研究内容、研究进展计划、以及现有的条件四个环节。这个个环节首先保持为空吧。因为这个开题报告的格式可能还是有一些问题的。

```{.nwcode title="hnureport.tex的内容（示例性）"}
<<开题报告/研究来源>>
%\lipsum[1-2]
%\subsection{子标题}
%\lipsum[1-2]
%\subsubsection{子子标题}
%\lipsum[3-4]
<<开题报告/研究内容>>
%\lipsum[2]
<<开题报告/研究进展计划>>
%\lipsum[3]
<<开题报告/现有条件>>
```

各个部分先保持为空，等到具体写论文的时候再把各个部分添加上去。

```{.nwcode title="开题报告/研究来源"}
\section{研究来源}
```

```{.nwcode title="开题报告/研究内容"}
\section{研究内容}
```

```{.nwcode title="开题报告/研究进展计划"}
\section{研究进展计划}
```

```{.nwcode title="开题报告/现有条件"}
\section{现有条件}
```

模板给出的四个部分有些混乱，并且有一部分的内容是重复的。上面说，研究来源包括研究的目的和意义、国内外研究现状与发展趋势、主要参考资料、是否为导师科研课题的一部分等。在研究目的与意义里面，既有研究目的，又有研究意义；在国内外研究现状与趋势里面，既有国内的研究现状，又有国外的研究现状与趋势。这两个部分得分离开。但是这种分离确实会让人感到很不爽。

参考文献的格式自然不必说了，就是所谓的GB格式。

在参考资料之外，还要明确是导师科研课题的一部分，还是说是在导师的指导下独立完成的论文。这两个特性是不同的。

第二部分是研究内容。研究内容要包括说明研究的主要内容；研究的主要框架结构；可能的创新之处；需要重点解决的问题，以及预期的研究成果。

* 研究的主要内容：进行摘要式的描述
* 研究的主要框架结构：包括导论、文献回顾（也叫文献综述）两个部分。其中的导论包括研究的背景、目的和意义、思路与方法、研究的主要内容，可能的创新点这几个部分。文献综述则分成国内文献综述与国外一般文献综述两个部分。可以把国外文献综述放在前面（因为国外的研究总是比国内的进展要快一些）。其它的内容包括结束说、致谢、主要参考文献等。

可能的创新之处，则是对于可能的创新点进行一一的罗列。需要重点解决的问题需要分析重点解决的问题以及其可能的难处。而预期的研究成果，则是期望得到的结果。当然，这样写论文的话，其实跟独立做项目没有什么区别，本质上就是自己对于所写的内容做一个保证而已。

第三部分是研究的进展与计划。包括研究的方法、技术方案、实验方法、研究的时间安排、可能遇到的问题、问题的解决方案等。

* 研究的方法以及技术方案
* 研究时间安排
* 可能遇到的问题
* 问题的解决方案

第四部分是研究的现有的条件。包括已经做过的相关研究工作；本单位或者外单位可供使用的仪器设备和实验条件；以及已经获得或者将要获得的经费等。


### 主论文的结构


再比如说主论文的结构：

```{.nwcode title="hnuthesis.tex"}
\documentclass{hnuthesis}
\usepackage{lipsum}
\author{任呈祥}
\title{海南大学毕业论文}

\begin{document}

\maketitle
\tableofcontents

<<hnuthesis.tex的内容（示例）>>

\end{document}
```

假设论文现在的内容还是一片lipsum

```{.nwcode title="hnuthesis.tex的内容（示例）"}
\lipsum[50]
```

如何生成内容的指示都在Makefile当中了。从逻辑上来说，首先应该是生成三个头文件，然后是生成三个相应的tex文件，这些都是从notangle与noweave中得到的。生成相应的文件之后就开始进行编译。编译的过程放在latexmk文件当中。

这样的报告跟之前写的怎样生成自己的报告很不一样。那个时候的报告是整篇文章的目的都是生成同一个cls与tex文件。但是这里要生成几个不同的cls与tex文件。主文件可以有很多个，但是如果生成的是多个thesis，那么就要为每个论文都生成一个cls文件，这样显得比较冗杂。还不如直接就生成thesis.cls与thesis.tex文件好。但是details.nw却是一个虚拟的nw文件。因为我们的写作报告需要很多的内容才可以整理好。

现在的原则显然是，webfiles是统一管理的。这些webfiles使用同一个

### 论文答辩的结构整理

\lipsum[1]
