# 使用接口介绍[11-20-2016 22:59:46 CST]


## 使用接口简介[11-20-2016 23:03:52 CST]

使用\LaTeX{}写论文的时候，我们最希望做的就是能够直接就开始论文的编写。比如采用article文类那样，首先使用一个`\documentclass`{.latex}指令，然后在这个指令的基础之上添加一些只跟我们写文档相关的指令：比如声明作者，声明所使用的参考文献。接下来就可以直接写`\begin{document}`{.latex}这样的指令了。本文类就是希望达到这样的目标，具体来说，我们可以通过如下的参数开始一篇论文的编写：

```{.nwcode .latex title="thesis.tex示例文件的结构"}
\documentclass{hnuthesis}
\addbibresource{citation/myrefs.bib}
```

```{.nwcode .latex title="thesis.tex示例文件的结构"}
\Author{任呈祥}
\EnglishAuthor{Chengxiang Ren}

\Title{海南大学研究生学位论文模板}
\EnglishTitle{How to write a definite template in \LaTeX{} for the Hainan University (Draft Version)}

\Date{2016年10月24日}
\EnglishSubmissionDate{October, 2016}

\EnglishCollege{College of Information Science and Technology}

\DegreeType{学术型}
\EnglishDegreeType{Science}

\SchoolCode{10589}
\ClassificationCode{分类码}
\StudentCode{140812002}
\SecurityLevel{绝密(启用前)}

\SchoolLogoFile{pictures/hainu.png}

\Major{计算机科学与技术}
\EnglishMajor{Computer Science and Technology}

\Supervisor{XXX 教授}
\EnglishSupervisor{Prof. XXX}

\usepackage{lipsum}
```

```{.nwcode .latex title="thesis.tex示例文件的结构"}
\begin{document}

\TitlePage
\EnglishTitlePage
\Declarations
\EnglishKeywords{abc, def, ghi, lms}
\ChineseKeywords{模板，中文，海南大学，毕业论文}
\begin{ChineseAbstract}
    \lipsum[1-2]
\end{ChineseAbstract}
\begin{EnglishAbstract}
    \lipsum[1-2]
\end{EnglishAbstract}
\TableOfContents

%% your contents here

\end{document}
```
