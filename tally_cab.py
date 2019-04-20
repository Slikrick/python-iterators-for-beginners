with open("tally_cab.csv") as f:
    # We skip the header that describes the format
    next(f)
    # We want the sum()
    # of all float values
    # in the first column
    # of all the lines in the file
    t = sum(float(s.split(",")[0]) for s in f)
    print(t)

# How would you add up the fares? Mess with the data
# further on your own. Additional csv's can be found here:
# https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
