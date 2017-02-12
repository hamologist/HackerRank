import Control.Monad
import System.IO

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print ((multiplesOfN 3 n) + (multiplesOfN 5 n) - (multiplesOfN 15 n))

multiplesOfN :: Int -> Int -> Int
multiplesOfN n end = n * (x * (x + 1) `div` 2) 
    where x = (end - 1) `div` n
