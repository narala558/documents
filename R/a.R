l <- list(time = 1:40)

d <- read.csv("http://www.ats.ucla.edu/stat/data/hsb2.csv")
x <- d$race

head(d)
typeof(d)
names(d)
class(d)

head(x)
class(x)
typeof(x)
names(x)


## for (name in names(d)) {
##     print(name)
##     print(head(d[[name]]))
## }
