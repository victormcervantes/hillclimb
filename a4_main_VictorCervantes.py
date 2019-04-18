# Victor Cervantes
# cs-335, Spring 2019
# Asst 4

from a4_aux_VictorCervantes import *
#from graph_12_5 import *
from graph_200_14 import *

print()
print("Victor Cervantes")
print("cs-335, Spring 2019, Asst 4")
print()

graph = getGraph()  
n = getN()
k = getK()


for i in range(1):
   soln = hillClimbClique(n, k, graph)
   h = getHeuristic(n, k, soln, graph)
   print()
   print("Heuristic: " + str(h))
   print(soln)
   print() 
