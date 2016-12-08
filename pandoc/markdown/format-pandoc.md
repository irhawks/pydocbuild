## Pandoc文档的编写@2015年 05月 26日 星期二 07:30:15 CST

现在自己熟悉起来也比较容易了。在LaTeX中自己可以使用fullcite一类的命令帮助完成相应的工作。这样一份代码可以生成HTML、TeX与PDF等多种格式。自己也相信这种机制会给自己带来非常大的方便。为什么输出成PDF需要LaTeX？这不是没有原因的。大概因为LaTeX向其它的格式转换非常麻烦。包含宏的时候尤其如此。所以，markdown与restructredText可以看成LaTeX的一个子集。

### 工程组织

组织Pandoc可以采取这样的步骤。相对而言，template属于排版的时候的样式表。排版的时候肯定有一些样式需要自己定制，所以放在templates目录下。而CSL与filters就比较一般性了，所以放在lib或者resources目录下可能还是比较合适。在定位它们的时候，采取相对定位的方式，比如通过`${PROJ_DIR}/templates`来访问指定的目录。

自己认为参考文献的管理工作可以自动化完成，自己只需要在文档中找出引用就可以了。也就是说，外部引用由工程管理，而不是角色自己使用。这样的话，.bib文件应该放在某个资源文件目录下。

在写YAML配置文件的时候注意各个字段的含义。最好应该参照一个模板来做。在default.latex文件中可以找到模板是怎样输出的。这样的话，自己也好有一个更清晰的印象。至于pandocargs选项，目前来看，似乎是不能使用的，所以自己还是要把--filter写到命令行当中。

## Pandoc编程介绍[06-21-2015 10:07:31]

按自己的理解，所有的数据分析，所有的文档处理等都建立在编程的基础上。本质上它们都是编程的过程。那么，编程的重点是什么。难道就是写出操作过程来？不一定，编程也可以是声明式的，也可以用于产生其它的任何的东西。因此，编程有很多种方式。在数据分析中，在文档管理中，甚至在管理社会的过程中，我们都要与编程打交道。

Pandoc的读取器Readers与写入器Writters都在Text.Pandoc模块里面。参考<http://johnmacfarlane.net/BayHac2014/#/readers-and-writers>，我们可以在Haskell的交互式命令行中尝试写几行代码出来：

```haskell
:m + Text.Pandoc
let doc = readMarkdown def "*hi*"
doc
writeLaTeX def doc
readMarkdown def{readerSmart = True} "dog's"
```

在第三行之后会显示出doc的内容（是一长串的文法）。此外，我们看到，在第二行回车之后Haskell再执行加载模块的过程。大概这反映了Haskell的惰性求值的特性：即使是模块，实际上也是在第一次使用的时候才被加载的。

上面的文法中，readMarkdown是从字符串中生成Pandoc文法树。而writeLaTeX则是从文法树中生成LaTeX文本。

Pandoc的类型定义在模块Text.Pandoc.Definition当中。使用`pandoc -t native`{.shell}可以看出来一个Markdown文档经过编译之后的文法树。

Text.Pandoc.Builder是构建文档的重要的类。因为单独操作List太麻烦了，所以Pandoc使用Builder建立了Inlines与Blocks这样的元素（继承自Sequences），这样可以匹配更复杂的一些结构。对一个Pandoc文法树进行变换，则要使用Text.Pandoc.Generic与Text.Pandoc.Walk。下面是让文本中的所有的字母大写的程序：

```haskell
module AllCaps(allCaps) where
import Text.Pandoc.Definition
import Data.Char(toUpper)

allCaps :: Inline -> Inline
allCaps (Str xs) = Str $ map toUpper xs
allCaps x = x
```

上面的代码中，把allCaps导出为模块的一个函数，然后它会把字符串转成大写，其它的元素仍然保持原状。（不过，代码中的美元符号是什么意思还真不明白）。不过，上面的代码不是直接执行的，而是采用如下的方式：

```haskell
ghci AllCaps.hs
Text.Pandoc.Walk.walk allCaps $ Para [Emph [Str "hi]]
```

上面的代码中，一定要使用Walk来调用allCaps，也就是walk把allCaps应用在某个文档中。allCaps显然不是直接应用于某个元素上的。

### 过滤器的本质

这一点对于写过滤器至关重要。实际上，过滤器就是一个变换`f :: Pandoc -> Pandoc`{.haskell}，也就是说，过滤器把一个Pandoc文档变成另外一个Pandoc文档。如果过滤器成为一个单独的程序的话，过滤器要从main开始。形式如下：

```haskell
main = interact (show . f . read)
```

通过

