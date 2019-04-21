# import the modules
import csv
import json

# reader dict collection
bankAndBranchDict = []

# https://www.paymentsnz.co.nz/resources/industry-registers/bank-branch-register/
# read bank branch registry
with open("Bank_Branch_Register.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        bankAndBranchDict.append(dict(row))
csvfile.close()

# New banks collection for JSON
sBanks = {}

# For each branch
for branch in bankAndBranchDict:
  # If we don't have the Bank yet
  if branch["Bank_Number"] not in sBanks:
    # Add the bank
    sBanks[branch["Bank_Number"]] = {"Bank_Name": branch["Bank_Name"], "Branches": {}}
  # Clone the branch info
  branchDict = branch.copy()
  # Get the number
  branchNumber = branchDict.pop("Branch_Number")
  # Remove Bank Attributes from Branch
  del branchDict["Bank_Number"]
  del branchDict["Bank_Name"]
  # Add Branch to Bank
  sBanks[branch["Bank_Number"]]["Branches"][branchNumber] = branchDict
 
# Dump Bank Dict into JSON file
jsonDump = json.dumps(sBanks)
jsonFile = open("banks.json","w")
jsonFile.write(jsonDump)
jsonFile.close()