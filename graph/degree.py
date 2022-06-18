def degree(matrix):
    x = input("\nIs this matrix a directed matrix?\(yes/no)")
    
    degrees=[]
    outdegrees=[]
    indegrees=[]
    #degree
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
        print(f"Degrees: {degrees}")
        
        
        
    #outdegree
    if x == "yes":
        for value in matrix:
            degree = 0
            for i in value:
                degree = degree+i
            outdegrees.append(degree)
        print(f"Outdegrees: {outdegrees}")
            
    # indegree
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
        





