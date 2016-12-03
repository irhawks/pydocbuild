# 模板文件(附加的和多余的元素，由用户自行添加[11-21-2016 11:01:20 CST]

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


## 在开题报告当中的模板文件设置[11-21-2016 09:44:50 CST]


<!-- \chapter{文书模板写作[09-23-2016 22:52:51 CST]}来自于ENDO.131分类的document-general.md -->

\refsection

按照模板来写各种各样的资料。提供了丰富的格式的支持，让研究者可以关注内容。不用花大量的时间留在排版与编辑上。


## 文档的特性的选项（以前写的）

### 文档特性的定制

```{.nwcode title="多栏选项设置（可选项）"}
\RequirePackage{multicol}
\RequirePackage[breaklinks,colorlinks,linkcolor=blue]{hyperref}
\hypersetup{ %hidelinks,
    backref=true,pagebackref=true,%
    hyperindex=true,colorlinks=true,breaklinks=true,%
    colorlinks,%urlcolor=red,
    allcolors=black,
    bookmarks=true,bookmarksopen=false,%
}
```

这些特性，应该说是基本上不影响层次标题等层次性的设置。

## 字体与符号设置（宽松的与多余的，可以选择性地加到开题报告当中

```{.nwcode title="设置数学公式与常见的包"}
\RequirePackage[fleqn,nointlimits,sumlimits,fixamsmath]{mathtools}
\RequirePackage{amsfonts,amssymb}
\RequirePackage{mathptmx}
\RequirePackage{mathrsfs}
\RequirePackage{latexsym}
\RequirePackage{texnames}
\RequirePackage{mflogo}
\newcommand{\intoo}[2]{\mathopen{]}#1\,;#2\mathclose{[}}
\newcommand{\ud}{\mathop{\mathrm{{}d}}\mathopen{}}
\newcommand{\intff}[2]{\mathopen{[}#1\,;#2\mathclose{]}}
\RequirePackage[euler-digits]{eulervm}
\RequirePackage{MnSymbol}

\def\mff#1{\hbox{$\mathfrak{#1}$}}
\def\mbf#1{\hbox{$\mathbf  {#1}$}}
\def\mbf#1{\hbox{$\pmb     {#1}$}}
\def\mbb#1{\hbox{$\mathbb  {#1}$}}
\def\msc#1{\hbox{$\mathscr {#1}$}}
%\def\AA{\hbox{$\mathbb A$}}
\def\CC{\hbox{$\mathbb C$}}
\def\HH{\hbox{$\mathbb H$}}
\def\NN{\hbox{$\mathbb N$}}
\def\QQ{\hbox{$\mathbb Q$}}
\def\RR{\hbox{$\mathbb R$}}
\def\TT{\hbox{$\mathbb T$}}
\def\ZZ{\hbox{$\mathbb Z$}}

\def\dim{\hbox{\rm dim}}
\def\sgn{\hbox{\rm sgn}}
\def\d{\hbox{\rm d}}

\def\dom{\hbox{\rm dom}}
\def\ran{\hbox{\rm ran}}
\def\FLD{\hbox{\rm FLD}}

\def\det#1{\hbox{$\mathrm{det} #1$}}


%\RequirePackage{eufrak}
%\RequirePackage{eucal}
%\RequirePackage{mathrsfs}
%\RequirePackage[euler-digits,euler-hat-accent]{eulervm}
%\RequirePackage{bbold}
%\RequirePackage{MnSymbol}
%\RequirePackage{mflogo}
%\RequirePackage{metalogo}
%\RequirePackage{xltxtra}
```

### 公式与定理环境设置[09-24-2016 15:56:24 CST]

```{.nwcode title="公式与定理环境设置"}
\RequirePackage{amsthm}
\RequirePackage{thmtools}
\declaretheorem[name=导师语录]{techwords}
\declaretheorem{Theorem}
%%%% 参考thmtools手册。该宏包的使用是非常方便的。有必要还可以使用cleveref
```


### 风格与样式设置

这里我们不做所谓的风格与样式的太多的定义。太过华丽也不符号毕业论文的风格。但是detail文件可能确实需要比较多的标注，像nowebtrunk之类的东西，以及索引之类的肯定都是要有的。但是后两者就不太需要了。但是我们还是先把资源添加上去。

