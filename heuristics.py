"""
heuristics.py
-------------
Heuristics for the basic maze problem (Question 6).

A heuristic is a function heuristic(state, problem) that returns an estimate
of the cost of the cheapest path from 'state' to a goal. For a MazeProblem,
'state' is a (row, col) tuple and the goal position is 'problem.goal'.
"""

import math
import util

"""
Need to updated this file. Cant change the problem.py file.
We look at this later.
"""

def nullHeuristic(state, problem=None):
    """The trivial heuristic: it knows nothing, so it always says 0."""
    return 0


def manhattanHeuristic(state, problem):
    """
    Q6: the Manhattan distance from 'state' to problem.goal:
        |row1 - row2| + |col1 - col2|
    """
    "*** YOUR CODE HERE ***"
    if problem is None:
        return 0
    goal = problem.getGoal()
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def euclideanHeuristic(state, problem):
    """
    Q6: the straight-line (Euclidean) distance from 'state' to problem.goal.
    """
    "*** YOUR CODE HERE ***"
    if problem is None:
        return 0
    goal = problem.getGoal()
    return math.sqrt((state[0] - goal[0])**2 + (state[1] - goal[1])**2)

