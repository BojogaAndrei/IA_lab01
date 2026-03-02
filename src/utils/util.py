from scipy.spatial.distance import cityblock

def citeste_vectori(nume_fisier):
    with open(nume_fisier, 'r') as f:
        linii = f.readlines()
        v1 = [float(x) for x in linii[0].split()]
        v2 = [float(x) for x in linii[1].split()]
    return v1, v2
def manhattan_manual(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie saa aiba aceeasi dimensiune!")
    distanta = sum(abs(a-b) for a, b in zip(v1, v2))
    return distanta
def manhattan_scipy(v1, v2):
    return cityblock(v1, v2)