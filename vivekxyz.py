from  collections import defaultdict
#creating a graph class
class graph:
    def _init_(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distances={}
    def addnode(self,value):
        self.nodes.add(value)

    def addedge(self,fromnode,tonode,distance):
        self.edges[fromnode].append(tonode)
        self.distances[(fromnode,tonode)]=distance


# Here the shortest path function as follows: 
def dijkstra(graph,initial):
    visited={initial:0}
    path=defaultdict(list)

    nodes=set(graph.nodes)
    while nodes:
        minnode=None
        for node in nodes:
            if node in visited:
                if minnode is None:
                    minnode=node
                elif visited[node]<visited[minnode]:
                    minnode=node
        if minnode is None:
            break
        nodes.remove(minnode)
        currentweight=visited[minnode]

        for edge in graph.edges[minnode]:
            weight=currentweight+graph.distances[(minnode,edge)]
            if edge not in visited or weight<visited[edge]:
                visited[edge]=weight
                path[edge].append(minnode)
    return visited,path

a=graph()
a.addnode("A")
a.addnode("B")
a.addnode("C")
a.addnode("D")
a.addnode("E")
a.addedge("A","B",2)
a.addedge("A","D",3)
a.addedge("A","C",6)
a.addedge("B","E",5)
a.addedge("E","C",1)
a.addedge("D","E",6)