```shell
pandoc -t native -s | runghc f.hs | pandoc -f native -s -t latex
```

就可以执行一个过滤器。但是过滤器也可以变成JSON的格式。这样处理的速度会快一点。代码如下：

```shell
pandoc -t json -s | runghc fjson.hs | pandoc -f json -s -t latex
```

或者采用简化的形式：

```shell
pandoc -s -t latex --filter fjson.hs
```

Text.Pandoc.JSON模块提供了toJSONFilter命令。该模块把任何一个`a->a`或者`a->[a]`或者`a-> IO a`的函数变成一个JSON过滤器，其中a是一个Pandoc的类型。用法是：

```shell
import Text.Pandoc.JSON
import ALlCaps (allCaps)
main = toJSONFilter allCaps
```

比如下面的代码，将强调变成是全大写的形式（而不使用加粗）

```haskell
import Text.Pandoc.JSON
import Text.Pandoc.Walk
import AllCaps (allCaps)

emphToCaps :: Inline -> [Inline]
emphToCaps (Emph xs) = walk allCaps xs
emphToCaps x = [x]

main :: IO ()
main = toJSONFilter emphToCaps
```

实际上，`pandoc --filter`命令把输出的格式作为第一个参数传递给过滤器，因此，过滤器可以根据输出的格式决定自己的行为。toJSONFilter的输出格式是Maybe。这样，具有格式设置的Pandoc的filter就写成了：

```haskell
import Text.Pandoc.JSON
import Text.Pandoc.Walk
import AllCaps (allCaps)

emphToCaps :: Maybe Format -> Inline -> [Inline]
emphToCaps (Just f) (Emph xs)
  | f == Format "html" || f == Format "latex" = [SmallCaps xs]
emphToCaps _ (Emph xs) = walk allCaps xs
emphToCaps _ x = [x]

main :: IO ()
main = toJSONFilter emphToCaps
```

<http://johnmacfarlane.net/BayHac2014/exercises.pdf>上面给出了编写过滤器的常见的任务，然而自己觉得，没有答案，怎么看？里面提出的问题还是比较好的，比如嵌入TikZ，识别python代码块，再比如说，把强调变成是下划线的格式。

### Pandoc文档的结构[06-21-2015 11:11:41]

参考了<http://www.pandoc.org/scripting.html>。整个文档的模式是这样的，整个文档是树状的结构，根元素是`Pandoc`。文档中，有一个`Meta`的块，里面包含各种键值对，以及`Block`块的列表。这些Block中，每一个都是一个元素。`Block`可以有许多的类型，比如有的`Block`是`Header`，有的是`Para`。各个`Block`中内部都由`Inline`的元素构成。Pandoc的AST结构，可以详见<http://hackage.haskell.org/package/pandoc-types>。

下面一段代码：

```haskell
behead :: Block -> Block
behead (Header n _ xs) | n >= 2 = Para [Emph xs]
behead x = x
```

可能很容易理解：就是说，behead是一个Block到Block的变换，如果Block的类型是Header，并且Header的参数层次大于等于二，那么就把内容直接转成Emph一样的Inline的元素，其它的情况下保持不变。Pandoc的读取与写入可以是这样的：

```haskell
readDoc :: String -> Pandoc
readDoc = readMarkdown def

writeDoc :: Pandoc -> String
writeDoc = writeMarkdown def
```

这样就实现了Markdown格式与Pandoc文法树的相互转换。

如果要从标准输入和标准输出读取，那么就是：

```haskell
main :: IO ()
main = interact (writeDoc . walk behead . readDoc)
```

walk函数就是把一个`Block->Block`的函数，变成一个`Pandoc->Pandoc`的函数。

下面的代码是匹配与处理Inline元素的方法：

```haskell
extractURL :: Inline -> [String]
extractURL (Link _ (u,_)) = [u]
extractURL (Image _ (u,_)) = [u]
extractURL _ = []
```

上式说明了Link与Image都可以看成是Inline的元素，其中u是元素的内容。对于行内元素来说，query函数可以把一个作用在Inline上面的函数变成一个作用在整个Pandoc上面的函数。

这样一来，写一个filter处理过程的方式就清楚了，首先是匹配我们感兴趣的元素，比如Inline或者Block，写出这样的处理函数之后，我们现用walk或者query把它提升到对整个Pandoc进行变换的函数。变换之后，再进行write的操作。不过，这种过程当中，我们并没有涉及到输出的格式的问题。

