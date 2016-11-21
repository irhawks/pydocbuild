# 研究生周报的编写[10-14-2015 19:17:16 CST]

一个简单的周报的模板，但是足够精美。首先我们来看csweekly.cls文档。该头文件提供了编写周报的时候必须的环境。

```{.nwcode .latex title="csweekly.cls"}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{csweekly}[2015/08/26 v1.0 海南大学研究生周报]
```

然后是编程特性与一些绘图方面的支持：

```{.nwcode .latex title="csweekly.cls"}
\LoadClass[fontset=adobe,11pt,a4paper]{ctexart}
\RequirePackage{calc,etoolbox,expl3,xparse}

\RequirePackage[x11names,svgnames,table,hyperref]{xcolor}
\usepackage[colorlinks]{hyperref}
\usepackage{tikz}
\usetikzlibrary{shadings}
\usetikzlibrary{decorations.pathmorphing}
\usetikzlibrary{decorations.text}
\usetikzlibrary{decorations.fractals}
%\usetikzlibrary{backgrounds}
\pgfdeclarelayer{background}
\pgfdeclarelayer{foreground}
\pgfsetlayers{background,main,foreground}
\usetikzlibrary{patterns}
\usetikzlibrary{shadows}
\usetikzlibrary{tikzmark}
\usepackage[top=1in,bottom=1in,left=1in,right=0.8in]{geometry}

\RequirePackage[most,minted]{tcolorbox}

\RequirePackage{enumitem}
\setlist{nolistsep}

\RequirePackage{xeCJKfntef}
\usepackage[OT1]{eulervm}
```

周报上面有许多的要求的，包括字体与格式等其它的许许多多的方面。这里我们需要几个特殊的字体，特别是其中的毛体，可能在标题上面显得更好一些。

```{.nwcode .latex title="csweekly.cls"}
\ProvideDocumentCommand{\chuHao}{}{\fontsize{42pt}{80pt}\selectfont}
\ProvideDocumentCommand{\erHao}{}{\fontsize{30pt}{40pt}\selectfont}
\setCJKfamilyfont{hwxk}{csweekly/maoti.ttf}
\newcommand{\maoti}{\CJKfamily{hwxk}}
%\parindent20pt
%\renewcommand{\baselinestretch}{1.3}
```

周报的第一页往往是重点照顾的对象。因为第一页里面有许多的程式化与装饰的内容。当然，实际的周报格式规范还是得参考学校的有关规定才行。一般来说，比较复杂的形状，我们都使用TikZ来绘制。为此我们定义几个方便调用TikZ的命令与设置。其中tikzmark的作用是在当前位置创建一个锚点。

```{.nwcode .latex title="csweekly.cls"}
\tikzstyle{every picture}+=[remember picture]
\def\tikzmark#1{\tikz[remember picture]\coordinate(#1);}
```

研究生周报的题头比较复杂，包括比较复杂的内容。这里我们使用xparse的参数解析定义一个生成题头的命令。下面的该样式的具体内容

```{.nwcode .latex title="csweekly.cls"}
<<提供创建标头的命令>>
```

该样式首先满行写一个海南大学的文字，然后画一个分形的横线，右边是一个柯契曲线，下面是“研究生周报这几个大字，再下面有信息科学技术学院的标题。在研究生周报的右边是一个海南大学的图标，该图标中心最高点正好是柯契曲线的最高点。

```{.nwcode .latex title="提供创建标头的命令"}
\ProvideDocumentCommand{\makeStruct}
{O{csweekly/hainu.png} O{研究生周报}}
{\pagestyle{empty}
    <<csweekly题头第一行的“海南大学”装饰文字>>
    <<csweekly题头的“研究生周报”五个大字以及学院名称>>
    <<csweekly题头的海南大学的图标（放在minipage右边）>>
    <<csweekly题头的网点效果>>
}
```

