#실습과제 12-1
library(survival)

kidney

kidsurv<-with(kidney, Surv(time, status))
plot(kidsurv, xlab = "time", ylab="status")

kidsurvfit <- with(kidney, survfit(Surv(time, status)~sex))
kidsurvfit
plot(kidsurvfit)

nafld1

nafsurv <- with(nafld1, Surv(futime, status))
plot(nafsurv, xlab="futime", ylab= 'status')

nafsurvfit <- with(nafld1, survfit(Surv(futime, status)~male))
plot(nafsurvfit, col = c('red','blue'))

#실습과제 12-2
kidney
kidcox<-with(kidney, coxph(Surv(time,status)~sex+frail))
#sex, frail

survfit(kidcox, newdata = data.frame(sex=1, frail=1))
#평균 30명이면 살 수 있다


nafld1

with(nafld1, coxph(Surv(futime, status)~age+male+weight+height+bmi))
#age, male

nafcox<-with(nafld1, coxph(Surv(futime, status==0)~age+male))

survfit(nafcox, newdata = data.frame(age=40, male=0))

#실습과제 12-3

library(ISwR)
graft.vs.host

with(graft.vs.host, coxph(Surv(time, dead)~gvhd))
#5%유의구간에서는 gvhd값의 두 그룹별로 생존시간에 차이가 있다

#log-rank 테스트
survdiff(Surv(time, dead)~gvhd, graft.vs.host)
#5%신뢰수준에서 p-value 기각 된다/ 관계가 있음


veteran

vetcox<-with(veteran, coxph(Surv(time, status)~trt))
plot(vetcox)
vetcox

vetsurvfit <-survfit(Surv(time, status)~trt, data=veteran)
plot(veteransurvit, col =c('red','green'))

