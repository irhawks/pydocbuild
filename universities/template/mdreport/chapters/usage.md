# 使用接口介绍[11-20-2016 22:59:46 CST]


## 使用接口简介[11-20-2016 23:03:52 CST]

使用\LaTeX{}写论文的时候，我们最希望做的就是能够直接就开始开题报告的编写。比如采用article文类那样，首先使用一个`\documentclass`{.latex}指令，然后在这个指令的基础之上添加一些只跟我们写文档相关的指令：比如声明作者，声明所使用的参考文献。接下来就可以直接写`\begin{document}`{.latex}这样的指令了。本文类就是希望达到这样的目标，具体来说，我们可以通过如下的参数开始一篇开题报告的编写：

这里我们遇到一个神奇的现象，就是如果我们在下面的代码当中空一行，则立马会出现tikz与calc和math-dollar redefine的错误。不知道这是什么原因。

\begin{minted}{latex}
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
\usepackage{lipsum}
\end{minted}

正文区存放如下的内容：

\begin{minted}{sh}
\begin{document}
\pagestyle{empty}
\makecover
\clearpage
\AddToShipoutPicture{\BackgroundPic}
\makeheader
\section{xx}
\end{document}
\end{minted}
