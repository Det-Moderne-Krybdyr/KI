A = "A"
B = "B"
C = "C"
D = "D"

Environment = {A: "Dirty", B: "Dirty", C: "Dirty", D: "Dirty", "Current": A}


def REFLEX_VACUUM_AGENT(loc_st):  # Determine action
    location, status = loc_st
    if status == "Dirty":
        return "Suck"
    if location == A:
        return "Down"
    if location == B:
        return "Left"
    if location == C:
        return "Right"
    if location == D:
        return "Up"


def Sensors():  # Sense Environment
    location = Environment["Current"]
    return (location, Environment[location])


def Actuators(action):  # Modify Environment
    location = Environment["Current"]
    if action == "Suck":
        Environment[location] = "Clean"
    elif action == "Right" and location == A:
        Environment["Current"] = B
    elif action == "Down" and location == A:
        Environment["Current"] = C
    elif action == "Left" and location == B:
        Environment["Current"] = A
    elif action == "Down" and location == B:
        Environment["Current"] = D
    elif action == "Up" and location == C:
        Environment["Current"] = A
    elif action == "Right" and location == C:
        Environment["Current"] = D
    elif action == "Left" and location == D:
        Environment["Current"] = C
    elif action == "Up" and location == D:
        Environment["Current"] = B


def run(n):  # run the agent through n steps
    print("    Current                        New")
    print("location    status  action  location    status")
    for i in range(1, n):
        (location, status) = Sensors()  # Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end="")
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors()  # Sense Environment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))


if __name__ == "__main__":
    run(20)
