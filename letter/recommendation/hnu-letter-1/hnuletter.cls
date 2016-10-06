%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% NEU Letter LaTeX Template
% Version 0.1 (02/12/14)
%
% This template has been downloaded from:
% https://github.com/karya0/neuletter
%
% Copyright (C) 2014 by Kapil Arya <kapil@ccs.neu.edu>
%
% License: CC BY-NC-SA 3.0 (http://creativecommons.org/licenses/by-nc-sa/3.0/)
%
%  2014/02/11 - Initial import
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% neuletter.sty - Northeastern U. letterhead style (for letter class)

% User can define:
% \Name{Sender's name} required
% \Department{Department name, default: CCIS}
% \DeptAddr{Dept addr withing NEU, default: 202 WVH}
% \Phone{phone numner, default: CCIS phone}
% \Fax{fax numner, default: CCIS fax}
% \Email{email addr, default empty}
% \Url{homepage url, default empty} % Unused so far

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hnuletter}[2016/10/05 Hainan University News Letter]
\LoadClass[11pt,a4paper]{letter}
\RequirePackage[margin=1in]{geometry}
\RequirePackage{fullpage}
\RequirePackage[11pt,fontset=adobe]{ctex}
\RequirePackage[sc]{mathpazo}
\setmainfont{URW Palladio L}
\RequirePackage{graphicx}
\linespread{1.05}   % Palladio needs more leading (space between lines)

%%% define fields
\newcommand*{\Name}[1]{\def\sendername{#1}}
\newcommand*{\Department}[1]{\def\deptname{#1}}
\newcommand*{\DeptAddr}[1]{\def\deptaddr{#1}}
\newcommand*{\Phone}[1]{\def\phonenum{#1}}
\newcommand*{\Fax}[1]{\def\faxnum{#1}}
\newcommand*{\Email}[1]{\def\emailaddr{#1}}
\newcommand*{\Url}[1]{\def\urladdr{#1}}
\newcommand*{\UnivAddr}[1]{\def\univaddr{#1}}
\newcommand*{\UnivName}[1]{\def\univname{#1}}

%%% set default fields.
\Name{Default Name}
\Department{College of Information Science and Technology}
\DeptAddr{Room 220, College of Information Science and Technology}
\Phone{+86 10000000000}
\Fax{+1-617-373-5121}
\Email{sample@hotmail.com}
\Url{http://yucongduan.org}
\UnivName{Hainan University}
%\UnivAddr{Hainan University, No. 58, Renmin Avenue, Haikou, Hainan Province, 570228, P.R. China}
\UnivAddr{Hainan University, No. 58, Renmin Avenue, Haikou, P.R. China}

\RequirePackage{xparse}
\RequirePackage{tabu,booktabs}
%\RequirePackage{multirow}
% From address

\def\sendername{\fromname}

\tabcolsep=0pt

\DeclareDocumentCommand{\PrintFromFields}{}{
\begin{minipage}[m]{1cm}
    \centering\includegraphics[width=1cm]{UnivLogo.png}
\end{minipage}
\begin{minipage}{0.8\textwidth}
    \textsc{\Huge\univname }
\end{minipage}\\[2pt]
\rule{\textwidth}{1pt}
\begin{raggedright}
\univaddr
\end{raggedright}\\[-5pt]
\rule{\textwidth}{1pt}\vspace{3pt}
\begin{tabu} to \textwidth {>{\raggedright}X[5]X[3]}
    \sendername & Phone: \phonenum \\
    \deptname & Email: \emailaddr \\
%    & Fax: \faxnum\\
    \multicolumn2{l}{\deptaddr }
\end{tabu}
\rule{\textwidth}{1pt}\vspace{4pt}
}

\address{\PrintFromFields{}}

% To addr
\DeclareDocumentCommand{\opening}{m}{
    %\thispagestyle{empty}
    \fromaddress \\ {\raggedright \hspace*{0.5\textwidth}\@date} \\
    \toname 
    \toaddress
\vspace{0.2in}\\
\noindent #1
% Uncomment the 4 lines below to print a footnote with custom text
%\def\thefootnote{}
%\def\footnoterule{\hrule}
%\footnotetext{\hspace*{\fill}{\footnotesize\em Footnote text}}
%\def\thefootnote{\arabic{footnote}}
}


\signature{\sendername}

\DeclareDocumentCommand{\closing}{+m}{
\vspace{0.3in}
\noindent
\hspace*{0.5\textwidth}
\parbox{3in}{\raggedright #1 \vskip 0.2in \fromsig}
\vfill
}

\RequirePackage{fancyhdr}
\pagestyle{fancy}
\lhead{}
\chead{}
\rhead{}
\lfoot{From: \sendername}
\cfoot{To: \toname}
\rfoot{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.4pt}
