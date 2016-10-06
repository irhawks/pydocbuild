% Source: http://tex.stackexchange.com/a/150903/23931

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{statementCN}[2016/10/05 A Statement of Purpose Template]
\LoadClass[12pt,a4paper,fontset=adobe]{ctexart}
\RequirePackage[margin=1in]{geometry}
\RequirePackage{xcolor}
\RequirePackage{fancyhdr}
\RequirePackage{tgschola} % or any other font package you like

\RequirePackage{tabu,booktabs}

\setmainfont{TeX Gyre Schola}
\linespread{1.3}
\setlength{\parskip}{0pt}
\setlength{\parindent}{24pt}

\newcommand{\Title}[1]{\def\soptitle{#1}}
\newcommand{\Name}[1]{\def\yourname{#1}}
\newcommand{\Email}[1]{\def\youremail{#1}}
\newcommand{\Web}[1]{\def\yourweb{#1}}
\newcommand{\University}[1]{\def\youruniversity{#1}}

\Title{个人陈述}
\Name{张三}
\Email{email@address.edu}
\Web{https://www.abcd.com/}
\University{海南大学}

\newcommand{\statement}[1]{\par\smallskip
  \underline{\textcolor{blue}{\textbf{#1:}}}\space
}

\usepackage[colorlinks,breaklinks, pdftitle={\yourname - \soptitle}, pdfauthor={\yourname}, unicode]{hyperref}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{%
  \footnotesize\sffamily
  \yourname\quad
  %web: \textcolor{blue}{\itshape\yourweb}\quad
  \textcolor{blue}{\youremail} \quad \youruniversity}

\extrarowsep=0mm
\renewcommand{\maketitle}{
    \begin{center}\LARGE\soptitle\end{center}
        \vspace{-8pt}
    \begin{tabu} to \textwidth {XX[2c]X[r]}
        & \large 申请博士招生材料 & \large \yourname %
        %%% 可以在这里写上是哪个大学，中英文习惯是不相同的
    \end{tabu}
    \hrule\vspace{1pt}\hrule height 1pt\bigskip
}
