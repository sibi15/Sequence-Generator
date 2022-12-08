# check prime

n=int(input("Enter number to check if prime or not"))
if n>1:                         # prime numbers are greater than 1
    for i in range(2,n):
        if n%i==0:              # has factors
            print(n, "is not a prime number")
            print(i, "multiplied by", (n//i), "is equal to", n)
            break
    else:                               # condition when remainder is non-zero
        print(n, "is a prime number")
