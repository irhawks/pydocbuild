# 缺省模板配置文件


## 模板格式化的文档


```{.nwcode .latex title="模板格式化文档"}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{blue-report}[2016/12/02 v1.0 商业报告计划书]
```

```{.nwcode .latex title="缺省加载的模板"}
\LoadClass[11pt,twoside,a4paper]{article}

\RequirePackage{calc,etoolbox,expl3,xparse}
\RequirePackage[x11names,svgnames,table,hyperref]{xcolor}
\RequirePackage[breaklinks,colorlinks,allcolors=blue]{hyperref}

\RequirePackage{graphicx}
\RequirePackage[table,svgnames]{xcolor}
\RequirePackage{tikz}

\RequirePackage{booktabs}
\RequirePackage{paralist}
\setlength{\pltopsep}{0.0pt}
\setlength{\plitemsep}{0.0pt}

\definecolor{color1}{HTML}{000060}
\definecolor{color2}{HTML}{333333}

%%%----需要Lato Black字体
\RequirePackage{fontspec}
\defaultfontfeatures{Mapping=tex-text}

\RequirePackage{geometry}
\RequirePackage{eso-pic}
```

更高一些的设置标题之类的模板

```{.nwcode .latex title="标题设置与页眉页脚设置"}
\RequirePackage[hang]{caption}
\RequirePackage{titlesec}
\RequirePackage{titletoc}

\RequirePackage{fancyhdr}

\RequirePackage{empheq}
```

## 字段设置

用于批量地制造各类模板

字体之类的也放在fonts目录下作为备用

```{.nwcode .latex title="报告模板"}
\makeatletter
\ProvideDocumentCommand\LogoName{m}{
    \gdef\report@logoname{#1}}
\gdef\report@logoname{}

\ProvideDocumentCommand\Background{m}{
    \gdef\report@background{#1}}
\gdef\report@background{template/cover.png}

\ProvideDocumentCommand\LogoPath{m}{
    \gdef\report@logopath{#1}}
\gdef\report@logopath{template/logo.png}
```

## 设置

字体基本设置

```
\setmainfont{Lato Regular}
\newfontfamily\headingfont{Lato Black}
```

```
\geometry{a4paper,
hmargin=20mm,vmargin=20mm,left=1.4in,right=1in,
head=0ex,foot=3ex,bottom=1.5in}

%%% caption设置
\DeclareCaptionFormat{upper}{#1#2\uppercase{#3}\par}
\captionsetup{labelfont={bf,color=color2},textfont={normalsize,color=color2},format = upper,figurename=FIGURE,tablename=TABLE}

%%% 来自titlesec的titleformat设置
\titleformat{\section}{\color{color1}\headingfont\Large\bfseries\uppercase}{\thesection}{1em}{}[\titlerule]
\titleformat{\subsection}{\color{color1}\headingfont\large\bfseries\uppercase}{\thesubsection}{1em}{}
\titleformat{\subsubsection}{\color{color1}\headingfont\bfseries\uppercase}{\thesubsubsection}{1em}{}

%%% 来自titletoc的titleformat设置
\dottedcontents{section}[0cm]{\bfseries}{0.5cm}{20cm}

%%% fancyhdr的页眉页脚设置(默认的页脚设置)
\linespread{1.5}
\pagestyle{empty}
\fancyfoot[OL,ER]{\color{color2}\thepage}
\pagestyle{fancy}
\renewcommand\headrulewidth{0pt}
\renewcommand\footrulewidth{0pt}
\footskip1cm
\fancyhead[OL,ER]{}
\fancyhead[OC,EC]{}
\makeatletter
\fancyhead[OR,EL]{\color{color2}\@date}
\makeatother
\newlength{\myheight}
\fancyfoot[OR,EL]{\color{color2}\thepage}
\makeatletter
\fancyfoot[OL,ER]{
\settoheight{\myheight}{\thepage}
\raisebox{-2ex-0.5\myheight}{\includegraphics[height=4ex]{\report@logopath}}
}
\makeatletter
\fancyfoot[OC,EC]{\color{color2} \report@logoname }

%%% 背景图片设置
\def\BackgroundPic{%
\put(0,0){%
\parbox[b][\paperheight]{\paperwidth}{%
\vfill
\centering
\includegraphics[width=\paperwidth,height=\paperheight,%
keepaspectratio]{\report@background}%
\vfill
}}}

\DeclareDocumentCommand{\maketitle}{}{
\thispagestyle{empty}
\AddToShipoutPicture*{\BackgroundPic}
%\ClearShipoutPicture
%
\phantom{a}
\vskip-1cm
\phantom{a}\hskip-2cm
\begin{tabular}{l}
	\begin{minipage}{\textwidth}
      \color{white}\headingfont\Huge\@title\\[1em]
  \end{minipage}
\end{tabular}
\vskip3.5cm
\hskip0cm
\begin{tabular}[c]{@{}p{0.8\textwidth}@{}}
      \color{white}\headingfont\LARGE\@author\\[2em]
\end{tabular}
\vfill
\begin{center}\Large \color{white}\@date\phantom{abcdefghikj}\end{center}
%
\pagestyle{empty}\clearpage
\phantom{a}\vfill\begin{center}\large\rm This Page Intentionally Left Blank\end{center}\vfill
    \cleardoublepage
}

\DeclareDocumentCommand{\TableOfContents}{}{
    \tableofcontents
    \cleardoublepage
    %% 正文的开始，使用阿拉伯数字重新编号，从第一页开始
    \pagenumbering{arabic}
    \setcounter{page}{1}
    \fancyfoot[OC,EC]{\color{color2}\report@logoname}
}

%%% 一般情况下，建议直接使用Copyright而不再添加目录了
\DeclareDocumentEnvironment{Copyright}{}
{%%版权声明页---
    \pagenumbering{Roman}
    \setcounter{page}{1}
    \pagestyle{fancy}
    \phantom{a}
    \section*{权利声明}
    \addcontentsline{toc}{section}{权利声明}
    \vskip1cm}
{\cleardoublepage \TableOfContents}

\RequirePackage{ccicons}
\DeclareDocumentCommand{\defaultCopyright}{
```

