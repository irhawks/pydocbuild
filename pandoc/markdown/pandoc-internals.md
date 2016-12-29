# Pandoc的内部结构[12-03-2016 15:34:52 CST]

## 通过别人写的过滤器了解Pandoc文档构造[12-03-2016 15:35:08 CST]

内容见<https://github.com/chaoxu/blog/blob/master/MathDoc.hs>。可以处理如下的情况：<https://raw.githubusercontent.com/chaoxu/blog/master/posts/2011-12-21-fill-a-checkerboard.md>

```markdown
This was a homework problem for CSE 548. It's also a very common puzzle. 

{Problem}
    Given a $n\times n$ checkerboard, one can put a few checkers on it. A rule transform a checkerboard to the next. The rule states one can put a new checker if and only if at least two of it's adjacent positions (up, down, left, right) has a checker. Apply the rule until no more checker can be added. Show that if originally the checkerboard has only $n-1$ checkers, then when the process terminates, there exist cells not filled by a checker.

{Proof}
    Consider any $n-1$ pieces that are already placed on the board. Consider the following process:

    1. Pick any piece that was never considered, so we have a filled rectangle(square) of $1\times 1$. 
    2. Find another piece that can form a larger filled rectangle from the previous rectangle.(so Manhattan distance of at most $2$ from the rectangle). This means one only regard the checkers in the rectangle and the new piece, and do the transformation until nothing more can be done. It must be form a new rectangle. If the previous rectangle is a $a\times b$ rectangle, the new rectangle is among one of the following sizes: $a\times b$(the new piece is inside the rectangle), $a\times (b+1), a\times (b+2), (a+1)\times (b+1)$ or $(a+2)\times b$. Note if the new rectangle is a $c\times d$ rectangle, $c+d\leq a+b+2$. Let the new rectangle be the one we are considering.
    3. If there is no other piece fit the description in step 2. Go to step 1.

    The process will in the end form $k$ rectangles, such that the sum of the perimeter is at most $4(n-1)$, because each time step $2$ is run, we increase the perimeter of one of the rectangle by at most 4, each time step $1$ is run, we create a rectangle of perimeter 4. We can run those step at most $n-1$ times because there are only $n-1$ checkers. 

    If any two of the rectangles can form a larger one, then the perimeter of the new rectangle is at most the sum of the two smaller one. To show this, one can consider two cases: If they overlap, then it's clearly true. If they do not overlap, there are only 2 distinct positions. Either their diagonal touch, or their diagonals doesn't touch. Try both and you will see this is true. (It's hard to draw things and post on a blog).

    This shows the largest filled rectangle can be produced from $n-1$ checkers have perimeter $4(n-1)$, but to fill the $n\times n$ board, one need $4n$ as a perimeter. Therefore no configuration of $n-1$ checkers can result a filled board.
```

在该处理器当中，处理的是由大括号开头和结尾的一行，行里面是定理之类的环境，里面仍然是markdown的代码。`MathDoc.hs`的结构是这样的：