```{.nwcode .latex title="csweekly题头第一行的“海南大学”装饰文字"}
\noindent\begin{tikzpicture}[remember picture,
decoration=Koch snowflake,
draw=blue,fill=blue!20,thick,
left color=black,right color=blue,circular drop shadow]
    \draw[draw=Indigo] (1\textwidth/5,10pt) node {
        \begin{CJKfilltwosides}{2\textwidth/5-6pt} 
            \large\bfseries 海\hfill 南\hfill 大\hfill 学 
    \end{CJKfilltwosides}};
    \draw[draw=NavyBlue] (0,0) -- (2\textwidth/5,0);
    \draw[draw=NavyBlue!80,decorate,decoration=Cantor set] decorate{ (2\textwidth/5,0) -- (2.5*\textwidth/5,0)};
    \draw[draw=NavyBlue!50] decorate{(2.5\textwidth/5,0) -- (2.8*\textwidth/5,0) };
    \draw[draw=NavyBlue!70] decorate{decorate{ (2.8\textwidth/5,0) -- (3.2*\textwidth/5,0) }};
    \draw[draw=NavyBlue!80] decorate{ decorate{ decorate{ (3.2\textwidth/5,0) -- (4*\textwidth/5,0) }}};
    \draw[draw=NavyBlue] decorate{ decorate{ decorate{ decorate{ (4\textwidth/5,0) -- (\textwidth,0) }}}};
\end{tikzpicture}\\
```

```{.nwcode .latex title="csweekly题头的“研究生周报”五个大字以及学院名称"}
\vskip-30pt\hskip-22pt
\begin{tikzpicture}[remember picture]
    \node(A) at (3.2pt,-1.1pt) {};
    \fill[upper left=NavyBlue, upper right=white] (0,0)  rectangle (\textwidth, 2pt);
\end{tikzpicture}\\\vskip-40pt
\noindent\begin{minipage}[t]{(\textwidth)/4*3}\vspace{0pt}
\vskip25pt
\begin{CJKfilltwosides}{\textwidth}
\sffamily\erHao \color{black} 
研\hfill 究\hfill 生\hfill 周\hfill 报\hfill 告
\end{CJKfilltwosides}\\[15pt]
\noindent\tikz\shade [left color=red!20,right color=blue!20] (0,0) rectangle (1.05\textwidth,1pt);
\noindent\tikz[remember picture]\node(C) at (0,0) {
    \begin{CJKfilltwosides}{1.05\textwidth-6pt}
        信息科学技术学院版
    \end{CJKfilltwosides}
};
\end{minipage}\hfill
```

```{.nwcode .latex title="csweekly题头的海南大学的图标（放在minipage右边）"}
\noindent\tikzmark{LM}\begin{minipage}[t]{(\textwidth-1pt)/5}\vspace{0pt}
    \begin{center}
    \includegraphics[width=3cm]{#1}
\end{center}
\end{minipage}
```

接下来在我们为研究生周报添加网点效果。

```{.nwcode .latex title="csweekly题头的网点效果"}
\begin{tikzpicture}[overlay]
\begin{pgfonlayer}{background}
%    \fill[blue!20,pattern=dots] (LM) rectangle (C.south west);
    \fill[pattern=dots,opacity=0.2] (A.north west) rectangle (C.south east);
\end{pgfonlayer}
\end{tikzpicture}
%\noindent\tikz\shade[upper left=red,upper right=green,
%lower left=blue,lower right=yellow](0,0) rectangle (\textwidth,12pt);
%%\tikz\draw[] (0,0)--(\textwidth,0);
%\noindent\begin{tikzpicture}[decoration={straight zigzag,meta-segment length=1.1cm}]
%    \draw [decorate,fill=yellow!80!black]
%    (0,0) rectangle (\textwidth,12pt);
%\end{tikzpicture}
```

## 添加目录样式

在海南大学周报的第一页，我们想在最下面添加一个目录。目录是多栏的，同时样式又比较丰富，所以使用multicol与etoc宏包。

```{.nwcode .latex title="csweekly.cls"}
\RequirePackage{multicol}
%%目录
\RequirePackage{etoc}
```

提供mainToc这样一个方便制作目录的命令：