## fancy boxes, optional

```
\RequirePackage{tcolorbox}
\tcbuselibrary{many}

\RequirePackage{wrapfig}
\def\fullboxbegin{
\bigskip
\begin{tcolorbox}[colback=color1,colframe=color1,coltext=white,arc=0mm,boxrule=0pt]
}
\def\fullboxend{\end{tcolorbox}\medskip}
%
\def\leftboxbegin{
\begin{wrapfigure}{l}{0.5\textwidth}
\begin{tcolorbox}[colback=color1,colframe=color1,coltext=white,arc=0mm,boxrule=0pt]
}
\def\leftboxend{
\end{tcolorbox}
\end{wrapfigure}
}
%
\def\rightboxbegin{
\begin{wrapfigure}{r}{0.5\textwidth}
\begin{tcolorbox}[colback=color1,colframe=color1,coltext=white,arc=0mm,boxrule=0pt]
}
\def\rightboxend{
\end{tcolorbox}
\end{wrapfigure}
}
%
\newcounter{frames}
\def\frameboxbegin#1{
\bigskip
\refstepcounter{frames}
\begin{tcolorbox}[colback=white,colframe=color1,arc=0mm,title={\MakeUppercase{\textbf{Frame \arabic{frames}}: #1}}]
}
\def\frameboxend{
\end{tcolorbox}
}
%%%


\newtcolorbox{otherboxB}[2][]{nobeforeafter,tcbox raise base, enhanced,frame hidden,boxrule=0pt,interior style={top color=green!10!white, bottom color=green!10!white,middle color=blue!20},fuzzy halo=1pt with green,title=#2,fonttitle={\bfseries\color{black}},#1}
\newtcolorbox{otherboxG}[2][]{nobeforeafter,tcbox raise base, enhanced,frame hidden,boxrule=0pt,interior style={top color=green!10!white, bottom color=green!10!white,middle color=green!20},fuzzy halo=1pt with green,title=#2,fonttitle={\bfseries\color{black}},#1}
\newtcolorbox{otherboxY}[2][]{nobeforeafter,tcbox raise base, enhanced,frame hidden,boxrule=0pt,interior style={top color=green!10!white, bottom color=green!10!white,middle color=yellow!20},fuzzy halo=1pt with green,title=#2,fonttitle={\bfseries\color{black}},#1}


\newcolumntype{Y}{>{\raggedleft\arraybackslash}X}% see tabularx
\RequirePackage{array,tabularx}

\captionsetup[table]{skip=,}
\def\tabcaption#1{\captionof{table}{#1}}

\newtcolorbox{ctable}[2][]{%
enhanced,fonttitle=\bfseries\large,fontupper=\normalsize\sffamily,colback=yellow!10!white,colframe=blue!50!black,colbacktitle=blue!40!white, coltitle=black,center title,title={#2},#1}
```
