#!/usr/bin/env runhaskell
-- includes.hs
import Text.Pandoc.JSON
import Text.Pandoc.Generic
import Text.Pandoc.Walk
import Data.Maybe

extractNwcodeToLaTeX :: Maybe Format -> Block -> Block
extractNwcodeToLaTeX (Just (Format "latex")) (CodeBlock (id, classes, namevals) contents)
    | "nwcode" `elem` classes = RawBlock (Format "latex") 
            (unlines ["\\begin{latexcode}%",
                "[title={" ++ (fromMaybe "*" (lookup "title" namevals)) ++ "}]",
                contents, 
                "\\end{latexcode}"])
extractNwcodeToLaTeX _ (CodeBlock (id, classes, namevals) contents)  = 
    CodeBlock (id, filter (\ x -> not (x == "nwcode")) classes, namevals) contents
extractNwcodeToLaTeX _ x = x

main :: IO ()
main = toJSONFilter extractNwcodeToLaTeX


{-
exportNowebCodeChunks :: Maybe Format -> Pandoc -> Pandoc
exportNowebCodeChunks (Just "latex") = -}