```{.nwcode .latex title="csweekly.cls"}
\ProvideDocumentCommand{\mainToc}{}{
\begingroup\parindent 0pt \parfillskip 0pt \leftskip 0cm \rightskip 1cm
\etocsetstyle {section}
{}
{\leavevmode\leftskip 0cm\relax}
{\bfseries\normalsize\makebox[.5cm][l]{\etocnumber.}%
    \etocname\nobreak\hfill\nobreak
\rlap{\makebox[1cm]{\mdseries\etocpage}}\par}
{}
\etocsetstyle {subsection}
{}
{\leavevmode\leftskip .5cm\relax }
{\mdseries\normalsize\makebox[1cm][l]{\etocnumber}%
    \etocname\nobreak\hfill\nobreak
\rlap{\makebox[1cm]{\etocpage}}\par}
{}
\etocsetstyle {subsubsection}
{}
{\leavevmode\leftskip 1.5cm\relax }
{\mdseries\normalsize\makebox[1cm][l]{\etocnumber}%
    \etocname\nobreak\hfill\nobreak
\rlap{\makebox[1cm]{\etocpage}}\par}
{}
%\etocruledstyle[1]{\bfseries \Large My first etoc: TOC}
\etocsettocstyle{}{}
\tableofcontents
\endgroup}
```

周报中表格是非常多见的，我们使用tabularx宏包来制作表格。

```{.nwcode .latex title="csweekly.cls"}
\RequirePackage{tabularx}

\def\tabularxcolumn#1{m{#1}}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}% see tabularx
```


## 添加各种字段

周报汇报的时候总是需要写清楚导师，所填的是与哪个主题相关的。这个时候我们就来设置周报中的各种字段。首先我们定义一种tcolorbox的样式。

```{.nwcode .latex title="csweekly.cls"}
\newtcolorbox{mybox}[1][]{
    enhanced,frame hidden,
    colframe=yellow,
    sharp corners,
    colback=green!7,coltitle=blue!50!black,colbacktitle=blue!20,
    center title,
    boxrule=0pt,toprule=1.25mm,bottomrule=1.25mm,
    extras unbroken and first={
    borderline north={0.25mm}{0.5mm}{blue,decoration={zigzag,amplitude=0.5mm},decorate}},
    extras unbroken and last={
    borderline south={0.25mm}{0.5mm}{blue,decoration={zigzag,amplitude=0.5mm},decorate}},
    #1
}
```

```{.nwcode .latex title="csweekly.cls"}
\tcbset{meta1/.style={enhanced jigsaw,fonttitle=\bfseries\large,fontupper=\large\sffamily,
colback=blue!10!white,colframe=red!50!black,colbacktitle=Salmon!30!white,
%coltitle=black,center title,
leftrule=2pt,rightrule=0pt,toprule=0pt,bottomrule=0pt,boxrule=0pt,frame hidden,
borderline west={1mm}{0mm}{green},
borderline north={1pt}{0mm}{blue!20},
%%borderline south={1pt}{0mm}{blue!20},
tabularx={p{2.5cm}Y}}}
```

第一个关键字的表格是所在单位，指导教师与周报的提交日期。之所以这些东西放在最前面，可能是因为根据周报的逻辑，周报是我们作为打工者向学校递交的某种证明，这种证明是在单位中存放的，所以为了单位的管理的方便，我们都是把与单位相关的信息放在最前面。至于提交者则放在稍靠后的位置。

```{.nwcode .latex title="csweekly.cls"}
\arrayrulecolor{blue!20}
\ProvideDocumentCommand{\makeFirstMeta}{O{信息学院14计算机系} O{} O{\today}}{
\begin{tcolorbox}[meta1,borderline west ={1mm}{0mm}{blue}]
所在单位 & #1 \\ \arrayrulecolor{blue!20}\hline
指导教师 & #2 \\ \arrayrulecolor{blue!20}\hline
提交日期 & #3 \\ \arrayrulecolor{blue!20}\hline
\end{tcolorbox}}
```

实际上，周报的汇表的方式可能是多种多样的。可能是由一个人写，但是其实也是可以允许以整个小组的名义来发送的。或许还得有小组成员的签字。这里的主要的内容就是汇报周报的人与汇报的主题了。

```{.nwcode .latex title="csweekly.cls"}
\ProvideDocumentCommand{\makeSecondMeta}{O{} O{} O{}}{
\begin{tcolorbox}[meta1,borderline west ={1mm}{0mm}{blue!80!black!50}]
所在组 & #1 \\\arrayrulecolor{blue!20}\hline
汇报人 & #2 \\\arrayrulecolor{blue!20}\hline
汇报主题 & #3 \\\arrayrulecolor{blue!20}\hline
\end{tcolorbox}}
```

