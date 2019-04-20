with open("addresses.csv") as f:
    for line in f:
        line = line.upper()
        print(f"line length: {len(line)}\nline: {line}")

