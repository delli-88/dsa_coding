class Graph():
    def __init__(self) -> None:
        self.adjacency_list = {}
        
    def __repr__(self) -> str:
        return str(self.__dict__)

    def insert(self,vertex1,vertex2):
        if self.adjacency_list.get(vertex1)==None:
            self.adjacency_list[vertex1] = [vertex2]
        else:
            self.adjacency_list[vertex1].append(vertex2)

        # comment below for Directed Graph
        if self.adjacency_list.get(vertex2)==None:
            self.adjacency_list[vertex2] = [vertex1]
        else:
            self.adjacency_list[vertex2].append(vertex1)
        

    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')
        return


myGraph = Graph()
n,m = [int(_) for _ in input().split()]
for _ in range(m):
    v1,v2 = [int(_) for _ in input().split()]
    myGraph.insert(v1,v2)
print(myGraph)

