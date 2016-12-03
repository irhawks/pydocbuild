# 整个论文的版面设计的排版(核心元素)[11-21-2016 11:01:46 CST]

# 开题报告的模板文件的结构[11-21-2016 10:49:39 CST]


## 文类所需要的基本软件包[11-21-2016 10:53:53 CST]


首先我们需要分析开题报告模板需要哪些基本的元素。也就是基本的宏包。注意制作模板的时候我们只添加最基本的宏包，至于数学符号等可选的项目我们暂时不添加。

把这些特性添加上去，至于具体设置页边距等，我们还是放在相应的*.cls文件里面。

1. 无论做什么，首先都需要让latex具有足够多的编程性。比如检索引擎，添加tikz绘图支持等，添加latex3的命令等。
2. 开题报告有一些基本的模板需要制作，比如需要在模板当中插入表格以及插入海南大学的图片，因此表表格支持与图片支持也添加上去。

```{.nwcode title="提升latex编程能力的宏包"}
\RequirePackage[x11names,dvipsnames,svgnames,table,hyperref]{xcolor}

\definecolor{ocre}{RGB}{243,102,25}
\RequirePackage{etex}
\RequirePackage{morewrites}
\RequirePackage{xstring}
\RequirePackage{xparse}

\RequirePackage{tikz}
\RequirePackage{pgfplots}
\pgfplotsset{compat=1.13}
\usetikzlibrary{calc}
\usetikzlibrary{shadows,patterns,decorations.pathmorphing}
```

### 在确定封面字段之前准备好tabu软件包，以制来制作标题栏的表格

```{.nwcode title="模板风格化元素/表格元素"}
%%扩展表格功能的宏包
\RequirePackage{booktabs}
\RequirePackage{colortbl}
\RequirePackage{makecell}
\RequirePackage{multirow}
%%提供表格排版的宏包
%\RequirePackage{array}
\RequirePackage{tabularx}
%%后续宏包有longtable、ltablex等
\RequirePackage{longtable}
\RequirePackage{tabu}
```

### 图片加载所需要的软件包

```{.nwcode title="模板风格化元素/插图元素"}
\RequirePackage{graphicx} % Required for including pictures
\RequirePackage[multidot,filenameencoding=utf8,space]{grffile}
```

这里面包括调用tikz、xcolor、hyperref和multicol在内的多种选项。其中，geometry的设置在三个不同的文体当中是不同的。所以，在各个文类当中再进行设定。


## 模板的基本设置[11-21-2016 13:36:22 CST]

### 页面设置

根据开题报告的要求，页边距设置为左右1英寸，上下3厘米。

```{.nwcode title="设置页面布局"}
\RequirePackage[includeall,margin=1in,top=3cm,bottom=3cm]{geometry}

% 加载基本软件包之包，设置文档的页边距属性
\geometry{margin=1in,top=3cm,bottom=3cm}
```

### 语言、字体与字号设置

统一的选项指的是各种特性，但是还需要专门针对开题报告进行设置。比如特殊的一些命令与格式。标准的开题报告使用的字体与其它的样式都和Linux下面的设置有一些不同，为了使两者更像，我们使用Windows的字体，并且调整好间距我们可以在加载文类的时候就使用中文的文类，但是也可以在中间使用ctex的相关的选项。虽然直接使用ctexbook这样的文类会很好，但是可能非常破坏文件的结构性，所以我们还是在语言、字体与符号中使用ctex以及相应的中文的字体的支持。如果想使用中文风格的目录与索引等字，应该在后面逐个修改。或者通过ctexset相关的命令。

加载太多的字体与符号可以显著降低生成文档的速度。所以有时候可能还尽可能减少一些符号的使用。暂时不使用的符号，我们可以先注释掉。


```{.nwcode title="设置语言、字体与字号"}
\RequirePackage[fontset=adobe,zihao=-4,
    heading,sub3section,sub4section]{ctex}
\defaultfontfeatures{Mapping=tex-text}
\xeCJKsetup{CJKmath=true}

% \ctexset{zihao=-4} zihao只能在加载ctex的时候才能使用。
\setCJKmainfont{SimSun}
\setCJKsansfont{KaiTi\_GB2312}
\setCJKmonofont{SimHei}
\xeCJKsetup{AutoFakeBold=true,AutoFakeSlant=true}
\setlength{\baselineskip}{20pt}
%\setmainfont{Adobe Garamond Pro}
```

