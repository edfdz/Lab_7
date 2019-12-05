from Randomized import Randomized_Hamiltonian
from Backtracking import Backtracking_Hamiltonian


E = [(11, 25), (25, 7), (7, 11), (4, 25), (11, 4), (7, 4)]
V = [11, 25, 7, 4]

print("Backtracking Hamiltonian")
print(Backtracking_Hamiltonian(V, E))
print("Randomized Hamiltonian")
print(Randomized_Hamiltonian(V, E))

E = [(11,25), (7,11), (4,2), (11,4), (25,2), (5,4)]
V = [11,25,7,4,2]

print("Backtracking Hamiltonian")
print(Backtracking_Hamiltonian(V, E))
print("Randomized Hamiltonian")
print(Randomized_Hamiltonian(V, E))