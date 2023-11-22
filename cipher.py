alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sentence = input("What is your sentence? ")
capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#encryptcnt = int(input("What is your shift number? "))

newsent = ''

for letr in sentence:
    if letr in capital:
        first = capital.index(letr)
#       second = (first + encryptcnt) % 26
        second = (first + 5) % 26
        cba = capital[second]
        newsent+=cba 
    elif letr in alpha:
        third = alpha.index(letr) 
#       fourth = (third + encryptcnt) % 26
        fourth = (third + 5) % 26
        abc = alpha[fourth]
        newsent+=abc
    else:
        newsent+=letr
print(newsent)
    