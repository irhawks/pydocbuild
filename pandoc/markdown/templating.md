# 模板与模板系统[12-15-2016 13:54:08 CST]

模板引擎系统通常包括HTML、CSS、Javascript。模板引擎有基于字符串的，也有像Scala的play所使用的那种类型安全的模板引擎。其效果与LaTeX类似。<http://www.csdn.net/article/2013-09-16/2816951-top-five-javascript-templating-engines>上面介绍了五种JavaScript的模板引擎。读完这些之后，我们或许会对于扩展Markdown有更多的启发。

当然，LaTeX也有类似的机制。其实自己觉得扩展方面，其实LaTeX做得更好。比如Verbatim模式`\begin{verbatim} ... \end{verbatim}`，以及Verb模式`\Verb|...|`这样的行内的模式。其实已经是非常先进的了。但是有时候，我们还是想用一个作用于markdown的模板引擎系统，以减轻markdown的排版压力。比如说在排版的时候使用变量。这个时候就不仅仅是嵌入代码这样简单的事情了。可以基于原来的markdown的系统，比如左单引号的方式。但是似乎又不是很好。当然， `` `$varname`{.java} `` 这样的方式也不是不能使用。但是总显得麻烦。或许使用这样的扩展也不错：``{{your coding here}}.{extend}``。总而言之，有非常多的选择。但是一旦有了选择之后，我们就要注意不能随便变。而且模板系统是基于字符串替换的，它未必理解markdown的语义系统。(比如自动计算上下文semantic信息。

个人觉得，也许应该给Markdown添加一个Semantic类型的元素。这个Semantic类型的元素可以根据上下文类型进行转换。比如

```haskell
Semantic := Semantic SemanticType SemanticBody
SemanticType := JavaCode | PythonCode | ...
processSemantic :: Semantic -> Block
processSemantic :: Semantic ImageDrawing = ...
```

上文中的内容，就是在Pandoc当中定义Semantic的Block类型，而Semantic的Block类型需要进一步被处理成各种各样的Block或者其它的样式（其实Semantic也可以看成是一种InlineBlock或者其它的部分）。创建相应的Semantic过滤器就可以了。

Mustache模板使用`{{ ... }}`来表示占位符。在双大括号里面的内容是需要处理的内容。里面的内容表示被处理的代码。Underscore模板使用的是`<%..%>`。EJS的模板系统与Underscore是类似的。至于Jade，则像SCSS之于CSS，产生了比较大的外观变化。也有一些使用`{%..%}`来表示模板引擎。

Haskell下面的Template Engine有The heterocephalus package之类的。自然而然，与Scala一样，这些包都至少有一定的类型安全特性。(如果里面能够嵌入一个完整的编程语言就好了。或者Template Engine可以支持多种语言。甚至是像Jupyter的Notebook那样工作(通过调用后端的各种编译器来生成文档)。

在Haskell当中，Yesod使用的模板是类型安全的[Shekespearean](http://www.yesodweb.com/book/shakespearean-templates)。

注：在使用上，在左括号上面直接接一个特殊符号的现象可能并不多，正式的文本当中，甚至在许多代码当中也并不多见，因此大概可以利用上。比如`%{`、`<{`、`>{`、`#{`、`@{`、`?{`这样的符号。既然实际当中绝少出现，似乎我们就可以把它们理解成一个特殊的Block吧。也许可以通过这样的方式来扩展Pandoc的解析。但是解析的时候似乎应该注意的是，这些符号应该与Pandoc一起作用。这样的话，Pandoc的工作过程是这样的：

Tokenize -> Resolve -> Generate. 其中首先的Tokenize当中就应该识别出来文档的顶层结构。然后Resolve来求解，最后是生成文档。比如


```
{% for i = 1:10 %}
# Hello, world, {> titleOf(i) <}
{% end for%}
```

这样的语句应该首先看出来代码结构，然后生成十个顶级标题。(其中`{>`的含义应该是表示把函数的Show属性拿出来)。
