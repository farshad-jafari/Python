def beautifier (hour,minute,second):
    """this function beautifies the representation of time in this way:
        it shows each component of time with two digits;)"""
    if second < 10:
            temp_s = '0'+str(second)
    else:
        temp_s = str(second)
    if minute < 10:
            temp_m = '0'+str(minute) #It is ok to have sth like this str('hey')
    else:
        temp_m = str(minute)
    if hour < 10:
            temp_h = '0'+str(hour)
    else:
        temp_h = str(hour)
    return temp_h, temp_m, temp_s
class time:
    def __init__ (arg,hour,minute,second):
        arg.hour = hour
        arg.minute = minute
        arg.second = second
    def show (arg):
        h, m, s = beautifier(arg.hour, arg.minute, arg.second)
        return h + ':' + m + ':' + s
    def __str__ (arg):
        h, m, s = beautifier(arg.hour, arg.minute, arg.second)
        return h + ':' + m + ':' + s
    def __repr__ (arg):
        h, m, s = beautifier(arg.hour, arg.minute, arg.second)
        return h + ':' + m + ':' + s
    def __add__ (self,other):
        temp_hour = self.hour + other.hour #at first we add all quantities then we decide which one to correct. similar in subtraction
        temp_minute = self.minute + other.minute
        temp_second = self.second + other.second
        if temp_second >= 60:
            temp_second -= 60
            temp_minute += 1
        if temp_minute >= 60:
            temp_minute -= 60
            temp_hour += 1
        if temp_hour >= 24:
            temp_hour -=24
        
        h, m, s = beautifier(temp_hour, temp_minute, temp_second)
        return h + ':' + m + ':' + s
    def __gt__ (self,other):
        self_total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        other_total_seconds = other.hour * 3600 + other.minute * 60 + other.second
        if self_total_seconds > other_total_seconds:
            return True
        else:
            return False
    def __eq__ (self,other):
        self_total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        other_total_seconds = other.hour * 3600 + other.minute * 60 + other.second
        if self_total_seconds == other_total_seconds:
            return True
        else:
            return False
    def __lt__ (self,other):
        self_total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        other_total_seconds = other.hour * 3600 + other.minute * 60 + other.second
        if self_total_seconds < other_total_seconds:
            return True
        else:
            return False
    def __sub__ (self,other):
        if self < other:
            print('error')
        else:
             temp_hour = self.hour - other.hour 
             temp_minute = self.minute - other.minute
             temp_second = self.second - other.second
             if temp_second < 0:
                 temp_second += 60
                 temp_minute -= 1
             if temp_minute < 0:
                 temp_minute += 60
                 temp_hour -= 1
             if temp_hour >= 24:
                 temp_hour -=24
             h, m, s = beautifier(temp_hour, temp_minute, temp_second)
             return h + ':' + m + ':' + s
        

        
