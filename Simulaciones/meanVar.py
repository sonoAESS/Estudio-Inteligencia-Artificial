import numpy as np

MLD=[923,963,689]
MPI=[453,962,689]
MLNS=[913,773,689]

print(np.mean(MLD))
print(f"[{np.min(MLD)};{np.max(MLD)}]")
print(np.var(MLD))
print("")

print(np.mean(MPI))
print(f"[{np.min(MPI)};{np.max(MPI)}]")
print(np.var(MPI))
print("")

print(np.mean(MLNS))
print(f"[{np.min(MLNS)};{np.max(MLNS)}]")
print(np.var(MLNS))
print("")