```{.nwcode title="风格与样式设置"}
\RequirePackage[framemethod=tikz,xcolor]{mdframed}
\RequirePackage[draft]{minted}
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
```

```{.nwcode title="风格与样式设置"}
\RequirePackage{float}

\RequirePackage{paralist}
\setlength{\pltopsep}{0.0pt}
\setlength{\plitemsep}{0.0pt}
\RequirePackage{enumitem} % Customize lists
\setlist{nolistsep} % Reduce spacing

\newtcolorbox{tColorBoxCommonViolet}[1][]{left=0mm,right=0mm,top=2mm,bottom=0mm,breakable,
    enhanced jigsaw,colback=BlueViolet!10,arc=1mm,colframe=BlueViolet!50,
    size=title,boxrule=0.5pt,opacityback=0.8,#1}
\newenvironment{nowebtrunk}[1][]%
    {\begin{tColorBoxCommonViolet}[#1]} %
    {\end{tColorBoxCommonViolet}
}
%\renewcommand{\CJKglue}{\hskip 1pt plus 0.08\baselineskip minus 0.5pt}
\renewcommand{\CJKglue}{\hskip 1pt plus 3pt minus 0.6pt}
\setlength{\parskip}{0.75ex plus .2ex minus .5ex}
\renewcommand{\baselinestretch}{1.2}
\linespread{1.5}
```

### 索引与表格等元素

```{.nwcode title="正文风格设置"}
\RequirePackage{siunitx}
\RequirePackage{empheq}
```

索引等其它的功能我们先不加上去。

### 添加注解

details里面需要很多的脚注与边注这样的记号，这样的记号可以加速文档的编号，提升相关的思想，因此一般还是一定要有

```{.nwcode title="添加remark标记"}
\tikzset{remarksymbol/.style={
        rectangle,draw=red,
        fill=white,scale=1,overlay}}
\mdfdefinestyle{remark}{%
    hidealllines=true,leftline=true,
    skipabove=12,skipbelow=12pt,
    innertopmargin=0.4em,%
    innerbottommargin=0.4em,%
    innerrightmargin=0.7em,%
    rightmargin=0.7em,%
    innerleftmargin=1.7em,%
    leftmargin=0.7em,%
    middlelinewidth=.2em,%
    linecolor=red,%
    fontcolor=red,%
    firstextra={\path let \p1=(P), \p2=(O) in ($(\x2,0)+0.5*(0,\y1)$)
    node[remarksymbol] {注};},%
    secondextra={\path let \p1=(P), \p2=(O) in ($(\x2,0)+0.5*(0,\y1)$)
    node[remarksymbol] {注};},%
    middleextra={\path let \p1=(P), \p2=(O) in ($(\x2,0)+0.5*(0,\y1)$)
    node[remakrsymbol] {注};},%
    singleextra={\path let \p1=(P), \p2=(O) in ($(\x2,0)+0.5*(0,\y1)$)
    node[remarksymbol] {注};},%
}
\newmdenv[style=remark]{remark}
```

### 参考文献与索引的设置

现在我们先设置参考文献吧。有一些选项是在加载biblatex\parencite{biblatex}的包的时候必须设定的，有一些则可以通过命令单独设置。通过\cite[文献][第3.1.1节]{biblatex}，我们知道，backend、style、bibstyle、citestyle、natbib、mcite相关的选项是必须在加载宏包的时候就要设定的。所以我们也需要在总文件中有载它。

```{.nwcode title="加载biblatex"}
\RequirePackage[backend=biber,
    style=caspervector,sorting=centy,utf8,
    sortcites=true,autopunct=true,hyperref=true,url=false,doi=false,
    natbib]{biblatex}
```

