# 自己写的pandoc过滤器（使用Haskell）[11-08-2016 17:07:30 CST]

## 自己写的生成.nw文件的pandoc的过滤器[11-08-2016 17:08:05 CST]

自己终于磕磕绊绊地写出来了一个执行Haskell过滤的一个Pandoc的过滤器，在生成的格式为latex的情况下可以正常输出结果。

个人感觉，过程当中，最重要的是掌握[Data.Maybe](https://hackage.haskell.org/package/base-4.9.0.0/docs/Data-Maybe.html)。因为这样可以把Maybe值解压出来。然后就是字符串的连接，使用`++`符号。再一个困难就是使用Haskell的lookup函数来查找一个键的值。<https://www.haskell.org/hoogle/?hoogle=lookup>。还有，就是参考[Pandoc的定义](http://hackage.haskell.org/package/pandoc-types-1.17.0.4/docs/Text-Pandoc-Definition.html#t:Format)来构造生成的块，比如RawBlock。

在写过滤器的过程中处己参考了几个Haskell过滤器，比如<https://github.com/dfaligertwood/pandoc-filters/blob/master/pandoc-sidenotes.hs>，<https://github.com/dfaligertwood/pandoc-filters/blob/master/pandoc-ednotes.hs>、以及<https://github.com/dfaligertwood/pandoc-filters/blob/master/pandoc-divs.hs>。

有了这个过滤器，应该足以处理使用Noweb所写的Pandoc的笔记了吧。（ENDO.1分类当中有一个format-pandoc.nw文件，该文件比较详细地描述了Pandoc的文档模型）。

```{.haskell #nwcode}
#!/usr/bin/env runhaskell
-- includes.hs
import Text.Pandoc.JSON
import Text.Pandoc.Generic
import Text.Pandoc.Walk
import Data.Maybe

extractNwcodeToLaTeX :: Block -> IO Block
extractNwcodeToLaTeX cb@(CodeBlock (id, classes, namevals) contents) =
    case elem "nwcode" classes of
        True  -> return (RawBlock (Format "latex") $ 
            unlines ["\\begin{nowebtrunk}\n<<" ++ 
                (fromMaybe "*" (lookup "title" namevals)) ++ ">>=",
                contents, 
            "@ \\end{nowebtrunk}"])
extractNwcodeToLaTeX x = return x

main :: IO ()
main = toJSONFilter extractNwcodeToLaTeX


{-
exportNowebCodeChunks :: Maybe Format -> Pandoc -> Pandoc
exportNowebCodeChunks (Just "latex") = -}
```


### 过滤器的另外一种写法[11-08-2016 19:02:18 CST]

同样是针对latex输出写nwcode的例行程序，我们还可以这样写

```{.haskell}
#!/usr/bin/env runhaskell
-- includes.hs
import Text.Pandoc.JSON
import Text.Pandoc.Generic
import Text.Pandoc.Walk
import Data.Maybe

extractNwcodeToLaTeX :: Maybe Format -> Block -> Block
extractNwcodeToLaTeX (Just (Format "latex")) (CodeBlock (id, classes, namevals) contents)
    | "nwcode" `elem` classes = RawBlock (Format "latex") 
            (unlines ["\\begin{nowebtrunk}",
                "<<" ++ (fromMaybe "*" (lookup "title" namevals)) ++ ">>=",
                contents, 
            "@ \\end{nowebtrunk}"])
extractNwcodeToLaTeX _ x = CodeBlock (id, classes, namevals) contents

main :: IO ()
main = toJSONFilter extractNwcodeToLaTeX
```

这样写的话，结构更好，因为这里可以准确地匹配特定的Format，而不用再额外地判断相应的输出的格式。如果不匹配相应的格式，直接输出就行了。（也就是直接返回原来的codeBlock，而把nwcode的标记给去掉。把nwcode的标记去掉的方法是这样的：

```{.haskell}
import Data.List
extractNwcodeToLaTeX _ CodeBlock (id, classes, namevals) contents = 
    CodeBlock (id, filter (\ x -> not (x == 'nwcode')) classes, namevals) contents
```


真要学习pandoc的filter，可以从github上面搜“pandoc filter”，然后就可以找到很多别人已经写好的pandoc的有关的资料了。
