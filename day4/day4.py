input = open('./input.txt', 'r').read().split('\n')

def pt1():
    subsets = 0

    for pair in input:
        r1 = pair[:pair.index(',')]
        r2 = pair[pair.index(',')+1:]

        r1_list = list(range(int(r1[:r1.index('-')]), int(r1[r1.index('-') + 1:]) + 1, 1))
        r2_list = list(range(int(r2[:r2.index('-')]), int(r2[r2.index('-') + 1:]) + 1, 1))

        if set(r1_list) <= set(r2_list) or set(r2_list) <= set(r1_list):
            subsets += 1

    print(subsets)

def pt2():
    overlaps = 0

    for pair in input:
        r1 = pair[:pair.index(',')]
        r2 = pair[pair.index(',')+1:]

        r1_list = list(range(int(r1[:r1.index('-')]), int(r1[r1.index('-') + 1:]) + 1, 1))
        r2_list = list(range(int(r2[:r2.index('-')]), int(r2[r2.index('-') + 1:]) + 1, 1))

        if not set(r1_list).isdisjoint(r2_list):
            overlaps += 1

    print(overlaps)


if __name__ == '__main__':
    pt1()
    pt2()