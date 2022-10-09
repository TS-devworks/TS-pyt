def seconds_difference(time_1, time_2):
    return time_2 - time_1    
    


def hours_difference(time_1, time_2):
    hr = time_2 - time_1
    diff_in_hr = hr / 3600
    return diff_in_hr



def to_float_hours(hours, minutes, seconds):
    return hours + (minutes / 60) + (seconds / 60 / 60)
    
def seconds_difference(time_1, time_2):
    return time_2 - time_1    
    


def hours_difference(time_1, time_2):
    hr = time_2 - time_1
    diff_in_hr = hr / 3600
    return diff_in_hr



def to_float_hours(hours, minutes, seconds):
    return hours + (minutes / 60) + (seconds / 60 / 60)



def to_24_hour_clock(hours):
    return hours % 24



### Write your get_hours function definition here:
def get_hours(sec): #from seconds to hours - working
    secnd = sec % (24 * 3600)
    hrs = secnd // 3600
    return hrs



### Write your get_minutes function definition here:
def get_minutes(sec): #from seconds to minutes - working
    return(sec % 3600) // 60



### Write your get_seconds function definition here:
def get_seconds(seconds):
    '''Returns remainer of seconds then converts to minutes'''
    return (seconds % 3600) % 60



def time_to_utc(utc_offset, time):
    return to_24_hour_clock(time - utc_offset)



def time_from_utc(utc_offset, time):
    return to_24_hour_clock(time + (utc_offset))





def to_24_hour_clock(hours):
    return hours % 24



### Write your get_hours function definition here:
def get_hours(sec): #from seconds to hours - working
    secnd = sec % (24 * 3600)
    hrs = secnd // 3600
    return hrs



### Write your get_minutes function definition here:
def get_minutes(sec): #from seconds to minutes - working
    return(sec % 3600) // 60



### Write your get_seconds function definition here:
def get_seconds(seconds):
    '''Returns remainer of seconds then converts to minutes'''
    return (seconds % 3600) % 60



def time_to_utc(utc_offset, time):
    return to_24_hour_clock(time - utc_offset)



def time_from_utc(utc_offset, time):
    return to_24_hour_clock(time + (utc_offset))