此外，JSONFilter用于把Pandoc转换JSON格式的树。它与Pandoc可以相互转换。因此，可以让Pandoc输出JSON格式，然后使用JSON格式的过滤器，这样可以导出到其它的语言的接口。总而言之一句话，Pandoc格式中中关心内容，处理格式的问题是通过自己写脚本来完成的。

#### 下面的函数匹配具有include属性的CodeBlock


> 注意下面的代码当中，把`@<<`进行了转义。否则的话编译的结果就会被noweb错误解析。

```haskell
#!/usr/bin/env runhaskell
-- includes.hs
import Text.Pandoc.JSON

doInclude :: Block -> IO Block
doInclude cb@(CodeBlock (id, classes, namevals) contents) =
  case lookup "include" namevals of
       Just f     -> return . (CodeBlock (id, classes, namevals)) =@<< readFile f
       Nothing    -> return cb
doInclude x = return x

main :: IO ()
main = toJSONFilter doInclude
```

主要的布骤也很简单，就是使用`cb@`进行匹配。那么，关键的问题就来了，一个是各种各样的元素该怎样匹配，另外一个，就是如果已有一个元素了，我们该怎样把这个元素转换成另外一种元素（由于Haskell是静态类型的）。

#### 处理Markdown文本中的原始HTML，并且处理输出格式的过滤器：

```haskell
-- handleruby.hs
import Text.Pandoc.JSON
import System.Environment (getArgs)

handleRuby :: Maybe Format -> Inline -> Inline
handleRuby (Just format) (Link [Str ruby] ('-':kanji,_))
  | format == Format "html"  = RawInline format
    $ "<ruby>" ++ kanji ++ "<rp>(</rp><rt>" ++ ruby ++ "</rt><rp>)</rp></ruby>"
  | format == Format "latex" = RawInline format
    $ "\\ruby{" ++ kanji ++ "}{" ++ ruby ++ "}"
  | otherwise = Str ruby
handleRuby _ x = x

main :: IO ()
main = toJSONFilter handleRuby
```

该过滤器可以将出现在Markdown中类似`[はん](飯)`{.markdown}的链接，处理成`<ruby>ご<rt></rt>飯<rp>（</rp><rt>はん</rt><rp>）</rp></ruby>`{.html}这样的HTML文本。而上面的脚本的关键在于handleRuby功能。特别要注意对format的匹配，是如何与Pandoc中的Inline元素配合的。具体的函数是所谓的`RawInline format $ "strings"`{.haskell}，也就是说RawInline可以接受字符串并构造出相应的内容。

上面的代码中，注意ruby不是编程语言中的ruby命令，而是ruby风格的HTML高亮。而且在上面的脚本中，ruby只是模式匹配中的一个变量。

#### 示范LaTeX的Math功能

假如我们想把所有的InlineMath改成DisplayMath，可以写如下的过滤器：

```haskell
mathConvert :: Inline -> Inline
mathConvert (Math InlineMath xs) = (Math DisplayMath xs)
mathConvert x = x
```

这样的话，可以把行内公式转换成为行间公式。但是我们可能有其它的需求，比如说，我们想在markdown文本中使用`\(..\)`来输入行内公式，以及我们想给行间公式编号，或者输出更复杂的DisplayMath形式。那个时候又该怎么办？

第一个要求明显是要改变Pandoc解析器的行为。第二个明显是要添加引用功能。不过，输出的格式倒是容易改变，比如，通过Format来改变输出的函数。但是输入该怎么办。但是输入该怎么办？在HTML的格式的情况下，我们甚至还希望输出数学公式为SVG的格式。这个时候当然也是需要处理的。

下面是一个将数学公式转换成SVG的格式的示例：

```haskell
import Text.Pandoc.JSON
import System.Directory
import System.FilePath ((</>))
import qualified Data.Hash.MD5 as MD5
import System.IO
import System.IO.Temp
import System.Process
import Control.Monad (unless)

mathToSvg :: Inline -> IO Inline
mathToSvg m@(Math mathType x) = do
  let wrap = removeNewline . case mathType of
                   InlineMath -> \x' -> "\\("++x'++"\\)"
                   DisplayMath -> \x' -> "\\["++x'++"\\]"
      preamble =[
          "\\documentclass[border=1pt,varwidth]{standalone}",
          "\\usepackage{standalone}" ++
          "\\usepackage{amsmath}" ++
          "\\begin{document}"
        ]
      postamble = [ "\\end{document}" ]
      removeNewline = filter (`notElem` "\r\n")

  tempDir <- getTemporaryDirectory
  let cacheDir = tempDir </> "pandoc.texsvg.cache"
  createDirectoryIfMissing True cacheDir
  let mathHash = MD5.md5s $ MD5.Str $ show m
      outfilename =  cacheDir </> mathHash ++ ".svg"

  fileExists <- doesFileExist outfilename

  unless fileExists $
    withSystemTempDirectory "pandoc.dir" $ \tmpDir ->
      do
        origDir <- getCurrentDirectory
        setCurrentDirectory tmpDir
        phandle <- runProcess "latex"
                             (preamble ++ [wrap x] ++ postamble)
                             Nothing Nothing Nothing (Just stderr) Nothing
        _ <- waitForProcess phandle
        shandle <- runProcess "dvisvgm"
                             ["-b2pt", "-Z1.2", "-n", "-o", outfilename, "standalone.dvi"]
                             Nothing Nothing Nothing Nothing Nothing
        _ <- waitForProcess shandle
        setCurrentDirectory origDir

  svg <- readFile outfilename
  return $ RawInline (Format "html") $ case mathType of
    InlineMath -> svg
    DisplayMath -> "<p>"++svg++"</p>"
mathToSvg x = return x
```

