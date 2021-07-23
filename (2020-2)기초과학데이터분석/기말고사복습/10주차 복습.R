#실습과제 week10-1

#10-1 1번
prop.test(0,10,0.2)

binom.test(0,10,0.2)


for (i in  11:25){
  k <- prop.test(0,i,0.2)
  print(k$p.value)
}

for (i in  11:25){
  k <- binom.test(0,i,0.2)
  print(k$p.value)
}

prop.test(0,21,0.2)
binom.test(0,17,0.2)

#둘다 95%, 99%신뢰구간에서 귀무가설 기각할 수 없음/ 차이가 없다
#차이가 있기 위해서는 prop.test 21명 / binom.test 17명

#실습과제 10-2

rockdied <-c(210,122)
rocktotal <-c(747,661)
rocksurv <- c(537,539)

rock<-matrix(c(210,122,537,539),2)
rock
prop.test(rockdied,rocktotal)
#차이는 유의미하다 (대립가설 채택)


healsuccess <- c(23,18)
healtotal<- c(30,31)
heal <- matrix(c(23,7,18,13),2)
heal

prop.test(healsuccess,healtotal)
#귀무가설 기각x

fisher.test(heal)
#귀무가설 기각 x

power.t.test(delta = 0.15, sd=0.2, power = 0.8, type = "paired")
#같은 사람에 대해서 두개의 treat을 했기 때문에 type="paired"이다
#각 그룹에 16개가 필요하다 / n = 15.98026 / 16명하면 기각 능력 생김
