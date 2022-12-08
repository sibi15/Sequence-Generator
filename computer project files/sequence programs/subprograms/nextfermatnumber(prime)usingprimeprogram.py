# find 6th fermat number using prime program:
# create a infinitely adding list of Fermat Numbers and apply the prime program to find the next prime fermat number


L=[]
ctr=0
while True:
    ctr+=1
##    if ctr>101:
##        print("why")
##        break
    for i in range(ctr):
        f=(2**(2**i))+1
        L.append(f)
        #print(L)
print('POOP')

def prime_list(List):
    print(List)
    for n in range(0,len(List)):
        if List[n]>1:
            for j in range(2,n):
                if List[n]%j==0:
                    break
            else:
                print(List[n], "is the next number (prime) in the fermat numbers sequence")
                print("found")
                break
            break
        break
    


    
prime_list(L)
        
    
    
    
