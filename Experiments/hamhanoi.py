def TowerOfHanoi(n, source, auxiliary, destination):
    if n == 0:
        return
    TowerOfHanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    TowerOfHanoi(n-1, auxiliary, source, destination)

n = 1

TowerOfHanoi(n, "A", "B", "C")