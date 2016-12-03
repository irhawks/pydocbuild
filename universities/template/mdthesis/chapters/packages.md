# 模板文件

\normalsize

## 工作计划[10-24-2016 17:46:48 CST]

本小节来记录自己期望对这节内容所做的改进。在使用的宏包上，当前还是存在许多的不足的。许多的时候，因为文体的限制，我们必须要添加一些能够排版代码的宏包。如果不能排版代码，将会给我们造成极大的损失。

## 文类概述


在写模板的时候也按照写\LaTeX{}文类的标准的过程。首先写文类，然后写需要加载的宏包，然后定义一系列的变量，最后设计本文类特有的一些风格元素。

```{.nwcode title="hnuthesis.cls"}
<<hnuthesis.cls的文类定义>>
<<hnuthesis.cls的核心宏包>>
<<hnuthesis.cls的元素设置>>
<<hnuthesis.cls的变量定义>>
<<hnuthesis.cls的外观风格>>
```

csweekly的文类名为csweekly，版本是2015年08月版本，类型是海南大学研究生周报

```{.nwcode title="hnuthesis.cls的文类定义"}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hnuthesis}[2016/10/24 v1.1 海南大学 硕士研究生毕业论文模板]
```




## 核心宏包

hnuthesis.cls首先在语言上需要支持中文，页面最好是固定的A4纸。最好也能够包含彩色与链接。因此tikz等宏包也包含在内。
```{.nwcode title="hnuthesis.cls的核心宏包"}
\LoadClass[zihao=-4,a4paper,oneside]{ctexbook}
\RequirePackage{calc,etoolbox,expl3,xparse}

\RequirePackage[x11names,svgnames,table,hyperref]{xcolor}
\RequirePackage[colorlinks,breaklinks,linkcolor=black]{hyperref}
```

对于ctex宏包，我们希望一开始的时候都把标准的字体设置成-4号字体。这样的话就不用在正文当中显式地改变基准字体的大小了。

```{.nwcode title="hnuthesis.cls的核心宏包"}
\RequirePackage{tikz}
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
%\usepackage[margin=1in]{geometry}
%% 几何设置按照海南大学硕士论文的要求进行

%%% 显然加载graphicx等宏包也是必须的设置
\RequirePackage[left=3.0cm,right=2.5cm, top=2.5cm,bottom=2.5cm,includeheadfoot]{geometry}
%%% 纠正图片加载的时候的一些错误。（比如不能正确处理点号与空格）
\RequirePackage{graphicx}
\RequirePackage[multidot,filenameencoding=utf8,space]{grffile}

```

geometry的includeheadfoot选项可以使得排版的时候尽量使整体保持在一定的范围之内。

## 界面风格的元素的设置


```{.nwcode title="hnuthesis.cls的核心宏包"}
%\RequirePackage[most,minted]{tcolorbox}
\RequirePackage[most]{tcolorbox}
```

### 元素设置

有些设置我们在geometry当中已经定了。比如我们需要的页面设置。但是像下划线之类的我们可能还没有使用。还有数学符号。浮动体等的支持也没有提及。这些特性宏包的调用与支持即称为所谓的\emph{元素设置}。

```{.nwcode title="hnuthesis.cls的元素设置"}
\RequirePackage{xeCJKfntef}
%\ProvideDocumentCommand{\chuHao}{}{\fontsize{42pt}{80pt}\selectfont}
%\ProvideDocumentCommand{\erHao}{}{\fontsize{20pt}{30pt}\selectfont}
```

设置多栏与目录的排版

