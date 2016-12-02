## Gnuplot的过滤器的编写[12-02-2016 22:57:22 CST]

其实Gnuplot也是一样的原理，也同样地是把代码编译成图片。这种类似于Jupyter的东西，似乎可以创建一个过滤器系统。

比如在yaml当中指定PATH作为输出路径，则接下来我们可以把markdown代码块当中的东西保存到一个文件当中(可以以SHA1存储)。然后调用特定的程序文件执行转换图片等等操作。转换完成之后，生成可预期的文件名。根据这个文件名，markdown再把它导入到相应的位置。

在转换的过程当中，title等属性应该都能够尽量地得到保留。因此需要一种解析参数的有效的机制，就像是tcolorbox那样，可以支持非常长的代码块操作。

这样的过滤器系统也可以更复杂化，比如支持多段的拼接等操作。但是归根结底来说，markdown还是可以作为一种源代码描述语言而存在的。(比如在论文中插入图形，保存的就只是论文所期望的绘图方法就可以了)。有时候，很多的细小的图形并不需要我们单独在另外一个文件当中保存，直接放在文档里面就可以了。比如一段短小的tikz的代码块。


### 过滤器的编写

```haskell
module MB.Gnuplot
    ( gnuplotProcessor
    )
where

import Control.Monad
    ( forM
    )
import Data.List
    ( intercalate
    )
import Data.Digest.Pure.SHA
    ( showDigest
    , sha1
    )
import Data.ByteString.Lazy.Char8
    ( pack
    )
import System.Directory
    ( doesFileExist
    )
import System.Process
    ( readProcessWithExitCode
    )
import System.Exit
    ( ExitCode(..)
    )
import qualified Text.Pandoc as Pandoc
import MB.Types
import qualified MB.Files as Files

gnuplotProcessor :: Processor
gnuplotProcessor =
    nullProcessor { preProcessPost = Just renderGnuPlot
                  }

renderGnuPlot :: Blog -> Post -> IO Post
renderGnuPlot config post = do
  let Pandoc.Pandoc m blocks = postAst post
  newBlocks <- forM blocks $ \blk ->
               case blk of
                 Pandoc.CodeBlock (preambleName, classes, _) s ->
                     renderGnuPlotScript config preambleName s classes
                 b -> return b

  return $ post { postAst = Pandoc.Pandoc m newBlocks }

loadPreamble :: Blog -> String -> IO (Maybe String)
loadPreamble config preambleName = do
  let filename = Files.eqPreambleFile config $ preambleName ++ ".txt"
  e <- doesFileExist filename
  case e of
    False -> return Nothing
    True -> do
           s <- readFile filename
           s `seq` return ()
           return $ Just s

renderGnuPlotScript :: Blog
                    -> String
                    -> String
                    -> [String]
                    -> IO Pandoc.Block
renderGnuPlotScript config preambleName rawScript classes = do
  putStrLn $ "Rendering equation graph, type=" ++ preambleName

  mPreamble <- loadPreamble config preambleName

  case mPreamble of
    Nothing -> do
      putStrLn $ "Error: no such gnuplot preamble: " ++ preambleName
      return $ Pandoc.Para [Pandoc.Str "[[COULD NOT DRAW EQUATION]]"]
    Just preamble -> do

      let scriptLines = lines rawScript
          preambleLines = lines preamble
          digestInput = preambleName ++ rawScript

      -- Generate an image name in the images/ directory of the blog
      -- data directory.  Use a hash of the preamble name and script
      -- contents so we can avoid rendering the image again if it
      -- already exists.
      let hash = showDigest $ sha1 $ pack digestInput
          imageFilename = preambleName ++ "-" ++ hash ++ ".png"
          imagePath = Files.imageFilename config imageFilename
          outputLines = [ "set term png enhanced"
                        , "set output \"" ++ imagePath ++ "\""
                        ]
          fullScript = intercalate "; " $ outputLines ++ preambleLines ++ scriptLines

      -- Invoke gnuplot to render the image
      (status, out, err) <- readProcessWithExitCode "gnuplot" ["-e", fullScript] ""

      case status of
        ExitSuccess -> return ()
        ExitFailure _ -> do
                       putStrLn "Could not render equation:"
                       putStrLn "Equation was:"
                       putStrLn rawScript
                       putStrLn "gnuplot output:"
                       putStrLn out
                       putStrLn err

      return $ Pandoc.Para [Pandoc.RawInline "html" $ concat [ "<img src=\"/generated-images/"
                     , imageFilename
                     , "\" class=\""
                     , intercalate " " classes
                     , "\">"
                     ]
                           ]
```
