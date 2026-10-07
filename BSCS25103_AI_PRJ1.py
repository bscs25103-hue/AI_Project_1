
import util

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
        return CUTOFF
    return None

