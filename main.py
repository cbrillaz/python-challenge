import os
import csv

total = 0
total_months = 0
prev_val = 0
change_list = []
month_list = []
pairing = {}

bankCSV = os.path.join('..', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

with open(bankCSV, newline='') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        total += int(row[1])
        total_months += 1
       
        if prev_val:
            change_list.append(int(row[1]) - prev_val)
            prev_val = int(row[1])
            month_list.append(str(row[0]))
    
        else:
            prev_val=(int(row[1]) - prev_val)
        
def avg_profit(change_list):
    return round(sum(change_list) / len(change_list))

pairing = dict(zip(month_list, change_list))

##print the homework answers
print("-------------------------------")
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_profit(change_list)}")
print(f"Greatest Increase in Profits: {max(pairing, key=pairing.get)} (${max(change_list)})")
print(f"Greatest Decrease in Profits: {min(pairing, key=pairing.get)} (${min(change_list)})")









