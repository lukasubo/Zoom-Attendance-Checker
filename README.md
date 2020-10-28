#PURPOSE
This python script checks your Zoom lab's attendance with the following checks:
- Were students present in the first 15 minutes after the 10 minute grace period?
- Were students present in the last 15 minutes?
- Were students present for the time in between (i.e. how long spent in the lab)?


#REQUIREMENTS
This script requires Python 3, but uses only libraries that ship with Python by default.


#USAGE
`python3 attendance.py 'zoomreport.csv' 'studentlist.csv' S E`

Where:
- S = The start time, in 24H format (i.e. 8 AM = 8, 2 PM = 14)
- F = The end time, in 24H format
- zoomreport.csv = The usage report from Zoom. Do NOT check any of the checkboxes, just download the default CSV report.
- studentlist.csv = Pre-created next to the script. Replace the dummy emails with a list of student emails for your lab section.
