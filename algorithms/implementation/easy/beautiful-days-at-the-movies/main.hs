{-# LANGUAGE BangPatterns #-}

import Control.Monad
import System.IO
import Data.List (foldl')

main :: IO ()
main = do
    userInputTemp <- getLine
    let userInput = map read (words userInputTemp)
    print (beautifulDays (userInput !! 0) (userInput !! 1) (userInput !! 2))

beautifulDays :: Int -> Int -> Int -> Int
beautifulDays i j k = foldl' (\acc x -> if x then acc + 1 else acc + 0) 0 [isBeautiful x k | x <- [i..j]]

isBeautiful :: Int -> Int -> Bool
isBeautiful n k = (abs (n - (reverseInt n)) `mod` k) == 0

reverseInt :: Int -> Int
reverseInt n = rev n 0
    where
        rev 0 !y = y
        rev x !y = let (x', y') = x `quotRem` 10
                  in rev x' (10 * y + y')

reverseInt2 :: Int -> Int
reverseInt2 n = read (reverse (show  n)) :: Int
