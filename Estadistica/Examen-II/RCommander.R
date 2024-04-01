
setwd("/home/jorge/Clases")
Dataset <- readXL("/home/jorge/Descargas/23-24GR evaluaciÃ³n continua T3_ICpH.xlsx", rownames=FALSE, header=TRUE, na="", sheet="Datos1", stringsAsFactors=TRUE)
with(Dataset, (t.test(adhesion, cristal, alternative='two.sided', conf.level=.90, paired=TRUE)))
qt(c(0.001169), df=0.9, lower.tail=FALSE)

