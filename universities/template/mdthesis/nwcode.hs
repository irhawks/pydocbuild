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
        _ -> return (CodeBlock (id, classes, namevals) contents)
extractNwcodeToLaTeX x = return x

main :: IO ()
main = toJSONFilter extractNwcodeToLaTeX


{-
exportNowebCodeChunks :: Maybe Format -> Pandoc -> Pandoc
exportNowebCodeChunks (Just "latex") = -}

