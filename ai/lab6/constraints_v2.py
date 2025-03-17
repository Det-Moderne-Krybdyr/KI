from random import shuffle
import copy

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
        if(self.is_complete(assignment)):
            return assignment
        un_assigned_var = self.select_unassigned_variable(assignment)
        for v in self.order_domain_values(un_assigned_var,assignment):
            if(self.is_consistent(un_assigned_var,v,assignment)):
                if not self.forward_check(un_assigned_var,v):
                    print("forward check returned false")
                    continue
                assignment[un_assigned_var] = v
                result = self.recursive_backtracking(assignment)
                if result:
                    return result
                assignment.pop(un_assigned_var)
        return False
    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True

    def is_arc_consistent(self,x,y):
        for neighbor in self.neighbours[x]:
            if neighbor == y:
                pass




def create_australia_csp():
    wa, q, t, v, sa, nt, nsw = 'WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW'
    values = ['Red', 'Green', 'Blue']
    variables = [wa, q, t, v, sa, nt, nsw]
    domains = {
        wa: values[:],
        q: values[:],
        t: values[:],
        v: values[:],
        sa: values[:],
        nt: values[:],
        nsw: values[:],
    }
    neighbours = {
        wa: [sa, nt],
        q: [sa, nt, nsw],
        t: [],
        v: [sa, nsw],
        sa: [wa, nt, q, nsw, v],
        nt: [sa, wa, q],
        nsw: [sa, q, v],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        wa: constraint_function,
        q: constraint_function,
        t: constraint_function,
        v: constraint_function,
        sa: constraint_function,
        nt: constraint_function,
        nsw: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)

def create_south_america_csp():
    ven, col, ecu, peru, bol, chile, arg, para, uru,braz,guy_fr, suri, guy,pan,cost = "VEN", "COL", "ECU", "PERU", "BOL", "CHILE", "ARG", "PARA", "URU", "BRAZ", "GUY_FR", "SURI", "GUY", "PAN", "COST"

    values = ["Yellow","Green","Blue","Purple"]

    variables = ven, col, ecu, peru, bol, chile, arg, para, uru,braz,guy_fr, suri, guy,pan,cost 

    domains = {
        ven: values[:],
        col: values[:],
        ecu: values[:],
        peru: values[:],
        bol: values[:],
        chile: values[:],
        arg :values[:],
        para : values[:],
        uru :values[:],
        braz : values [:],
        guy_fr : values [:],
        suri : values [:],
        guy : values[:],
        pan : values[:],
        cost : values[:]
    }

    neighbours = {
        ven : [col,guy,braz],
        col: [ecu,peru,braz,ven],
        ecu: [peru,col],
        peru: [ecu,col,braz,bol,chile],
        bol: [braz,peru,chile,arg,para],
        chile: [arg,bol,peru],
        arg: [chile,bol,para,uru,braz],
        para: [bol,arg,braz],
        uru: [arg,braz],
        braz: [uru,arg,para,bol,peru,col,ven,guy,suri,guy_fr],
        guy_fr: [suri,braz],
        suri: [guy,guy_fr,braz],
        guy: [ven,suri,braz],
        pan: [cost,col],
        cost: [pan]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value
    
    constraints = {
        ven: constraint_function,
        col: constraint_function,
        ecu: constraint_function,
        peru: constraint_function,
        bol: constraint_function,
        chile: constraint_function,
        arg: constraint_function,
        para: constraint_function,
        uru: constraint_function,
        braz: constraint_function,
        guy_fr: constraint_function,
        suri: constraint_function,
        guy: constraint_function,
        pan: constraint_function,
        cost: constraint_function
    }

    return CSP(variables,domains,neighbours,constraints)

if __name__ == '__main__':
    #australia = create_australia_csp()
    #result = australia.backtracking_search()
    america = create_south_america_csp()
    result = america.backtracking_search()
    print(result)
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
