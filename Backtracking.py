def backtracking(g, v, temp):
    if len(temp) == len(g):
        for i in g[v]:
            if i == 0:
                return [v]
        return None
    for i in g[v]:
        if i not in temp:
            newTemp = list(temp)
            newTemp.append(i)
            p = backtracking(g, i, newTemp)
            if p is not None:
                p.append(v)
                return p
    return None  


def Backtracking_Hamiltonian(V, E):
    g = [[] for i in range(len(V))]
    for j in E:
        index1 = -1  
        index2 = -1
        for i in range(len(V)):
            if V[i] == j[0]:
                index1 = i
            if V[i] == j[1]:
                index2 = i
        if index1 != -1 and index2 != -1:
            g[index2].append(index1)
            g[index1].append(index2)
    p = backtracking(g, 0, [0])
    if p is None:
        return None   
    p.reverse()
    Eh = []
    for i in range(len(p) - 1):
        Eh.append((V[p[i]], V[p[i+1]]))
    Eh.append((V[p[-1]], V[0]))
    return Eh  