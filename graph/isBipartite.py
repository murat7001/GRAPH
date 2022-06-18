
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]

    def isBipartite(self, src):
        colorArr = [-1] * self.V
        queue = []
        colorArr[src] = 1
        queue.append(src)

        while queue:
            u = queue.pop()
            # Check for cycles in the Graph
            if self.graph[u][u] == 1:
                return False
            for v in range(self.V):
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        return True


def checkBipartite(matrix):

        # Quadrilateral
        g = Graph(len(matrix))
        g.graph =matrix
    
        if g.isBipartite(0):
            print ("\nThis matrix is Bipartite graph" )
        else:
            print ("\nThis matrix is NOT a Bipartite graph")