```{.nwcode title="hnuthesis.cls的元素设置"}
\RequirePackage{multicol}
%%目录
\RequirePackage{etoc}
\ProvideDocumentCommand{\mainToc}{}{
\begingroup\parindent 0pt \parfillskip 0pt \leftskip 0cm \rightskip 1cm
\etocsetstyle {chapter}
{}
{\leavevmode\leftskip 0cm\relax}
    {{\heiti\etocnumber
    \etocname}\hspace{5pt}\nobreak\dotfill\nobreak
    \rlap{\makebox[1.0cm][r]{\heiti\etocpage}}\par}
{}
\etocsetstyle {section}
{}
{\leavevmode\leftskip 0.5cm\relax}
{\normalsize\makebox[1cm][l]{\etocnumber}%
    \etocname\hspace{5pt}\nobreak\dotfill\nobreak
    \rlap{\makebox[1cm][r]{\mdseries\etocpage}}\par}
{}
\etocsetstyle {subsection}
{}
{\leavevmode\leftskip 1.0cm\relax }
{\songti\normalsize\makebox[1.5cm][l]{\etocnumber}%
    \etocname\hspace{5pt}\nobreak\dotfill\nobreak
    \rlap{\makebox[1cm][r]{\etocpage}}\par}
{}
\etocsetstyle {subsubsection}
{}
{\leavevmode\leftskip 1.5cm\relax }
{\normalsize\makebox[1.5cm][l]{\etocnumber}%
    \etocname\hspace{5pt}\nobreak\dotfill\nobreak
    \rlap{\makebox[1cm][r]{\etocpage}}\par}
{}
%\etocruledstyle[1]{\bfseries \Large My first etoc: TOC}
\etocsettocstyle{}{}
\tableofcontents
\endgroup}

%%% 设置目录的时候，对目录应该编号到那个层次也有说明，一般是编号到subsection，也就是第二级吧。
\setcounter{secnumdepth}{2}  
\setcounter{tocdepth}{2}  
```


表格与数学公式支持

```{.nwcode title="hnuthesis.cls的元素设置"}
\RequirePackage{tabu}
%\tabulinesep=_0pt^5pt
\extrarowsep=_-3pt^5pt
%%% 将tabcolsep设置为0pt有助于将在封面中的字段对齐到缩进24pt的位置，不会产生位置差
\tabcolsep=0pt
\RequirePackage{booktabs}

%%% 附加的表格的环境。
\RequirePackage{colortbl}
\RequirePackage{makecell}
\RequirePackage{multirow}
%%% 如果需要长的宏包的话，就添加长的宏包。
\RequirePackage{longtable}
```

下面是设置列表环境。等。
```{.nwcode title="hnuthesis.cls的元素设置"}
\RequirePackage{paralist}
\RequirePackage{enumitem}
\setlist{nolistsep}

%%% 减少paralist相关环境当中的缩进值。
\setlength{\pltopsep}{0.0pt}
\setlength{\plitemsep}{0.0pt}

%%% 字体与公式设置
\defaultfontfeatures{Mapping=tex-text}
\xeCJKsetup{CJKmath=true}

\everydisplay{
\abovedisplayskip0pt plus 1pt 
\abovedisplayshortskip0pt plus 1pt 
\belowdisplayskip1pt plus 1pt 
\belowdisplayshortskip1pt plus 1pt 
}

\RequirePackage{fancyhdr}
```

```{.nwcode title="普通的字距等距离的设置"}
\renewcommand{\CJKglue}{\hskip 1pt plus 3pt minus 0.6pt}
\setlength{\parskip}{0.75ex plus .2ex minus .5ex}
\renewcommand{\baselinestretch}{1.2}
\linespread{1.5}
```


数学公式的附加包（根据需要进行添加）

```{.nwcode title="附加的数学符号与公式"}
\RequirePackage[fleqn,nointlimits,sumlimits,fixamsmath]{mathtools}
\RequirePackage{amsfonts,amssymb}
\RequirePackage{mathptmx}
\RequirePackage{mathrsfs}
\RequirePackage{latexsym}
\RequirePackage{texnames}
\RequirePackage{mflogo}
\RequirePackage[OT1,euler-digits]{eulervm}
\RequirePackage{MnSymbol}

%%% 如果需要单位符号，以及对公式的强调，使用这个宏包。
\RequirePackage{siunitx}
\RequirePackage{empheq}
```

其中，为了排版方块（Checkbox），必须加载amssymb宏包）。

