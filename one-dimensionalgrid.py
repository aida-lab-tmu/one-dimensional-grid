import numpy as np
import networkx as nx
N = 100# the number of points
#一次元ネットワーク
    #################################################
indexlist=np.zeros(N)
d=np.zeros((N,N))
X = np.zeros(N)
A=np.zeros((N, N))
for i in range(N):
  indexlist[i]=i
  for i in range(N):#一次元ネットワークの座標設定
        X[i]=i
for i in range(N):
        for j in range(N):
            if (abs(X[i]-X[j])<=1 or abs(X[i]-X[j])>=N-1)and i!=j:#周期境界条件
                A[i,j]=1
edges = []
for i in range(N):
    for j in range(N):
        if A[i, j] != 0:
            edges.append((i, j)) #どのノードとどのノードがつながっているかのリスト作成

G = nx.Graph()
for i in range(N):
    G.add_node(i, pos=X[i]) # setting (x, y)-coordinates of nodes
G.add_edges_from(edges)
nx.draw(G, node_size=20)

for i in range(N):
    for j in range(N):
        d[i,i]+=A[i,j]
L=d-A
print(L)
