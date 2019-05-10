"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import numpy as np

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def find_bangalore_calls_list(call_list):
    """Function that finds all the area codes from bangalore (080) callers as a list
    Args:
        call_list: list of all telephone call observations
    Returns:
        list of all area codes of receivers of bangalore calls
    """
    # empty list to hold all calls from bangalore
    bangalore_calls = []

    for i in range(len(call_list)):
        # check if first phone number is from bangalore:
        if call_list[i][0][:5] == '(080)':
            # if yes, add receiver to the list
            # first split and add the first part
            if call_list[i][1][0] == '(':
                # add it to the list
                area_code = call_list[i][1].strip('(').split(')')
                bangalore_calls.append(area_code[0])
            elif call_list[i][1][:3] == '140':
                bangalore_calls.append('140')
            else:
                area_code = call_list[i][1].split(' ')
                bangalore_calls.append(area_code[0][:4])

    return bangalore_calls


def find_bangalore_calls_unique(call_list):
    """Function that returns a sorted list of only the unique phone numbers who received calls from bangalore
    Args:
        call_list: list of all bangalore calls
    Returns:
        list of unique numbers who received calls from bangalore in lexicographic order
        """
    bangalore_set = set(find_bangalore_calls_list(call_list))
    return list(sorted(bangalore_set))


def percent_called(call_list):
    """Function that returns the percentage of calls received from bangalore that are also from bangalore
    Args:
        call_list: list of all telephone call observations
    Returns:
        the percentage of callers that were from bangalore that received a call from a bangalore number
        """
    # get all bangalore calls
    lst = find_bangalore_calls_list(call_list)
    # create numpy array for easy calculation
    lst = np.array(lst)
    num_calls = len(lst)
    # print(num_calls)
    bangalore_calls = (lst == '080').sum()
    # print(bangalore_calls)
    return round((bangalore_calls / num_calls) * 100.0, 2)


def print_calls(call_list):
    """Function that prints out each item in a call_list"""
    for i in call_list:
        print(i)


"""Task 3, Part A answer"""

unique_calls = find_bangalore_calls_unique(calls)

print("The numbers called by people in Bangalore have codes:")
print_calls(unique_calls)

"""Task 3, Part B answer"""

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      .format(percent_called(calls)))










