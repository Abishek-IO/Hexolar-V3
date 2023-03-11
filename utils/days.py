def get_days_in_month(month, year):
  is_leap_year = False
  if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):
      is_leap_year = True

  days_in_months_map = {
    1: 31,
    2: 29 if is_leap_year else 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
  }

  return days_in_months_map[month]

def get_day_no_in_year(date, month, year):
  day_number = 0

  counting_month = 1
  while (counting_month < month):
    day_number += get_days_in_month(counting_month, year)
    counting_month += 1

  day_number += date

  return day_number
  
def get_prev_date(date, month, year):
  if (date == 1):
    if (month == 1):
      return 31, 12, year-1
    
    return get_days_in_month(month - 1, year), month - 1, year

  return date - 1, month, year
  
def get_next_date(date, month, year):
  if (date == get_days_in_month(month, year)):
    if (month == 12):
      return 1, 1, year+1
    
    return 1, month + 1, year

  return date + 1, month, year
