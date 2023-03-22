import csv

poll_data = r"PyPoll\Resources\election_data.csv"

unique_names = set() #I want to use .add as itll help capture unique values easily!
                    #I will create a "un_list" that has the same thing as above but in a list format instead of set()

raymon_vote = 0 
diana_vote = 0
charles_vote = 0

with open(poll_data, 'r') as openfile: #this opens the .csv
    
    csv_reader = csv.reader(openfile, delimiter=",") #this reads the.csv
    next(csv_reader) #skipping the headers
    
    for row in csv_reader:
        unique_names.add(row[2])
    
    un_list = list(unique_names)
    # Raymon Anthony Doane is (un_list[0])
    # Diana DeGette (un_list[1])
    # Charles Casper Stockham (un_list[2])
    
    openfile.seek(0) 
    # Admittiedly ChatGPT made me aware I needed this 
    # to reset the position of the "file pointer" as after the last for loop it was at the very bottom so I can use another for that I wanted to use below. 
    next(csv_reader) #we need this again as it resets back to the very top.
    
    for row in csv_reader:
        if row[2] == un_list[0]:
            raymon_vote += 1
        elif row[2] == un_list[1]:
            diana_vote += 1
        elif row[2] == un_list[2]:
            charles_vote += 1

    #toal vote number calc and the % of votes are calculated for each member 
    total_vote = charles_vote + raymon_vote + diana_vote
    charles_per = (charles_vote/total_vote)*100
    diana_per = (diana_vote/total_vote)*100
    raymon_per = (raymon_vote/total_vote)*100

    #this if statement determines who the winner is 
    if charles_vote > diana_vote and charles_vote > raymon_vote:
        winner = 'Charles Casper'
    elif diana_vote > charles_vote and diana_vote > raymon_vote:
        winner = 'Diana DeGette'
    else:
        winner = 'Raymon Anthony Doane'

    #final statements that are printed for output
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_vote}")
    print("-------------------------")
    print(f"{un_list[2]}: {charles_per}% ({charles_vote})")
    print(f"{un_list[1]}: {diana_per}% ({diana_vote})")
    print(f"{un_list[0]}: {raymon_per}% ({raymon_vote})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    #now we move to put all these statements into a list for putting them into the txt file
    output = []
    output.append("Election Results")
    output.append("----------------------------")    
    output.append(f"Total Votes: {total_vote}")  
    output.append("----------------------------") 
    output.append(f"{un_list[2]}: {charles_per}% ({charles_vote})")
    output.append(f"{un_list[1]}: {diana_per}% ({diana_vote})")
    output.append(f"{un_list[0]}: {raymon_per}% ({raymon_vote})")
    output.append("-------------------------")
    output.append(f"Winner: {winner}")
    output.append("-------------------------")

    #we now make the file itself and write it with what values in the output to where ever your explorer is 
    with open("pypoll_output.txt", "w") as outfile:
        outfile.write('\n'.join(output))