def productExceptSelf(prob):
        
    answer = []
    n = len(prob)
    for i in range(n-1):
        put = put * put[i]
        answer.append(put)
        print(put)

   

productExceptSelf([1,2,3,4])