```{.nwcode title="hnuthesis.cls的元素设置"}
\RequirePackage[fleqn,nointlimits,sumlimits,fixamsmath]{mathtools}
\RequirePackage{amsfonts,amssymb}
```

根据需要，还可以选择自己期望的数学定理的环境

```{.nwcode title="附加的数学定理与环境"}
\RequirePackage{amsthm}
\RequirePackage{thmtools}
%%%% 参考thmtools手册。该宏包的使用是非常方便的。有必要还可以使用cleveref
```


### 代码环境的排版

对代码的排版推荐使用minted宏包，加上tcolorbox。

```{.nwcode title="附加的代码排版环境"}
\RequirePackage{minted}
\newmintinline[TC]{latex}{breaklines,breakanywhere,showspaces}
\usepackage{tcolorbox}
\tcbuselibrary{most,minted}
\DeclareTCBListing{latexcode}{ O{} }{%
    listing engine=minted,minted style=colorful,
    minted language=latex,
    minted options={breaklines,breakanywhere,
        fontsize=\small,linenos,numbersep=3mm},
    colback=blue!10!white,colframe=blue!40,
    arc=1mm,boxrule=0.5pt,
    listing only,
    %size=title,
    left=5mm,top=0mm,bottom=0mm,
    enhanced jigsaw,opacityback=0.5,breakable,
    interior style={%
        left color=blue!30!white, right color=blue!10},
    overlay={%
        \begin{tcbclipinterior}
            \fill[red!20!blue!20!white] (frame.south west) %
                rectangle ([xshift=5mm]frame.north west);
        \end{tcbclipinterior}},#1}

\newtcolorbox{tColorBoxCommonViolet}[1][]{left=0mm,right=0mm,top=2mm,bottom=0mm,breakable,
    enhanced jigsaw,colback=BlueViolet!10,arc=1mm,colframe=BlueViolet!50,
    size=title,boxrule=0.5pt,opacityback=0.8,#1}

\newenvironment{nowebtrunk}[1][]%
    {\begin{tColorBoxCommonViolet}[#1]} %
    {\end{tColorBoxCommonViolet}}
```

```{.nwcode title="hnuthesis.cls"}
<<附加的代码排版环境>>
```


想自由地控制浮动体，可以使用float宏包

```{.nwcode title="对浮动体的更多的控制"}
\RequirePackage{float}
```

### 风格化设置

```{.nwcode title="hnuthesis.cls的变量定义"}
\hypersetup{pdftitle={\@title},
pdfauthor={\@author}}
```


### 外观风格设置

```{.nwcode title="hnuthesis.cls的外观风格"}

```

为了更方便调用，我们设置在文档开始的时候自动排版第一页（makeCsHeaders）
```{.nwcode title="hnuthesis.cls的外观风格(暂时不用)"}
\AfterBeginDocument{\setcounter{page}{-100}
%\pagestyle{fancy}
%\setcounter{page}{1}}
```



## 参考文献

```{.nwcode title="附加的文献与引用系统"}
\RequirePackage[backend=biber, style=caspervector,utf8,
    sortcites=true,autopunct=true,hyperref=true,
%    citestyle=authoryear-icomp,
    natbib]{biblatex}
```

```{.nwcode title="hnuthesis.cls"}
<<附加的文献与引用系统>>
```


定制标题的话，可以使用titlesec。当然，ctexset也提供了更改标题格式的一系列的命令。

```{.nwcode title="定制标题"}
%\RequirePackage{titlesec}
```


## 字体的设置


中文字体当中，我们还需要添加一个华文行楷，因为排版海南大学的图标的时候要用到。

```{.nwcode title="hnuthesis.cls的外观风格"}
\setCJKfamilyfont{xingkai}{STXINGKA.TTF}
\newcommand{\xingkai}{\CJKfamily{xingkai}}
%%% 设置字体为Charis SIL字体，如果没有，还可以改正。
\setmainfont{Charis SIL}
%%% 还有就是使用的字体当中，最好不使用穷人的黑体，加粗直接使用黑体，不使用加粗的宋体。
```

### abc我们的小节

#### defghi我们小节小小节
