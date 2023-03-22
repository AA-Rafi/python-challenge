import csv

budget_data = r"PyBank\Resources\budget_data.csv"
x = [] #this will house all the values of col 2 (Profit/Loss), excluding the header
y = [] # this will house all the values of col 1 (Date), excluding the header

with open(budget_data, 'r') as openfile:
    
    csv_reader = csv.reader(openfile, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        x.append(int(row[1]))
        y.append(row[0])


    sum_changes = sum(x) #incorrect numerator for Average
    months = len(x) #denonator for Average
    average_change = sum_changes/months #Average of Profit and Loss (placeholder)

    #following code used to find max value AND associated month
    max_value = max(x)
    max_index = x.index(max_value)
    max_month = y[max_index]

    #following code used to find min value AND associated month
    min_value = min(x)
    min_index = x.index(min_value)
    min_month = y[min_index]


    #final statements that are printed for output
    print("Financial Analysis")
    print("----------------------------")    
    print(f"Total Months: {months}")  
    print(f"Total: {sum_changes}")  
    print(f"Average Change: {average_change} Although I know this isnt what we want")
    print(f"Greatest Increase in Profits: {max_month} (${max_value})")  
    print(f"Greatest Decrease in Profits: {min_month} (${min_value})")  

    #now we move to put all these statements into a list for putting them into the txt file
    output = []
    output.append("Financial Analysis")
    output.append("----------------------------")    
    output.append(f"Total Months: {months}")  
    output.append(f"Total: {sum_changes}")  
    output.append(f"Average Change: {average_change} Although I know this isnt what we want")
    output.append(f"Greatest Increase in Profits: {max_month} (${max_value})")  
    output.append(f"Greatest Decrease in Profits: {min_month} (${min_value})")  

    #we now make the file itself and write it with what values in the output to where ever your explorer is 
    with open("pybank_output.txt", "w") as outfile:
        outfile.write('\n'.join(output))

    
