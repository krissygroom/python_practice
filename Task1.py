"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import numpy as np
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


# # first combine the two lists for easier use
# def combine_lists(call_list, text_list):
#     """Function to combine two lists of call or text observations"""
#     return call_list + text_list
#
#
# # extract the first and second items of each call/text in the combined list
# def extract_numbers(numbers_list):
#     """Function that extracts the telephone numbers from a list"""
#     new_list1 = [item[0] for item in numbers_list]
#     new_list2 = [item[1] for item in numbers_list]
#     return new_list1 + new_list2
#
#
# # implement the number of different telephone numbers function
# def count_unique_numbers(call_list, text_list):
#     """Function that performs the calculations for finding unique numbers in a list
#     Args:
#         call_list: list of telephone call observations
#         text_list: list of text message observations
#     Returns:
#         An int representing the number of unique telephone numbers in both records
#     """
#     lists_combined = combine_lists(call_list, text_list)
#     all_numbers = extract_numbers(lists_combined)
#
#     # convert all_numbers into numpy array
#     all_numbers = np.asarray(all_numbers)
#     num_unique = np.unique(all_numbers)
#
#     return len(num_unique)


# much better approach as suggested by Udacity reviewer!
# I definitely overcomplicated it in above code, plus is faster in below code.
def approach_2(calls, texts):
    records = set()
    for i in range(len(calls)):
        records.add(calls[i][0])
        records.add(calls[i][1])
    for i in range(len(texts)):
        records.add(texts[i][0])
        records.add(texts[i][1])
    return len(records)


"""Answer to Task 1:
"""
print("There are {0} different telephone numbers in the records.".format(approach_2(calls, texts)))

# unique_numbers = count_unique_numbers(calls, texts)
# print("There are {} different telephone numbers in the records!".format(unique_numbers))