周报信息与元数据放在最后，是对于周报的内容的概述和总结。

```{.nwcode .latex title="csweekly.cls"}
\ProvideDocumentCommand{\makeThirdMeta}{O{} O{} O{}}{
\begin{tcolorbox}[meta1,borderline west ={1mm}{0mm}{blue!80!green!100}]
摘要 & \rmfamily #1 \\\arrayrulecolor{blue!20}\hline
关键字&\rmfamily #2 \\\arrayrulecolor{blue!20}\hline
其它 & \rmfamily #3 \\\arrayrulecolor{blue!20}\hline
\end{tcolorbox}}
```

就像\LaTeX{}标准文类提供了`\author`{.latex}命令来指定作者字段一样，周报也有很多的要指定的字段，而且也有默认的字段，仿照标准文类，我们为周报定义一系列的字段从而方便周报的编写，让写周报的只需要考虑周报的内容就可以了。

```{.nwcode .latex title="csweekly.cls"}
\ProvideDocumentCommand{\institution}{m}{\gdef\csweekly@institution{#1}}
\gdef\csweekly@institution{信息学院14计算机系}
\ProvideDocumentCommand{\supervisor}{m}{\gdef\csweekly@teacher{#1}}
\gdef\csweekly@teacher{段玉聪}
\ProvideDocumentCommand{\group}{m}{\gdef\csweekly@studentgroup{#1}}
\gdef\csweekly@studentgroup{14计算机系}
\ProvideDocumentCommand{\summary}{m}{\gdef\csweekly@abstract{#1}}
\gdef\csweekly@abstract{}
\ProvideDocumentCommand{\keyword}{m}{\gdef\csweekly@keyword{#1}}
\gdef\csweekly@keyword{--}
\ProvideDocumentCommand{\others}{m}{\gdef\csweekly@others{#1}}
\gdef\csweekly@others{--}
```

最后，所有的生成周报的标题头的工作放在一个makeCsHeaders命令里面，只要有这样的一个命令，就可以生成周报的第一页的内容了，不用我们再管理更细的内容，接下来我们只需要写正文区就可以了，导言区可以尽量地精简。

```{.nwcode .latex title="csweekly.cls"}
\ProvideDocumentCommand{\makeCsHeaders}{}{
\makeStruct \vfill\vfill\vfill
\makeFirstMeta[\csweekly@institution][\csweekly@teacher][\@date]
\vfill
\makeSecondMeta[\csweekly@studentgroup][\@author][\@title]
\vfill
\makeThirdMeta[\csweekly@abstract][\csweekly@keyword][\csweekly@others]
\vfill \vfill \vfill
\def\contentsname{}
\begin{mybox}[breakable]
\begin{multicols}{2}
\mainToc
\end{multicols}
\end{mybox}
\clearpage
}
```

我们在文档开始后添加一个钩子，这样的话不用用户自己手动输入生成周报标题的命令了。

```{.nwcode .latex title="csweekly.cls"}
\AfterBeginDocument{\setcounter{page}{-100}\makeCsHeaders}
```


## 使用示例

下面是使用周报的一个示例文档：

```{.nwcode .latex title="csweekly.tex"}
\documentclass{csweekly}
\usepackage{lipsum}

\institution{信息科学技术学院14计算机科学与技术系}
\supervisor{段}
\date{8月27日}

\group{第一组}
\author{任}
\title{测试标题}

\summary{你好，摘要}
\keyword{你好，关键字}
\others{你好，其它成员}
```

正文的部分是这样的：

```{.nwcode .latex title="csweekly.tex"}
\begin{document}

\begin{multicols}{2}

\section{hello, world}
\subsection{hello, world}
\subsection{hello, world}
\subsubsection{hello, world}
\subsubsection{hello, world}
\section{hello, world}
\subsection{hello, world}
\subsection{hello, world}
\subsubsection{hello, world}
\subsubsection{hello, world}
\section{hello, world}
\subsection{hello, world}
\subsection{hello, world}
\subsubsection{hello, world}
\subsubsection{hello, world}

\section{意见与建议}
\section{参考文献}

\end{multicols}

\end{document}
```


