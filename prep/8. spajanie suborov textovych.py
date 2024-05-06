with open("p1.txt", "r") as p1:
    with open("p2.txt", "r") as p2:
        with open("p3.txt", "r") as p3:
            with open("november.txt", "w") as november:
                november.write(f"{p1.read()}\n{p2.read()}\n{p3.read()}\n")
