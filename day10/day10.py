from argparse import ArgumentParser
import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, PULP_CBC_CMD

def read_file(is_demo):
    file_name = "day10/input.txt" if not is_demo else "day10/demo-input.txt"
    return open(file_name, "r").read()

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--demo", "-d", action='store_true', help="Use demo input")
    return parser.parse_args()

def parse_machines(args):
    machines = []
    for line in read_file(bool(args.demo)).split("\n"):
        problem, rest = line.split(" ", 1)
        target = [int(light == "#") for light in problem[1:-1]]
        
        rest, joltages = rest.split(" {", 1)
        joltages = list(map(int, joltages[:-1].split(",")))
        
        buttons = [tuple(map(int, btn[1:-1].split(","))) for btn in rest.split()]
        machines.append((target, buttons, joltages))
    return machines

def solve_machine(target, buttons, is_binary=True):
    num_targets = len(target)
    num_buttons = len(buttons)
    
    # Build constraint matrix: A[i,j] = 1 if button j affects target i
    A = np.zeros((num_targets, num_buttons), dtype=int)
    for j, button in enumerate(buttons):
        for i in button:
            A[i, j] = 1
    
    prob = LpProblem("MinPresses", LpMinimize)
    
    if is_binary:
        # Part 1: Binary variables with mod 2 constraints
        x = [LpVariable(f"x{i}", cat='Binary') for i in range(num_buttons)]
        s = [LpVariable(f"s{i}", cat='Integer', lowBound=None) for i in range(num_targets)]
        
        prob += lpSum(x)
        for i in range(num_targets):
            prob += lpSum(A[i, j] * x[j] for j in range(num_buttons)) - 2 * s[i] == target[i]
    else:
        # Part 2: Integer variables with exact constraints
        x = [LpVariable(f"x{i}", cat='Integer', lowBound=0) for i in range(num_buttons)]
        
        prob += lpSum(x)
        for i in range(num_targets):
            prob += lpSum(A[i, j] * x[j] for j in range(num_buttons)) == target[i]
    
    prob.solve(PULP_CBC_CMD(msg=0))
    
    if prob.status == 1:  # Optimal
        return sum(int(value(x[i])) for i in range(num_buttons))
    return 0

def solution_one(args):
    machines = parse_machines(args)
    total_presses = 0
    for target, buttons, _ in machines:
        total_presses += solve_machine(target, buttons, is_binary=True)
    return total_presses

def solution_two(args):
    machines = parse_machines(args)
    total_presses = 0
    for _, buttons, joltages in machines:
        total_presses += solve_machine(joltages, buttons, is_binary=False)
    return total_presses

if __name__ == "__main__":
    args = parse_args()
    print("Solution 1:", solution_one(args))
    print("Solution 2:", solution_two(args))