### 标题样式的设置

titlesec的格式定衣：以后也许会把titlesec移动到公共的目录当中。

```{.nwcode title="设置hnureport标题的样式"}
\RequirePackage{titlesec}
\titleformat{\section}
{\fontsize{14pt}{20pt}\bfseries} % title
{\thesection} %before
{1em} % space
{}
\titleformat{\subsection}%
{\bfseries}%
{\thesubsection}%
{1em}
{}
\titleformat{\subsubsection}%
{}%
{\thesubsubsection}%
{1em}
{}
\titlespacing*{\section}{0pt}{6pt}{4pt}
\titlespacing*{\subsection}{0pt}{3pt}{2pt}
\titlespacing*{\subsubsection}{0pt}{1pt}{0pt}
```


## 开题报告的字段与用户接口的设计


```{.nwcode title="用户接口模块"}
<<封面字段>>
<<定义封面上的表格>>
<<生成封面的命令>>

<<添加开题报告的背景线框>>

<<正文中出现的字段>>
<<正文标题头>>
<<告诉文类在最后添加评语>>
```


### 首先我们来设置必要的在封面中出现的字段以及选项

按照标准，在封面中应该出现学号（在左上角）、题目、研究生姓名、专业、学位类别、专业领域、导师姓名这几项。这里我们定义了比较多的字段，有些字段可能根本用不上。

```{.nwcode title="封面字段"}
% 定义学院与机构
\ProvideDocumentCommand{\institution}{m}{\gdef\hnu@institution{#1}}
\gdef\hnu@institution{--} 

% 定义导师姓名（在封面中的），允许有第二导师
\ProvideDocumentCommand{\supervisor}{m D[]{}}{%
    \gdef\hnu@primaryteacher{#1}
    \gdef\hnu@secondaryteacher{#2}}
\gdef\hnu@primaryteacher{--} 
\gdef\hnu@secondaryteacher{}

% 定义学号
\ProvideDocumentCommand{\studentnumber}{m}{\gdef\hnu@studentnumber{#1}}
\gdef\hnu@studentnumber{--} 

% 定义题目（就是title不用改了，直接使用\@title的命令）和姓名（就是研究生的姓名，作者）
%

% 定义专业
\ProvideDocumentCommand{\profession}{m}{\gdef\hnu@profession{#1}}
\gdef\hnu@profession{--} 

% 定义学位类别
\ProvideDocumentCommand{\degreetype}{m}{\gdef\hnu@degreetype{#1}}
\gdef\hnu@degreetype{--} 

% 定义专业领域
\ProvideDocumentCommand{\domain}{m}{\gdef\hnu@domain{#1}}
\gdef\hnu@domain{--} 

% 定义研究方向
\ProvideDocumentCommand{\direction}{m}{\gdef\hnu@direction{#1}}
\gdef\hnu@direction{--} 

% 定义入学年月
\ProvideDocumentCommand{\admissionDate}{m}{\gdef\hnu@admissionDate{#1}}
\gdef\hnu@admissionDate{--} 
```


### 使用tabu来完成封面当中的表格

封面中的表格，本质上就是给表格添加一个下划线的效果而已（这比添加文字线要好得多了）。我们可以借助于tabu包的tabucline选项来完成。

```{.nwcode title="定义封面上的表格"}
\ProvideDocumentCommand{\coverTable}{}{
\begin{tabu}to 100mm {>{\large}X[3.2,c]>{\large}X[7,c]}
姓\hfill 名：& \@author \\\everyrow{\tabucline{2}}
题\hfill 目: & \@title \\
专\hfill 业\hfill 名\hfill 称: & \hnu@profession \\
研\hfill 究\hfill 方\hfill 向：& \hnu@direction\\
导\hfill 师\hfill 姓\hfill 名：& \hnu@primaryteacher, \hnu@secondaryteacher \\
入\hfill 学\hfill 年\hfill 月：& \hnu@admissionDate\\
\end{tabu}}
```

整个封面队了中间的表之外还有海南大学的位置以及与学号有关的信息。

