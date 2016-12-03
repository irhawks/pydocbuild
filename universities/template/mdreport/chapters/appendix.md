%% 在这里添加上附录文献

\appendix


# 编写本文档的方法

本周会记录本身符合hnuthesis.cls的模板文件，使用的也是这个文类。但是光使用这个文类是不够的，还需要引用其它的宏包。因此在引用hnuthesis.cls之后，我们需要引用几类宏包文件。写正常的周报告的时候并不需要引用这些宏包。

首先是noweb宏包。noweb宏包允许我们从.nw文件中生成.tex文件，并且生成的.tex文件中的trunk标记可以正确被定义，常用的方法是：

```{.nwcode title="为本说明文件添加noweb宏包"}
\usepackage{noweb}
\noweboptions{nomargintag,hyperidents,smallcode,longchunks}
%% fix noweb dimen issues
\setlength{\nwdefspace}{0pt}
\setlength{\codehsize}{\textwidth-2\parindent}
```

上面的代码中，我们不仅加载了noweb宏包，而且调整了代码显示的宽度，并且允许代码进行换行，还可以生成代码的索引。

其次，为了使noweb块本身变得更漂亮一些，我们使用了tcolorbox宏包，

```{.nwcode title="为本说明文件添加tcolorbox宏包"}
\usepackage{tcolorbox}
\tcbuselibrary{most,minted}
```

并定义了latexcode、nowebtrunk等环境。

```{.nwcode title="为本说明文件添加tcolorbox宏包"}
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

\newtcolorbox{tColorBoxCommonViolet}[1][]{
	left=0mm,right=0mm,top=2mm,bottom=0mm,breakable,
    enhanced jigsaw,colback=BlueViolet!10,arc=1mm,colframe=BlueViolet!50,
    size=title,boxrule=0.5pt,opacityback=0.8,#1}

\newenvironment{nowebtrunk}[1][]%
    {\begin{tColorBoxCommonViolet}[#1]} %
    {\end{tColorBoxCommonViolet}}
```

特殊的断行设置。在mono字体中默认是不断行的，但是我们要强制让它能够断行。这个时候结合hyphenat宏包实现。

```{.nwcode title="为本说明文件添加hyphennat宏包"}
\hyphenpenalty=0
\usepackage[htt]{hyphenat}
```
