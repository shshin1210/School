#2
library(ISwR)

red.cell.folate

#(a)
power.t.test(delta = 50, sd=40, sig.level = 0.05, power = 0.8)

#(b)
with(red.cell.folate, anova(lm(folate~ventilation)))
aov_red<-with(red.cell.folate, aov(folate~ventilation))

summary(aov_red)

#(c)

#ventilation종류별로 차이가 있다. p-value가 0.05보다 작기 때문이다.



#16

juul2

#(a)
juul2_age9to18 <- subset(juul2, juul2$age >=9 & juul2$age<18, na.rm =T)
juul2_age9to18

#(b)
#age height menarche sex igf1 tanner testvol weight
multi_juul2<-with(juul2_age9to18, lm(igf1~sex+age+height+tanner+weight))
summary(multi_juul2)
drop1(multi_juul2, test="Chisq")

multi_juul2<-with(juul2_age9to18, lm(igf1~sex+age+height+tanner))
summary(multi_juul2)
drop1(multi_juul2, test="Chisq")

multi_juul2<-with(juul2_age9to18, lm(igf1~ age+height+tanner))
summary(multi_juul2)
drop1(multi_juul2, test="Chisq")

#important : age, height, tanner

#(c)
pred.frame <-data.frame(age = 14, height = seq(110,160), tanner =3)
pp<-predict(multi_juul2, interval="pred", newdata=pred.frame)
pp



#17
secher

#(a)

secherlm<-with(secher, lm(log(bwt)~log(bpd)+log(ad)))
summary(secherlm)

#log(bwt) = -5.8615 + 1.5519*log(bpd) + 1.4667*log(ad)
#bwt = (exp)^{(-5.8615) + 1.5519*log(bpd) + 1.4667*log(ad)}

#(b)

cystfibr

lm.pemax.hq <- with(cystfibr, lm(pemax~height+I(height^2)))
summary(lm.pemax.hq)

#pemax = 615.36248 - 8.08324(height) + 0.03064(height^2)

#(c)

pred.frame <- data.frame(height =seq(110, 180, 3))
predict(lm.pemax.hq, interval="pred", newdata=pred.frame)



#18

graft.vs.host

#(a)

gvhglm1<-with(graft.vs.host, glm(gvhd~rcpage+type+preg+log(index)+donage), binomial)
summary(gvhglm1)
drop1(gvhglm1, test="Chisq")

#important : log(index), donage
gvhglm2<-with(graft.vs.host, glm(gvhd~log(index)+donage), binomial)
drop1(gvhglm2, test="Chisq")
summary(gvhglm2)

#(b)

#gvhd = -0.259950 + 0.287872*log(index) +0.021490*donage
pred.frame = data.frame(index = seq(1,3), donage = 20)
predict(gvhglm2, interval="pred", newdata=pred.frame)


#(c)
confgvh<-confint(gvhglm2, level = 0.95)
confgvh


#19

malaria

#(a)

malglm<- with(malaria, glm(mal~age+log(ab)), binomial)
summary(malglm)

# mal = 0.892733 -0.009984*age -0.112385*log(ab)

#(b)
pred.frame = data.frame(age =15 , ab = seq(300,500))
pp3 <-predict(malglm, interval="pred", newdata=pred.frame)
pp3

#(c)
library(ggplot2)
confmal<-confint(malglm, level = 0.95)
confmal
plot(confmal, type='p',main="신뢰구간",pch=1:3)
legend(0.2,1,c('Intercept','age','log(ab)'), pch=1:3)

