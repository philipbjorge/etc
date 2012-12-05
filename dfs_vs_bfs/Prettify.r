library(graphics)
rm(list=ls(all=TRUE))
png("plots.png", 6000, 6000)

files <- list.files(pattern=".data$", full.names=TRUE)
rows <- length(files) / 6
par(mfrow=c(rows,6))

for(i in 1:length(files)) {
  meta <- as.list(readLines(files[[i]], n=3))
  names(meta) <- c("title", "algorithm", "nodes")
  data <- scan(files[[i]], what=integer(0), skip=3, quiet=TRUE)
  
  d <- density(data)
  plot(d, main=paste0(meta$title, "[NOTE: Axis not scaled. This is for seeing distribution.]"), sub=paste0(meta$algorithm, " on ", meta$nodes, " nodes"), xlab="Edges before discovery")
  polygon(d, col="red", border="blue")
}
dev.off()
