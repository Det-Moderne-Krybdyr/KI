import functools
from pprint import pformat
from itertools import product


def multiply_vector_elements(vector):
    def mult(x, y):
        return x * y
    return functools.reduce(mult, vector, 1)


class Variable:
    def __init__(self, name, assignments, probability_table, parents=None):
        self.name = name
        self.assignments = {k: i for i, k in enumerate(assignments)}
        self.reverse_assignments = {i: k for k, i in self.assignments.items()}
        for key, val in probability_table.items():
            if len(val) != len(assignments):
                raise ValueError("Inconsistent table and assignment size")
        self.probability_table = probability_table
        self.parents = parents or []
        self.children = []
        self.marginal_probabilities = [0] * len(assignments)
        self.ready = False

    def get_probability(self, value, parents_values):
        return self.probability_table[parents_values][self.assignments[value]]

    def get_conditional_probability(self, value, parent_vals):
        total = 0
        given = []
        marginal = []
        for i, parent in enumerate(self.parents):
            if parent.name in parent_vals:
                given.append((i, parent_vals[parent.name]))
            else:
                marginal.append(i)

        for row_key, row_val in self.probability_table.items():
            valid = True
            for gi in given:
                if row_key[gi[0]] != gi[1]:
                    valid = False
                    break
            if valid:
                p_parents = 1
                for mi in marginal:
                    parent = self.parents[mi]
                    p_parents *= parent.get_marginal_probability(row_key[mi])
                total += row_val[self.assignments[value]] * p_parents
        return total

    def calculate_marginal_probability(self):
        if self.ready:
            return
        if not self.parents:
            self.marginal_probabilities = list(self.probability_table[()])
        else:
            total = [0] * len(self.assignments)
            parent_values = [p.assignments.keys() for p in self.parents]
            for combo in product(*parent_values):
                parent_vals = dict(zip([p.name for p in self.parents], combo))
                p_joint = 1
                for p in self.parents:
                    p.calculate_marginal_probability()
                    p_joint *= p.get_marginal_probability(parent_vals[p.name])
                probs = self.probability_table[tuple(parent_vals[p.name] for p in self.parents)]
                for i in range(len(probs)):
                    total[i] += probs[i] * p_joint
            self.marginal_probabilities = total
        self.ready = True

    def get_marginal_probability(self, val):
        return self.marginal_probabilities[self.assignments[val]]

    def is_child_of(self, node):
        return node in self.parents


class BayesianNetwork:
    def __init__(self):
        self.variables = []
        self.varsMap = {}

    def set_variables(self, var_list):
        self.variables = var_list
        self.varsMap = {v.name: v for v in var_list}

    def calculate_marginal_probabilities(self):
        for var in self.variables:
            var.calculate_marginal_probability()

    def get_joint_probability(self, values):
        missing = [v.name for v in self.variables if v.name not in values]

        if not missing:
            prob = 1
            for var in self.variables:
                val = values[var.name]
                parent_vals = tuple(values[p.name] for p in var.parents)
                prob *= var.get_probability(val, parent_vals)
            return prob

        # Marginalize over missing variables
        domains = {v.name: list(v.assignments.keys()) for v in self.variables}
        total = 0
        for assignment in product(*[domains[v] for v in missing]):
            assignment_dict = dict(zip(missing, assignment))
            full_values = {**values, **assignment_dict}
            total += self.get_joint_probability(full_values)
        return total

    def get_conditional_probability(self, values, evidents):
        joint_all = self.get_joint_probability({**values, **evidents})
        denom = 0
        assignments = list(values.items())
        var_name, var_val = assignments[0]
        for alt_val in self.varsMap[var_name].assignments:
            new_values = values.copy()
            new_values[var_name] = alt_val
            denom += self.get_joint_probability({**new_values, **evidents})
        return joint_all / denom if denom > 0 else 0


def print_marginal_probabilities(network):
    print("Marginal probabilities:")
    for var in network.variables:
        print(f"  {var.name}:")
        for val in var.assignments:
            prob = var.get_marginal_probability(val)
            print(f"    {val}: {prob:.6f}")


def print_joint_probability(network, values):
    print("Joint probability of")
    print("   ", pformat(values))
    print(f"is {network.get_joint_probability(values):.6f}")


def print_conditional_probability(network, values, evidents):
    print("Given")
    print("   ", pformat(evidents))
    print("Conditional probability of")
    print("   ", pformat(values))
    print(f"is {network.get_conditional_probability(values, evidents):.6f}")


def fuel_tank():
    # Tables: true index 0, false index 1
    t1 = {(): (0.3, 0.7)}
    t2 = {(): (0.3, 0.7)}
    t3 = {(): (0.2, 0.8)}

    t4 = {
        ("true",): (0.7, 0.3),
        ("false",): (0.1, 0.9),
    }

    t5 = {
        ("true", "true"): (0.05, 0.95),
        ("true", "false"): (0.6, 0.4),
        ("false", "true"): (0.3, 0.7),
        ("false", "false"): (0.7, 0.3),
    }

    t6 = {
        ("true", "true", "true"): (0.9, 0.1),
        ("true", "true", "false"): (0.8, 0.2),
        ("true", "false", "true"): (0.3, 0.7),
        ("true", "false", "false"): (0.2, 0.8),
        ("false", "true", "true"): (0.6, 0.4),
        ("false", "true", "false"): (0.5, 0.5),
        ("false", "false", "true"): (0.1, 0.9),
        ("false", "false", "false"): (0.01, 0.99),
    }

    dt = Variable("DT", ("true", "false"), t1)
    em = Variable("EM", ("true", "false"), t2)
    ftl = Variable("FTL", ("true", "false"), t3)
    v = Variable("V", ("true", "false"), t4, [dt])
    sms = Variable("SMS", ("true", "false"), t5, [dt, em])
    hc = Variable("HC", ("true", "false"), t6, [dt, ftl, em])

    net = BayesianNetwork()
    net.set_variables([dt, em, ftl, v, sms, hc])
    net.calculate_marginal_probabilities()

    print_marginal_probabilities(net)
    print()

    values = {
        "DT": "true",
        "EM": "false",
        "FTL": "true",
        "V": "true",
        "SMS": "true",
        "HC": "true",
    }
    print_joint_probability(net, values)
    print()

    print_conditional_probability(net, {"HC": "true"}, {"FTL": "true"})


# Run it
fuel_tank()
