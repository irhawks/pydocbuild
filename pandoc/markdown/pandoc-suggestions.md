# 自己对pandoc的一些想法[12-03-2016 16:07:31 CST]

[12-03-2016 15:59:25 CST]似乎Pandoc的系统还有一些缺陷，文档模型还不够细致。比如说，Table的结构其实应该是这样的：

```
-- 一个表格应该是一个二维的Block的结构　
TableBody := TableBody [[Block]]
-- 一个表格添加上一个块，应该是一个带有元数据的结构
Table := Table (TableCaption TableBody)
-- 而TableCaption应该由标题等部分来构成
TableCaption := TableCaption Title Reference AttributeList
-- 其中的属性应该是链值对
AttributeList := AttributeList [(key, val)]
```

各种各样的Caption结构，其实也可以用在其它的环境当中，比如Theorem当中。

```
-- 定理环境由一个标题和一个主体来构成
Theorem := Theorem Caption TheoremBody
-- Caption环境则指出Caption的类型等
Caption = Caption "Theorem" Title Number Reference Attributes
```

所以说，设计一个编程语言，起点是其数据类型定义。特别是构造各种各样的数据类型或者数据结构。(Pandoc当中的其实已经是递归数据结构了)。


### 应该有默认属性[12-03-2016 16:15:33 CST]

自己觉得像行内属性，比如`` `import sys`{.python} ``这样的代码块，其实应该可以设置默认语言的，也就是默认的属性。但是要设置默认的属性并且可以更改，还是得借助于Pandoc的指令，相当于Pandoc有一个指令式的结构决定当前的块具有怎样的属性，这就需要一个存储器来存储Pandoc当前的Read的状态。这样的话，Pandoc更像是一个编程语言。只有全局状态而没有局部状态的Pandoc，似乎很难应付这种默认参数的情况吧。

> 但是如果markdown文档有了自己的局部状态，似乎也并不好处理，这个时候需要通过遍历来把各种各样的指令处理掉，比如在模型树的某个层次上约定的默认的代码语言，那么在构建好树之后，就应该将这个指令应用到所有的没有设置语言的代码当中，结果，就必须进行一种自顶向下的递归了。当然，如果有一天能够自动推断代码语言也是不错的选择。

### 应该对于单行文本也有属性[12-03-2016 16:31:17 CST]

我们在表达强调的时候，可能会希望有不同的颜色，比如我们可能希望markdown代码`*Emphed*{color=red}`来表示使用红色的字体来强调。这也未尝不可，虽然不是什么标准的做法。原则上这样的代码应该也能够写出来。如果不愿意，那么其实我们还可以以这样的形式来表达行内文本的强调：`*Emphed*{.wrong}`，`*Emphed*{.right}`。通过wrong和right来表示不同的强调语义。

### 应该能够直接插入构造符[12-03-2016 16:34:19 CST]

比如我们可能希望在中间添加特定的LaTeX代码，这个时候Pandoc可能以这样的形式而出现：

```markdown
markdown text before ...

{-- LaTeX definitions are required
% LaTeX Verbatim Output
\newcommand...
--}

markdown text after ..
```

这种样式，使得在输出LaTeX需要相应的定义的时候，可以直接按照RawBlock输出到特定的格式当中。

> 但是这样好像违反了人们制作markdown的本意。人们制作markdown的本意其实是希望文档足够简单的，而不是添加各种各样的复杂的扩展与处理结构。



## 对于Pandoc的改进计划(定义列表)[12-04-2016 22:14:43 CST]

为了更好地转换成latex的列表，自己建议对于definition list采用如下的结构：

```
    ~~~Defintion {inline, aboveskip=10pt}
    [Item1] Explanation1
    [Item2] Explanation2
    ~~~
```

这样做的唯一的好处其实就是可以将被解释项变得更为紧凑了。此外，我们还可以给Definition添加上各种各样的属性，比如aboveskip，inline等（表示行内代码）结构。