```{.nwcode title="生成封面的命令"}
\ProvideDocumentCommand{\makecover}{}{
    \noindent 学号：\hnu@studentnumber \\\phantom{a}
\begin{center}\vskip-40pt\Huge \ttfamily 海\ 南\ 大\ 学\end{center}
\begin{center}\vskip25pt\huge 研究生学位论文开题报告书 \end{center}
    \vfill\vfill
    \begin{center} \coverTable \end{center}
    \vfill\vfill\vfill
\begin{center}\large 海南大学研究生处制\end{center}
    \vfill
    \pagebreak
}
```


### 如何处理更多的细节－各页处添加方框(相当于背景图片)

接下来我们要在每页的四周添加一个方框，以便这个方框能够正好盖住文本区。使得正文正好可以不受到任何影响地去排版。

```{.nwcode title="添加正文当中的水印"}
\usepackage[grid]{eso-pic}
\newcommand\BackgroundPic{
\parbox[0,0][\paperwidth][\paperheight]{width}{text} 
\noindent\begin{tikzpicture}
\draw[red] (0,0)--(1,0);
\draw (-2mm,-2mm) rectangle (\textwidth+2mm, \textheight+2mm);
\end{tikzpicture}
}
```

使用background宏包插入内容的时候，注意其默认选项。比如placement为中间的时候，background的作者将方向设定为有一定角度的旋转。此时需要手动将angle值设为0。上面是一个比较容易的配置方法：


```{.nwcode title="添加开题报告的背景线框"}
\RequirePackage[pages=all,placement=bottom,angle=0,scale=1,opacity=1,firstpage=false]%
{background}

\backgroundsetup{contents={
    \parbox[b][\paperheight]{\paperwidth}{
        \begin{tikzpicture}
            \node at (0,0){};
            \draw[line width=1pt] (0.95in, 2.9cm + \footskip) rectangle(\textwidth+1.05in,\textheight+3.05cm+\footskip);
            \node at (\paperheight, \paperwidth){};
        \end{tikzpicture}}
},color=black}

%\backgroundsetup{contents={-\thepage-}}
```

上面的思路是首先设置一个parbox，大小为页面那么大，那么这个parbox就会自动地被background宏包放在中间，从而parbox的边缘与页面正好是对齐的。然后parbox里面的内容其实也存在对齐的现象。所以我们将tikzpicture的内容也变成大小和页面大小一样。

添加边框是从第三页开始的，所以从第三页开始，我们加入命令：
AddToShipoutPicture{BackgroundPic}

在需要的时候，还可以取消这些命令。



## 正文标题头的设置

正文的标题头包括更多的字段。但是有一些是和前面的重复的。像研究生姓名，专业、专业领域都是重复的。毕业时间、导师课题姓名、研究生课题名称、计划完成初稿与计划定稿时间都是新的。所以我们先定义好这些题头。第一导师与第二导师先按照之前的命令来设。

导师在这里是分第一导师与第二导师的。

```{.nwcode title="正文中出现的字段"}
% 定义毕业时间
\ProvideDocumentCommand{\graduatedate}{m}{\gdef\hnu@graduatedate{#1}}
\gdef\hnu@graduatedate{--} 

% 定义导师课题名称
\ProvideDocumentCommand{\teachertopic}{m}{\gdef\hnu@teachertopic{#1}}
\gdef\hnu@teachertopic{--} 

% 定义学生选题名称
\ProvideDocumentCommand{\studenttopic}{m}{\gdef\hnu@studenttopic{#1}}
\gdef\hnu@studenttopic{--} 
\ProvideDocumentCommand{\plannedfirstdraft}{m}{\gdef\hnu@plannedfirstdraft{#1}}
\gdef\hnu@plannedfirstdraft{--} 
\ProvideDocumentCommand{\plannedManuscript}{m}{\gdef\hnu@plannedManuscript{#1}}
\gdef\hnu@plannedManuscript{--} 

% 定义学生开题报告的名称
\ProvideDocumentCommand{\researchTopic}{m}{\gdef\hnu@researchTopic{#1}}
\gdef\hnu@researchTopic{--} 

% 定义是否与导师科研课题相关
\ProvideDocumentCommand{\isRelevant}{m}{\gdef\hnu@isRelevant{#1}}
\gdef\hnu@isRelevant{是} 
```

然后利用这些字段排出来适用于主内容的表格：

