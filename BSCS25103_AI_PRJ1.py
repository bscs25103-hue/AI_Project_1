
import util
from util import Stack, Queue, PriorityQueue, CUTOFF
from heuristics import nullHeuristic

def depthFirstSearch(problem):
    visited = set()
    startState = problem.getStartState()
    DataStruct = util.Stack()
    
    startItem = (startState, [], 0)

    DataStruct.push(startItem)
        
    while not DataStruct.isEmpty():
        state, actions, cost = DataStruct.pop()
        
        if problem.isGoalState(state):
            return actions
            
        if state not in visited:
            visited.add(state)
            
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    newActions = actions + [action]
                    newCost = cost + stepCost
                    newItem = (successor, newActions, newCost)
                    
                    
                    DataStruct.push(newItem)
                        
    return None

def depthLimitedSearch(problem, limit):
    stack = util.Stack()
    startState = problem.getStartState()
    stack.push((startState, [], {startState}, 0))
    
    PathCut = False
    
    while not stack.isEmpty():
        state, actions, path_set, depth = stack.pop()
        
        if problem.isGoalState(state):
            return actions
            
        if depth < limit:
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in path_set:
                    new_path = path_set.union({successor})
                    stack.push((successor, actions + [action], new_path, depth + 1))
        else:
            PathCut = True

    if PathCut:
        return util.CUTOFF
    return None


def uniformCostSearch(problem):
    DataStruct = util.PriorityQueue()
    visited = set()
    
    Start = problem.getStartState()
    DataStruct.push((Start, [], 0), 0)
    
    while not DataStruct.isEmpty():
        state, actions, cost = DataStruct.pop()
        
        if problem.isGoalState(state):
            return actions
            
        if state not in visited:
            visited.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    newCost = cost + stepCost
                    DataStruct.push((successor, actions + [action], newCost), newCost)
                    
    return None


def aStarSearch(problem, heuristic=nullHeuristic):

    DataStruct = util.PriorityQueue()
    visited = set()
    
    Start = problem.getStartState()
    CostVal = 0
    HueVal = heuristic(Start, problem)
    DataStruct.push((Start, [], CostVal), CostVal + HueVal)
    
    while not DataStruct.isEmpty():
        state, actions, cost = DataStruct.pop()
        
        if problem.isGoalState(state):
            return actions
            
        if state not in visited:
            visited.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    newCost = cost + stepCost
                    priority = newCost + heuristic(successor, problem)
                    DataStruct.push((successor, actions + [action], newCost), priority)
                    
    return None