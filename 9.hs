main = print $ product . head $ [[a, b, c] | a <- [1..1000], b <- [1..1000], c <- [1000 - a - b], a^2 + b^2 == c^2]
