#데이터 찾기
library(survival)
data("colon")
colon

colon2 <-na.omit(colon)
colon2
str(colon)
summary(colon)

#로지스틱 회귀분석 시행 하기
colonglm <- with(colon2, glm(status~rx+sex+age+obstruct+perfor+adhere+
                      nodes+differ+extent+surg, family = binomial))
summary(colonglm)

#drop1함수로 유의미한 변수 찾기
drop1(colonglm, test = "Chisq")

library(ggplot2)
library(plotly)

#나이에 따른 status차이 (차이 없음)
boxplot(age~status,colon , xlab = "Status", ylab = "Age", cex=1.2)
plot(age~jitter(status), colon,cex=1.2, xlab='Status')

#그래프로 변수 확인

ggplot_data<- ggplot(colon, aes(x=status, fill = factor(rx))) +
  geom_bar() +  ggtitle("rx에 따른 생존 여부") 
ggplotly(ggplot_data, height = 600, width=750)

ggplot_data<- ggplot(colon, aes(x=status, fill = factor(nodes))) +
  geom_bar() +  ggtitle("nodes에 따른 생존 여부") 
ggplotly(ggplot_data, height = 600, width=750)

ggplot_data<- ggplot(colon, aes(x=status, fill = factor(extent))) +
  geom_bar() +  ggtitle("extent에 따른 생존 여부") 
ggplotly(ggplot_data, height = 600, width=750)
