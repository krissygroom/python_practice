"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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


def extract_call_numbers(call_list):
    """Extracts the numbers and seconds from the call list
    Args:
        call_list: full list of calls
    Returns:
        a new list of individual phone numbers with seconds
    """
    call_ex1 = [(call[0], call[3]) for call in call_list]
    call_ex2 = [(call[1], call[3]) for call in call_list]
    return call_ex1 + call_ex2


# ok so now just need to add the seconds time to each of the numbers in the calls list
# this is how to get the key with the maximum value from the dictionary: max(dict, key=dict.get)
# create a function to do this:
def phone_durations(num_list):
    """Function creates dictionary that holds all the unique phone numbers and tallies the seconds
    Args:
        num_list: list of telephone call observations
    Returns:
        a dictionary of telephone numbers as key and aggregated seconds of the call as the value
    """
    # create empty dictionary
    num_dict = {}
    # iterate through the number list and the seconds and add each phone number with the amount of seconds
    # to the dictionary if it is not in the dictionary.
    # if it is in the dictionary, then just add the seconds to its value
    for i in range(len(num_list)):
        seconds = int(num_list[i][1])
        number = num_list[i][0]
        if number not in num_dict:
            num_dict[number] = seconds
        else:
            num_dict[number] += seconds
    return num_dict


def find_max_call(all_calls):
    """Function that calculates the maximum seconds from the calls dictionary
    Args:
        all_calls: list of telephone call observations
    Returns:
        the maximum number of seconds (int) and the phone number that made the longest call (str)
    """
    call_list = extract_call_numbers(all_calls)
    durations_dict = phone_durations(call_list)
    max_number = max(durations_dict, key=durations_dict.get)
    max_seconds = durations_dict[max_number]
    return max_number, max_seconds


# practice_calls = [['801 375', '3333', '01-09-2016 06:01:12', '186'],
#                   ['3333', '1234', '01-09-2016 06:01:59', '2093'],
#                   ['9999', '1010', '01-09-2016 06:03:51', '1975']]
#
#
# list_example = [('801 375', '186'), ('3333', '2093'), ('9999', '1975'), ('3333', '186'), ('1234', '2093'),
#                 ('1010', '1975')]
#
# print(phone_durations(list_example))
#
# print(find_max_call(practice_calls))

"""Answer to Task 1:
"""

longest_call_number = find_max_call(calls)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_call_number[0],
                                                                                          longest_call_number[1]))

