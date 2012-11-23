# N is the set of nodes {a,b,c..}
# A is the set of arcs with costs {(a,b,1),(a,c,2)..}
#
# Use: Kruskal(N,A)

class Kruskal:
  def __init__ (self, N, A):
    self.A = sorted(A, key= lambda A: A[2])
    self.N = N
    self.n = len(N)
    self.C = [[u] for u in self.N]
    self.T = []

  def execute(self):
    for shortestA in self.A:
      u, v = shortestA[0], shortestA[1]
      ucomp, vcomp = self.find(u), self.find(v)
      if (ucomp != vcomp):
        print u, v, ":",self.C
        self.merge(ucomp, vcomp)
        self.T.append((u,v))
        if (len(self.T) == (self.n-1)): break

    print "\nMinimum spanning tree:\n", self.T
    return self.T
  
  def find (self, u):
    i = 0
    for c in self.C:
      if (u in c): return (c,i)
      i = i + 1

  def merge (self, ucomp, vcomp):
    self.C = [ucomp[0] + vcomp[0]] + [i for j, i in enumerate(self.C) if j not in [ucomp[1], vcomp[1]]]

# My experiment 

N = ["a1","a2","a3", "a4", "a5", "a6", "a7"]
A = [("a1","a2",1), ("a1","a4",4),
 ("a2","a4",6), ("a2","a5",4), ("a2","a3",2),
 ("a3","a5",5), ("a3","a6",6),
 ("a4","a5",3), ("a4","a7",4),
 ("a5","a6",8), ("a5","a7",7),
 ("a6","a7",3)]

myExperiment = Kruskal(N, A)
myExperiment.execute()