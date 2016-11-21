# 文书模板写作[09-23-2016 22:52:51 CST]

按照模板来写各种各样的资料。提供了丰富的格式的支持，让研究者可以关注内容。不用花大量的时间留在排版与编辑上。


<!--\chapter{各类文档的\LaTeX{}排版[09-23-2016 22:25:39 CST]}-->

## 文档的特性的选项（以前写的）

### 文档特性的定制

这个时候我们参考GodWorld.cls里面的设置方法，把这些特性添加上去，至于具体设置页边距等，我们还是放在相应的*.cls文件里面。

```{.nwcode .latex title="文档特性设置"}
\RequirePackage[x11names,dvipsnames,svgnames,table]{xcolor}
\definecolor{ocre}{RGB}{243,102,25}
\RequirePackage{tikz}
\RequirePackage{pgfplots}
\pgfplotsset{compat=1.12}
\usetikzlibrary{calc}
\usetikzlibrary{shadows,patterns,decorations.pathmorphing}

\RequirePackage{etex}
\RequirePackage{morewrites}
\RequirePackage{xstring}
\RequirePackage{geometry}
```

这里面包括调用tikz、xcolor、hyperref和multicol在内的多种选项。其中，geometry的设置在三个不同的文体当中是不同的。所以，在各个文类当中再进行设定。

```{.nwcode .latex title="文档特性设置"}
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

```{.nwcode .latex title="文档特性设置"}
\RequirePackage{graphicx} % Required for including pictures
\RequirePackage[multidot,filenameencoding=utf8,space]{grffile}
```

### 字体与符号设置

我们可以在加载文类的时候就使用中文的文类，但是也可以在中间使用ctex的相关的选项。虽然直接使用ctexbook这样的文类会很好，但是可能非常破坏文件的结构性，所以我们还是在语言、字体与符号中使用ctex以及相应的中文的字体的支持。如果想使用中文风格的目录与索引等字，应该在后面逐个修改。或者通过ctexset相关的命令。

加载太多的字体与符号可以显著降低生成文档的速度。所以有时候可能还尽可能减少一些符号的使用。暂时不使用的符号，我们可以先注释掉。

```{.nwcode .latex title="语言、字体与符号设置"}
\RequirePackage[fontset=adobe,zihao=-4,
    heading,sub3section,sub4section]{ctex}
\setmainfont{Adobe Garamond Pro}
\defaultfontfeatures{Mapping=tex-text}
\xeCJKsetup{CJKmath=true}
```

在上面的设置中，如果ctex不使用heading选项，那么就不能通过ctex的接口设置chapter与section的名称。修改sub3section与sub4section是把paragraph与subparagraph的格式都设置成跟section一样，不需要吃掉后面的空格。

```{.nwcode .latex title="语言、字体与符号设置"}
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

```{.nwcode .latex title="公式与定理环境设置"}
\RequirePackage{amsthm}
\RequirePackage{thmtools}
\declaretheorem[name=导师语录]{techwords}
\declaretheorem{Theorem}
%%%% 参考thmtools手册。该宏包的使用是非常方便的。有必要还可以使用cleveref
```


### 风格与样式设置

这里我们不做所谓的风格与样式的太多的定义。太过华丽也不符号毕业论文的风格。但是detail文件可能确实需要比较多的标注，像nowebtrunk之类的东西，以及索引之类的肯定都是要有的。但是后两者就不太需要了。但是我们还是先把资源添加上去。

```{.nwcode .latex title="风格与样式设置"}
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

```{.nwcode .latex title="风格与样式设置"}
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

```{.nwcode .latex title="正文风格设置"}
\RequirePackage{siunitx}
\RequirePackage{empheq}
%%扩展表格功能的宏包
\RequirePackage{booktabs}
\RequirePackage{colortbl}
\RequirePackage{makecell}
\RequirePackage{multirow}
%%提供表格排版的宏包
\RequirePackage{array}
\RequirePackage{tabularx}
%%后续宏包有longtable、ltablex等
\RequirePackage{longtable}
\RequirePackage{tabu}
```

索引等其它的功能我们先不加上去。

### 添加注解

details里面需要很多的脚注与边注这样的记号，这样的记号可以加速文档的编号，提升相关的思想，因此一般还是一定要有

```{.nwcode .latex title="添加remark标记"}
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

```{.nwcode .latex title="加载biblatex"}
\RequirePackage[backend=biber,
    style=caspervector,sorting=centy,utf8,
    sortcites=true,autopunct=true,hyperref=true,url=false,doi=false,
    natbib]{biblatex}
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

```{.nwcode .latex title="加载biblatex/不使用caspervector"}
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

```{.nwcode .latex title="Pandoc的命令选项"}
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
