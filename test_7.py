from Randomized import Randomized_Hamiltonian
from Backtracking import Backtracking_Hamiltonian


E = [(1, 2), (2, 3), (3, 1), (4, 2), (1, 4), (3, 4)]
V = [1, 2, 3, 4]


print("Backtracking Hamiltonian")
print(Backtracking_Hamiltonian(V, E))
print("Randomized Hamiltonian")
print(Randomized_Hamiltonian(V, E))


E = [(1,2), (3,1), (4,2), (1,4), (2,5), (5,4)]  #
V = [1,2,3,4,5]


print("Backtracking Hamiltonian")
print(Backtracking_Hamiltonian(V, E))
print("Randomized Hamiltonian")
print(Randomized_Hamiltonian(V, E))