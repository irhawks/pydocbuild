## TIKZ过滤器的写法[12-02-2016 22:53:29 CST]

主要是在markdown当中就有tikz图片的代码，然后以图片的形式插入到文档中。

其实我们也可以这样搞：对于所有的需要编译成图片的代码段，我们直接输入.toFigure属性就可以了。如果有toFigure属性，那么就表示我们希望得到的是代码执行的结果而不是代码的部分属性。其实这也就是一种交叉的笔记本而已了。也许可以使用Jupyter之类的导出为markdown。

Use this

    ```latex
    \begin{tikzpicture}
    
    \def \n {5}
    \def \radius {3cm}
    \def \margin {8} % margin in angles, depends on the radius
    
    \foreach \s in {1,...,\n}
    {
      \node[draw, circle] at ({360/\n * (\s - 1)}:\radius) {$\s$};
      \draw[->, >=latex] ({360/\n * (\s - 1)+\margin}:\radius) 
        arc ({360/\n * (\s - 1)+\margin}:{360/\n * (\s)-\margin}:\radius);
    }
    \end{tikzpicture}
    
    ```

to get 

```latex
\begin{tikzpicture}

\def \n {5}
\def \radius {3cm}
\def \margin {8} % margin in angles, depends on the radius

\foreach \s in {1,...,\n}
{
  \node[draw, circle] at ({360/\n * (\s - 1)}:\radius) {$\s$};
  \draw[->, >=latex] ({360/\n * (\s - 1)+\margin}:\radius) 
    arc ({360/\n * (\s - 1)+\margin}:{360/\n * (\s)-\margin}:\radius);
}
\end{tikzpicture}
```

### 过滤器的编写


```python
#!/usr/bin/env python3

"""
Pandoc filter to process raw latex tikz environments into images.
Assumes that pdflatex is in the path, and that the standalone
package is available.  Also assumes that ImageMagick's convert
is in the path. Images are put in the tikz-images directory.
"""

import hashlib
import re
import os
import sys
import shutil
from pandocfilters import toJSONFilter, Para, Image
from subprocess import Popen, PIPE, call
from tempfile import mkdtemp

imagedir = "target/tikz-images"
imagelinkdir = "../tikz-images"


def sha1(x):
    return hashlib.sha1(x.encode(sys.getfilesystemencoding())).hexdigest()


def tikz2image(tikz, filetype, outfile):
    tmpdir = mkdtemp()
    olddir = os.getcwd()
    os.chdir(tmpdir)
    f = open('tikz.tex', 'w')
    f.write("""\\documentclass{standalone}
             \\usepackage{tikz}
             \\begin{document}
             """)
    f.write(tikz)
    f.write("\n\\end{document}\n")
    f.close()
    p = call(["xelatex", 'tikz.tex'], stdout=sys.stderr)
    os.chdir(olddir)
    if filetype == 'pdf':
        shutil.copyfile(tmpdir + '/tikz.pdf', outfile + '.pdf')
    else:
        call(["convert", tmpdir + '/tikz.pdf', outfile + '.' + filetype])
    shutil.rmtree(tmpdir)


def tikz(key, value, format, meta):
    if key == 'RawBlock':
        [fmt, code] = value
        if fmt == "latex" and re.match("\\\\begin{tikzpicture}", code):
            outfile = imagedir + '/' + sha1(code)
            if format == "html":
                filetype = "png"
            elif format == "latex":
                filetype = "pdf"
            else:
                filetype = "png"
            src = outfile + '.' + filetype
            if not os.path.isfile(src):
                try:
                    os.mkdir(imagedir)
                    sys.stderr.write('Created directory ' + imagedir + '\n')
                except OSError:
                    pass
                tikz2image(code, filetype, outfile)
                sys.stderr.write('Created image ' + src + '\n')
            return Para([Image([], [imagelinkdir+'/'+sha1(code)+'.'+filetype, ""])])

if __name__ == "__main__":
    toJSONFilter(tikz)
```
