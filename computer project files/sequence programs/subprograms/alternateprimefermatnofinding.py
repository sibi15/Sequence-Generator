import sys
def prime_list(List):
    print(List)
    for n in range(0,len(List)):
        if List[n]>1:
            for j in range(2,List[n]):
                if List[n]%j==0:
                    print(List[n])
                    print("no prime fermat number in this range")
                    break
                    
            else:
                    print(List[n], "is the next number (prime) in the fermat numbers sequence")
                    print("found")
                    
                
                
                
                
    

L=[]
ctr=0
#while True:
 #   ctr+=1
##    if ctr>101:
##        print("why")
##        break
try:
    for i in range(0,100):
        f=2**(2**i)+1
        L.append(f)
        
except MemoryError:
          sys.exit()
    
        
prime_list(L)
        
    
    
    
