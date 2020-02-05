"""Generate sales report showing total melons each salesperson sold."""

# initializing two empty lists, one for sales people and one for melons sold
salespeople = []
melons_sold = []
#  open the sales-report.txt file where the data is stored
f = open('sales-report.txt')
# go through each line in the data file
for line in f:
    # strip off all the white space (on the right side of the line)
    line = line.rstrip()
    # parse out each entry using the | as a delimiter
    entries = line.split('|')

    # salesperson is the first entry in each line
    salesperson = entries[0]
    # melonds is the third entry in each line
    melons = int(entries[2])

    # if the salesperson in the line we are currently looking at, 
    # is in the list of salespeople create a new entry in the salesperson
    # list. Get the position of that entry in the salesperson list and
    # add the associated # of melons at the same position in the melons list
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    # Otherwise the salesperson exists already and we want to update their melon
    # count with the new amount added to the existing amount for a running total
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# here we want to print out the salesperson and their corresponding melon total
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
