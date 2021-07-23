#13-1
beaver1

Beaver1 <- beaver1

Beaver1 <- with(beaver1, transform(Beaver1, date = as.Date(day,origin = '1989-12-31' )))
Beaver1


#13-2

library(ISwR)

secher
secherlm <- with(secher, lm(log(bwt)~ log(bpd)+log(ad)))
summary(secherlm)

#log(bwt) = -5.8615 + 1.5519*log(bpd) + 1.4667*log(ad)

juul2

juul2_age25 <- subset(juul2, juul2$age>=25, na.rm=T)
juul2_age25

juul2_age25_lm1<- with(juul2_age25, lm(sqrt(igf1)~age+height+weight))
summary(juul2_age25_lm1)
juul2_age25_lm2<- with(juul2_age25, lm(igf1~age+height+weight))
summary(juul2_age25_lm2)

anova(juul2_age25_lm1)


#13-3

a <- gl(2, 2, 8) ; b<- gl(2, 4,8); x <- 1:8; y <- c(1:4, 8:5); z<-rnorm(8)


summary(lm(z~a+b))
anova(lm(z~a+b))
summary(lm(z~a*b))
anova(lm(z~a*b))
summary(lm(z~x*y))
anova(lm(z~x*y))





