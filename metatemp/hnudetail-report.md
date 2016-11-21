
## 头文件的设计


### 主文件的头文件

```{.nwcode .latex title="hnudetail.cls"}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hnudetail}[2015/09/20 main head file]
\LoadClass[a4paper,11pt]{book}
<<文档特性设置>>
\geometry{margin=1in}
<<语言、字体与符号设置>>
```

将主文件的默认字体大小改为11pt。注意这里的方法是来自于<http://www.latex-community.org/forum/viewtopic.php?f=5&t=3477>，是重新加载size11pt的结果。加载之后页边距也改变了，所以得重新设定。目前来看，重新定义相对字体大小的命令确实不是那么容易的。中间涉及到很我的改变。不只是各个字号的大小，还包括medskip等一大批间距。

不过，其实也许把命令放在相应的文件中比较好。默认把10pt当成是缺省大小。

```{.nwcode .latex title="hnudetail.cls"}
\renewcommand*\@ptsize{0}
\let\small\relax
\let\footnotesize\relax
\let\scriptsize\relax
\let\tiny\relax
\let\large\relax
\let\Large\relax
\let\LARGE\relax
\let\huge\relax
\let\Huge\relax
\input{size1\@ptsize.clo}
\geometry{margin=1in}
```

```{.nwcode .latex title="hnudetail.cls"}
<<公式与定理环境设置>>
<<风格与样式设置>>
<<正文风格设置>>
<<添加remark标记>>
<<加载biblatex/不使用caspervector>>
```

头文件的标题的设置是这样的。我们在chapter标题前面不加任何换行的选项了。

```{.nwcode .latex title="hnudetail.cls"}
%\RequirePackage{titlesec}
%\titlespacing*{\chapter}{0pt}{20pt}{20pt}
%\titleformat{\chapter}[hang]{\centering\Large\bfseries}{第\,\thechapter\,章}{1em}{}[]
%\ctexset{chapter={name = {第,章}},
%    section={name = {\S},number=\arabic{section}},
%    subsection={number={\arabic{section}.\arabic{subsection}}},
%}
```

### 开题报告的头文件

开题报告说白了就是一张带有封面的表格。这个表格的很多的字段也都是固定的。一个良好的开题报告应该使学生仅仅关注于内容的方面而不用考虑太多的格式。填表的时候的关键是什么呢？其实对于开题报告而言，就是选择相应的字段真上去而已。latex又支持中文的字段名称，所以我们完全可以按照它题目中的内容的要求来，就像之间写过的周报一样。

开题报告采用双面打印。封面页与表头里面含有较多的字段，而在表格里面是包括研究来源在内的大段大段的文字。正文中的文字彩用小四号宋体，使用3mm的行间距（也就是20pt的间距）。

主要的要求有：

* 课题来源。包括研究的目的和意义；国内外研究现状与发展趋势；主要参考资料；是否为导师科研课题的一部分
* 研究内容。说明研究的主要内容；研究的主要框架结构；可能的创新之处；需要重点解决的问题；预期研究成果
* 研究进展计划。包括研究的方法、技术方案、实验方法；研究时间安排；可能遇到的问题；问题的解决方案
* 现有条件。包括已经做过的有关研究工作、本单位或外单位可供使用的仪器设备和实验条件、已经获得或将要获得的经费
* 指导教师评语、开题报告审查小组意见
* 双面打印

具体地说，开题报告一式六份，其中的五份送开题报告审查小组专家（可复印）、一份存档（导师签名必须原件）；开题通过后结合专家建议在导师指导下修改确定开题报告内容并填写进《培养手册》。

整份开题报告的编写还真的没有那么容易。把整个开题报告当成是一个完整的文档可能并非是好的解决的方案。因为严格来说，开题报告只是关心开题报告里面的内容的，而且那么多的格式的问题。


#### 开题报告的基本特性选取

文体我们选择最简单的article。主要的内容就是所谓的研究来源、研究内容、研究进展计划与现有条件。作为四节。其它的地方我们不使用手工的方式生成。全是自动的。

```{.nwcode .latex title="hnureport.cls"}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hnureport}[2015/09/20 main head file]
\LoadClass[12pt,a4paper]{article}
<<文档特性设置>>
\geometry{margin=1in,top=3cm,bottom=3cm}
<<语言、字体与符号设置>>
<<风格与样式设置>>
<<正文风格设置>>
<<加载biblatex>>
<<生成开题报告的有关命令>>
```

统一的选项指的是各种特性，但是还需要专门针对开题报告进行设置。比如特殊的一些命令与格式。标准的开题报告使用的字体与其它的样式都和Linux下面的设置有一些不同，为了使两者更像，我们使用Windows的字体，并且调整好间距

```{.nwcode .latex title="hnureport.cls"}
%\ctexset{zihao=-4} zihao只能在加载ctex的时候才能使用。
\setCJKmainfont{SimSun}
\setCJKsansfont{KaiTi\_GB2312}
\setCJKmonofont{SimHei}
\xeCJKsetup{AutoFakeBold=true,AutoFakeSlant=true}
\setlength{\baselineskip}{20pt}
```

