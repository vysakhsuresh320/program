INPUT_FILE = 'sample_input2.txt'
OUTPUT_FILE = 'sample_output2.txt'

numOfEmployees = 0
items = []

# Open the input file in a scope so that it automatically closes
with open(INPUT_FILE, 'r') as inp:
    lines = inp.readlines()
    startOfItemsInput = False
    # Read each line from input one by one
    for line in lines:
        # Ignore empty lines
        strippedLine = line.strip()
        if strippedLine:
            # Check if items input has started
            if strippedLine == 'Goodies and Prices:':
                startOfItemsInput = True
                continue
            # start_items_input will be false only for the number of employees lines
            if not startOfItemsInput:
                numOfEmployees = int(strippedLine.split(":")[1].strip())
            else:
                itemName = strippedLine.split(":")[0].strip()
                itemPrice = int(strippedLine.split(":")[1].strip())
                items.append((itemPrice, itemName))

# Sort items by first element of the tuple
items.sort()

startIndex = 0
maxDifference = items[numOfEmployees - 1][0] - items[0][0]

# Iterate through the sorted list to find difference between i th element and i + numEmployees element
for i in range(0, len(items) - numOfEmployees + 1):
    if items[i + numOfEmployees - 1][0] - items[i][0] < maxDifference:
        startIndex = i
        maxDifference = items[i + numOfEmployees - 1][0] - items[i][0]

with open(OUTPUT_FILE, 'w') as op:
    print("The goodies selected for distribution are:", file=op)
    print("", file=op)
    
    for i in range(0, numOfEmployees):
        print(items[startIndex + i][1],": ",items[startIndex + i][0], file=op)

    print("", file=op)
    print("And the difference between the chosen goodie with highest price and the lowest price is ",maxDifference, file=op)
