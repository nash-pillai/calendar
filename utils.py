def colorize(code, txt): return f"\033[{code}m{txt}\033[0m"

# Day/Mon/Year
events = [
  {"name": "New Year's Day", "date": "1/1/2020", "time": "13:30"},
  {"name": "Martin Luther King Jr. Day", "date": "20/1/2020", "time": "13:30"},
  {"name": "Presidents' Day", "date": "17/2/2020", "time": "13:30"},
  {"name": "Memorial Day", "date": "25/5/2020", "time": "13:30"},
  {"name": "Independence Day", "date": "4/7/2020", "time": "13:30"},
  {"name": "Labor Day", "date": "7/9/2020", "time": "13:30"},
  {"name": "Columbus Day", "date": "12/10/2020", "time": "13:30"},
  {"name": "Veterans Day", "date": "11/11/2020", "time": "13:30"},
  {"name": "Thanksgiving Day", "date": "26/11/2020", "time": "13:30"},
  {"name": "Christmas Day", "date": "25/12/2020", "time": "13:30"}
]