这里，mathToSvg变成了输出IO Inline的格式。

在输入检测方面，似乎可以是这样：检测到一个RawBlock之后，可以判断这个RawBlock是否是以`\begin{tikzpicture}`之类的开头的。如果是，那么就可以执行某些操作。不过，我们也很好奇，Pandoc是采用什么样的算法决定一个Block的类型的呢？也许我们可以通过Haskell的Shell先看一下。

在Pandoc中，latex环境不论是放在行内还是行间都被解析成RawBlock。（有一些预定义的environment被理我成inline的格式，其它的都是block级别的元素。与environment相比，如果environment在行内，可以使用span风格的HTML标签。

亳无疑问，排版的工作应该是一种声明式的编程的方法。有一个非常不好的地方，就是在Pandoc的文档中没有办法使用和定义变量。但是个人觉得应该是能够使用的。而且使用了变量之后的表现力应该是更好。像文学编程那样在注释中嵌入代码应该是更好的一些方法。这样，以后自己得多学习Haskell、OCaml以及Coq这些高级的语言了。


## 学习Pandoc的Markdown格式@2015年 05月 26日 星期二 14:47:32 CST

要在Pandoc下面有更好的体验，还是应该使用Pandoc扩展了的Makrdown。Pandoc的扩展主要体现在footnote、table、ordered lists、definition lists、fenced code blocks、superscript、subscript、strikeout、title blocks、automatic tables of contents、embedded latex math、citation等方面。参考<http://pandoc.org/README.html> 。

Pandoc的优势在于不是把Markdown简单用正则表达式解析，而是构造Markdown对应的语法树。这样的话，还便于应用程序的进一步的处理，比如过滤器。Pandoc的输出是单文件的，意味着这更适合于PDF输出，而非多页的HTML。如果是多页的HTML的话，应该使用另外的编译技巧。比如如下的代码：

```shell
pandoc -o ouptput.html input.md
```

上面告诉我们怎样调用pandoc程序输出结果。实际上，pandoc还可以从网址中得到结果，并不限于一个本地文件。-f表示转换前的文件类型--from，而-t表示转换后的文件类型--to。如果是文本，默认采用utf-8编码。不是此编码的，可以用iconv工具转换。

* 有些文件类型生成的时候，在头部有一些装饰，比如latex的导言区，HTML的头。对于这些格式，只有使用-s选项的时候，相应的头部才会出现在输出当中。
* 另外，有些时候，在.md文件里面有一些不能被pandoc解析的latex或者HTML命令。pandoc默认的做法是在生成分析树的时候把它们去掉。如果想保留它们，应该使用-R(--parse-raw)选项。
* -s(--smart)用于转换原有的.pandoc文档中一些格式，比如---,--，会优化排版效果。对于latex与context，此选项默认是开启的。除非使用--no-tex-ligatures把此功能关掉。
* 用户若想自定义template模板文件，最直接的方法是利用pandoc -D FORMAT选项，把模板打印出来，然后在原来的模板的基础上再改。
* TeX的层次标题系统与markdown不同。使用--chapters可以决定把.pandoc文件中的顶层的目录将被转换成chapter标题。而beamer则被转换成part。如果想对节编号，应该启用-N(--number-sections)选项。要改变latex处理引擎（只在生成PDF的时候才用到），使用--latex-engine=pdflatex,lualatex,xelatex选项。
* 参考文献的管理也有一定的技巧。一般来说，使用--csl指定引用样式，使用--biblatex指定相应的后端。但是使用biblatex之后，处理的结果只出现在latex当中，HTML文档中的引用就不会再出现了。

