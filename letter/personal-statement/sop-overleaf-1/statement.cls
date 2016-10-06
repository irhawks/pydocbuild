% Source: http://tex.stackexchange.com/a/150903/23931

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{statement}[2016/10/05 A Statement of Purpose Template]
\LoadClass[11pt,a4paper]{ctexart}
\RequirePackage[margin=1in]{geometry}
\RequirePackage{xcolor}
\RequirePackage{fancyhdr}
\RequirePackage{tgschola} % or any other font package you like
\setmainfont{TeX Gyre Schola}
\linespread{1.10}
\setlength{\parskip}{5pt}

\newcommand{\Title}[1]{\def\soptitle{#1}}
\newcommand{\Name}[1]{\def\yourname{#1}}
\newcommand{\Email}[1]{\def\youremail{#1}}
\newcommand{\Web}[1]{\def\yourweb{#1}}
\newcommand{\University}[1]{\def\youruniversity{#1}}

\Title{Statement of Purpose}
\Name{firstname lastname}
\Email{email@address.edu}
\Web{https://www.abcd.com/}
\University{Hainan University}

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

\renewcommand{\maketitle}{
    \begin{center}\LARGE\soptitle\\
        \large of \yourname\ (PhD applicant)
    \end{center}
    \hrule\vspace{1pt}\hrule height 1pt\bigskip
}
