import Control.Monad
import System.IO

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print( sum([ x | x <- fibs n, even x ]) )

fibs :: Int -> [Int]
fibs n = takeWhile (\x -> x < n) genFibs
    where genFibs = 1 : 1 : [ a + b | (a, b) <- zip genFibs (tail genFibs) ]
