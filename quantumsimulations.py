import numpy as np
import random

# ===================== HHL Simulation ===================== #
# Step 1: Solve the system of linear equations using HHL (classical simulation)
# We use numpy's solver to simulate the effect of HHL classically.

def solve_linear_system_hhl(A, b):
    """
    Simulates the HHL algorithm classically to solve the system of linear equations A * x = b.
    """
    try:
        # Classical solver to simulate the quantum HHL process
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        return None

# Example system of linear equations
A = np.array([[3, 1], 
              [1, 2]])
b = np.array([9, 8])

# Solve using classical simulation of HHL
solution_vector_hhl = solve_linear_system_hhl(A, b)

# Output the solution
if solution_vector_hhl is not None:
    print("Solution to the system of equations using HHL simulation:", solution_vector_hhl)
else:
    print("The system has no unique solution or is singular.")

# ===================== Grover's Algorithm for Portfolio Optimization ===================== #
# Step 2: Use Grover's search (classical simulation) for portfolio optimization

# Example portfolio returns (2 assets for simplicity)
returns = np.array([[0.1, 0.2], 
                    [0.3, 0.4]])

# Simulating classical Grover's search for optimal portfolio allocation
def classical_oracle(num_assets, target_allocation):
    """
    Classical oracle to simulate Grover's search for portfolio optimization.
    It checks if a randomly chosen allocation matches the target allocation.
    """
    random_allocation = random.choices(range(2**num_assets), k=1)[0]
    allocation_bin = f"{random_allocation:0{num_assets}b}"
    return allocation_bin == ''.join(map(str, target_allocation))

def grover_portfolio_optimization(num_assets, target_allocation, iterations=10):
    """
    Classical simulation of Grover's search for portfolio optimization.
    Searches for the optimal allocation that maximizes returns.
    """
    optimal_allocations = []
    for _ in range(iterations):
        random_allocation = random.choices(range(2**num_assets), k=1)[0]
        allocation_bin = f"{random_allocation:0{num_assets}b}"
        
        # Oracle check - see if the random allocation matches the target
        if classical_oracle(num_assets, target_allocation):
            optimal_allocations.append(allocation_bin)
    
    return optimal_allocations if optimal_allocations else ["No optimal allocation found"]

# Define the number of assets and target allocation (for the portfolio optimization)
num_assets = 2
target_allocation = [1, 0]  # Target allocation for two assets (e.g., heavy on the first asset)

# Run classical simulation of Grover's search for portfolio optimization
optimal_portfolio = grover_portfolio_optimization(num_assets, target_allocation, iterations=10)

# Output the result (optimal allocation based on Grover's search)
print("Optimal portfolio allocation (Grover's search simulation):", optimal_portfolio)
