import re
import math

def add_time(start, duration, start_day = None):
  days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  s = re.split('[:\s]', start)
  d = duration.split(":")
  time = ""
  hour = 0
  minute = 0
  post = s[2]
  counter = 0
  final_day = ""
  later = ""
  
  # Calculate Minutes
  if int(s[1]) + int(d[1]) > 59:
    minute += int(s[1]) + int(d[1]) - 60
  else:
    minute += int(s[1]) + int(d[1])
  if minute < 10:
    minute = "0" + str(minute)
  else:
    minute = str(minute)
  
  # Calculate Hour and AM/PM
  hour += int(s[0]) + int(d[0])
  while hour > 12:
    hour -= 12
    counter += 1
    if post == "AM":
      post = "PM"
    else:
      post = "AM"
  if int(s[1]) + int(d[1]) > 59:
    hour += 1
    if (counter % 2) == 0:
      if post == "AM":
        post = "PM"
      else:
        post = "AM"
    if int(s[0]) + int(d[0]) <= 12:
      if post == "PM":
        post = "AM"
      if post == "AM":
        post = "PM"
  hour = str(hour)

  # Calculates Number of Days Later
  num = math.ceil(counter/2)
  if s[2] == "PM":
    if counter == 1:
      later += "(next day)"
  if counter > 1:
    if counter != 2:
      later += "(" + "{l}".format(l=str(num)) + " days later)"
    else:
      if int(d[0]) <= 24 and (int(s[1]) + int(d[1])) < 60:
        later += "(next day)"
      else:
        later += "(2 days later)"

  # Concat Time String
  time += hour + ":" + minute + " " + post
  
  # If Optional Argument is Given, Returns Day of Week  
  if start_day:
    for day in days:
      if re.match("^{start_day}$".format(start_day=start_day), day, re.IGNORECASE):
        index = days.index(day)
        if counter == 0 or counter == 1:
          daycalc = (index)            
        elif counter == 2:
          daycalc = (index + counter)
          if int(d[0]) <= 24 and (int(s[1]) + int(d[1])) < 60:
            daycalc -= 1
        elif counter > 2:
          daycalc = (index + num)
        while daycalc > 6:
          daycalc -= 7
        final_day += days[daycalc]

        if later != "":
          return time + ", " + final_day + " " + later
        return time + ", " + final_day 
        

  if later != "":
    return time + " " + later
  return time


# Example call:
# add_time("11:43 PM", "24:20", "tueSday")
