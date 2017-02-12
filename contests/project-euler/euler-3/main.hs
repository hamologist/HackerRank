import Control.Monad
import System.IO
import Data.Set

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print (largestPrimeFactor n)

largestPrimeFactor' :: Int -> Int
largestPrimeFactor' x = findLargestPrimeFactor x (reverse (primesTo x))
    where 
        findLargestPrimeFactor _ [] = 0
        findLargestPrimeFactor n (y:ys)
            | m == 0    = y
            | otherwise = findLargestPrimeFactor n ys
            where
                m = n `mod` y

primesTo :: Int -> [Int]
primesTo n = f [2..n]
    where 
        f []     = []
        f (x:xs) = x : f ( toList ((fromList xs) `difference` fromList([x*x, x*x+x..n])) )

largestPrimeFactor 2 = 2
largestPrimeFactor 3 = 3
largestPrimeFactor x
    | x `mod` 2 == 0 = largestPrimeFactor (x `div` 2)
    | otherwise      = f 3 x
    where 
        f i n
            | n `mod` i == 0 = f 3 (n `div` i)
            | i < sqN        = f (i+2) n
            | n > 2          = n
            | otherwise      = i
            where
                sqN = truncate (sqrt (fromIntegral n))
