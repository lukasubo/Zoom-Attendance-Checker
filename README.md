# PURPOSE
This Python script performs the following checks on your Zoom meeting usage report:
- Were students present in the first 15 minutes after the 10 minute grace period?
- Were students present in the last 15 minutes?
- Were students present for the time in between (i.e. how long spent in the lab)?


# REQUIREMENTS
This script requires Python 3, but uses only the Python standard library. No other packages are needed.


# USAGE
1. Replace the dummy emails in 'studentlist.csv' with a list of student emails for your lab section. This will be used to check for absent students and exclude non-students from checks.
2. Replace the dummy names in 'studentlist.csv'. These will be used to display the absent students - but not to check.
3. Run the below command.

`python attendance.py 'zoomreport.csv' S E`

If the above does not work, try:

`python3 attendance.py 'zoomreport.csv' S E`

Where:
- S = The start time, in 24H format (i.e. 8 AM = 8, 2 PM = 14).
- E = The end time, in 24H format.
- zoomreport.csv = The usage report from Zoom. Do NOT check any of the checkboxes, just download the default CSV report.

This will print a list of students with attendance problems to STDOUT.

# DOWNLOAD LINK
https://github.com/lukasubo/Zoom-Attendance-Checker/archive/main.zip