```{.nwcode title="正文中应该出现的biblatex选项}
\addbibresource{citation/ref-format.bib}
\addbibresource{citation/ref-service.bib}
\addbibresource{citation/chinese.bib}

\addbibresource{citation/readme.bib}
\addbibresource{citation/classmate.bib}
\addbibresource{citation/Duan_Yucong.bib}
\addbibresource{citation/nuSMV.bib}
\addbibresource{citation/modelcheck-cn.bib}
\addbibresource{citation/xaas-mainref.bib}
\addbibresource{citation/xaas-references.bib}
\addbibresource{citation/xaas-surveyed.bib}
\addbibresource{citation/1104.bib}
\addbibresource{citation/udod-references.bib}
\addbibresource{citation/life-references.bib}
\addbibresource{citation/report.bib}
\addbibresource{citation/contract.bib}

\DeclareSourcemap{
\maps[overwrite]{
  \map{\step[typesource=article, fieldset=type,fieldvalue={J}]}
  \map{\step[typesource=book, fieldset=type,fieldvalue={M}]}
  \map{\step[typesource=inbook,fieldset=type,fieldvalue={M}]}
  \map{\step[typesource=collection,fieldset=type,fieldvalue={M}]}
  \map{\step[typesource=incollection,fieldset=type,fieldvalue={M}]}
  \map{\step[typesource=manual,fieldset=type,fieldvalue={M/OL}]}
  \map{\step[typesource=online,fieldset=type,fieldvalue={M/OL}]}
  \map{\step[typesource=patent,fieldset=type,fieldvalue={S}]}
  \map{\step[typesource=periodical,fieldset=type,fieldvalue={J}]}
  \map{\step[typesource=proceedings,fieldset=type,fieldvalue={C}]}
  \map{\step[typesource=inproceedings,fieldset=type,fieldvalue={C}]}
  \map{\step[typesource=reference,fieldset=type,fieldvalue={M/OL}]}
  \map{\step[typesource=inreference,fieldset=type,fieldvalue={M/OL}]}
  \map{\step[typesource=report,fieldset=type,fieldvalue={R}]}
  \map{\step[typesource=thesis,fieldset=type,fieldvalue={D}]}
  \map{\step[typesource=unpublished,fieldset=type,fieldvalue={M}]}
  \map{\step[typesource=conference,fieldset=type,fieldvalue={C}]}
  \map{\step[typesource=masterthesis,fieldset=type,fieldvalue={D}]}
  \map{\step[typesource=phdthesis,fieldset=type,fieldvalue={D}]}
  \map{\step[typesource=techreport,fieldset=type,fieldvalue={R}]}
}
}
```

```{.nwcode title="加载biblatex/不使用caspervector"}
\RequirePackage[backend=biber,
    sortcites=true,autopunct=true,hyperref=true,
    citestyle=authoryear-icomp,
    natbib]{biblatex}
\addbibresource{citation/ref-format.bib}
\addbibresource{citation/ref-service.bib}
\addbibresource{citation/chinese.bib}
```

注意这里我们后端使用biber[@biber]，而索引的格式选用caspervector[@caspervector]。目前来看两者都是比较有缺陷的格式。但是目前也只好这样了。casper-vector对于国家标准文献著录格式[@gbt7714-2005]做了一些修改。另外，如果没有utf8选项，那么在分析论文的时候仍然会导致错误。

我们在这里设置工程中所有需要引用的文献，无论是关于排版参考方面的还是关于选题讨论的，无论是是出现在论文的正文当中，我们都使用统一的文件。这样的话，便于同时管理各个文献。

使用caspervector的时候，使用parencite产生的是方括号的引用标记，使用cite产生的只是一个引用的符号，使用supercite产生的引用标记被方括号括起来，且是上标的形式。这几种引用的方式都是biblatex中已经存在的。所以以后我们还是得使用parencite或者supercite。另外，在索引的命令的前后都可以添加中括号里面的开选元素。

注意每个论文的biblatex可能的区别。在主说明当中，因为需要经常查看论文，所以使用一种清晰的格式是非常必要的。这个时候可以不使用caspervector。


## Pandoc的头文件当中需要包括的内容[11-20-2016 21:52:36 CST]

在将.md转换成.nw文档的时候，注意nw文档的头文件当中应该包括pandoc的那些特殊符号的解释符号，具体如下：

