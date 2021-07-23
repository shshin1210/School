library(ISwR)

#14-1
malaria

mallm<- with(malaria, glm(mal~age+log(ab)), binomial)
summary(mallm)

#14-2
graft.vs.host

gvhlm<-with(graft.vs.host, glm(gvhd~type+preg+log(index)+donage), binomial)
summary(gvhlm)

drop1(gvhlm, test="Chisq")
anova(gvhlm, test ="Chisq")

#14-3
Counts <- c(13, 40, 157, 40, 21, 61)
Total <- c(108, 264, 375, 310, 181, 162)
Age <- gl(3, 1, 6)
Type <- gl(2,3,6)

anova(glm(Counts/Total~Age+Type, weights=Total, binomial), test="Chisq")

#14-4

confint(mallm)
confint(gvhlm)

#14-5

floridashark <- read.csv(file = "C:\\Users\\queenSSH\\Documents\\R\\floridashark.csv")

floridashark

sharkglm<-with(floridashark, glm(Attacks~Year+offset(log(Population)), poisson))
summary(sharkglm)


floridashark <- transform(floridashark, Year1=Year-1945)                    #poisson°ú °°À½
sharkfitpoi <- with(floridashark, glm(Attacks~offset(log(Population))+Year1,family="poisson"))
summary(sharkfitpoi)

plot(sharkglm)

#14-6

bcmort

bcglm1<-with(bcmort, glm(bc.deaths~age+cohort, poisson))
summary(bcglm1)

bcglm2 <-with(bcmort, glm(bc.deaths~(age+cohort)^2, poisson))
summary(bcglm2)

drop1(bcglm1, test = "Chisq")
confint(bcglm1)
