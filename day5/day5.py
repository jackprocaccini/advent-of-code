input = open('./input.txt', 'r').read().split('\n')

stack_1 = ['N', 'R', 'G', 'P']
stack_2 = ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C']
stack_3 = ['M', 'S', 'V']
stack_4 = ['L', 'S', 'R', 'C', 'Z', 'P']
stack_5 = ['P','S','L','V','C','W','D','Q']
stack_6 = ['C','T','N','W','D','M','S']
stack_7 = ['H','G','D','W','P']
stack_8 = ['Z','L','P','H','S','C','M','V']
stack_9 = ['R','P','F','L','W','G','Z']

stack_map = {
    '1': stack_1,
    '2': stack_2,
    '3': stack_3,
    '4': stack_4,
    '5': stack_5,
    '6': stack_6,
    '7': stack_7,
    '8': stack_8,
    '9': stack_9
}

def pt1():
    for instruction in input:
        instr_list = instruction.split(' ')

        num_items = int(instr_list[1])
        from_stack = instr_list[3]
        to_stack = instr_list[len(instr_list) - 1]

        for x in range(num_items):
            item = stack_map.get(from_stack).pop()
            stack_map.get(to_stack).append(item)

    print_results()

def pt2():
    for instruction in input:
        instr_list = instruction.split(' ')

        num_items = int(instr_list[1])
        from_stack = stack_map.get(instr_list[3])
        to_stack = stack_map.get(instr_list[len(instr_list) - 1])

        items = from_stack[-num_items:]

        to_stack.extend(items)

        for x in range(num_items):
            from_stack.pop()

    print_results()

def print_results():
    final_str = ''
    for key in stack_map.keys():
        stack = stack_map.get(key)

        final_str += stack[len(stack) - 1]

    print(final_str)    


if __name__ == '__main__':
    # pt1()
    pt2()