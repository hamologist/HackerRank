import fileinput

time_ref = {
    1:  'one',
    2:  'two',
    3:  'three',
    4:  'four',
    5:  'five',
    6:  'six',
    7:  'seven',
    8:  'eight',
    9:  'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

def check_hour(H):
    return (H+1)%12 if H != 11 else 1

def pretty_minutes(M):
    normal_ref = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty'
    }
    if M in time_ref:
        return time_ref[M]
    else:
        ones = M % 10
        tens = (M - ones) / 10
        if ones != 0:
            return "{0} {1}".format(normal_ref[tens], time_ref[ones])
        else:
            return "{0}".format(normal_ref[tens])

def gen_time_string(H, M):

    if M == 0:
        time = "{hour} o' clock".format(hour=time_ref[H])
    elif M == 1:
        time = "one minute past {hour}".format(hour=time_ref[H], minute=pretty_minutes(M))
    elif M == 15:
        time = "quarter past {hour}".format(hour=time_ref[H])
    elif M < 30:
        time = "{minutes} minutes past {hour}".format(hour=time_ref[H], minutes=pretty_minutes(M))
    elif M == 30:
        time = "half past {hour}".format(hour=time_ref[H])
    elif M == 45:
        time = "quarter to {hour}".format(hour=time_ref[check_hour(H)])
    elif M == 59:
        time = "one minute to {hour}".format(hour=time_ref[check_hour(H)])
    else:
        time = "{minutes} minutes to {hour}".format(hour=time_ref[check_hour(H)], minutes=pretty_minutes(60-M))

    return time

H, M = [int(num.strip()) for num in fileinput.input()]
print(gen_time_string(H, M))
