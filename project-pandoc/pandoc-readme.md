# 现在自己打算从头开始学习Pandoc[11-07-2016 19:31:03 CST]

除了需要Haskell的编程的技术，更多地还是需要关于HTML等文档调整系统的说明。因为自己在读Haskell的Pandoc的手册的时候，自己发现自己对于里面的数据结构有一些不了解。不知道该怎样构造出来。而看过HTML之后就比较明白了。

Pandoc库里面有一个Builder，用于比较简单地构造出来Pandoc文档。这样的文档显示的效果还是非常不错的。


### 从尝试开始阅读Pandoc手册开始[11-07-2016 19:33:27 CST]

首先当然是要阅读[Pandoc Types](http://hackage.haskell.org/package/pandoc-types-1.17.0.4/docs/Text-Pandoc-Definition.html)。特别是里面的Definition。因为它定义了一个Pandoc文档的抽象结构模型。首先，一个Pandoc的文档由如下的构造器来构造`Pandoc Meta [Block]`{.haskell}。其中的Meta当然是元数据字段，比如标题等内容，而`[Block]`自然而然就是块文件的列表了，比如各个段落。而要构造一个Block有许多的方式，分别是：

* `Plain [Inline]`
* `Para [Inline]`
* `LineBlock [[Inline]]`
* `CodeBlock Attr String`
* `RawBlock Format String`
* `BlockQuote [Block]`
* `OrderedList ListAttributes [[Block]]`
* `BulletList [[Block]]`
* `DefinitionList [ ([Inline], [[Block]]) ]`
* `Header Int Attr [Inline]`
* `HorizontalRule`
* `Table [Inline] [Alignment] [Double] [TableCell] [[TableCell]]`
* `Div Attr [Block]`
* `Null`

等等。其中我们自然而然地可以看出，Block的定义是递归的。因为一个Div构造子里面仍然可以包含一个Block。

接下来我们可以看其它的元素的构成。比如Inline元素的构造子可以是：

* `Str String`
* `Emph [Inline]`
* `Strong [Inline]`
* `Strikeout [Inline]`
* `Superscript [Inline]`
* `Subscript [Inline]`
* `SmallCaps [Inline]`
* `Quoted QuoteType [Inline]`
* `Cite [Citation] [Inline]`
* `Code Attr String`
* `Space`
* `SoftBreak`
* `LineBreak`
* `Math MathType String`
* `RawInline Format String`
* `Link Attr [Inline] Target`
* `Image Attr [Inline] Target`
* `Note [Block]`
* `Span Attr [Inline]`

我们可以看出Inline的定义也是递归的，并且包括了许多的实用的段落内部的元素。

在Pandoc的模型当中，明显模型当中，一个Emph只能管一个Inline对象而不能跨行起作用。但是这跟Pandoc的markdown没有关系，因为Markdown可以将跨行的Emph折开。（实际上也不能跨行起作用。显然，Pandoc的模型，也是以段落为基本结构的。也许有一天我们的一个Emph也可以强调多个行，但是今天，Pandoc模型还不容许这样做。也许有一天我们会改进强调的方法，从而容许多个段落用一个Emph来解析。

另外，String已经是Data.String包里面的数据结构了，是基础数据结构。


## 学习Pandoc的时候需要准备的一些HTML的知识[11-07-2016 19:48:46 CST]


在Pandoc当中，我们知道`Link Attr [Inline] Target`构成一个Block。但是Attr、Target各自由什么构成？我们来看如下的Pandoc的标记：

```markdown
[这是到百度的链接](http://www.baidu.com "百度一下，你就知道"){#baidu .mylink attr="hello"}
```

这个标记当中是有非常多的属性的，既有主要文字`这是到百度的链接`，又有网页地址`http://www.baidu.com`，还有`百度一下，你就知道`，还有引用标记`#baidu`，以及类名`.mylink`，以及属性名`attr=hello`。就比较复杂了。

其实这与HTML的历史是分不开的。<http://hdwiki.q.baike.com/article-17421.html>上面区分了alt属性与title属性。而<http://xueguang668.blog.163.com/blog/static/977221222011215364377/>则向我们指出，有一些HTML元素是有title属性的，title属性相当于tooltip，鼠标放上去会显示title属性的值。而alt表示替换文字，原意指的是如果图片不能显示，那么就使用图片中的文字代替（alt属性对于搜索引擎优化具有重要的意义）。

使用alt属性是为了给那些不能看到你文档中图像的浏览者提供文字说明。这包括那些使用本来就不支持图像显示或者图像显示被关闭的浏览器的用户，视觉障碍的用户和使用屏幕阅读器的用户。替换文字是用来替代图像而不是提供额外说明文字的。

理解这一点，我们对于Pandoc的Link的构造器也就会有更多的理解了吧。
