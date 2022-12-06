input = open('./input.txt', 'r').read()

# A sincere fuck you to whoever wrote this problem
# Spent more time trying to interpret your problem than writing the actual code to solve it

def pt1():
    start_index = 0
    end_index = 4
    chars_processed = 4

    while end_index < len(input):
        str_slice = input[start_index:end_index]

        slice_set = ''.join(set(str_slice))

        if len(slice_set) == 4:
            print(chars_processed)
            break
        else:
            start_index += 1
            end_index += 1
            chars_processed += 1


def pt2():
    start_index = 0
    end_index = 14
    chars_processed = 14

    while end_index < len(input):
        str_slice = input[start_index:end_index]

        slice_set = ''.join(set(str_slice))

        if len(slice_set) == 14:
            print(chars_processed)
            break
        else:
            start_index += 1
            end_index += 1
            chars_processed += 1           
    

if __name__ == '__main__':
    # pt1()
    pt2()