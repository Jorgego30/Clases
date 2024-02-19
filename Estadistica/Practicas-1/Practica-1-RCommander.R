
setwd("/home/jorge/Clases/Estadistica/Practicas-1")
Practica_1a <- readXL("/home/jorge/Clases/Estadistica/Practicas-1/23_24GR_Tema3_problemas.xlsx", rownames=FALSE, header=TRUE, na="", sheet="1a", 
  stringsAsFactors=TRUE)
prin
local({
  .Table <- with(Practica_1a, table(obstáculo))
  cat("\ncounts:\n")
  print(.Table)
  cat("\npercentages:\n")
  print(round(100*.Table/sum(.Table), 2))
})

t<-table(Practica_1a$obstáculo)# hace el recuento de las frecuencias
t*100/sum(t) #se expresan las frecuencias en términos relativos
with(Practica_1a, Barplot(obstáculo, xlab="obstáculo", ylab="Frequency", label.bars=TRUE))
with(Practica_1a, Barplot(obstáculo, xlab="obstáculo", ylab="Frequency", label.bars=TRUE))
library(colorspace, pos=15)
with(Practica_1a, piechart(obstáculo, xlab="", ylab="", main="obstáculo", col=rainbow_hcl(4), scale="percent"))
with(Practica_1a, piechart(obstáculo, xlab="", ylab="", main="obstáculo", col=rainbow_hcl(4), scale="percent"))
with(Practica_1a, Barplot(obstáculo, xlab="obstáculo", ylab="Frequency", label.bars=TRUE))
with(Practica_1a, piechart(obstáculo, xlab="", ylab="", main="obstáculo", col=rainbow_hcl(4), scale="percent"))
plot(table)

Practica_1b <- readXL("/home/jorge/Clases/Estadistica/Practicas-1/23_24GR_Tema3_problemas.xlsx", rownames=FALSE, header=TRUE, na="", sheet="1b", stringsAsFactors=TRUE)
t<-table(Practica_1b$tiempo.ejec)# hace el recuento de las frecuencias
t
library(abind, pos=16)
library(e1071, pos=17)
numSummary(Practica_1b[,"tiempo.ejec", drop=FALSE], statistics=c("mean", "sd", "IQR", "quantiles"), quantiles=c(0,.25,.5,.75,1))
numSummary(Practica_1b[,"tiempo.ejec", drop=FALSE], statistics=c("mean", "sd", "IQR", "quantiles"), quantiles=c(0,.25,.5,.75,1))
binnedCounts(Practica_1b[,"tiempo.ejec", drop=FALSE])
numSummary(Practica_1b[,"tiempo.ejec", drop=FALSE], statistics=c("mean", "sd", "IQR", "quantiles"), quantiles=c(0,.25,.5,.75,1))
binnedCounts(Practica_1b[,"tiempo.ejec", drop=FALSE],breaks=seq(0,102,17))
with(Practica_1b, Hist(tiempo.ejec, scale="frequency", breaks="Sturges", col="darkgray"))
with(Practica_1b, Hist(tiempo.ejec, scale="frequency", breaks="Sturges", col="darkgray"))
h<-with(Practica_1b, Hist(tiempo.ejec, labels=T, scale="frequency", breaks=seq(0,102,17),col="darkgray"))
h
Practica_1.2 <- readXL("/home/jorge/Clases/Estadistica/Practicas-1/23_24GR_Tema3_problemas.xlsx", rownames=FALSE, header=TRUE, na="", sheet="2", stringsAsFactors=TRUE)

local({
  .Table <- with(Practica_1.2, table(clasificación))
  cat("\ncounts:\n")
  print(.Table)
  cat("\npercentages:\n")
  print(round(100*.Table/sum(.Table), 2))
})
local({
  .Table <- with(Practica_1.2, table(obstáculo))
  cat("\ncounts:\n")
  print(.Table)
  cat("\npercentages:\n")
  print(round(100*.Table/sum(.Table), 2))
})

local({
  .Table <- xtabs(~clasificación+obstáculo, data=Practica_1.2)
  cat("\nFrequency table:\n")
  print(.Table)
  .Test <- chisq.test(.Table, correct=FALSE)
  print(.Test)
})
local({
  .Table <- xtabs(~obstáculo+clasificación, data=Practica_1.2)
  cat("\nFrequency table:\n")
  print(.Table)
  .Test <- chisq.test(.Table, correct=FALSE)
  print(.Test)
})
local({
  .Table <- xtabs(~obstáculo+clasificación, data=Practica_1.2)
  cat("\nFrequency table:\n")
  print(.Table)
  cat("\nTotal percentages:\n")
  print(totPercents(.Table))
  .Test <- chisq.test(.Table, correct=FALSE)
  print(.Test)
})
local({
  .Table <- xtabs(~obstáculo+clasificación, data=Practica_1.2)
  cat("\nFrequency table:\n")
  print(.Table)
  cat("\nTotal percentages:\n")
  print(totPercents(.Table))
  .Test <- chisq.test(.Table, correct=FALSE)
  print(.Test)
})
with(Practica_1.2, Barplot(obstáculo, xlab="obstáculo", ylab="Frequency", label.bars=TRUE))
with(Practica_1.2, Barplot(obstáculo, by=clasificación, style="divided", legend.pos="above", xlab="obstáculo", ylab="Frequency", label.bars=TRUE))
with(Practica_1.2, Barplot(obstáculo, by=clasificación, style="divided", legend.pos="above", xlab="obstáculo", ylab="Percent", scale="percent", label.bars=TRUE))
with(Practica_1.2, Barplot(obstáculo, by=clasificación, style="divided", legend.pos="above", xlab="obstáculo", ylab="Percent", scale="percent", label.bars=TRUE))
mosaicplot(.Table, shade=T)
.Table <- xtabs(~obstáculo+clasificación, data=Practica_1.2)

