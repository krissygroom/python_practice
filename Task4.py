"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from Task1 import extract_numbers

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def create_non_marketer_list(call_list, text_list):
    # start with text list
    no_marketer_texts = extract_numbers(text_list)
    # get unique values
    no_marketer_texts = list(set(no_marketer_texts))
    print(no_marketer_texts)

    # get 2nd number from calls list - receiver number
    no_marketer_calls = get_receiver_num(call_list)
    print(no_marketer_calls)

    # combine lists
    no_marketers = no_marketer_texts + no_marketer_calls

    # not needed to be sorted here but am doing so to check test cases
    return list(sorted(set(no_marketers)))


def get_receiver_num(call_list):
    new_list = [item[1] for item in call_list]
    return list(set(new_list))


def test_cases():
    practice_texts = [['4545', '1234', '01-09-2016 06:03:22'],
                      ['4545', '5678', '01-09-2016 06:05:35'],
                      ['1234', '9999', '01-09-2016 06:05:35'],
                      ['1234', '9999', '01-09-2016 06:05:35'],
                      ['1234', '9999', '01-09-2016 06:05:35'],
                      ['1234', '9999', '01-09-2016 06:05:35']]

    practice_calls = [['801 375', '3333', '01-09-2016 06:01:12', '186'],
                      ['3333', '1234', '01-09-2016 06:01:59', '2093'],
                      ['9999', '1010', '01-09-2016 06:03:51', '1975'],
                      ['9999', '1010', '01-09-2016 06:03:51', '1975'],
                      ['9999', '1010', '01-09-2016 06:03:51', '1975'],
                      ['9999', '1010', '01-09-2016 06:03:51', '1975'],
                      ['2020', '1010', '01-09-2016 06:03:51', '1975']]

    return create_non_marketer_list(practice_calls, practice_texts)


print(test_cases())