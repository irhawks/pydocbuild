# 整个论文的版面设计的排版


## 页眉与页脚的排版

```{.nwcode title="hnuthesis.cls"}
\makeatletter
\RequirePackage{fancyhdr}
    \pagestyle{fancy}\fancyhead{}
    \fancyhead[LO]{\zihao{-4}海南大学硕士学位论文}
    %\fancyhead[CE]{\zihao{4} \hnuthesis@Title }
    \fancyhead[RO]{\zihao{-4}\leftmark}
    \fancyfoot{}
    \fancyfoot[CO,CE]{\thepage}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\baselinestretch}{1.5}
```


## 必须定义的一系列的字段

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\SchoolCode}{m}{\gdef\hnuthesis@SchoolCode{#1}}
\gdef\hnuthesis@SchoolCode{10589} %%% 默认是海南大学的Code

\ProvideDocumentCommand{\ClassificationCode}{m}{\gdef\hnuthesis@ClassificationCode{#1}}
\gdef\hnuthesis@ClassificationCode{}

\ProvideDocumentCommand{\StudentCode}{m}{\gdef\hnuthesis@StudentCode{#1}}
\gdef\hnuthesis@StudentCode{}

\ProvideDocumentCommand{\SecurityLevel}{m}{\gdef\hnuthesis@SecurityLevel{#1}}
\gdef\hnuthesis@SecurityLevel{}

\ProvideDocumentCommand{\SchoolLogoFile}{m}{\gdef\hnuthesis@SchoolLogoFile{#1}}
\gdef\hnuthesis@SchoolLogoFile{}

%%% 根据这些字段，我们来制作论文的标题头
\newcolumntype{Y}{>{\begin{CJKfilltwosides}{44pt}}l<{\end{CJKfilltwosides}}}
\ProvideDocumentCommand{\TitlePageLeftHeader}{}{
    \zihao{5}
    \begin{tabu} to 0.3\textwidth {Yp{12pt}X[c]}
        学校代码&：& \hnuthesis@SchoolCode \\\tabucline{3}
        分类号&：& \hnuthesis@ClassificationCode \\\tabucline{3}
\end{tabu}}


\newcolumntype{Z}{>{\begin{CJKfilltwosides}{22pt}}l<{\end{CJKfilltwosides}}}
\ProvideDocumentCommand{\TitlePageRightHeader}{}{
    \zihao{5}
    \begin{tabu} to 0.3\textwidth {Zp{12pt}X[c]}
        学号&：& \hnuthesis@StudentCode \\\tabucline{3}
        密级&：& \hnuthesis@SecurityLevel \\\tabucline{3}
\end{tabu}}

\ProvideDocumentCommand{\TitlePageCenterHeader}{}{
\begin{minipage}[c]{2.5cm}
\centering\includegraphics[height=3cm]{\hnuthesis@SchoolLogoFile}
\end{minipage}}

\ProvideDocumentCommand{\TitlePageHeader}{}{
\noindent
\begin{center}
\TitlePageLeftHeader 
\hfill\hfill \TitlePageCenterHeader 
\hfill\hfill \TitlePageRightHeader
\hfill
\end{center}
}
```

\TitlePageHeader

这里添加上海南大学的黑体

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\TitlePageBody}{}{
    \centerline{\ziju{0.2}\zihao{0} \xingkai 海南大学}
\vspace{25mm}
    \centerline{\zihao{1}\ziju{0.7}\heiti 硕士学位论文}
}
```

\TitlePageBody

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\Supervisor}{m}{\gdef\hnuthesis@Supervisor{#1}}
\gdef\hnuthesis@Supervisor{}

\ProvideDocumentCommand{\Major}{m}{\gdef\hnuthesis@Major{#1}}
\gdef\hnuthesis@Major{}

\ProvideDocumentCommand{\Author}{m}{\gdef\hnuthesis@Author{#1}}
\gdef\hnuthesis@Author{}

\ProvideDocumentCommand{\Title}{m}{\gdef\hnuthesis@Title{#1}}
\gdef\hnuthesis@Title{}

\ProvideDocumentCommand{\Date}{m}{\gdef\hnuthesis@Date{#1}}
\gdef\hnuthesis@Date{}

\ProvideDocumentCommand{\DegreeType}{m}{\gdef\hnuthesis@DegreeType{#1}}
\gdef\hnuthesis@DegreeType{}


\ProvideDocumentCommand{\TitlePageFooter}{}{
    \begin{tabu} to 0.8\textwidth {>{\begin{CJKfilltwosides}{55pt}}l<{\end{CJKfilltwosides}} p{12pt} X[c]}
        题目&：& \hnuthesis@Title \\\tabucline{3}
    作者&：& \hnuthesis@Author\\\tabucline{3}
    指导教师&：& \hnuthesis@Supervisor \\\tabucline{3}
    类别&：& \hnuthesis@DegreeType \\\tabucline{3} 
    专业&：& \hnuthesis@Major \\\tabucline{3}
    时间&：& \hnuthesis@Date \\\tabucline{3}
\end{tabu}
}
```

\TitlePageFooter

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\TitlePage}{}{
\thispagestyle{empty}
\TitlePageHeader \vfill \TitlePageBody \vfill \vfill 
    \begin{center}\TitlePageFooter\end{center} \vfill
\newpage
}
```


## 英文标题页

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\EnglishTitle}{m}{\gdef\hnu@EnglishTitle{#1}}
\gdef\hnu@EnglishTitle{}

\ProvideDocumentCommand{\EnglishDegreeType}{m}{\gdef\hnu@EnglishDegreeType{#1}}
\gdef\hnu@EnglishDegreeType{}

\ProvideDocumentCommand{\EnglishCollege}{m}{\gdef\hnu@EnglishCollege{#1}}
\gdef\hnu@EnglishCollege{}

\ProvideDocumentCommand{\EnglishAuthor}{m}{\gdef\hnu@EnglishAuthor{#1}}
\gdef\hnu@EnglishAuthor{}

\ProvideDocumentCommand{\EnglishSupervisor}{m}{\gdef\hnu@EnglishSupervisor{#1}}
\gdef\hnu@EnglishSupervisor{}

\ProvideDocumentCommand{\EnglishMajor}{m}{\gdef\hnu@EnglishMajor{#1}}
\gdef\hnu@EnglishMajor{}

\ProvideDocumentCommand{\EnglishSubmissionDate}{m}{\gdef\hnu@EnglishSubmissionDate{#1}}
\gdef\hnu@EnglishSubmissionDate{}

%%% 英文标题页
\ProvideDocumentCommand{\EnglishTitlePage}{}{
\thispagestyle{empty}
\phantom{a}\vspace{10pt}
\begin{center} \rm\Huge\bf\hnu@EnglishTitle \end{center}
\vfill\vfill
\begin{center} \large\rm\it A Thesis 
Submitted in Partial Fulfillment of the Requirement\\
for the Master of \hnu@EnglishDegreeType\ in \hnu@EnglishMajor
\end{center}
\vfill
\begin{center} \large\rm\bf By\\ \hnu@EnglishAuthor \\ \end{center}
\vfill
%\begin{center}
%Postgraduate Program \\
%\hnu@EnglishCollege\\
%Hainan University
%\end{center}
%\vfill
{%\large
    \rm
\begin{tabu} to 0.8\textwidth {XX[3]}
Supervisor : & \hnu@EnglishSupervisor \\
Major: & \hnu@EnglishMajor \\
Submitted: & \hnu@EnglishSubmissionDate 
\end{tabu}}
\vfill
    \begin{center}
\large\rm\bf Hainan University, Haikou, P.~R.~China\\
2016
    \end{center}
    \vfill\vfill
\newpage
}
```

\EnglishTitlePage




## 一些元素与文字的排版


第三页是所谓的原创性声明与使用授权说明的模板

```{.nwcode title="hnuthesis.cls"}
<<原创性声明>>
<<授权说明>>
```

```{.nwcode title="原创性声明"}
\DeclareDocumentCommand{\originalityDeclaration}{}{
    \begin{center}\zihao{4}\heiti 原创性声明\end{center}
        \zihao{5}\vspace{-3pt}
本人郑重声明： 所呈交的学位论文, 是本人在导师的指导下,独立进行研究工作所取得的成果。 除文中已经注明引用的内容外,本论文不含任何其他个人或集体已经发表或撰写过的作品或成果。对本文的研究做出重要贡献的个人和集体, 均已在文中以明确方式标明。本声明的法律结果由本人承担。

    \vspace{8pt}
\begin{tabu} to 0.8\textwidth {X[1.5] X}
论文作者签名: & 日期:\hfill 年\hfill 月\hfill 日\hfill
\end{tabu}
}
```


```{.nwcode title="授权说明"}
\DeclareDocumentCommand{\authorityDeclaration}{}{
    \begin{center}\zihao{4}\heiti 学位论文版权使用授权说明\end{center}
        \zihao{5}\vspace{-3pt}

本人完全了解海南大学关于收集、保存、使用学位论文的规定, 即：学校有权保留并向国家有关部门或机构送交论文的复印件和电子版, 允许论文被查阅和借阅。本人授权海南大学可以将本学位论文的全部或部分内容编入有关数据库进行检索, 可以采用影印、缩印或扫描等复制手段保存和汇编本学位论文。本人在导师指导下完成的论文成果，知识产权归属海南大学。

保密论文在解密后遵守此规定。

    \vspace{8pt}
\begin{tabu} to 0.8\textwidth{X[1.5] X}
论文作者签名: &  导师签名: \\
日期:\hfill 年 \hfill 月\hfill 日\hfill\hfill\hfill  & 
日期:\hfill 年 \hfill 月\hfill 日\hfill
\end{tabu}
}
```


### CALIS论文发布声明

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\CalisDeclaration}{}{
\songti\zihao{5} 
本人已经认真阅读“CALIS 高校学位论文全文数据库发布章程”，
同意将本人的学位论文提交“CALIS 高校学位论文全文数据库”中全文发布，
并可按“章程”中规定享受相关权益。

\underline{同意论文提交后滞后：$\square$半年；$\square$一年；$\square$二年发布}。

\begin{tabu} to 0.8\textwidth{X[1.5] X}
论文作者签名: &  导师签名: \\
日期:\hfill 年 \hfill 月\hfill 日\hfill\hfill\hfill  & 
日期:\hfill 年 \hfill 月\hfill 日\hfill
\end{tabu}
}
```

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\Declarations}{}{
\thispagestyle{empty}
\centerline{\heiti\zihao{3}海南大学学位论文原创性声明和使用授权说明}
    \vspace{15pt}
\originalityDeclaration
\vfill
\authorityDeclaration
%%% 使用dotline填充见教程<http://tex.stackexchange.com/questions/332357/customizing-the-length-of-dotfill>.
\vspace{15pt}\\
    \centerline{\hbox to 0.9\textwidth{\dotfill}}
\vfill
\CalisDeclaration
\vfill\vfill
\newpage
}
```

\newpage\Declarations


## 摘要与英文摘要

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\EnglishKeywords}{m}{\gdef\hnu@EnglishKeywords{#1}}
\gdef\hnu@EnglishKeywords{}

\ProvideDocumentCommand{\ChineseKeywords}{m}{\gdef\hnu@ChineseKeywords{#1}}
\gdef\hnu@ChineseKeywords{}

\ProvideDocumentEnvironment{ChineseAbstract}{}%
{\newpage\thispagestyle{empty}\pagenumbering{Roman}\setcounter{page}{1}
\centerline{\heiti\zihao{3} 摘\quad 要}
\addcontentsline{toc}{chapter}{摘要}
\songti\zihao{-4}
}%
{\vskip1cm
\noindent \heiti\zihao{-4} 关键词：\songti\zihao{-4} \hnu@ChineseKeywords}

\ProvideDocumentEnvironment{EnglishAbstract}{}%
{\newpage\thispagestyle{empty}%\pagenumbering{Roman}\setcounter{page}{1}
\addcontentsline{toc}{chapter}{Abstract}
\centerline{\bf\zihao{3} Abstract}
\rm\zihao{-4}
}%
{\vskip1cm
    \noindent {\bf\zihao{-4} Keywords: }\songti\zihao{-4} \hnu@EnglishKeywords}
```



## 目录与其它的内容的处理

处理完摘要与英文摘要之后就进入目录当中了。目录的编号页也使用罗马数字。目录结束之后，使用正文的编号

```{.nwcode title="hnuthesis.cls"}
\ProvideDocumentCommand{\TableOfContents}{}{
    \newpage \zihao{-4}\chapter*{目录}
    \addcontentsline{toc}{chapter}{目录}
\mainToc\newpage
\pagenumbering{arabic}\setcounter{page}{1}
}
```


还需要完成一系列的工作。比如论文的第一章是绪论。第二章是相关理论基础。最后还有参考文献、硕士期间发表的论文和研究成果，致谢等。其中有一些还涉及到对目录的处理的。

好像有些时候，标题还是需要改换一下。


## 章节标题与编号的问题

好像小节按照1.1这样的编号也可以。但是还是自己使用ctexset自定义的好。

```{.nwcode title="hnuthesis.cls"}
\ctexset{
    chapter/format = \heiti\Large\centering,
    chapter/beforeskip=0pt,
    section/format = \heiti\zihao{4},
    subsection/format=\heiti\zihao{-4},
    subsubsection/format=\heiti
}
```


## 应用于本文类的特殊设置

主要包括：1.因为noweb当中的字体是等宽的，不能正常断行，所以需要加强断行。

```{.nwcode title="hnuthesis.cls"}
\hyphenpenalty=0
\usepackage[htt]{hyphenat}
```
