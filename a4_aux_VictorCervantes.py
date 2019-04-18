# Victor Cervantes
# cs-335, Spring 2019
# Asst 4

import math
import random


def hillClimbClique(n, k, graph):  # returns best state found

   state = getRandomState(n, k)
   h = getHeuristic(n, k, state, graph)
   nextState = getBestNeighbor(n, k, state, graph) 
   hNext = getHeuristic(n, k, nextState, graph)
   
   while hNext > h:
      state = nextState
      h = hNext
      nextState = getBestNeighbor(n, k, state, graph) 
      hNext = getHeuristic(n, k, nextState, graph)
        
   return state


###########################################
def getRandomState(n, k):  # returns random list of k verties (between 0 and n - 1)
   state = []
   index = 0                     #start from index 0
   while index < k:  
      v = random.randint(0, n-1) #randint is inclusive therefore we want someting up to n-1
      if v not in state:         #check to make sure the number is not already in the state
         state.append(v)         #append number
         index += 1              #increment index
   return state



###########################################
def getHeuristic(n, k, state, graph):   # returns the number of conflicts in "state" given the graph
   heuristic = 0              #start heuristic at 0
   for i in range(0, k - 1):  
      for j in range (i + 1, k): #start j at i+1 to avoid same index
         if graph[state[i]][state[j]] == 1:  #if the graph has a 1 there is a clique
            heuristic += 1          #increment heuristic value when clique is found
   return heuristic




###########################################
def getBestNeighbor(n, k, state, graph):  # returns the neighbor of "state" with the fewest conflicts.      
   #print("Getting best heuristic for: ", state)          #for testing purposes
   bestNeighbor = []
   bestHeuristic = 0
   neighbors= []        #list of states
   for j in range(n):
      if (j not in state):    #go thourgh every number and find those not in state
         for i in range(k):
            copy = list(state)  
            copy[i] = j        #replace each index with number
            #print("appending to neighbors: ", copy)        #for testing purposes
            neighbors.append(copy)  #append neighbor state to neigbors[]
   #print(str(neighbors)) #testing purposes
   for i in neighbors:        #traverse through each neighboring state
      heuristic = getHeuristic(n, k, i, graph)     #get heuristic of state
      if bestHeuristic < heuristic:
         #print("heuristic of ", i, "is: ", heuristic) #for testing puroposes
         bestHeuristic = heuristic        
         bestNeighbor = i                 #if heuristic is greater update bestHeuristic and update bestNeighbor
   return bestNeighbor