```{.nwcode title="正文标题头"}
\ProvideDocumentCommand{\makeHeader}{}{
\noindent\begin{tabu} to \textwidth {X[0.5,c]X[0.5,c]X[c]X[c]X[0.2,c]}
论文题目 & \multicolumn{4}{c}{\hnu@researchTopic} \\
\multicolumn{2}{c}{学位论文计划定稿时间} & \hnu@plannedManuscript & 是否与导师科研课题相关 & \hnu@isRelevant \\
\end{tabu}}
```


```{.nwcode title="正文标题头(做废的，现在没有那么复杂)"}
%\newcommand{\minitab}[2][l]{\begin{tabular}{#1}#2\end{tabular}}
\ProvideDocumentCommand{\makeheader}{}{
\noindent\begin{tabu} to \textwidth {X[1.1,l]|X[1.2,c]|X[c]|X[c]}
\multirow{2}*{研究生姓名} & \multirow{2}*{\@author} & 
第一导师 & \hnu@primaryteacher 
\\\tabucline{3-4}
& & 第二导师 & \hnu@secondaryteacher 
\\\tabucline-
专业 & \hnu@profession & 专业领域 & \hnu@domain 
\\\tabucline-
毕业时间 & \multicolumn{3}{c}{\hnu@graduatedate}
\\\tabucline-
导师课题名称 & \multicolumn{3}{c}{\hnu@teachertopic}
\\\tabucline-
研究生课题名称 & \multicolumn{3}{c}{\hnu@studenttopic}
\\\tabucline-
计划完成初稿时间 & \hnu@plannedfirstdraft & 
计划定稿时间 & \hnu@plannedmanuscript 
\\\tabucline-
\end{tabu}}
```

## 后缀（指导教师评语与开题评审小组意见）


首先是指导教师评语，然后是开题评审小组意见。这两个东西都得放到页末的位置。

```{.nwcode title="告诉文类在最后添加评语"}
\AtEndDocument{\vfill\vfill\hrule
    \noindent{\fontsize{14pt}{22pt}\selectfont\bfseries 指导教师评语：}\\
\vskip2.5cm\vfill
\hfill \begin{tabu} to 0.4\textwidth {XX[2]}
导师签名：& \\
\multicolumn{2}{c}{\hfill 年\hfill 月\hfill 日}
\end{tabu}\\\pagebreak[2]
\hrule
\noindent{\fontsize{14pt}{22pt}\selectfont\bfseries 开题评审小组意见：}\\
\vskip3cm\vfill
\hfill \begin{tabu} to 0.4\textwidth {XX[2]}
组长签章： & \\
\multicolumn{2}{c}{\hfill 年\hfill 月 \hfill 日}
\end{tabu}
}
```

## 其它的设置

单纯这也还并不能够满足开题报告的格式的要求。其它的方面需要注意的就只是打印的问题了。要确保是双面打印，并且一般内容的题头应该放在奇数页（或者前两者不参加编号）。在实际内容上，可能标题需要使用四号加粗的字体，标题前面的编号采用大写的中文数字编号（使用titlesec来设置），然后就是小节的标题了。小节的标题可能使用小括号括起来的小写中文表示第几小节。

此外，具体的格式还包括参考文献的引用格式等。而且在引用的时候还要按照中文专著、外文专著、中文期刊、外文期刊；学位论文、网络文章的次序来排（这种排列顺序或许不是那么好），而且在排列的时候还得使用数字。要分别排各个参考文献的话，还是有一些难度。而且要使用biblatex可能还是有一些困难。特别是相关的Type的选项。可能还是得使用caspervector的选项设置了。

## 开题报告的基本特性选取

文体我们选择最简单的article。主要的内容就是所谓的研究来源、研究内容、研究进展计划与现有条件。作为四节。其它的地方我们不使用手工的方式生成。全是自动的。

```{.nwcode title="hnureport.cls"}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hnureport}[2016/11/21 Header file for Hainan University's theis report]
\LoadClass[12pt,a4paper]{article}
<<提升latex编程能力的宏包>>

<<模板风格化元素/插图元素>>
<<模板风格化元素/表格元素>>

<<设置页面布局>>
<<设置语言、字体与字号>>
<<设置hnureport标题的样式>>

<<用户接口模块>>
```