## 加亮pandoc行内文本的另外一种方法[12-08-2016 20:30:38 CST]

critiicmarkup<https://github.com/vim-pandoc/vim-criticmarkup>项目提出了一种新的加亮VIM标记的方法。这种标记可能更容易操作，比如：

```markdown
Additions: That was a {++very ++}hasty comment.
Deletions: It is {--not --} uncommon for people to tell the truth.
Substitutions: The {~~bird~>condor~~} flew majestic through the skies.
Comments: I believe this is not enough.{>> @editor on what grounds? <<}
Highlights: {==Some sources==}{>> Which? <<} mention ὰταραξία as the ancient skeptics goal.
```

可以实现加亮，下划线，删除线等标记的效果。应该说，这样的标记确实是非常方便的。但是在pandoc当中，可能使用中括号才是更合理的做法。毕竟各类标识使用的都是中括号的方式。但是有时候好像使用大括号也是可以的。目前在pandoc当中，中括号与美元符号都不是随便可以使用的（前者表示超链接，后者表示latex），还有@符号，也不是随便可以使用的。此外，`~~`符号在pandoc里面也是有特殊的含义的。


### 定理环境的设计[12-08-2016 20:35:22 CST]

自己觉得定理环境还是应该根据pandoc的设置来。大概可以这样做：

```markdown
    ~~~Theorem #1.1 {inline, aboveskip=10pt}
    a^2+b^2=c^2
    ~~~
```

还有一些数学公式环境，比如Align等等。我们不妨这样设计：

```markdown
    ~~~LaTeX.Aligned #1.1 {inline, aboveskip=10pt}
    放置数学公式环境
    ~~~
```

因为用这样的表示语言的话，会使得文档结构的层次更清晰一些吧。

markdown一方面要保持通用性，另一方面又要解析各种各样的不同的Block结构，确实是比较困难吧。再比如化学当中经常出现的化学式，又该怎样排版呢？使用chemfig？这样的话，其实又是必须要有一个排版行内Code的工具。

归根结底，pandoc还是需要各种各样的filter与processor。并且还可能需要维护一个全局的列表吧。文档原始代码的话，不妨使用`.raw`类型，或者`.pandoc`类型。或者说同时保持这种类型，但是在derivations的时候注明是verbatim抄录。比如

```markdown
    ~~~Html .Raw .Verbatim {inline}
    <div>abc</div>
    ~~~
```

因为毕竟是需要按照本体论的思想来处理：这段代码块的类型是什么，有什么样的属性，pandoc怎样处理它们。还有一个层次：功能是什么。比如说，Theorem环境，可能是LaTeX的代码的格式，也可以是HTML代码格式，也可以是Pandoc的代码格式（因为Pandoc应该也容许在代码当中混入其它的标记语言吧）。这样的话，就容许我们从各种各样的不同的来源当中copy与paste有关内容了。比如具有Theorem功能的代码块，我们默认的仍然是markdown格式，因为这种格式可以输出多种语言。但是如果用户非得选择的话，我们应该也容许使用LaTeX格式来定义Theorem。全面描述应该是这样的：

```markdown
    ~~~function=Theorem format=LaTeX label=th1.1 [attribute_list]
    ~~~
```

### 关于markdown的parser改变行为的问题[12-08-2016 21:02:39 CST]

pandoc在解析markdown文件之类的时候，根本的问题也就是改变部分parser的方式而已。这个时候，自己觉得应该把markdown看成是一种编程语言。允许这种编程语言切换不同的parser的模式。比如有的地方，我们可能希望pandoc当中允许比较宽泛的解析定义。这个时候可以这样：

```markdown
    texts above ..., where `$ abc $` will not be regarded as latex formula.
    ~~~ParserOptions (start ...) (name = Ext_Enhanced_LaTeX_Formular)
    Change parser extensions to correctly parse `$ abc $`
    ~~~
    Then you can  type `$ a^2 + b^2 =c^2 $` as a latex formula
```

