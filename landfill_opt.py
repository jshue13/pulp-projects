# Mixed integer linear optimization problem

'''
The Metropolis city council is examining four landfill sites
as candidates for use in the city's solid waste disposal network.
The monthly costs per ton have been estimated for operating at each
site and for transportation to each site from the various collection
areas. In addition, the amortized monthly cost for the facility at each
proposed site has also been estimated. What is the optimal configuration
and the minimum monthly system cost?
'''

# run 'pip install pulp' in the terminal if PuLP is not already installed
import pulp 

'''
PARAMETERS AND DATA
'''
# List of all the landfills
landfills = ["L1", "L2", "L3", "L4"]

# Dictionary of fixed costs for each landfill
landfills_fixed_cost = {"L1": 1000, "L2": 800, "L3": 700, "L4": 900}

# Dictionary of operating costs per ton for each landfill
landfills_op_cost = {"L1": 8, "L2": 10, "L3": 9, "L4": 11}

# List of collection areas
collection_areas = ['A', 'B', 'C', 'D', 'E', 'F']

# Dictionary of the waste supplied from each collection areas (in tons)
waste = {'A':500, 'B':700, 'C':1500, 'D':1000, 'E':1800, 'F':1200}

# Cost matrix for each transportation path
costs = [
    # Collection areas
    # A B C D E F
    [14, 12, 13, 10, 8, 11], # L1 Landfills
    [16, 11, 8, 15, 12, 10], # L2
    [10, 12, 9, 14, 10, 8], # L3
    [8, 14, 11, 12, 11, 6], # L4
]

# The cost data is made into a dictionary
costs = pulp.makeDict([landfills, collection_areas], costs, 0)

# Creates a list of tuples containing all the possible routes for transport
routes = [(l, c) for l in landfills for c in collection_areas]


'''
INITIATE THE PROBLEM / MODEL INSTANCE
'''
# Creates the 'prob' variable to contain the problem data
prob = pulp.LpProblem("Landfill Location Problem", pulp.LpMinimize)


'''
DECISION VARIABLES
'''
# Whether or not to use a specific landfill location
landfill_yn = pulp.LpVariable.dicts("Yes or No", landfills, 0, None, cat='Binary')

# The tons of waste for each route (landfill and collection area combination)
vars = pulp.LpVariable.dicts("Route", (landfills, collection_areas), 0, None, cat='Continuous')


'''
OBJECTIVE FUNCTION
'''
# The objective function is added to 'prob' first
prob += (
    pulp.lpSum([vars[l][c] * costs[l][c] for (l, c) in routes]) + # transportation costs
    pulp.lpSum([landfills_fixed_cost[l] * landfill_yn[l] for l in landfills]) + # fixed costs
    pulp.lpSum([landfills_op_cost[l] * vars[l][c] for (l, c) in routes] # operating costs
    ), 
    "Sum_of_Costs",
)


'''
CONSTRAINTS
'''
# The demand minimum constraints are added to prob for each demand node (collection area)
for c in collection_areas:
    prob += (
        pulp.lpSum([vars[l][c] for l in landfills]) >= waste[c],
        "Sum_of_Tons_out_of_Collection_Area_%s" % c,
    )

# The linking constraints for each landfill location 
for l in landfills:
    prob += (
        pulp.lpSum([vars[l][c] for c in collection_areas]) <= landfill_yn[l] * 9999,
        "Linking_constraint_for_Landfill_%s" % l,
    )


'''
RUN THE PROBLEM / MODEL AND GET RESULTS
'''
# The problem data is written to an .lp file
prob.writeLP("LandfillLocation.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", pulp.LpStatus[prob.status])
print('\n')

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

print('\n')
# The optimised objective function value is printed to the screen
print("Total Cost of Transportation = ", pulp.value(prob.objective))

