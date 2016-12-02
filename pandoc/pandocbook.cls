%%% 在原来的unibook1的基础上，去掉了各种绘图的选项，以便能够具有更快的生成的速度。同时又能够有比较完善的功能。使用的宏包尽可能与GodWorld.cls接近。

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{pandocbook}
    [2016/10/22 v2.0 unified note book with pandoc support]
\LoadClassWithOptions{book}
\RequirePackage[twoside,
    top=1in,bottom=1in,left=1in,right=1in,%
    headsep=10pt,a4paper]{geometry}
\makeatletter
\RequirePackage[x11names,dvipsnames,svgnames,%
    table,hyperref]{xcolor}
\definecolor{ocre}{RGB}{243,102,25}
\RequirePackage{calc}
\RequirePackage{expl3}
\RequirePackage{tikz}
\RequirePackage{pgfplots}

%%% 最好的办法还是使用文字链接代替直接出现的URL。
%\usepackage[anythingbreaks]{breakurl}
\RequirePackage{hyperref}
\hypersetup{hidelinks,backref=true,pagebackref=true,%
    hyperindex=true,colorlinks=true,breaklinks=true,%
    urlcolor= ocre,bookmarks=true,bookmarksopen=false,%
    pdftitle={Title},pdfauthor={Author}
}
%\usepackage[hyphenbreaks]{breakurl}
%%% 下面的方案用来解决URL当中的断行的问题。
%\RequirePackage{etoolbox}
%\appto\UrlBreaks{\do\-}


