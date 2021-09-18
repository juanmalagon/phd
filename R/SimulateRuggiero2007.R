library("deaR")

data(package="deaR")

data("Ruggiero2007")
force(Ruggiero2007)
View(Ruggiero2007)

datadea <- read_data(Ruggiero2007
                     , ni=2
                     , no=1
                     , nd_inputs = 2)

result <- model_basic(datadea
                      , orientation="io"
                      , rts="crs")

efficiencies(result)
summary(result)
slacks(result)

help(package="deaR")