```{.haskell title="MathDoc.hs"}
module MathDoc ( mathdoc, mathdocInline) where
import Text.Pandoc
import Text.Regex (mkRegex, matchRegex)
import Data.Maybe
import Text.Pandoc.Writers.HTML
--import Data.String.Utils
import Data.Set (insert)
import System.Environment (getArgs)
import Data.List (nub, intercalate, isPrefixOf)
import Text.CSL.Pandoc
import System.IO.Unsafe
import Data.Array((!))
import Data.Bits((.|.))
import Data.Either

import qualified Data.Map as M

setMeta key val (Pandoc (Meta ms) bs) = Pandoc (Meta $ M.insert key val ms) bs

-- On mac, please do `export LANG=C` before using this thing
mathdocRead = def{readerExtensions = insert Ext_tex_math_double_backslash $ 
                                     insert Ext_tex_math_single_backslash $ 
                                     insert Ext_raw_tex pandocExtensions}
mathdocWrite = def{writerHTMLMathMethod = MathJax "",
                   writerHtml5          = True,
                   writerHighlight      = True,
                   writerNumberSections = True}

readDoc :: String -> Pandoc
readDoc x = head $ rights [readMarkdown mathdocRead x]

writeDoc :: Pandoc -> String
writeDoc x = writeHtmlString mathdocWrite (unsafePerformIO $ processCites' complete)
  where complete = setMeta "csl" (MetaInlines [Str "bib_style.csl"])
                   $ setMeta "link-citations" (MetaBool True)
                   $ setMeta "reference-section-title" (MetaInlines [Str "References"])
                   $ setMeta "bibliography" (MetaInlines [Str "reference.bib"]) x

writeDocT :: Pandoc -> String
writeDocT = writeHtmlString mathdocWrite

mathdoc :: String->String
mathdoc = compute . formatTheorem

mathdocInline :: String->String
mathdocInline = removeP . writeDocT . readDoc
  where removeP x = drop 3 (take ((length x) - 4) x) 
  
incrementBlock = ["Theorem",
                  "Conjecture",
                  "Definition",
                  "Example",
                  "Lemma",
                  "Problem",
                  "Proposition",
                  "Corollary"]
otherBlock = ["Proof","Remark"]

buildOr [x] = x
buildOr (l:ls) = l ++ '|' : buildOr ls
regex = "^\\{("
                 ++ buildOr (incrementBlock ++ otherBlock)
                 ++ ")\\}(\\((.*)\\)|$)$" 
blocks = mkRegex regex 

matchBlock = matchRegex blocks

buildReplace (t,n,i) = [(concat ["[",t," ",show i,"]"], link2),
                        (concat ["[",t," ",n,"]"], link2)]
  where link2 = "[" ++ t ++ " " ++ show i ++ "]"
                ++ "(#" ++ t ++ "-" ++ show i++")"

formatTheorem s = replaceMany replaceTable (formatBlocks s)
  where replaceTable = nub $ concatMap buildReplace (blocksAssoc s)

replaceMany [] s = s
replaceMany ((x,y):xs) s = replaceMany xs (replace x y s)

-- Format a block
formatBlocks xs = unlines $ fst $ formatBlocks' (lines xs) 1
blocksAssoc xs = snd $ formatBlocks' (lines xs) 1

formatBlocks' :: [String]->Int->([String],[(String,String,Int)])
formatBlocks' [] _ = ([],[])
formatBlocks' (x:xs) n= ([result] ++ results, assoc++assocs)
  where (result,inc,assoc) = formatBlock x n
        (results, assocs)  = formatBlocks' xs (n+inc)

formatBlock :: String->Int->(String,Int,[(String,String,Int)])
formatBlock x n
 | result    = ("######"++ name ++typeDes,inc, [(bType,name,n),(bType,show n,n)])
 | otherwise = (x,0,[])
 where  result = isJust $ matchBlock x
        [bType,_,name] = fromJust $ matchBlock x
        name' = if null name then "" else "\"" ++  name ++ "\""
        index = if bType `elem` otherBlock then "" else show n
        inc = if bType `elem` otherBlock then 0 else 1
        typeDes = " {type="++ bType ++" index="++ index ++" name=" ++ name' ++ "}"

compute x = (writeDoc $ bottomUp latex $ bottomUp theoremize $ readDoc x) ++ "\n"

latex :: Block -> Block
latex (RawBlock (Format "latex") s) = RawBlock (Format "html") ("<span class=\"math\">" ++s ++ "</span>")
latex x = x

theoremize :: [Block] -> [Block]
theoremize xs = t xs
  where t (x:y:xs)
         | isTheorem x = makeTheorem x y ++ (t xs)
         | otherwise   = x:(t (y:xs))
        t x = x
        
makeTheorem (Header _ (_,_,parm) _) (CodeBlock o xs) = [rawStart,rawHead] ++ content ++ [rawEnd]
  where t = fromJust $ lookup "type" parm
        name = fromJust $ lookup "name" parm
        index = fromJust $ lookup "index" parm
        sectionhead = concat ["<section class=\"theorem-environment ",
                    t,
                    "\" id=\"",
                    t,
                    "-",
                    index,
                    "\">"]
        inittext = "<span class=\"theorem-header\">" ++ typetext ++ indextext ++ nametext ++ "</span>"
        typetext = "<span class=\"type\">" ++ t ++ "</span>" 
        indextext = if null index 
                     then "" 
                     else "<span class=\"index\">" ++ index ++ "</span>"
        nametext = if null name 
                     then "" 
                     else "<span class=\"name\">" ++ (stripParagraph $ mathdocInline name) ++ "</span>"
        end = "</section>"
        rawEnd = RawBlock (Format "html") end
        rawStart = RawBlock (Format "html") sectionhead
        rawHead = RawBlock (Format "html") inittext
        content = (getDoc . readDoc) xs
makeTheorem x y = [x,y]

-- strip <p> and </p> of the beginning to the end of the html.
stripParagraph html = if take 3 html == "<p>" 
                        then take (length html - 8) (drop 3 html)
                        else html

getDoc (Pandoc _ xs) = xs

isTheorem :: Block -> Bool
isTheorem (Header 6 (_, [], param) _) =
    if isJust t
      then (fromJust t) `elem` (incrementBlock ++ otherBlock)
      else False
  where t = lookup "type" param
isTheorem x = False


-- copied missingh's replace implementation, because missingh runs into dependency hell...
-- remove this and uncomment import Data.String.Utils if you can solve this problem somehow
replace :: Eq a => [a] -> [a] -> [a] -> [a]
replace old new l = intercalate new . split old $ l

spanList :: ([a] -> Bool) -> [a] -> ([a], [a])
spanList _ [] = ([],[])
spanList func list@(x:xs) =
    if func list
       then (x:ys,zs)
       else ([],list)
    where (ys,zs) = spanList func xs

split :: Eq a => [a] -> [a] -> [[a]]
split _ [] = []
split delim str =
    let (firstline, remainder) = spanList (not . isPrefixOf delim) str
        in 
        firstline : case remainder of
                                   [] -> []
                                   x -> if x == delim
                                        then [[]]
                                        else split delim 
(drop (length delim) x)
```