titlesec的格式定衣：以后也许会把titlesec移动到公共的目录当中。

```{.nwcode .latex title="hnureport.cls"}
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

```{.nwcode .latex title="生成开题报告的有关命令"}
<<封面字段>>
<<定义封面上出现的表>>
<<生成封面的命令>>
<<添加正文当中的水印>>
<<正文中出现的字段>>
<<正文标题头>>
<<告诉文类在最后添加评语>>
```

#### 首先我们来设置必要的在封面中出现的字段以及选项

按照标准，在封面中应该出现学号（在左上角）、题目、研究生姓名、专业、学位类别、专业领域、导师姓名这几项。这里我们定义了比较多的字段，有些字段可能根本用不上。

```{.nwcode .latex title="封面字段"}
% 定义学院与机构
\ProvideDocumentCommand{\institution}{m}{\gdef\hnu@institution{#1}}
\gdef\hnu@institution{--} 
% 定义导师姓名（在封面中的）
\ProvideDocumentCommand{\supervisor}{m D[]{}}{%
    \gdef\hnu@primaryteacher{#1}
    \gdef\hnu@secondaryteacher{#2}}
\gdef\hnu@primaryteacher{--} 
\gdef\hnu@secondaryteacher{}
% 定义学号
\ProvideDocumentCommand{\studentnumber}{m}{\gdef\hnu@studentnumber{#1}}
\gdef\hnu@studentnumber{--} 
% 定义题目（就是title不用改了）和姓名（就是研究生的姓名）
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
```

封面中的表格，本质上就是给表格添加一个下划线的效果而已（这比添加文字线要好得多了）。我们可以借助于tabu包的tabucline选项来完成。

```{.nwcode .latex title="定义封面上出现的表"}
\ProvideDocumentCommand{\covertable}{}{
    \extrarowsep=^25pt
    \begin{tabu}to 100mm {>{\large\bfseries}X[3.2,c]>{\large}X[7,c]}
        \everyrow{\tabucline{2}}
题\hfill 目: & \@title \\
        \everyrow{\tabucline-}
 & \\
        \everyrow{\tabucline{2}}
研\hfill 究\hfill 生\hfill 姓\hfill 名：& \@author \\
    专\hfill 业: & \hnu@profession \\
    学\hfill 位\hfill 类\hfill 别: & \hnu@degreetype \\
    专\hfill 业\hfill 领\hfill 域：& \hnu@domain \\
    导\hfill 师\hfill 姓\hfill 名：& 
        \hnu@primaryteacher \hskip20pt
        \hnu@secondaryteacher \\
\end{tabu}}
```

整个封面队了中间的表之外还有海南大学的位置以及与学号有关的信息。

```{.nwcode .latex title="生成封面的命令"}
\ProvideDocumentCommand{\makecover}{}{
    \noindent 学号：\hnu@studentnumber \\\phantom{a}
\begin{center}\vskip-40pt\Huge \ttfamily 海\ 南\ 大\ 学\end{center}
\begin{center}\vskip-25pt\huge 研究生学位论文开题报告 \end{center}
    \vfill\vfill
    \begin{center} \covertable \end{center}
    \vfill\vfill\vfill
\begin{center}\large 海南大学研究生处制\end{center}
    \vfill
    \pagebreak
}
```


#### 如何处理更多的细节－各页处添加方框

接下来我们要在每页的四周添加一个方框，以便这个方框能够正好盖住文本区。使得正文正好可以不受到任何影响地去排版。

```{.nwcode .latex title="添加正文当中的水印"}
\usepackage{eso-pic}
\newcommand\BackgroundPic{
\put(68,-85){
\parbox[b][\paperheight]{\paperwidth}{%
%\vfill
%\centering
\begin{tikzpicture}
\draw (0,0) rectangle (\textwidth+2, \textheight+2);
\end{tikzpicture}
\vfill
}}}
```

添加边框是从第三页开始的，所以从第三页开始，我们加入命令：
AddToShipoutPicture{BackgroundPic}

在需要的时候，还可以取消这些命令。


#### 正文标题头的设置

正文的标题头包括更多的字段。但是有一些是和前面的重复的。像研究生姓名，专业、专业领域都是重复的。毕业时间、导师课题姓名、研究生课题名称、计划完成初稿与计划定稿时间都是新的。所以我们先定义好这些题头。第一导师与第二导师先按照之前的命令来设。

导师在这里是分第一导师与第二导师的。

```{.nwcode .latex title="正文中出现的字段"}
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
\ProvideDocumentCommand{\plannedmanuscript}{m}{\gdef\hnu@plannedmanuscript{#1}}
\gdef\hnu@plannedmanuscript{--} 
```

然后利用这些字段排出来适用于主内容的表格：

```{.nwcode .latex title="正文标题头"}
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

#### 后缀（指导教师评语与开题评审小组意见）


首先是指导教师评语，然后是开题评审小组意见。这两个东西都得放到页末的位置。

```{.nwcode .latex title="告诉文类在最后添加评语"}
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

#### 其它的设置

单纯这也还并不能够满足开题报告的格式的要求。其它的方面需要注意的就只是打印的问题了。要确保是双面打印，并且一般内容的题头应该放在奇数页（或者前两者不参加编号）。在实际内容上，可能标题需要使用四号加粗的字体，标题前面的编号采用大写的中文数字编号（使用titlesec来设置），然后就是小节的标题了。小节的标题可能使用小括号括起来的小写中文表示第几小节。

此外，具体的格式还包括参考文献的引用格式等。而且在引用的时候还要按照中文专著、外文专著、中文期刊、外文期刊；学位论文、网络文章的次序来排（这种排列顺序或许不是那么好），而且在排列的时候还得使用数字。要分别排各个参考文献的话，还是有一些难度。而且要使用biblatex可能还是有一些困难。特别是相关的Type的选项。可能还是得使用caspervector的选项设置了。


#### 参考学长的开题报告[10-29-2015]

前两天从别处得到了一个学长的开题报告（刘骥），所以自己又参照这种报告的格式对文献进行了整理。与之前自己参照的外国语学院的模板有一些不一样的地方。所以可能得进行修改一下。大部分的修改是细节上的。

我们看一下主要的改变。主要的改变是

\begin{description}
    \item[封面页] 在左上方的学号消失了；题目变成了一行，宽度增加，并且好像使用了加粗的字体；题目、姓名、专业、学位类别、导师姓名这些字段依然保留。但是专业领域字段消失了，代之以研究方向。另外，上面的海南大学研究生处制的文字位置也升高了不少。
    \item[题头] 导师姓名不再区分第一导师与第二导师而是排在一起；专业、研究方向以及毕业时间在表格的同一行里面。所谓的“专业领域”其实就是研究方向。导师课题名称、研究生课题名称、计划完成初稿的时间、计划定稿的时间保留不变。
\end{description}

在结构上的变化是第一部分内容变成了立题依据。比如第一句话是

> 本课题《多宿主系统中传输协议拥塞控制的研究》是周星教授国家自然基金项目《下一代互联网多宿主系统国际测试床构建与性能分析》（项目号：61363008）的子课题。

第一部分立题依据的第一小节是研究的目的与意义；第二小节是“多路径传输的研究现状”以及本课题的研究方法；第三小节是“测试床构建现状”，可能也就相当于目前所具有的设备吧。之后用一个小节附上参考文献，这就是第一部分的内容了。参考文献按照GB/T 7714 2005的格式规范进行附录。

第二部分是研究的内容（说明课题的具体研究内容、独创以及新颖之处、重点解决的问题、预期的研究成果）。可以说各个学校都是这样说的。但是在实践起来却千差万别。所以具体怎样诠释大概各个学校有很大的差异吧。

第二部分的第一节研究内容，可以是在第一部分立题依据的后面细化。比如第1.1里面只是提到了受到支持，但是并没有提到是怎样受到支持的（比如说，现在什么具有了怎样的条件，可以进行什么样的实验等）。只能这样说：有了导师的课题的支持，写开题报告完全不是一个问题（在开题报告里面写学长的工作、论述实验设备就足够撑起来开题报告了）。这一节大概占有不到半页的空间。

第二部分的第二节是“项目创新之处”。创新之处的罗列也可能是多个方面的。比如某学长的提法就是，

**首先指出已有方法是一个热点，同时有各种各样的局限**。

> 众所周知，拥塞控制是确保互联网鲁棒性的重要因素，也是治理控制机制和应用的基础，一直是网络，特别是互联网络研究的执点问题。本项目又是基于下一代互联网多宿主系统的传输协议拥塞控制问题，其测试手段，与待考虑的因素都更加复杂，如，云计算、大数据时代的多样性应用，多种接入方式等，所以需要考虑提出新的策略或进行相应改进。目前虽然有几个网络应用测试床，但它们往往是针对单个接口或单一接入的应用，并不适合于多宿主系统中多路径传输网络性能的测试。

**然后说明本研究在所用设备、研究方法对比、研究思路上的新颖的地方**。

> 本项目的创新之处在于：首先，本子课题是基于一个崭新的多宿主测试平台--Hainan University NorNet平台;其次，在该平台上对下一代互联网传输协议--MPTCP和CMT-SCTP--的拥塞控制进行测试、对比与分析；最后，着力于找到一种合适的能处理多路径的拥塞控制机制，使通信吞吐量达到最大化。

第二部分的第三节是拟解决的问题，并在第四节指出各期的研究成果。

第三部分是研究进展计划。第一节是研究方法。可能是计划的研究方法，也可能是已经实现的研究方法。比如说，学长的一篇开题报告中提到的是论述建立一个良好的拥塞控制机制应该按照什么样的参考指标、如果将指标科学化或者形式化。制定了这样的标准之后，应该通过什么样的方法达到这样的标准等。

第三部分的第二节是所谓的技术方案。对于通信来说是一种实验的方法，对于计算机来说应该是实现一个程序，设计实现分析的方法并与其它的方法进行对比。这跟数学建模的操作的过程是类似的。

第三部分的第三节是研究进度。研究进度当然是要卡着学校的时间表。比如学长是2015年07月毕业，开题报告中的“计划完成初稿时间”是在2014年12月而计划定稿时间是在2015年03月。显然这个日期指的是研究生论文的日期。对于我们而言，也许应该就是在开题之后的几年之内吧。那么时间的安排就比较多了。在开题中可以把开题报告中已经做的东西都列举下来。比如刚开学的时候就开始做了哪些事情（即使是简单地阅读文献或者是做了初步的系统）。

第四部分是“现有条件”包括具体已经做过的有关研究工作与经费等。该内容有半页到一页的空间。当然，仍然是强调该课题是从属于导师的。

> 关于开题报告的内容格式的编写，其实可以留到第四章的时候再进行确定。在第一章的时候提到原则就行了。至于各节应该关心什么，其实并不可能在刚开始的时候就能够定下来。也许后面的各个section都有所不同。所以在后面还要进行调整。


### 正式论文的头文件

```{.nwcode .latex title="hnuthesis.cls"}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hnuthesis}[2015/09/20 main head file]
\LoadClass[12pt,fontset=adobe,a4paper]{ctexbook}
\RequirePackage[margin=1in]{geometry}
``` 


### 论文答辩的头文件

论文答辩是比较后期的事情了。暂时也不考虑答辩方面的事情。论文答辩指是PPT相关的演讲材料。


## 海南大学硕士论文模板[04-04-2016 11:13:08 CST]

这里自己参考了数学系14级徐爱娟同学与13级付春燕所提供的毕业模板。模板的格式符合毕业论文的要求，但是格式是CCT的，显得比较旧了。而且也没有使用模板技术。因此接下来我们就对模板作出必要的补充。

原来的论文的结构是这样的：


论文首先使用的是cctart的宏包，（还是twoside?），之后加载一系列的数学符号。处理悬挂缩进时使用hangindent，使用textindent处理管理。整体而言就是处理这些缩进的符号。

```latex
%\documentclass[11pt]{cctbook}
\documentclass[11pt, a4paper, twoside]{cctart}
%\documentclass[a4paper]{article}

\usepackage{mathrsfs}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{amsmath}
%\usepackage[dvips]{graphics}
\usepackage{graphicx}
\usepackage{indentfirst}
\def\hang{\hangindent\parindent}
\def\textindent#1{\indent\llap{#1\enspace}\ignorespaces}
\def\re{\par\hang\textindent}
```

接下来是论文中比较核心的东西。比如设置缩进与页面宽度。这些参数决定了毕业论文在外貌上是否像是毕业论文。

```latex
\usepackage{geometry}
\geometry{left=3.0cm, right=2.5cm, top=2.5cm, bottom=2.5cm}

\headsep 0.5 true cm
\topmargin 0pt
\oddsidemargin 0pt
\evensidemargin 0pt
\textheight 22.6 true cm
\textwidth 16 true cm

\parindent 2\ccwd
\footskip 1truecm
\end{latexcode}

页眉页脚设置是毕业设文的继续。

\begin{latexcode}
\usepackage{fancyhdr}
\pagestyle{fancy} \fancyhead{}
\fancyhead[CO]{\songti\zihao{5}海南大学硕士学位论文}
\fancyhead[CE]{\songti\zihao{5}关于丢番图方程的Jes'manowicz猜想}
\lfoot{} \cfoot{}
\renewcommand{\headrulewidth}{0.4pt}
\cfoot{\thepage\ {} \ {}}
%----------------------------------------------
\renewcommand\baselinestretch{1.5}
```


### 第一页封面设计

之后就是正文里面的内容了。第一部分是封面设计。正文顶部有海南大学的图标，因此就被采用使用figure浮动体来排（位于TOP范围当中）。但是这样的实践并不好。中间的logo.jpg是海南大学的图标。

```latex
\newpage
\thispagestyle{empty} {
学校代码:\underline{~~~~~10589~~~~~~}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
学号:\underline{~~13070104210003~~} }

{
分~~类~~号:\underline{~~~~~~~~~~~~~~~~~~}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
密级:\underline{~~~~~~~~~~~~~~~~~~~~~~~~~} } \

%\
\begin{figure}
\centering
\includegraphics[width=1.8in]{logo.jpg}
\end{figure}
\end{latexcode}

在添加了上面的内容之后就开始展示海南大学硕士学位论文的LOGO。其中的海南大学是楷体零号字体、硕士学位论文是黑体一号字体。

\begin{latexcode}
\linespread{2.2}\vspace{52mm}

\centerline{\zihao{0}\kaishu 海南大学}\

\vspace{9mm}
\centerline{\LARGE\zihao{1}\heiti\textbf
硕~~~~士~~~~学~~~~位~~~~论~~~~文~~~~}
```

而留下足够的空格之后，就是列表来显示一些字段了，比如题目、作者、指导教师、专业、时间等。个人感觉国内的论文总是大量的文字，显得十分复杂，这样的东西看起来就非常难受。论文还不如红头文件好看。

```latex
\vspace{3cm}
{\zihao{4}

{~~~~~~~~~~题~~~~~~~~~~目:\underline{~~~~~~~~~ 关于丢番图方程的Jes'manowicz猜想~~~~~~~~~~~~~~}}

{~~~~~~~~~~作~~~~~~~~~~者:\underline{~~~~~~~~~~~~~~~~付~~~~~~~~春~~~~~~~~燕~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}}

{~~~~~~~~~~指~导~教~师:\underline{~~~~~~~~~~~~~~~~邓~~谋~~杰~~教~~授~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}}

{~~~~~~~~~~专~~~~~~~~~~业:\underline{~~~~~~~~~~~~~~~~应~~~~~用~~~~~数~~~~~学~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}}

{~~~~~~~~~~时~~~~~~~~~~间:\underline{~~~~~~~~~~~~~~~~2016~~年~~3~~月~~1~~日~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}}
}
```

这样的做法显然并不正确。应该使用更好的方法处理和替换掉论文。

海南大学第二页是英文附录页。提交的是英文的标题与作者等内容。看起来像仍然是一系列的字段。这些字段我们不妨放在一起处理。

封面有两页，一个中文的版本一个英文的版本。这就是国内论文的结构。个人对这种情况也非常不满。感觉有点多余，使论文显得非常冗长。不如采取更为紧凑的方式来组织论文。毕业论文也需要指定以紧凑的格式来弄。

```latex
\newpage
\thispagestyle{empty}

\centerline{\rm \Huge \bf  On the conjecture of Jes'manowicz }
\vspace{0.6cm}
\centerline{\rm \Huge \bf  about some Diophantine Equations}

\vfill 

\centerline{\Large\rm\it A Thesis }
\vspace{0.3cm}
\centerline{\Large\rm\it Submitted in Partial Fulfillment of the Requirement}
\vspace{0.3cm}
\centerline{\Large\rm\it For the Master Degree of in College of}
\vspace{0.3cm}
\centerline{\Large\rm\it Information Science and Technology}\

\vfill

\centerline{\Large\rm\bf By }
\vspace{0.3cm}
\centerline{\Large\rm\bf Fu~chunyan }\

\vfill

{\large\rm Supervisor:~~~~Deng Moujie}\vspace{0.3cm}

{\large\rm  Major:~~~~Applied mathematics}\vspace{0.3cm}

{\large\rm Submitted:~~~~May, 2016}\vspace{0.3cm}
```


个人感觉这样的标题页设计出来应该有一些很好的参考选项。比如使用vfill之类的，这样可以让人觉得各个元素的摆放是灵活处理的，适合于论文的，不会因为原来的论文放在间距为10cm的位置而就让现在的论文放在10cm的位置。可能像“作者”放在“标题”与下面的字段中间这样的要求更合理。再比如表格是左对齐还是居中对齐。我们如果不能给出来模板的Specification，也就是一个失败的模板。（学校出的很多的格式规范都是乱命）。



### 原创性说明

可能因为内容较多吧。原创性说明的字体是比较小的。大量使用的是五号字体。

```latex
\newpage

\thispagestyle{empty} \topmargin=0cm

\centerline{\heiti \zihao{3}
海南大学学位论文原创性声明和使用授权说明}\

\centerline{\songti \bf \zihao{4} 原创性声明 }\ {\songti \zihao{5}
本人郑重声明： 所呈交的学位论文, 是本人在导师的指导下,
独立进行研究工作所取得的成果。 除文中已经注明引用的内容外,
本论文不含任何其他个人或集体已经发表或撰
写过的作品或成果。对本文的研究做出重要贡献的个人和集体, 均已在文中以
明确方式标明。本声明的法律结果由本人承担。}\ \vskip .5truecm
{\songti
\zihao{5}论文作者签名：~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~日期：~~~~~~~~~年~~~~~~~~~月~~~~~~~~~
日}\

\ \vskip .5truecm \centerline{\songti \bf
\zihao{4}学位论文版权使用授权说明 }\
{\songti\zihao{5}本人完全了解海南大学关于收集、保存、
使用学位论文的规定, 即：学校有权保留并向国家有关部门
或机构送交论文的复印件和电子版, 允许论文被查阅和借阅。
本人授权海南大学可以将本学位论文的全部或部分内容编入有
关数据库进行检索, 可以采用影印、缩印或扫描等
复制手段保存和汇编本学位论文。本人在导师指导 下完成的论文成果,
知识产权归属海南大学。

保密论文在解密后遵守此规定。}\
\vskip .5truecm
{\songti\zihao{5}
论文作者签名：~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~导师签名：~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}

{\songti\zihao{5}日期：~~~~~~~~~~~~
年~~~~~~~~~月~~~~~~~~~日~~~~~~~~~~~~~~~~~~~日期：~~~~~~~~~年~~~~~~~~~月~~~~~~~~~日}

.....................................................................................................................................

\vspace{1.5cm}

{\songti\zihao{5}本人已经认真阅读~"CALIS高校学位论文全文数据库发布章程"~,
同意将本人的学位论文提交~\\
"CALIS高校学位论文全文数据库"中全文发布,
并可按"章程"中规定享受相关权益。

\underline{同意论文提交后滞后：□半年；□一年；□二年发布}}。

\vskip .5truecm

{\songti\zihao{5}
论文作者签名：~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~导师签名：~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}

{\songti\zihao{5}日期：~~~~~~~~~~~~
年~~~~~~~~~月~~~~~~~~~日~~~~~~~~~~~~~~~~~~~日期：~~~~~~~~~~~~年~~~~~~~~~月~~~~~~~~~日}
```


### 中文摘要与英文摘要

之后就是摘要页。摘要单独成为一页。正常使用的是四号宋体。自己觉得可以这样处理摘要与关键字。因为要区分中文摘要与英文摘要，因此我们弄出来cnabstract与enabstract两个摘要环境，然后使用一个摘要命令来分割中文的方面与英文的方面，就像是这样：

```latex
\begin{abstract}
中文摘要内容
\keywords 中文关键字
\english
英文摘要内容
\keywords 英文关键字
\end{abstract}
```

不过现在自己又改变想法了。即然学校的毕业论文中添加英文摘要的规定是乱命，那么我们不妨直接将摘要指定为中文摘要。也就是说，将摘要处理成中文的形式，如果要添加英文，那么就额外写上英文文献。

```latex
\newpage
\thispagestyle{empty}

\pagenumbering{Roman}\setcounter{page}{1}

\zihao{-4}

{\section*{\heiti\zihao{3} 摘\quad 要}}{\songti\zihao{-4}
本文利用初等数论中的简单同余法、二次剩余法、因式分解法、不等式法以及代数数论中的四次剩余特征理论,
对丢番图方程~$(na)^x+(nb)^y=(nc)^z$~的一些特殊情形进行了证明了Jes'manowicz猜想成立。
本文的主要结果如下：

1、丢番图方程~$(n^2-36)^x+(12n)^y=(n^2+36)^z$~仅有正整数解~$x=y=z=2$~。

2、如果正整数~$n$~满足~$n\equiv 3(\bmod 20)$~或者~$n\equiv 3(\bmod 8)$~，则丢番图方程$$(n(2n+7))^x+(2n(n+7))^y=(2n(n+7)+49)^z$$仅有正整数解~$x=y=z=2$~。

3、如果正整数~$n$~,~$a=7^{2r}-4$~满足~$P(a)|n$~或者~$P(n)\nmid a$~，则丢番图方程$$(n(7^{2r}-4))^x+(n(4\cdot7^r))^y=(n(7^{2r}+4)^z$$仅有正整数解~$x=y=z=2$~。

\vskip .5truecm

\vskip.1in \noindent {\heiti\zihao{-4} 关键词：}{\songti\zihao{-4} 指数丢番图方程；Jes'mannowicz猜想；商高数组；初等方法；四次剩余特征}
```

英文摘要

```latex
\newpage
\thispagestyle{empty}

{\section*{\bf\zihao{3} Abstract}} {\rm\zihao{-4}In this paper, using the method of simple congruence、quadratic residue、factorization、inequality in elementary number theory and biquadratic residue character theory in algebraic number theory，we prove that the conjecture of   holds true for some special cases of the Diophantine equation~$(na)^x+(nb)^y=(nc)^z$~．The main results of this paper are as follows:

1、The Diophantine equation~$(n^2-36)^x+(12n)^y=(n^2+36)^z$~ has only the positive integer solution ~$x=y=z=2$~.

2、If the positive integer~$n$~satisfied ~$n\equiv 3(\bmod 20)$~ or ~$n\equiv 3(\bmod 8)$~, then the Diophantine equation$$(n(2n+7))^x+(2n(n+7))^y=(2n(n+7)+49)^z$$ has only the positive integer solution ~$x=y=z=2$~.

3、If the positive integer~$n$~,~$a=7^{2r}-4$~satisfied ~$P(a)|n$~ or ~$P(n)\nmid a$~, then the Diophantine equation$$(n(7^{2r}-4))^x+(n(4\cdot7^r))^y=(n(7^{2r}+4)^z$$ has only the positive integer solution ~$x=y=z=2$~.}
\vskip .5truecm
{\parindent=0pt{\rm\zihao{4}\bf Key words:} {\rm\zihao{-4}Exponential Diophantine equation; Jes'manowicz' conjecture; Pythagorean triples；\\Elementary method；Biquadratic residue character}}
```


## 进入目录与内容

写完这这么多的摘要，总算是进入了正文了。不过，由于是学术文献，这大概与那种与机构密切相关的论文是差不多的。或许正确的处理方式还是像技术报告那样。在摘要与目录之间可以选择不换页。

```latex
\newpage
\thispagestyle{plain}
\pagenumbering{Roman}
\setcounter{page}{1}

{\section*{\heiti\zihao{3} 目\quad录}}\vskip .5truecm

{\songti\zihao{-4} ~~\parindent=0pt\songti\zihao{-4} {\bf 1}~~~~绪论}~$\dotfill$~1

{\songti\zihao{-4} ~~~~1.1~~ 丢番图方程的概述}~$\dotfill$~1

{\songti\zihao{-4} ~~~~1.2~~ 丢番图方程的研究成就}~$\dotfill$~1

{\songti\zihao{-4} ~~~~1.3~~ 本文的主要工作}~$\dotfill$~2

{\songti\zihao{-4} ~~\parindent=0pt\songti\zihao{-4} {\bf 2}~~~~丢番图方程\boldmath~$(n^2-36)^x+(12n)^y=(n^2+36)^z$~}~$\dotfill$~3

{\songti\zihao{-4} ~~~~2.1~~ 研究背景}~$\dotfill$~3

{\songti\zihao{-4} ~~~~2.2~~ 相关引理}~$\dotfill$~3

{\songti\zihao{-4} ~~~~2.3~~ 主要结果}~$\dotfill$~4

{\songti\zihao{-4} ~~\parindent=0pt\songti\zihao{-4} {\bf 3}~~~~丢番图方程\boldmath~$(n(2n+7))^x+(2n(n+7))^y=(2n(n+7)+49)^z$~}
~$\dotfill$~11

{\songti\zihao{-4} ~~~~3.1~~ 研究背景}~$\dotfill$~11

{\songti\zihao{-4} ~~~~3.2~~ 相关引理}~$\dotfill$~11

{\songti\zihao{-4} ~~~~3.3~~ 主要结果}~$\dotfill$~12

{\songti\zihao{-4} ~~\parindent=0pt\songti\zihao{-4} {\bf 4}~~~~丢番图方程\boldmath~$(n(7^{2r}-4))^x+(n(4\cdot7^r))^y=(n(7^{2r}+4)^z$~}~$\dotfill$~15

{\songti\zihao{-4} ~~~~4.1~~ 研究背景}~$\dotfill$~15

{\songti\zihao{-4} ~~~~4.2~~ 相关引理}~$\dotfill$~15

{\songti\zihao{-4} ~~~~4.3~~ 主要结果}~$\dotfill$~16
\vskip .5truecm
{\songti\zihao{-4} ~~参考文献}~$\dotfill$~29

{\songti\zihao{-4} ~~硕士期间发表的论文}~$\dotfill$~31

{\songti\zihao{-4} ~~致谢}~$\dotfill$~32
```

模板中给出的止录是手工打出来的，而且缩进似乎也并不好。可能主要还是参考文献、硕士期间发表的论文以及致谢有许多的问题。


### 论文的内容

首先是绪论，然后是介绍工作，最后有参考文献、致谢、附录等内容。格式大致就是这样的形式：

```latex
\newpage
\pagenumbering{arabic}\setcounter{page}{1}

{\section*{\parindent=0pt\heiti\zihao{3} {\Large}\parindent=0pt\heiti\zihao{3} {\Large\bf 1}~~~~绪论}}\vskip .5truecm

{\parindent=0pt\heiti\zihao{4} {\Large\bf 1.1}~~丢番图方程的概述}\vskip .5truecm
```

正文中的定理、命题、方程等都是手动编号而得来的。因此参考意义不大。

```latex
\newpage
{\parindent=0pt\vskip .5truecm

%\thispagestyle{fancy} \fancyhead[LE, LO]{\songti海南大学硕士学位论文}
% \fancyhead[RE, RO]{\songti 参考文献}

\begin{thebibliography}{99}
\bibitem{1} 曹珍富,丢番图方程引论[M],哈尔滨:哈尔滨工业大学出版社,1989.
\bibitem{2} 曹珍富, 不定方程及其应用[M], 上海交通大学出版社,2000.
\bibitem{3} 乐茂华，Gel'fond-Baker方法在丢番图方程中的应用，[M].北京：科学出版社，1998.
\bibitem{4} Andrew John Wiles, Modular elliptic curves and Fermat's Last Theorem[M], Annals of Mathematics, 1995,141:443-551.
\bibitem{5} Mordell L.J, Diophantine Equation[M],Academic Press Inc, 1969.
\bibitem{6} Shorey T.N.,Tijeman. R, Exponential Diophantine Equation[M],Cambridge University Press,2008.
\bibitem{7} Serpin'ski W., On the equation~$3^x+4^y=5^z$~[J], Wiadom．Mat．,1955-1956,1:194-195(in Polish)．
\bibitem{8} Jes'mannowicz L．,Several remarks on Pythagorean numbers[J], Wiadom．Mat．,1955-1956,1:196-202（in Polish）.
\bibitem{9} 曹珍富,丢番图方程引论[M],哈尔滨： 哈尔滨工业大学出版社，2012．
\bibitem{10} Dem'janenko V．A ,On Jes'mannowicz problem for Pythagorean numbers[J], Izv.Vyss．Ucebn．Zaved．, Matematika, 1965,48: 52-56(in Russian)．
\bibitem{11} Miyazaki T．, Generalizations of classical results on Jes'mannowicz' conjecture concerning Pythagorean triples[J], J．Number Theory,2013,133:583-595．
\bibitem{12} Miyazaki T．,Yuan Pingzhi, Wu Danyao, Generalizations of classical results on Jes'mannowicz' conjecture concerning Pythagorean triples II[J], J．Number Theory, 2014,141:184-201．
\bibitem{13} Y.D.Guo and M.H.Le, A note on Jes'mannowicz conjecture concerning Pythagorean numbers[J], Comment. Mat., Univ. St. Pauli, 1995, 44: 225-228.
\bibitem{14} Cao Z．F．,A note on the Diophantine equation ~$a^x+b^y=c^z$~[J], Acta Arith, 1999，91：85-93．
\bibitem{15} Terai N．,On Jes'mannowicz' conjecture concerning primitive Pythagorean triples [J],J，Number Theory，2014，141:316-323．
\bibitem{16} Laurent M．, Linear forms in two logarithms and interpolation determinants II[J], Acta Arith, 2008，133：325-348．
\bibitem{17} 李双志,关于商高数的Jes'mannowicz猜想[D],西南大学,2011.
\bibitem{18} 熊川,关于商高数的猜想[D], 西南大学,2013.
\bibitem{19} Deng Mou-Jie and Cohen G L., on the conjecture of Jes'mannowicz' concerning Pythagorean triples [J],Bulletin of the Australian Mathematics Society， 1998, 57(3):515-524.
\bibitem{20} Le Maohua,A note on Jes'mannowicz' conjecture concerning Pythagorean triples[J], Bulletin of the Australian Mathematics Society, 1999, 59(3):477-480.
\bibitem{21} Deng Mou-Jie,On the Diophantine equation ~$(na)^x+(nb)^y=(nc)^z$~[J], Bulletin of the Australian Mathematics Society, 2014,89 (2):316-321.
\bibitem{22} Tang Min and Weng Jian-Xin, Jes'mannowicz' Conjecture with Fermat numbers [J].Taiwan.J.Math,2014, 18(3):925-930.
\bibitem{23} Yang Zijuan and Tang Min, On the Diophantine equation ~$(8n)^x+(15n)^y=(17n)^z$~[J], Bulletin of the Australian Mathematics Society, 2012,86 (2):348-352.
\bibitem{24} Sun Cuifang and Cheng Zhi,A note on the Jes'mannowicz' conjecture [J], J. Math.PRC., 2013,33(5):788-794.
\bibitem{25} Miyazaki T,Yuan Pingzhi and Wu Danyao.,Generalizations of classical results on Jes'mannowicz' conjecture concerning Pythagorean triples[J], J. Number Theory, 2014, 141:184-201．


\end{thebibliography}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\newpage
\thispagestyle{fancy}
%\fancyhead[LE, LO]{\songti 海南大学硕士学位论文}
%\fancyhead[RE, RO]{\songti 硕士期间发表的论文}

{\section*{\heiti\zihao{3} ~~硕士期间发表的论文}}\vskip
.5truecm {\songti\zihao{-4}{\parindent=0pt


付春燕，邓谋杰.关于丢番图方程~$((7^{2r}-4)n)^x+((4\cdot7^r)n)^y=((7^{2r}+4)n)^z$~的Jes'mannowicz猜想[J]．黑龙江大学自然科学版学报,2015,32(5):596-599.}}




\newpage

{\section*{\songti\zihao{3} 致\quad谢}}\vskip .5truecm
\fangsong\zihao{-4}\setlength{\parindent}{2em}弹指一挥间，三年研究生生涯过去了。回首过去，留下了太多的美好回忆。不论是美丽的校园，还是可爱的同学们，慈祥的老师们都是我难忘的财富。

首先，我要感谢我的导师邓谋杰教授。感谢邓老师在这三年研究生学习期间对我学业上的耐心指导和生活上的悉心关怀。邓老师在身体状况不理想的情况下仍然指导我的论文写作，
我深表感激。邓老师严谨的学术作风，浑厚的学术底蕴都深深的感染了我,引导我在学术写作的道路上一步一步一个脚印的走下去。
生活中，邓老师还有师母的悉心关怀让我就像回到了家一样，而不是个离家几千里的游子。感谢邓老师，感谢师母。

其次，我要感谢数学系的老师们：尹建华教授，龙伦海教授，李会师教授，欧宜贵教授，孙建强教授，高泽图教授等所有任课教师，是他们帮助我打下了深厚的数学理论知识基础。
感谢他们的教诲与教导，没有他们的辛勤栽培，没有我的今天。

我还要感谢我的师姐、师妹。我们就像是一个家庭的兄弟姐妹，生活上互相帮助，学业上一起探讨研究，在他们这，我感受到了家的温暖。谢谢她们。
感谢我的研究生同学们，朋友们。我们一起上课，一起玩，一起学习。这些都将是我一辈子的珍贵回忆。

最后，我还要感些我的爸爸妈妈，是他们无条件的付出和奉献，支持我完成了我的学业。也是他们给了我奋斗下去的动力。
感谢都有关心爱护我的亲朋好友。祝福所有人能一生顺遂，平安幸福。

\vspace{5cm}

\hspace{13cm}付春燕

\hspace{12.5cm}~2016~年~3~月
\end{document}

```
