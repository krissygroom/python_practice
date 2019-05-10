"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


# add the seconds time to each of the numbers in the calls list
# this is how to get the key with the maximum value from the dictionary: max(dict, key=dict.get)
# create a function to do this:
def phone_durations(num_list):
    """Function creates dictionary that holds all the unique phone numbers and tallies the seconds
    Args:
        num_list: list of telephone call observations
    Returns:
        a dictionary of telephone numbers as key and aggregated seconds of the call as the value
    """
    # create empty defaultdict object
    num_dict = defaultdict(int)

    for num in num_list:
        num_dict[num[0]] += int(num[3])
        num_dict[num[1]] += int(num[3])

    return num_dict


def find_max_call(all_calls):
    """Function that calculates the maximum seconds from the calls dictionary
    Args:
        all_calls: list of telephone call observations
    Returns:
        the maximum number of seconds (int) and the phone number that made the longest call (str)
    """
    durations_dict = phone_durations(all_calls)
    max_number = max(durations_dict, key=durations_dict.get)
    max_seconds = durations_dict[max_number]
    return max_number, max_seconds


"""Answer to Task 1:
"""

longest_call_number = find_max_call(calls)
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(*longest_call_number))

