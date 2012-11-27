digs :: Integral x => x -> [x]
digs 0 = []
digs x = digs (div x 10) ++ [mod x 10]

main = print $ maximum [x*y | x <- [1..999], y <- [1..999], (digs $ x*y) == (reverse $ digs $ x*y)]
