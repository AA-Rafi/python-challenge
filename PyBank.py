import csv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
budget_data_path = os.path.join(current_dir, 'Resources', 'budget_data.csv')
y = [] # this will house all the values of col 1 (Date), excluding the header
x = [] # this will house all the values of col 2 (Profit/Loss), excluding the header

with open(budget_data_path, 'r') as openfile:
    csv_reader = csv.reader(openfile, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        x.append(int(row[1]))
        y.append(row[0])

    # Setting up "Total Months" and "Total" fields
    sum_changes = sum(x) # Returns value for Total
    total_months = len(x) # number of months

    # Setting up "Average Change" field
    change = [x[i] - x[i-1] for i in range(1, len(x))] 
    average_change = sum(change) / len(change)

    # Following code used to find max value AND associated month
    max_change = max(change)
    max_index = change.index(max_change)
    max_month = y[max_index + 1]

    # Following code used to find min value AND associated month
    min_change = min(change) 
    min_index = change.index(min_change)
    min_month = y[min_index + 1]

    # Final statements that are printed for output
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {sum_changes}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

    # Now we move to put all these statements into a list for putting them into the txt file
    output = []
    output.append("Financial Analysis")
    output.append("----------------------------")
    output.append(f"Total Months: {total_months}")
    output.append(f"Total: {sum_changes}")
    output.append(f"Average Change: {average_change}")
    output.append(f"Greatest Increase in Profits: {max_month} (${max_change})")
    output.append(f"Greatest Decrease in Profits: {min_month} (${min_change})")

    # We now make the file itself and write it with what values in the output to wherever your explorer is
    output_file_path = budget_data_path = os.path.join(current_dir, 'Analysis', 'pybank_output.txt')
    with open(output_file_path, "w") as outfile:
        outfile.write('\n'.join(output))

    print(f"Output saved to {output_file_path}")