在该文档当中，我们可以通过`setMeta`函数知道如何在原有的Pandoc文档当中添加元数据字段；通过mathdocRead函数知道怎样开启特定的Pandoc扩展选项，通过mathdocWrite知道Pandoc文档的输出样式。(`readDoc`和`writeDoc`则是真正的执行`String->Pandoc`或者`Pandoc->String`转换的函数。

而`formatTheorem`完成了将以`{Theorem}`为内容的行及其后具有缩进的行转换成相应的定理块的目的。还使用了`isTheorem`这样的函数来判定是否是定理块之类的环境。完成了这样的转换，自然可以输出定理环境了。

> 自己觉得任由Pandoc用户来定义各种各样的扩展其实是并不好的。我们可以定义一个标准的Pandoc内嵌语言机制。比如说，使用`{# instructions}`来表示Pandoc文档的扩展的东西，比如在其中引入`#include`这样的指令。并且由相应的程序来处理特定的指令与扩展。还有就是，表格、图片等的引用可以更好地处理，使用特殊的头即可。（为图片和表格添加特定的扩展属性，比如sideways等）。

> 注：自己觉得Pandoc的table处理得不好，不妨可以直接使用CSV格式作为表格来源。这样的话直接展示CSV就可以了。当然，Pandoc本身还是支持使用表格标题的，但是各种各样的引用好像就不支持了。各种各样的Attributes其实还是很烦人的。


## Pandoc的图片与表格的解析[12-28-2016 17:46:46 CST]

自己设想，表格体应该都可以转换成CSV的格式表达，不管表格体里面是否有跨行元素或者跨列的元素，应该都能够通过元素认识它们。也许表格可以按这样的方式表达：


```
A1: name
A2: title
A3: ...
B1-B3: Hello
```

通过这样的列表字段表达，或许更能够表达表格的含义。它表示在Grid布局当中各个元素应该代表什么。这样的话，我们也可以很快地找到内容。而且，这个时候，也允许表格当中的许多部分的元素保持空白，而且在描述的时候或许也能够保持一些语义信息。这种表示方法的关键是：将表格当中的内容当成实际的元素，然后通过A1这样的引用形式，来表示应该将相应的内容展现到哪里。自己觉得，这种方法可能比CSV更适合于表达试算表当中的信息。

而markdown当中的图片，自己觉得应该有一个preview的工具。为什么呢？有了一个文字形式表示的缩略图，或许可以更清楚地表达信息。至于OCR这样的技术，我们可以暂时不考虑，只考虑富媒体文件的表示问题。自己觉得有些内容可以以Base64编码的形式存储在markdown文件当中。而Base64编码当中，由于使用的字符有限，我们也可以压缩表示。

我们可以考虑一下在终端当中显示图像的一些程序，因为在终端当中也可以看电影和查看图片。再来看TermKit，所谓的新一代终端工具。<http://acko.net/>上面介绍了一个人发明的各种工具，比如使用图形关系来代替OpenGL的代码进行渲染。这样直观的图形可以变成代码，实在是很方便的一件事情。

img2txt也来自cacaview。纯文本地展示图形，称为所谓的ASCII art。有可能的话，在markdown里面添加一个缩略图或许也是不错的方案吧。

### Pandoc的Markdown的表格解析机制[12-28-2016 18:50:57 CST]

`Text.Pandoc.Writers.Markdown`负责写入markdown文件，将Pandoc变成Markdown的格式。导出有writeMarkdown与writePlain函数。其中的写入表格的函数是这样的：

```
pipeTable :: Bool -> [Alignment] -> [Doc] -> [[Doc]] -> State WriterState Doc
pandocTable :: WriterOptions -> Bool -> [Alignment] -> [Double] -> [Doc] -> [[Doc]] -> State WriterState Doc
gridTable :: WriterOptions -> Bool -> [Alignment] -> [Double] -> [Doc] -> [[Doc]] -> State WriterState Doc
```

负责写入的函数是

```haskell
blockToMarkdown opts t@(Table caption aligns widths headers rows) = do
```

其中的各行各列内容使用rows来表示。

所有的关键的问题就是如何表示各类模型，比如Table的模型。根本上来说，Table的元素内容应该视为一个二维表格（除了表格标题与引用标记之外）。每个表格里面是一些元素。里面的元素可以是非常任意的类型。要是自己的话，自己还是建议使用csv格式来表示表格。目前Pandoc的格式当中，正确转换表格的概率比较低。