%\RequirePackage{bookmark}
%\bookmarksetup{open, numbered,
%    addtohook={%
%        \ifnum\bookmarkget{level}=0 % chapter
%            \bookmarksetup{bold}%
%        \fi
%        \ifnum\bookmarkget{level}=-1 % part
%            \bookmarksetup{color=ocre,bold}%
%        \fi
%    }
%}
\RequirePackage{graphicx} % Required for including pictures
\RequirePackage[multidot,filenameencoding=utf8,space]{grffile}
%\graphicspath{{/home/hawk/note/extra/texclass/unibook1/}}
\RequirePackage[encoding=UTF8]{zhnumber}
\RequirePackage[framemethod=default]{mdframed}
\newmdenv[skipabove=7pt, skipbelow=7pt, backgroundcolor=black!5,
linecolor=ocre, innerleftmargin=5pt, innerrightmargin=5pt,
innertopmargin=5pt, leftmargin=0cm, rightmargin=0cm,
innerbottommargin=5pt]{tBox}
\newmdenv[skipabove=7pt, skipbelow=7pt, rightline=false,
leftline=true, topline=false, bottomline=false,
backgroundcolor=ocre!10, linecolor=ocre, innerleftmargin=5pt,
innerrightmargin=5pt, innertopmargin=5pt, innerbottommargin=5pt,
leftmargin=0cm, rightmargin=0cm, linewidth=4pt]{eBox}
\newmdenv[skipabove=7pt, skipbelow=7pt, rightline=false, leftline=true,
topline=false, bottomline=false, linecolor=ocre,
innerleftmargin=5pt, innerrightmargin=5pt, innertopmargin=0pt,
leftmargin=0cm, rightmargin=0cm, linewidth=4pt,
innerbottommargin=0pt]{dBox}
\newmdenv[skipabove=7pt, skipbelow=7pt, rightline=false,
leftline=true, topline=false, bottomline=false, linecolor=gray,
backgroundcolor=black!5, innerleftmargin=5pt, innerrightmargin=5pt,
innertopmargin=5pt, leftmargin=0cm, rightmargin=0cm,
linewidth=4pt, innerbottommargin=5pt]{cBox}
\setlength{\parskip}{0.75ex plus .2ex minus .5ex}
\renewcommand{\baselinestretch}{1.2}
\RequirePackage{paralist}
\setlength{\pltopsep}{0.0pt}
\setlength{\plitemsep}{0.0pt}
\RequirePackage{enumitem} % Customize lists
\setlist{nolistsep} % Reduce spacing
\renewcommand{\tablename}{表}
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{longtable}
\RequirePackage{tabu}
\renewcommand{\figurename}{图}
%% 英文remark环境
%% Tighter line spacing and white space after remark
%% 中文Remark环境
\newenvironment{remark}{\par\vspace{10pt}\small
\begin{list}{}{
    \leftmargin=35pt % Indentation on the left
    \rightmargin=25pt}%
\item\ignorespaces % Indentation on the right
\makebox[-2.5pt]{%
    \begin{tikzpicture}[overlay]
        \node[draw=ocre!60,line width=1pt,%
                circle,fill=ocre!25,font=\sffamily\bfseries,%
                inner sep=2pt,outer sep=0pt] %
        at (-15pt,0pt){\textcolor{ocre}{注}};%
    \end{tikzpicture}} % Orange R in a circle
\advance\baselineskip -1pt}{\end{list}\vskip5pt}
\everydisplay{
    \abovedisplayskip0pt plus 1pt
    \abovedisplayshortskip0pt plus 1pt
    \belowdisplayskip1pt plus 1pt
    \belowdisplayshortskip1pt plus 1pt
}
\RequirePackage{amsthm}
\makeatletter
\newtheoremstyle{ocrenumbox}% % Theorem style name
{0pt}% Space above
{0pt}% Space below
{\normalfont}% % Body font
{}% Indent amount
{\small\bf\sffamily\color{ocre}}% % Theorem head font
{\;}% Punctuation after theorem head
{0.25em}% Space after theorem head
{\small\sffamily\color{ocre}\thmname{#1}%
    \nobreakspace\thmnumber{\@ifnotempty{#1}{}\@upn{#2}}
    % Theorem text (e.g. Theorem 2.1)
    \thmnote{%
        \nobreakspace\the\thm@notefont\sffamily\bfseries\color{black}
        ---\nobreakspace#3.}
} % Optional theorem note
\renewcommand{\qedsymbol}{$\blacksquare$}% Optional qed square

\newtheoremstyle{blacknumex}% Theorem style name
{5pt}% Space above
{5pt}% Space below
{\normalfont}% Body font
{} % Indent amount
{\small\bf\sffamily}% Theorem head font
{\;}% Punctuation after theorem head
{0.25em}% Space after theorem head
{\small\sffamily{\tiny\ensuremath{\blacksquare}}%
    \nobreakspace\thmname{#1}%
    \nobreakspace\thmnumber{\@ifnotempty{#1}{}\@upn{#2}}
    % Theorem text (e.g. Theorem 2.1)
    \thmnote{%
        \nobreakspace\the\thm@notefont\sffamily\bfseries
        ---\nobreakspace#3.}
}% Optional theorem note

\newtheoremstyle{blacknumbox} % Theorem style name
{0pt}% Space above
{0pt}% Space below
{\normalfont}% Body font
{}% Indent amount
{\small\bf\sffamily}% Theorem head font
{\;}% Punctuation after theorem head
{0.25em}% Space after theorem head
{\small\sffamily\thmname{#1}\nobreakspace%
    \thmnumber{\@ifnotempty{#1}{}\@upn{#2}}
    % Theorem text (e.g. Theorem 2.1)
    \thmnote{%
        \nobreakspace\the\thm@notefont\sffamily\bfseries
        ---\nobreakspace#3.}
}% Optional theorem note
\newtheoremstyle{ocrenum}% % Theorem style name
{5pt}% Space above
{5pt}% Space below
{\normalfont}% % Body font
{}% Indent amount
{\small\bf\sffamily\color{ocre}}% % Theorem head font
{\;}% Punctuation after theorem head
{0.25em}% Space after theorem head
{\small\sffamily\color{ocre}\thmname{#1}\nobreakspace%
    \thmnumber{\@ifnotempty{#1}{}\@upn{#2}}
    % Theorem text (e.g. Theorem 2.1)
    \thmnote{%
        \nobreakspace\the\thm@notefont\sffamily\bfseries\color{black}%
        ---\nobreakspace#3.}
} % Optional theorem note
\renewcommand{\qedsymbol}{$\blacksquare$}% Optional qed square
\makeatother
\newcounter{dummy}
\theoremstyle{ocrenumbox}
%% English Style
\newtheorem{notation}{Notation}[chapter]
%% Chinese Style
\theoremstyle{ocrenumbox}
\newtheorem{theoremeT}[dummy]{定理}
\newtheorem{problem}{问题}[chapter]
\newtheorem{exerciseT}{练习}[chapter]
\theoremstyle{blacknumex}
\newtheorem{exampleT}{例}[chapter]
\theoremstyle{blacknumbox}
\newtheorem{vocabulary}{词汇表}[chapter]
\newtheorem{definitionT}{定义}[section]
\newtheorem{corollaryT}[dummy]{推论}
\theoremstyle{ocrenum}
\newtheorem{proposition}[dummy]{命题}
\newtheorem{lemma}[dummy]{引理}
\def\proofname{证明:}
\newenvironment{theorem}%
    {\begin{tBox}\begin{theoremeT}}%
    {\end{theoremeT}\end{tBox}}
\newenvironment{exercise}%
    {\begin{eBox}\begin{exerciseT}}%
    {\hfill{\color{ocre}\tiny\ensuremath{\blacksquare}}%
        \end{exerciseT}\end{eBox}}
\newenvironment{definition}%
    {\begin{dBox}\begin{definitionT}}%
    {\end{definitionT}\end{dBox}}
\newenvironment{example}%
    {\begin{exampleT}}%
    {\hfill{\tiny\ensuremath{\blacksquare}}\end{exampleT}}
\newenvironment{corollary}%
    {\begin{cBox}\begin{corollaryT}}%
    {\end{corollaryT}\end{cBox}}
\RequirePackage[plain,section]{algorithm}
\RequirePackage{algorithmicx}
\RequirePackage[noend]{algpseudocode}
\floatname{algorithm}{算法}
\renewcommand{\listalgorithmname}{算法列表}
\makeatletter
\newenvironment{breakablealgorithm}
{% \begin{breakablealgorithm}
   \begin{center}
     \refstepcounter{algorithm}% New algorithm
     \hrule height.8pt depth0pt \kern2pt% \@fs@pre for \@fs@ruled
     \renewcommand{\caption}[2][\relax]{% Make a new \caption
       {\raggedright\textbf{\ALG@name~\thealgorithm} ##2\par}%
       \ifx\relax##1\relax % #1 is \relax
         \addcontentsline{loa}{algorithm}{\protect\numberline{\thealgorithm}##2}%
       \else % #1 is not \relax
         \addcontentsline{loa}{algorithm}{\protect\numberline{\thealgorithm}##1}%
       \fi
       \kern2pt\hrule\kern2pt
     }
}{% \end{breakablealgorithm}
     \kern2pt\hrule\relax% \@fs@post for \@fs@ruled
   \end{center}
}

\RequirePackage{minted}

%\RequirePackage{titlesec}
\RequirePackage{titletoc}

%%%%%%%%%%%参考文献
\def\refname{参~考~文~献}
\renewcommand{\bibname}{参~考~文~献}
\RequirePackage[style=alphabetic,citestyle=alphabetic,sorting=nyt,%
    sortcites=true,autopunct=true,hyperref=true,%
    abbreviate=false,backref=true,backend=biber,natbib]{biblatex}
\def\refname{参~考~文~献}
\renewcommand{\bibname}{参~考~文~献}
\defbibheading{bibempty}{}
%%%%%%%%%%%索引
%\RequirePackage{makeidx} % Required to make an index
%\renewcommand{\indexname}{索~引}
%\makeindex % Tells LaTeX to create the files required for indexing

%%%%%%%%%%%%%图片目录
\renewcommand{\listfigurename}{插图目录}
\titlecontents{figure}[0em]
{\addvspace{-5pt}\sffamily}
{\thecontentslabel\hspace*{1em}}
{}
{\ \titlerule*[.5pc]{.}\;\thecontentspage}
[]
%%%%%%%%%%%%%表格目录
\renewcommand{\listtablename}{表格目录}
\titlecontents{table}[0em]
{\addvspace{-5pt}\sffamily}
{\thecontentslabel\hspace*{1em}}
{}
{\ \titlerule*[.5pc]{.}\;\thecontentspage}
[]
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\renewcommand{\chaptermark}[1]{%
\markboth{\sffamily\normalsize\bfseries 第\zhnumber{\thechapter} 章\ #1}{}}
\renewcommand{\sectionmark}[1]{%
\markright{\sffamily\normalsize 第\thesection 节\hspace{5pt}#1}{}}
\pagestyle{fancy}
\fancyhf{} \fancyhead[LE,RO]{\sffamily\normalsize\thepage}
\fancyhead[LO]{\rightmark}
\fancyhead[RE]{\leftmark}
\renewcommand{\headrulewidth}{0.5pt}
\addtolength{\headheight}{2.5pt}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{\fancyhead{}\renewcommand{\headrulewidth}{0pt}}
\makeatletter
\renewcommand{\cleardoublepage}{
    \clearpage
    \ifodd\c@page
    \else \hbox{}
        \vspace*{\fill}
        \thispagestyle{empty}
        \newpage
    \fi
}
\def\appendixname{附录}
\newcommand{\thefrontcoverimage}{}%
\newcommand{\frontcoverimage}[1]{\renewcommand{\thefrontcoverimage}{#1}}%
\makeatletter
\newcommand{\@subtitle}{}%
\newcommand{\subtitle}[1]{\renewcommand{\@subtitle}{#1}}%

\RequirePackage[fontset=adobe]{ctex}

%\titleformat*{\section}%
%{\centering\large\bfseries}%
%{第\arabic{section} 节}%
%{1em}%
%{}[]
%\titleformat*{\subsection}%
%{\centering\large\bfseries}%
%{\arabic{section}.\arabic{subsection}}%
%{1em}%
%{}[]
\xeCJKsetup{CJKmath=true}
\RequirePackage[nointlimits,sumlimits]{mathtools}
\RequirePackage{amsfonts,amssymb}
%\RequirePackage{avant} % Use the Avantgarde font for headings
%\RequirePackage{times} % Use the Times font for headings
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

%\endinput
%%%
%%% End of file `unibook1.cls'.

%\setcounter{secnumdepth}{3}
%\setcounter{tocdepth}{3}




%%% necessary pandoc definitions

%%% 添加lmodern和amsmath其实是多余的选项，而且lmodern还会使一些符号的排版变得不正确。

%\RequirePackage{lmodern}
%\RequirePackage{amsmath}

\RequirePackage{ifxetex,ifluatex}
\RequirePackage{fixltx2e} % provides \textsubscript
\defaultfontfeatures{Ligatures=TeX,Scale=MatchLowercase}

% use upquote if available, for straight quotes in verbatim environments
\IfFileExists{upquote.sty}{\usepackage{upquote}}{}

%%% use microtype if available
%%\IfFileExists{microtype.sty}{%
%%\usepackage{microtype}
%%\UseMicrotypeSet[protrusion]{basicmath} % disable protrusion for tt fonts
%%}{}

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

\setmainfont{Charis SIL}

