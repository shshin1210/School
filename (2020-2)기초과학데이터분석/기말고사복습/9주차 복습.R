#실습과제 week 9-1
#grpf 별로 trypsin이 같은지 anova로 알아보기

fake.trypsin

trypsinanova2<-with(fake.trypsin, anova(lm(trypsin~grpf)))
trypsinanova2
#tyrpsin의 p-value가 매우 작다 / 그룹별로 trypsin이 같지 않다

trypsinanova<-with(fake.trypsin, aov(trypsin~grpf))
summary(trypsinanova)
#p-value가 매우 낮음/ 귀무가설 기각 가능
#적어도 평균이 다른 그룹 하나가 존재한다

#실습과제 week 9-2_1

library(ISwR)
secretin
with(secretin, anova(lm(gluc~person)))

#집단간 t-test를 수행
with(secretin, pairwise.t.test(gluc,person))

#anova에 대비되는 비모수 방법 : kruskal / 평균이 다른 그룹이 적어도 하나 존재
with(secretin, kruskal.test(gluc~person))

#실습과제 week 9-2_2

with(secretin, anova(lm(gluc~person+time)))

secretin

levels(secretin$time) <-c('pre',20,30,60,90)
#time이 x / person별로 구분 / y축은 gluc
with(secretin, interaction.plot(time, person, gluc))

