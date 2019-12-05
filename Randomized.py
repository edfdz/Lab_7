import random

def Randomized_Hamiltonian(V, E):
    maxTrials = 250
    if len(V) == 2:
        Eh = []
        for i in E:
            if (i[0] == V[0] and i[1] == V[1]) or (i[0] == V[1] and i[1] == V[0]):
                Eh.append(i)
                return Eh 
        return None 
    for i in range(maxTrials):
        random.shuffle(E)
        Eh = E[0:len(V)]
        connected = False
        for j in Eh:
            if j[0] != j[1]:
                connected = True 
                break
        if connected:
            vert = []
            for e in Eh:
                vert.extend(e)
            hamiltonian = True
            for v in V:
                if vert.count(v) != 2:
                    hamiltonian = False
                    break
            if hamiltonian:
                return Eh  
    return None  
