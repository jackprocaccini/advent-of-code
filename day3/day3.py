input = open('./input.txt', 'r').read().split('\n')

LC_AMOUNT = 96
UC_AMOUNT = 38

def pt1():
    priorities_sum = 0

    for rucksack in input:
        firsthalf, secondhalf = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        fh_trimmed = ''.join(set(firsthalf))
        sh_trimmed = ''.join(set(secondhalf))

        for x in fh_trimmed:
            if x in sh_trimmed:
                priorities_sum += get_points_for_char(x)

    print(priorities_sum)

def pt2():
    priorities_sum = 0
    index = 0

    while index < len(input):
        fs, ss, ts = input[index:index+3]

        fs_trimmed = ''.join(set(fs))
        ss_trimmed = ''.join(set(ss))
        ts_trimmed = ''.join(set(ts))

        for c in fs_trimmed:
            if c in ss_trimmed and c in ts_trimmed:
                priorities_sum += get_points_for_char(c)

        index += 3


    print(priorities_sum)
                    

def get_points_for_char(x: str) -> int:
    
    if x.isupper():
        return ord(x) - UC_AMOUNT
    else:
        return ord(x) - LC_AMOUNT

if __name__ == '__main__':
    pt1()
    pt2()