import os
import csv

election_data = os.path.join("election_data.csv")

# Creating a List of hold candidates name

candidates = []

# Creating a List to calcuate the total number of votes

number_votes = []

# List to calculate the % of votes received by each candidate

percentage_votes = []

# Maintaining a counter to count the total votes

total_votes = 0

with open(election_data, newline = "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    for row in csvreader:

        total_votes += 1

        if row[2] not in candidates:

            candidates.append(row[2])

            index = candidates.index(row[2])

            number_votes.append(1)

        else:

            index = candidates.index(row[2])

            number_votes[index] += 1


        # Adding % to number_votes list

    for votes in number_votes:

        percentage = (votes/total_votes) * 100

        percentage = round(percentage)

        percentage = "%.3f%%" % percentage

        percentage_votes.append(percentage)

    


        # Winning candidate

        winner = max(number_votes)

        index = number_votes.index(winner)
        
        winning_candidate = candidates[index]

 # Printing Out Results

print("Election Results")
print("-----------------------")
print(f"Total Votes : {str(total_votes)}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentage_votes[i])} ({str(number_votes[i])})")
print(f"Winning Candidate is : {winning_candidate}")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percentage_votes[i])} ({str(number_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))