```{.nwcode title="Pandoc的命令选项"}
\RequirePackage{lmodern}
%\RequirePackage{amssymb,amsmath}
\RequirePackage{ifxetex,ifluatex}
\RequirePackage{fixltx2e} % provides \textsubscript
%\defaultfontfeatures{Ligatures=TeX,Scale=MatchLowercase}

% use upquote if available, for straight quotes in verbatim environments
\IfFileExists{upquote.sty}{\usepackage{upquote}}{}

\RequirePackage{fancyvrb}
\newcommand{\VerbBar}{|}
\newcommand{\VERB}{\Verb[commandchars=\\\{\}]}
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\}}
% Add ',fontsize=\small' for more characters per line
\newenvironment{Shaded}{}{}
\newcommand{\KeywordTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{\textbf{{#1}}}}
\newcommand{\DataTypeTok}[1]{\textcolor[rgb]{0.56,0.13,0.00}{{#1}}}
\newcommand{\DecValTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
\newcommand{\BaseNTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
\newcommand{\FloatTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
\newcommand{\ConstantTok}[1]{\textcolor[rgb]{0.53,0.00,0.00}{{#1}}}
\newcommand{\CharTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
\newcommand{\SpecialCharTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
\newcommand{\StringTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
\newcommand{\VerbatimStringTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
\newcommand{\SpecialStringTok}[1]{\textcolor[rgb]{0.73,0.40,0.53}{{#1}}}
\newcommand{\ImportTok}[1]{{#1}}
\newcommand{\CommentTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textit{{#1}}}}
\newcommand{\DocumentationTok}[1]{\textcolor[rgb]{0.73,0.13,0.13}{\textit{{#1}}}}
\newcommand{\AnnotationTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textbf{\textit{{#1}}}}}
\newcommand{\CommentVarTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textbf{\textit{{#1}}}}}
\newcommand{\OtherTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{{#1}}}
\newcommand{\FunctionTok}[1]{\textcolor[rgb]{0.02,0.16,0.49}{{#1}}}
\newcommand{\VariableTok}[1]{\textcolor[rgb]{0.10,0.09,0.49}{{#1}}}
\newcommand{\ControlFlowTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{\textbf{{#1}}}}
\newcommand{\OperatorTok}[1]{\textcolor[rgb]{0.40,0.40,0.40}{{#1}}}
\newcommand{\BuiltInTok}[1]{{#1}}
\newcommand{\ExtensionTok}[1]{{#1}}
\newcommand{\PreprocessorTok}[1]{\textcolor[rgb]{0.74,0.48,0.00}{{#1}}}
\newcommand{\AttributeTok}[1]{\textcolor[rgb]{0.49,0.56,0.16}{{#1}}}
\newcommand{\RegionMarkerTok}[1]{{#1}}
\newcommand{\InformationTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textbf{\textit{{#1}}}}}
\newcommand{\WarningTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textbf{\textit{{#1}}}}}
\newcommand{\AlertTok}[1]{\textcolor[rgb]{1.00,0.00,0.00}{\textbf{{#1}}}}
\newcommand{\ErrorTok}[1]{\textcolor[rgb]{1.00,0.00,0.00}{\textbf{{#1}}}}
\newcommand{\NormalTok}[1]{{#1}}

\setlength{\parindent}{24pt}
\setlength{\parskip}{1pt plus 1pt minus 1pt}

\setlength{\emergencystretch}{3em}  % prevent overfull lines
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
% Redefines (sub)paragraphs to behave more like sections
\ifx\paragraph\undefined\else
\let\oldparagraph\paragraph
\renewcommand{\paragraph}[1]{\oldparagraph{#1}\mbox{}}
\fi
\ifx\subparagraph\undefined\else
\let\oldsubparagraph\subparagraph
\renewcommand{\subparagraph}[1]{\oldsubparagraph{#1}\mbox{}}
\fi

%%%%---------------------------------------------------------------

%\setmainfont{Charis SIL}
```


## 制作目录的时候的配置

开题报告本身是不需要目录的。但是我们在生成开题报告的时候，最好还是自己带一个目录吧。

处理完摘要与英文摘要之后就进入目录当中了。目录的编号页也使用罗马数字。目录结束之后，使用正文的编号

```{.nwcode title="为模板文件添加一个目录"}
\ProvideDocumentCommand{\TableOfContents}{}{
    \newpage \zihao{-4}\chapter*{目录}
    \addcontentsline{toc}{chapter}{目录}
\mainToc\newpage
\pagenumbering{arabic}\setcounter{page}{1}
}
```


## NOWEB的一些需要的宏包设置

主要包括：1.因为noweb当中的字体是等宽的，不能正常断行，所以需要加强断行。

```{.nwcode title="noweb宏包的断行选项"}
\hyphenpenalty=0
\usepackage[htt]{hyphenat}
```