自己目前的看法是，pandoc主要是替代自己写latex文档的方式。因为之前的latex文档需要自己手动嵌入各种图形与代码，太麻烦了，所以自己现在使用pandoc帮助分析一下latex文档。这样的话，各种嵌入的元素就不用每次都要编译。自己抱着这个目的的话，写好latex的模块就足够了，不用考虑HTML格式的问题。

### Pandoc的模板语言

Pandoc的模板的设计思路是利用美元符号在原有文档中插入指令。比如，一个原来的LaTeX文档中，美元符号用来排版公式，现在移到模板里的话，每个美元符号都变成两个美元符号，才能透过模块实现输出。

模板中的文件 -> 经过Pandoc模板系统的过滤 -> 正常的latex头文件

常见的语法有：

```
$if(variable)$
X
$else$
Y
$endif$

$for(author)$
<meta name="author" content="$author$" />
$endfor$

$for(author)$$author$$sep$, $endfor$

$author.name$ ($author.affiliation$)
```

Markdown的原设计者提出的Markdown的规范可以参考<http://daringfireball.net/projects/markdown/>。在markdown中，paragraph指的是由一个或者多个空白行隔开的一行或者多行连续的文本。在Pandoc中，使用了换行跳脱符`\[newline]`。用它表示强制产生一个换行符。

标题有不同的风格，可以使用setext风格（标题文字下面有一行等号或减号）。也可以使用Atx风格的头（在行首有一个或者若干个`#`在标题中，都可以使用强调。Pandoc的`blank_before_header`扩展，强制标题前面有空行。这样，在Pandoc中，行首的数字符号也可以当成引用。实际上，`#`在Pandoc中被广泛用作引用。比如：

```markdown
# My header (#foo)

## My Header ## (#foo)

My other header  (#foo)
------------------------------------------------------------
```

