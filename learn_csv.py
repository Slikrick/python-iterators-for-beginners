# We are going to import the csv module.
# On it's own csv can be simple, comma separated values
# but when you have fields in quotes and such it can be tricky
# to get right, so we are going to use python's built in csv
# module
import csv

# We are going to open the file, read the csv values
# and calculate some averages based on the data
with open('mlb_players.csv') as f:
    reader = csv.reader(f)
    total_height = 0 # inches
    total_weight = 0 # pounds
    total_age    = 0 # years
    lines = 0
    next(reader) # skip header
    for line in reader:
        # We don't want any malformed data or lines
        if len(line) < 6 or line[4] == ' ""':
            continue
        total_height += int(line[3])
        total_weight += int(line[4])
        total_age    += float(line[5])
        # probably a more elegant way to track the lines
        # for the average
        lines += 1
    print(f"Average height: {total_height/lines:.2f} inches")
    print(f"Average weight: {total_weight/lines:.2f} lbs")
    print(f"Average age: {total_age/lines:.0f} years")
