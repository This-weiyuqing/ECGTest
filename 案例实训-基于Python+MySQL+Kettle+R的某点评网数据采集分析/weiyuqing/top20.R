data<-read.csv(file="C:/weiyuqing_changedata/dazhongdata.csv",sep=",",header=TRUE,encoding = "utf-8")
selectscore1<-subset(data,city=="济南",select=c(shopName,tasteScore,environmentScore,serviceScore))
meanscore1<-rowMeans(selectscore1[2:4])
cdata1<-cbind(selectscore1[1],meanscore1)
top20_jinan<-cdata1[order(cdata1[2],decreasing = TRUE)[1:20],]

print(top20_jinan)

par(mfrow=c(3,1))
plot(factor(top20_jinan[,1]),top20_jinan[,2],xlable="济南TOP20商铺",ylab="综合评分",main="山东3大城市TOP20商铺综合评分")


selectscore2<-subset(data,city=="青岛",select=c(shopName,tasteScore,environmentScore,serviceScore))
meanscore2<-rowMeans(selectscore2[2:4])
cdata2<-cbind(selectscore2[1],meanscore2)
top20_qingdao<-cdata2[order(cdata2[2],decreasing = TRUE)[1:20],]
print(top20_qingdao)
plot(factor(top20_qingdao[,1]),top20_qingdao[,2],xlab="青岛TOP20商铺",ylab="综合评分")

selectscore3<-subset(data,city=="威海",select=c(shopName,tasteScore,environmentScore,serviceScore))
meanscore3<-rowMeans(selectscore3[2:4])
cdata3<-cbind(selectscore3[1],meanscore3)
top20_weihai<-cdata3[order(cdata3[2],decreasing = TRUE)[1:20],]
print(top20_weihai)
plot(factor(top20_weihai[,1]),top20_weihai[,2],xlab="威海TOP20商铺",ylab="综合评分")