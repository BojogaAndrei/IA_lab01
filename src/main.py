from utils.util import citeste_vectori, manhattan_manual, manhattan_scipy

def main():
    try:
        v1, v2 = citeste_vectori('input.txt')
        print(f"Vector 1: {v1}")
        print(f"Vector 2: {v2}")

        dist_manual = manhattan_manual(v1, v2)
        dist_scipy = manhattan_scipy(v1, v2)

        print("-"*30)
        print(f"Distanta Manhattan (Manual): {dist_manual}")
        print(f"Distanta Manhattan (Scipy): {dist_scipy}")

    except FileNotFoundError:
        print("Eroare fisier")
    except Exception as e:
        print(f"eroare {e}")
    
if __name__ == "__main__":
    main()
