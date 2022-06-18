import degree as dg


def isEuler(matrix):
    x = input("Is this matrix a directed matrix?\(yes/no)")
    
    degrees=[]
    outdegrees=[]
    indegrees=[]
    #undirected circuit
    if x == "no":
        k = 0
        for value in matrix:
            degree = 0
            for i in value:
                degree = degree+i
            if matrix[k][k] != 0:
                degree = degree+matrix[k][k]
            k += 1
            degrees.append(degree)
        
        flag=0
        for value in degrees:
            if (value%2!=0):
                flag=1
                print("There is not an euler circuit.")
                break
        if(flag==0):
            print("There is an euler circuit")
        
    #directed circuit
    if x == "yes":
        for value in matrix:
            degree = 0
            for i in value:
                degree = degree+i
            outdegrees.append(degree)
        print(f"Outdegrees: {outdegrees}")
        
        k = 0
        for i in range(0, len(matrix)):  
            degree = 0
            y = 0
            for value in matrix:
                degree = degree+matrix[y][k]
                y = y+1
            k = k+1
            indegrees.append(degree)
        print(f"Indegrees: {indegrees}")
            
        sum=0
        sum1=0
        for value in outdegrees:
            sum += value
        for value in indegrees:
            sum1 += value
        
        if(sum==sum1):
            print("There is an euler circuit")
        else:
            print("There is not an euler circuit")
