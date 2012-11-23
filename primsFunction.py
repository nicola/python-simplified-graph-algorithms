def Prim (Adj):
  T = []
  n = len(Adj)
  Nearest = []
  MinDist = []

  for i in range(0,n):
    Nearest.append(0)
    MinDist.append(0)

  for i in range(1, n):
    Nearest[i] = 0
    MinDist[i] = Adj[i][0]

  for i in range(0, n-1):
    min = None
    for j in range(1, n):
      if ((min and MinDist[j] and 0 <= MinDist[j] < min) or (not min and  0 <= MinDist[j])):
        min = MinDist[j]
        k = j

    T.append((k, Nearest[k]))
    print T

    MinDist[k] = -1
    MinDist[Nearest[k]] = -1

    for j in range(1, n):
      if ((MinDist[j] and Adj[k][j] and Adj[k][j] < MinDist[j]) or not MinDist[j] ):
        MinDist[j] = Adj[k][j]
        MinDist[k] = Adj[j][k]

        Nearest[j] = k
        Nearest[k] = j

  return T

# My experiment

# My experiment

Adj = [[None, 1, None, 4, None, None, None],
[1, None, 2, 6, 4, None, None],
[None, 2, None, None, 5, 6, None],
[4, 6, None, None, 3, None, 4],
[None, 4, 5, 3, None, 8, 7],
[None, None, 6, None, 8, None, 3],
[None, None, None, 4, 7, 3, None]]

Prim(Adj)