
from pysat.solvers import Solver

class c_sat:

  def solve(self, graph):
    solver = Solver()
    
    # Calcullate the number of nodes
    n = len(graph)
    
    # Each node has a color and there are 3 colors
    vars = {}
    color = 3
    
    # Ensure the vertex-color pair is distinct
    for i in range(n):
      for j in range(color):
        vars[(i, j)] = i * n + j + 1
    
    # Add a clause to the SAT solver for each vertex i
    for i in range(n):
      # vertex i must be colored with available color
      solver.add_clause([vars[(i, j)] for j in range(color)])
      
    # Ensure no two adjacent vertices can share the same color
    for i in range(n):
      for j in range(i + 1, n):
        if graph[i][j] == 1:
          for k in range(color):
            solver.add_clause([-vars[(i, k)], -vars[(j, k)]])
    
    return solver.solve()
  