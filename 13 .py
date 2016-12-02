Matrixs=[[0,1,0,0,0],[1,0,0,1,0],[0,0,0,1,1],[0,0,1,0,1],[0,0,1,1,0]]
add=0
#node for the edges to be added
CNode=3
          
#edges to be added 
Edges=[2,4]
Node=[1,3]

def Add_Node(Node,Matrixs):
  Matrixs.append([])
  for i in range (0,len(Matrixs)-1):
    Matrixs[len(Matrixs)-1].append(0)
  for i in range (0,len(Matrixs)):
    Matrixs[i].append(0)
    
  for i in range(0,len(Node)):
    Matrixs[len(Matrixs)-1][Node[i]]=1
    Matrixs[Node[i]][len(Matrixs)-1]=1

def Add_Edge(CNode,Edges):
  for i in range(0,len(Edges)):
          Matrixs[CNode-1][Edges[i]]=1
          Matrixs[Edges[i]][CNode-1]=1

def DFS(Matrixs,p):
  while len(Array)<len(Matrixs):
    for j in range (0,len(Matrixs)):
      if Matrixs[p][j]==1:
        if j<len(Matrixs):
          for d in range(0,len(Array)):
            if Array[d]==Matrixs[p][j]:
              break
            else:
              Array.append(j+1)
              p=j
  print(Array)
  
Array=[]
DFS(Matrixs,CNode)
#question 13 funcations 
if add==1:
  Add_Node(Node,Matrixs)
  Add_Edge(CNode,Edges)
for i in range (0,len(Matrixs)):
  print (Matrixs[i])
    