这样的话，其实我们不妨在每个markdown文件解析的时候就提出来明确的说明。比如中间定义一些新的解析器，这样的话，可以让markdown适应各种各样的环境。然而，如果将markdown视为一种编程语言，也可能并不是那么容易做到，尤其是在markdown当中还要定义各种各样的代码。

### 扩展markdown的codeblock的方法[12-08-2016 21:08:16 CST]

markdown的codeblock可以由 `` \`\`\` ``或者`~~~`开头的行来引起。但是其实这样的CodeBlock还可以是其它的格式，比如使用`@@@`，`$$$`、`%%%`、`^^^`，`[[[`、`@<<`等等符号都是可以的。因为这些符号单独出现并且作为一行的情况并不多见。甚至只有符号出现的行都是很少见的，这样的话，我们可以充分利用这些机制来解析Pandoc。

注：实际上，以特殊符号开头的行本来就不多（在文字工作当中）。

但是由于Haskell是一种静态编译的语言，实现动态运行可能还是有一些问题，这样的话，通过操作Haskell代码来定义即时作用的Parser可能就不太合适了。

注：我们的目标似乎是希望markdown能够像PHP语言那样嵌入在HTML当中，并且强力地操作HTML。这种嵌入式语言并不是那么容易可以做到的。然而，毕竟这样的事情我们还是需要做的。

至于行内插入简短的代码，似乎用文学编程当中的`@<..@>`也是一个不错的选择。毕竟出现`@<`与`@>`的情况也是非常少的。当然，我们还可以定义定义Parser的扩展，使得只在markdown文件当中的特定的一部分当中`@<...@>`才有效果。这样Parser扩展应该是`Ext_Literate_Programming_Verbatim_@< : String -> Block`。显然这种语言应该是一种能够动态改变Parser的语言。这种语言具有运行当中改变语言的词法解析与语法解析树的能力。自然语言其实就是属于这种动态Parser的语言。

注：当前的编程语言当中，动态地改变Parser，好像还需要一个非常复杂的类型构造器，必须手动构造这样的Parser（比如使用`NewSyntax`这样的函数），结果自然而然地改变Parser就会非常复杂。我们希望能够有一种Parser的元语言就可以了。比如直接正则表达式到Parser结构(`MatchString and build Syntax_Tree`。就像这样：

```markdown
    @<\(.*\)@> -> Emph "\1"
```

值得注意的是，这种正则表达式转换其实看起来也并不是那么复杂，因为我们完全可以使用这样模式。然而问题在于，正则表达式的匹配是全局匹配的，像VIM一样工作。而且正则表达式处理递归结构其实并不好。如果本质上是递归结构，其实应该这样转换：

```markdown
    String("@<") Block String("@>") -> Emph "\1"
```

这种递归结构解析，至少还会让我们看着更顺眼一些。Haskell提供了相应的Parser解析器。或许我们可以通过这个解析器来解析有关内容。但是要把Markdown弄成一个在运行的时候可以自行改变Parser结构的语言，恐怕还是非常困难的。


## 插入图片机制的理解[12-15-2016 11:57:43 CST]

直接使用插入图片的方法即可工作。fancybox不需要特别配置，直接从markdown产生。显然设计的思想就是，展示的方式属于layout，而不是内容。内容与格式相分离的要求使得我们直接展示图片就可以了。但是以后Pandoc应该支持FloatGroup这样的元素。也就是一个浮动组，包括各种元素。甚至还可以修改图片的显示位置。图片，表格之类的，都归为ReferenceObject。暂时这样吧。

实际上应该是这样的：正文当中仅仅是一维或者二维的元素而已。这些元素如果具有脱离上下文的意义，那么应该将它们独立出来。比如说特定的插图或表格。
