MOST_CALS = 70296
SECOND_MOST_CALS = 68707
THIRD_MOST_CALS = 66378

total = MOST_CALS + SECOND_MOST_CALS + THIRD_MOST_CALS
print('TOTAL CALS: {}'.format(total))


# input = open("input.txt", "r").read()

# input_trimmed = input.replace('\n', ',').split(',,')
# # input_trimmed = input.split('\n\n')

# # print(input_trimmed)

# max_cals = 0
# local_max_cals = 0
# for group in input_trimmed:
#     strs_as_nums = group.split(',')

#     for num in strs_as_nums:
#         local_max_cals += int(num)
    
#     if local_max_cals > max_cals and local_max_cals < MOST_CALS and local_max_cals < SECOND_MOST_CALS:
#         max_cals = local_max_cals

#     local_max_cals = 0

# print('ANSWER: {}'.format(max_cals))