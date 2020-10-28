import csv
import sys
import datetime

def mergeIntoList(key, row, list):  #This function checks is a student is already in the list.
                                    #It either adds the student or amends their current entry.
    if any(dict[key] == row[key] for dict in list): #Check if exists.
        for i, dict in enumerate(list): #If exists, iterate through list.
            if dict[key] == row[key]: #Stop at entry to be amended.
                dict['Join Time'] = min(dict['Join Time'], row['Join Time']) #Replace join time in entry if new one is prior.
                dict['Leave Time'] = max(dict['Leave Time'], row['Leave Time']) #Replace leave time in entry if new one is later.
                dict['Duration (Minutes)'] = dict['Duration (Minutes)'] + row['Duration (Minutes)'] #Sum durations.
                list[i] = dict #Puts the amended data in the list element.
    else: #If the user isn't already in the list.
        list.append(row) #Append them to it as a new element.
    return list #Function returns the list with the row integrated into it.

input_file = csv.DictReader(open(sys.argv[1], encoding='utf-8-sig')) #Opens the Zoom usage report.
student_file = csv.DictReader(open(sys.argv[2], encoding='utf-8-sig')) #Opens the list of student emails for the section.

list = [] #Initializes an empty list to fill with the usage report data.
student_list = []

for row in student_file: #Iterates through the student emails.
    student_list.append(row)

for row in input_file: #Reads the Zoom report.
    row['Join Time'] = datetime.datetime.strptime(row['Join Time'], '%m/%d/%Y %H:%M:%S %p') #Convert to Python date.
    date = row['Join Time'] #Record 'date' to get meeting date.
    row['Leave Time'] = datetime.datetime.strptime(row['Leave Time'], '%m/%d/%Y %H:%M:%S %p') #Convert to Python date.
    row['Duration (Minutes)'] = int(row['Duration (Minutes)']) #Convert to integer.
    if row['User Email'] == '': #For empty emails (phone-in).
        list = mergeIntoList('Name (Original Name)', row, list) #Merge by user name (phone number).
    else:
        if any(dict['User Email'] == row['User Email'] for dict in student_list): #Proceeds only if the student is in the student list.
            list = mergeIntoList('User Email', row, list) #Merge by email.
    #The above if-else is needed instead of just always merging by user name,
    #because some students change their name mid-meeting when dropping and re-joining.

print('') #newline to differentiate the output visually from the terminal prompt.

for val in list:
    trip = False #Stores whether a check was tripped for current val.
    if val['Join Time'] > datetime.datetime(date.year, date.month, date.day, int(sys.argv[3]), 25):
        print(val['Name (Original Name)'], 'joined late.', datetime.datetime.strftime(val['Join Time'], '%m/%d/%Y %H:%M:%S %p'))
        trip = True
    if val['Leave Time'] < datetime.datetime(date.year, date.month, date.day, int(sys.argv[4])-1, 45):
        print(val['Name (Original Name)'], 'left early.', datetime.datetime.strftime(val['Leave Time'], '%m/%d/%Y %H:%M:%S %p'))
        trip = True
    if val['Duration (Minutes)'] < (int(sys.argv[4]) - int(sys.argv[3]))*60-30:
        print(val['Name (Original Name)'], 'was present for only', val['Duration (Minutes)'], 'minutes.')
        trip = True
    if trip: #Adds a newline if a check was tripped, to space out individual students.
        print('')

for row in student_list: #Iterates through the student emails.
    if not any(dict['User Email'] == row['User Email'] for dict in list): #Checks if the student was absent.
        print(row['User Email'], 'was absent.\n') #Reports absent student.
