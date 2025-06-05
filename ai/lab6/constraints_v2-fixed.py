from random import shuffle
import copy
from collections import deque


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints
        self.legal_values = copy.deepcopy(domains)

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                saved_domains = copy.deepcopy(self.legal_values)

                if not self.forward_check(var, value):
                    self.legal_values = saved_domains  # restore domains
                    continue

                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result:
                    return result

                assignment.pop(var)
                self.legal_values = saved_domains  # backtrack
        return False

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var

    def is_complete(self, assignment):
        return len(assignment) == len(self.variables)

    def order_domain_values(self, variable, assignment):
        return self.legal_values[variable][:]

    def is_consistent(self, variable, value, assignment):
        for neighbor in self.neighbours[variable]:
            if neighbor in assignment and not self.constraints[variable](
                variable, value, neighbor, assignment[neighbor]
            ):
                return False
        return True

    def forward_check(self, var, value):
        self.legal_values[var] = [value]
        for neighbor in self.neighbours[var]:
            if value in self.legal_values[neighbor]:
                self.legal_values[neighbor].remove(value)
                if not self.legal_values[neighbor]:
                    return False
        return True


# ----------------- Optional: AC-3 -------------------


def ac3(csp):
    queue = deque([(xi, xj) for xi in csp.variables for xj in csp.neighbours[xi]])
    while queue:
        xi, xj = queue.popleft()
        if revise(csp, xi, xj):
            if not csp.legal_values[xi]:
                return False
            for xk in csp.neighbours[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True


def revise(csp, xi, xj):
    revised = False
    for x in csp.legal_values[xi][:]:
        if not any(x != y for y in csp.legal_values[xj]):
            csp.legal_values[xi].remove(x)
            revised = True
    return revised


# ----------------- CSP Instances -------------------


def create_south_america_csp():
    (
        ven,
        col,
        ecu,
        peru,
        bol,
        chile,
        arg,
        para,
        uru,
        braz,
        guy_fr,
        suri,
        guy,
        pan,
        cost,
    ) = (
        "VEN",
        "COL",
        "ECU",
        "PERU",
        "BOL",
        "CHILE",
        "ARG",
        "PARA",
        "URU",
        "BRAZ",
        "GUY_FR",
        "SURI",
        "GUY",
        "PAN",
        "COST",
    )

    values = ["Yellow", "Green", "Blue", "Purple"]
    variables = [
        ven,
        col,
        ecu,
        peru,
        bol,
        chile,
        arg,
        para,
        uru,
        braz,
        guy_fr,
        suri,
        guy,
        pan,
        cost,
    ]

    domains = {var: values[:] for var in variables}

    neighbours = {
        ven: [col, guy, braz],
        col: [ecu, peru, braz, ven],
        ecu: [peru, col],
        peru: [ecu, col, braz, bol, chile],
        bol: [braz, peru, chile, arg, para],
        chile: [arg, bol, peru],
        arg: [chile, bol, para, uru, braz],
        para: [bol, arg, braz],
        uru: [arg, braz],
        braz: [uru, arg, para, bol, peru, col, ven, guy, suri, guy_fr],
        guy_fr: [suri, braz],
        suri: [guy, guy_fr, braz],
        guy: [ven, suri, braz],
        pan: [cost, col],
        cost: [pan],
    }

    def constraint_function(v1, val1, v2, val2):
        return val1 != val2

    constraints = {var: constraint_function for var in variables}
    return CSP(variables, domains, neighbours, constraints)


# ----------------- Main -------------------

if __name__ == "__main__":
    csp = create_south_america_csp()

    print("Running AC-3...")
    ac3(csp)  # optional, for extra pruning

    print("Solving CSP with backtracking + forward checking...")
    result = csp.backtracking_search()

    if result:
        for country in sorted(result.keys()):
            print(f"{country}: {result[country]}")
    else:
        print("No solution found.")