## 添加周记的说明[02-28-2016 09:26:43 CST]

今天把周记的模板添加到这个分类当中去。意思是强调平时的积累的极端的重要性。周记的内容，有些是从平时所读论文中摘抄出来的，也具有一定的意义。记周记是一件长久的工作。这样的话，本卷就有许多文档要生成。


## 接下来来一个示例的周记文档[02-28-2016 09:34:30 CST]

周记应该使用csweekly.cls头文件，然后由于有许多周记，因此每个周记文件需要导出不同的名称。周记文档以csweekly-DATE.tex的格式出现。比如说，这样就可以了。但是要注意周报里面应该有作者与其它的内容。因为我们有周报的手册。

```{.nwcode .latex title="csweekly-sample.tex"}
\documentclass{csweekly}

\author{任呈祥}
\title{周记示范}

\begin{document}

\begin{multicols}{2}

\section{hello, world}
\subsection{hello, world}
\subsection{hello, world}
\subsubsection{hello, world}
\subsubsection{hello, world}
\section{hello, world}
\subsection{hello, world}
\subsection{hello, world}
\subsubsection{hello, world}
\subsubsection{hello, world}
\section{hello, world}
\subsection{hello, world}
\subsection{hello, world}
\subsubsection{hello, world}
\subsubsection{hello, world}

\section{意见与建议}
\section{参考文献}

\end{multicols}

\end{document}
```




## 周报告格式的安排[02-28-2016 20:08:28 CST]

现在回过头来看周报告，则对于那时候周报告的格式的不足之处了解得非常多了。

在研究生的阶段，甚至适用于本科生与博士生的阶段，所做的事情有非常重要的一点就是所有的事情都需要按照时间有序地推进。这种有序推进的性质，不说是所有的人的风格，也至少是大部分的人的风格了。无论是早早工作，还是在做着别的事情；无论是学习科学工程类，还是学习社科艺术类的知识，按照时间有序地推进都非常重要。甚至将工作按照时间有序推进不仅适用于本卷笔记对应的中青年的阶段，对于课题管理，对于第二卷与第三卷也有重大意义。因此，我们不妨在定义我们的人生目标的基础上，总是添加一些按照固定时间计划推进的东西。这样或许就比较完美了。

可能有些人觉得周报告的内容不足以使它单独有一个页面。但是有一张单独的页面或许也是一件不错的事情。如果我们只是向老师说明我们在做什么，那么周报告就不用弄得那么多，更不用\LaTeX{}的格式。但是如果我们自己想得到更多的收获，那么就需要弄好周报了。周报虽然通常只有三页以上，但是似乎单独弄出来一个标题页也不错。而且采用双面排版。这样的话，等到毕业，自己就有许多值得回忆的东西了。

自己现在觉得，写周报告在现在已有的模板的基础上，着重强调以下几个方面，可以进一步改进周报告的排版的质量。

* 全部采用统一的\LaTeX{}的格式，参考文献使用标准的BIBTEX引用系统，任何的文章也都不例外。
* 标题页占单独的一张，这一页是单面打印；其余的页都是双面打印。标题页上面导师、组别、提交日期、汇报主题、关键字、摘要以及其它的说明，还有目录都包含在内了，所以从第二面开始就是正文的内容，直接上各个小节。
* 各个小节可以自由选择是单栏排版或者是双栏排版。根据文本或者图片的大小以及多少作出灵活的调整。但是原则上页面布局中的上下左右间距应该调整好。统一规定周报告使用A4纸还是B5的纸张。
* 在内容排版的时候，从新的一页才开始编号，标题页不进行编页码。新的一页页码位置应该是统一的。除此之外，页面如果合适，应该在页面上留有页眉位置，用于标出当前页所排出来的节或者是小节。
* 公式等内容一般采取标准的、通行的格式。说是内部格式也行。但是要适合于长时间的研究。以后再读的时候，自己依然能够从里面得到知识。
* 最后的也就是最重要的原则，就是内容与格式的分离。做好内容与格式的分离，自己也可以把相关的周报告转成每周讲幻灯片的形式而不用费太大的气力。这样在相对少的时间内，既能同时满足自己日常研究的需求，也能够与其它同学做好交流的工作。
