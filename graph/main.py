import isBipartite as bp
import degree as dg
import isEulerian as er
import dijkstra as dk



n = int(input("Please enter matrix's row and coulm(n*n): "))
matrix = []


def takeMatrix():
    for i in range(n):
        single_row = list(map(int, input().split()))
        matrix.append(single_row)
    print(matrix)


takeMatrix()
#dg.degree(matrix)
#bp.checkBipartite(matrix)
#er.isEuler(matrix)
dk.checkDijkstra(matrix)