在上面的例子中，`#`后面的标识符表示的就是一个引用。(这一规定与PHPMarkdown是相容的）。除此之外，Markdown的标题后面还允许一系列的字段，如：

```markdown
# My header (-)

# My header   {.unnumbered}
```

上面两段意思是相同的，表示本标题不参加编号。不过，第二种用法值得注意。因为它引入了面向对象的机制：一个标题是一个对象，其.unnumbered属性指出这个标题是一个不参加编号的标题。

Pandoc的`auto_identifiers`扩展使得每一个标题都有一个默认的引用标记。这个引用标记是根据标题内容处理得到的：除掉源文件中标题的所有的链接、脚注、除了连字符、下划线、逗号之外的标点，空格与换行符(每一个空格与换行都改成一个连字符)、并把字母转换成小写，并把标题中第一个字母前面的所有的内容删掉。如果除掉之后什么也没有，就以`section`作为引用名子。这些链接将在生成目录等场合被用到。

一个引用，可以按照如下的方式被调用：

```markdown
See the section on
[header identifiers](#header-identifiers-in-html-latex-and-context).
```

或者按照如下的被减化的形式：

```markdown
[header identifiers]
[header identifiers][]
[the section on header identifiers][header identifiers]
```

如果标题有重名现象，那么相关的引用指向引用被首次定义的时候的位置。但是注意，如果自己定义了一个以\#开头的索引，那么就不能使用这种方式。

对于被引用的块，使用>号开始。比如：

```markdown
> This is a block quote. This
> paragraph has two lines.
>
> 1. This is a list inside a block quote.
> 2. Second item.

> This is a block quote. This
paragraph has two lines.

> 1. This is a list inside a block quote.
2. Second item.

> This is a block quote.
>
> > A block quote within a block quote.
```

其中，被引用的块是可以被嵌套的。Pandoc的`blank_before_blockquote`要求在被引用的块前面添加一个空白行。(除了在文档第一行的情况）

##### 抄录文本

抄录文本指的是空格、制表符等都保持原样输出的文本。在Markdown当中，抄录文本前面空四个空格（或者一个tab）。在输出的时候，抄录文本前的四个空格会被去掉。

```markdown
下面是抄录的文本：

    if (a > 3) {
        moveShip(5 * gravity, DOWN);
    }
```

抄录的文本常用来排版不知名的代码（已经知道名称的代码常用内置的格式化器，而不再被当成Verbatim Text。

##### 围起来的块（Fenced Code Blocks）

Fenced Code Blocks直译就是围起来的块。但是中文译法，应该是叫嵌入的块，简称FCB算了。FCB块由一个只包含三个或以上的波浪线或左单引号的行开始，然后以不少于前面的字符数目的行结束。如：FCB也是可以嵌套使用的。

```markdown
    ~~~~~~~
    if (a > 3) {
      moveShip(5 * gravity, DOWN);
    }
    ~~~~~~~
    
    ~~~~~~~~~~~~~~~~
    ~~~~~~~~~~
    code including tildes
    ~~~~~~~~~~
    ~~~~~~~~~~~~~~~~
```

Pandoc的`fenced_code_attributes`扩展允许在FCB开头的行的后面添加一系列的属性，比如如下形式：

```markdown
~~~~ {#mycode .haskell .numberLines startFrom="100"}
qsort []     = []
qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++
               qsort (filter (>= x) xs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

其中，mycode指的是FCB的标识符，haskell与numberLines都被当成class。startFrom当成一个具有值100的属性。这些属性中的一些可以被用于语法高亮等目的。Pandoc内置了一些处理语法高亮的模块。

FCB块还有几种针对编程语言块简化的形式。它们常用于排版编程语言，是在.md中已有的文字的基础上修饰的结果。（不像是TikZ代码）。

~~~markdown
    ```haskell
    qsort [] = []
    ```
    
    ``` {.haskell}
    qsort [] = []
    ```
~~~

##### 行块Line Blocks

直译过来就是行块。但是还是用LB来称呼好一些。LB块指的是每行以一个竖线开头。

```markdown
| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical

| 200 Main St.
| Berkeley, CA 94718
```

其含义是换行符按照原样输出。行块的概念是来自于restructuredText。

##### 列表

Markdown的列表似乎与ReST的列表没有什么不同。连接起来的，中间不带空行的表示compact列表，而换行代表松散列表。

```markdown
用法1

* one
* two
* three

用法2

* one

* two

* three

用法三

* here is my first
  list item.
* and my second.

用法四

* here is my first
list item.
* and my second.
```

列表内容中的每一项也都可以跨行使用，但是想要跨行后的文本也视为列表的一部分，必须在段落前缩进至少四个空格。

```markdown
* First paragraph.

  Continued.

* Second paragraph. With a code block, which must be indented
  eight spaces:

      { code }
```

列表也可以嵌套：

```markdown
* fruits
    + apples
        - macintosh
        - red delicious
    + pears
    + peaches
* vegetables
    + broccoli
    + chard
```

##### 排序号的列表

示例如下：

```markdown
1.  one
2.  two
3.  three

5.  one
7.  two
1.  three

#. one
#. two
```

Pandoc的startnum允许如下形式的扩展：

```markdown
9)  Ninth
```

```markdown
(5) Three 1. Four * Five

#. one
#. two
#. three
```

##### Definition Lists

DL类似于latex中的Description List。指的是有一个被解释的文字。在Pandoc中的`definition_lists`扩展中，使用DL的方法如下：

```markdown
Term 1

:   Definition 1

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.

下面的示例将在每个definition前面产生空格。

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b
```

##### Examples

Examples相当于提供一个编号的例子环境，用于展示多个例子。在at后面可以添加一个标识符，以便引用这个例子。

```markdown
1. My first example will be numbered (1).
2. My second example will be numbered (2).

Explanation of examples.

3. My third example will be numbered (3).
```

Numbered examples can be labeled and referred to elsewhere in the
document:

```
* This is a good example.

As (@good) illustrates, \ldots{}
```

Pandoc的机制使得在列表后面跟一个缩进四空格的代码块变得困难，因此，为了把代码块断开，需要显式地使用end of list。例如：

```markdown
-   item one
-   item two

<!-- end of list -->

    { my code block }
```

或者我们想要断开两个连续的列表的时候，也使用`<!--end of list-->`

```markdown
1.  one
2.  two
3.  three

<!-- -->

1.  uno
2.  dos
3.  tres
```

##### 水平线

仅仅使用星号、下划线、减号构成的段落，可以生成水平线。

```markdown
*  *  *  *

---------------
```

##### 表格的制作

暂时跳过这一节。

### Pandoc扩展@2015年 05月 26日 星期二 16:06:27 CST

Pandoc支持在markdown文本的开始添加metadata。metadata都以百分号作为开头。其中title、authors、date是标题的信息。Pandoc会识别它

```markdown
% title
% author(s) (separated by semicolons)
% date
```

元数据块中的内容会被用于填充模板，并不会出现在正常的markdown中。

本质上，这种扩展与yaml格式的元数据是等效的。

如果调用

```shell
pandoc chap1.md chap2.md metadata.yaml -s -o book.html
```

那么，元数据块就会被直接使用。注意，前面已经说过，元数据块只在构建模板以及被filter等工具使用，所以即使元数据在chap1.md中出现，也不会对md文件造成直接的影响。

不过，yaml文件必须以---开头，以---或者...结尾。如果yaml块有多个，并且设置了相同的字段，那么第一个块会优先采用。后续的设置无效。

在使用YAML文件的时候也要注意，YAML中的逗号具有特殊含义，因此字符串中若有逗号，必须使用双引号括起来。而在行尾添加一个竖线，则紧跟在后面的段落缩进的时候，整个段落中的文本被原样拷贝。

```yaml
    ---
    title:  'This is the title: it contains a colon'
    author:
    - name: Author One
      affiliation: University of Somewhere
    - name: Author Two
      affiliation: University of Nowhere
    tags: [nothing, nothingness]
    abstract: |
      This is the abstract.
    
      It consists of two paragraphs.
    ...
```

模板变量会自动从元数据中被读取。由于Markdown很多标记使用的都是普通字符，所以字符的转义就非常必要了。`\`*_()[]{}>#+-.!`都是需要转义的。

##### 行内强调文本

行内强调文本使用星号或者下划线包围。特别强调的时候，星号与下划线各有两个。

```markdown
This text is _emphasized with underscores_, and this
is *emphasized with asterisks*.

This is **strong emphasis** and __with underscores__.

A * or _ character surrounded by spaces, or backslash-escaped, will not trigger emphasis:

This is * not emphasized *, and \*neither is this\*.
```

因为下划线经常被当成是标识符的一疗分，所以当下划线左右两边都是字母或者数字的时候，并不会被解释成强调符号。删除线使用两个波浪线开始。下标则使用单个波浪线括起来，而上标则使用单个\^号括起来。

```markdown
H~2~O is a liquid.  2^10^ is 1024.

This ~~is deleted text.~~
```

注意，markdown的上标与下标只比tex中的上标与下标坚强一点点。下标与下标是不能跨空格的，若想跨空格，必须把空格转义。

##### 行内文本抄录

```markdown
To make a short span of text verbatim, put it inside backticks:

What is the difference between `>>=` and `>>`?

If the verbatim text includes a backtick, use double backticks:

Here is a literal backtick `` ` ``.

(The spaces after the opening backticks and 
before the closing backticks will be ignored.)

Note that backslash-escapes (and other markdown constructs) do not work in verbatim contexts:

This is a backslash followed by an asterisk: `\*`.
```

##### 带颜色的文本

在行内抄录的后面可以添加一个大括号。在括号里面可以指定编程语言等属性，就和在FCB中的一样。

```markdown
Attributes can be attached to verbatim text, just as with fenced code blocks:
`<$>`{.haskell}

To write small caps, you can use an HTML span tag:

<span style="font-variant:small-caps;">Small caps</span>
```

注意，Pandoc中可以直接嵌入HTML与TeX的代码。

### Pandoc数学公式以高级扩展@2015年 05月 26日 星期二 16:24:38 CST

Pandoc的`tex_math_dollars`扩展允许在两个美元符号之间的内容看成是一个TeX公式。但是Pandoc有一个限制，就是左美元符号必须紧跟一个非空白字符，而右美元符号左边也必须是一个非空白字符。并且，在美元符号的两侧，还需要空白字符：若右美元符号跟的是一个数字，那么数学模式就会失效。必要的地方，美元符号也可以使用反斜杠转义。

#### 原始HTML序列

Pandoc能够识别原始的HTML块。它们可以在文档的任何地方出现。（使用扩展`raw_html`扩展特性）。这种功能一般不看成扩展，因为原始的Markdown也支持HTML。

不过，在HTML块当中，引用与强调还是会被解析的。比如`*one*`会被解释成`<em>one</em>`。

#### 原始TeX序列

Pandoc也能识别原始的TeX控制序列。例如：

```markdown
This result was proved in \cite{jones.1967}.

\begin{tabular}{|l|l|}\hline
Age & Frequency \\ \hline
18--25  & 15 \\
26--35  & 33 \\
36--45  & 22 \\ \hline
\end{tabular}
```

一般来说，普通命令与环境才会被解析。为了支持TeX宏，必须使用`latex_macros`扩展（而不是`raw_latex`扩展）。使用`latex_macro`之后，可以在文本中使用newcommand与renewcommand自定义命令。

#### URL链接与内部链接

我们先不管这个特性。脚注我们也暂时不管。

引用有几种处理方法。在生成其它的格式的时候，需要使用pandoc-citeproc。不过，目前的实现似乎并不如意。

使用pandoc制作幻灯片，我们也暂时不管它。

### Pandoc的编程@2015年 05月 26日 星期二 16:45:37 CST

首先看pandoc的pandocfilters库。该库接受参数的形式是`{abc(key, value, format, meta)}`。函数中，key指的是元素的名称，如Code Block。而

```python
[[ident, classes, keyvals], code] = value
```

也就是value中的classes是块的类型（比如abc-notes，keyvals是传给块的参数，code是块里面的内容。format是输出的格式，meta则是环境变量，从环境中可取得元数据。

其中，我们看到。

```markdown
    ```abc-notes { start=100 }
    code
    ```
```

这个语法中，abc-notes是这个块的类型（一个块可有多个类型，比如同时是一个.haskell和.numberLines。匹配的时候，一个块也就可以有多次可能。键值对是放在keyvals中的，以

```python
[['', ['abc-notes'], [['startFrom', '100']]]
```

的形式存在。


## Pandoc文档系统更进一步介绍[04-14-2016 19:50:52 CST]

可能我们还是通过已有的模板来确定哪些评论系统更好。这个时候我们希望在网站上添加尽可能方便的模块。<http://maskray.me/blog/2012-11-14-build-static-website-with-docpad>上面列出了静态网站的一些要求。比如使用disqus这类的评论的系统，然后使用Node.js社区的一个Jade、Stylus等CSS的方案，方便我们去写CSS。个人觉得内容的管理系统可能是工程化管理的一个基本的要求吧。这个时候我们是在组织当中考虑问题而不是在其它的情况下。

其它的些建站的系统有Node.js社区的DocPad、Ruby的Slim等。Slim即是所谓的前端的一个模板语言。听起来似乎是方便了很多。不过自己学过太多的模板语言了。但是自己就是比较懒，不想写出来这些Slim的语言。Slim的模板的语言见<http://slim-lang.com/>。有时间自己也许应该专门为模板语言准备一份文档吧。

至于DocPad可以参考<https://github.com/docpad/docpad>。这些网站前端开发工具与后端是差不多的。都是使用编译系统与版本管理系统。DocPad看起来还不错，是一个不错的轻量级的开发的工具。有时间或许真的应该学习一下。

不妨参考一些博客的示例，比如<https://xinitrc.de/blog/2014/02/15/Magic-tricks.html>中的方案。里面包括数学在内的许多的东西都有。不过有希望的话，自己还是希望一份笔记可以支持多种输出的格式，像Pandoc这样的解决方案一样。可以参考这两个网站<https://github.com/sadhen/sadhen.com>，以及<https://github.com/xinitrc/xinitrc.de>。个人觉得是排版还不错的网站。

<https://github.com/bramblex/loveaira.me>也不错。不过是动态的网站。使用PureScript来写成的。静态网站生成器见<http://www.cnblogs.com/jifeng/p/3753696.html>。

简单的绘图的工具可以参考ditaa，或者所谓的plantuml这一个程序。使用它们可以快速地将内容引导出来。个人感觉好像应该弄一个协作的系统出来。让文档可以变得比较正常地能够引用别人的东西。如果不能引用，也就失去了许多意义了。最好还有一个讨论的系统，这样才比较好。

另外自己之前试过grunt-latex这样的一个程序。好像是用于自于编译latex的。不知道使用起来怎么样。另外，如果能够在PDF上面评论还不错。就像Wiley的PDF查看的系统那样。那样的话再加上改进，学习交流可能会更好一些。


## Pandoc的参考文献输入介绍[07-06-2016 15:58:34 CST]

根据Pandoc的文档，使用`[@abc]`与` @abc `这样的样式可以直接引用相应的条目。支持的后端条目包括.bib、.bibtex、.json、.xml、.yaml等格式。特别是reference可以嵌入到Pandoc的元数据当中（如果是.yaml，以reference字段标识，如果引用来自于文件，那么使用bibliography字段指明引用的文献）。

有了这样的机制，通常有两种选择方法可以让我们正确处理好引用。其中的一种是使用`pandoc-citeproc`。

```shell
pandoc --filter pandoc-citeproc filename.md
pandoc --filter pandoc-citeproc --bibliography myrefs.bib filename.md
```

而另外的一种就是，如果输出是PDF或者LaTeX，那么就使用natbib或者biblatex的样式输出，样式是：

```shell
pandoc --biblatex -t latex filename.md
```

这种方式就很好地处理了引用的问题，里面的引用会被处理成适当的biblatex引用命令。最后我们需要在文件结尾自行添加`\printbibliography[heading=none]`之类的命令，并且在头文件中指明所使用的\LaTeX{}的宏包。

## Pandoc文档模型[11-07-2016 18:26:33 CST]

要想从事开发的话，数据模型的理解还是必须要有的。自己这里就从读Haskell的Pandoc的文档库的代码开始吧。
