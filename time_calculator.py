def add_time(start, duration, day=''):
  
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  str_minutes = ''
  aux = ''
  days_passed = ''
  new_day = ''

  start_hours = int(start.split()[0].split(":")[0])
  start_minutes = int(start.split()[0].split(":")[1])

  duration_hours = int(duration.split(":")[0])
  duration_minutes = int(duration.split(":")[1])

  if start.split()[1] == "PM": start_hours = start_hours + 12

  minutes = ((start_hours + duration_hours) * 60 + start_minutes + duration_minutes)
  total_hours = minutes // 60
  total_minutes = minutes % 60

  if len(day) > 0:
      cont = 0
      day = day.lower()
      for d in days:
        cont = cont + 1
        if d.lower() == day:
          break
      pos_arr = (cont - 1 +(total_hours // 24)) % 7
      new_day = ', ' + days[pos_arr]

  if total_hours // 24 == 0:
    if len(new_day) > 0:
      days_passed = new_day
  elif total_hours // 24 == 1:
    days_passed = new_day + ' (next day)' if len(new_day) > 0 else ' (next day)'
  elif total_hours // 24 >= 2:
    if len(new_day) > 0:
      days_passed = new_day + ' ('+ str(total_hours // 24) +' days later)'
    else:
      days_passed = ' ('+ str(total_hours // 24) +' days later)'

  str_minutes = str(total_minutes) if len(str(total_minutes)) > 1 else ('0' + str(total_minutes))

  aux = ' PM' if total_hours % 24 >= 12 and total_hours % 24 <= 24 else ' AM'

  new_time = (str(total_hours % 12) if str(total_hours % 12)!='0' else '12' )+':' + str_minutes + aux + days_passed 

  
  return new_time