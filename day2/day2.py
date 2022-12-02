enemy_key = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scizzors'
}

player_key = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scizzors'
}

points_key_move = {
    'Rock': 1,
    'Paper': 2,
    'Scizzors': 3
}

points_key_outcome = {
    'win': 6,
    'draw': 3,
    'loss': 0
}

some_map = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
}

def pt2():
    total = 0
    rounds = open('./input.txt', 'r').readlines()

    # print(rounds)

    for round in rounds:
        # print('---------------------------------')
        round_trim = round.replace('\n', '').split(' ')
        # print(round_trim)

        enemy_move = enemy_key.get(round_trim[0])
        outcome = some_map.get(round_trim[1])

        player_move = calculate_player_move(outcome=outcome, enemy_move=enemy_move)

        round_points = calculate_round_points(outcome=outcome, player_move=player_move)
        # print('Round points: {}'.format(round_points))

        total += round_points
        # print('Total points after round: {}'.format(total))
        # print('---------------------------------')        

    print('TOTAL POINTS: {}'.format(total))    

def calculate_player_move(outcome: str, enemy_move: str) -> str:
    if outcome == 'win':
        if enemy_move == 'Rock':
            return 'Paper'
        elif enemy_move == 'Paper':
            return 'Scizzors'
        else:
            return 'Rock'

    elif outcome == 'loss':
        if enemy_move == 'Rock':
            return 'Scizzors'
        elif enemy_move == 'Paper':
            return 'Rock'
        else:
            return 'Paper'
    else:
        return enemy_move

def pt1():
    total = 0
    rounds = open('./input.txt', 'r').readlines()

    # print(rounds)

    for round in rounds:
        # print('---------------------------------')
        round_trim = round.replace('\n', '').split(' ')
        # print(round_trim)

        enemy_move = enemy_key.get(round_trim[0])
        player_move = player_key.get(round_trim[1])

        outcome = calculate_outcome(enemy_move=enemy_move, player_move=player_move)
        # print('Outcome of round for player: {}'.format(outcome))

        round_points = calculate_round_points(outcome=outcome, player_move=player_move)
        # print('Round points: {}'.format(round_points))

        total += round_points
        # print('Total points after round: {}'.format(total))
        # print('---------------------------------')

    print('TOTAL POINTS: {}'.format(total))

def calculate_outcome(enemy_move: str, player_move: str) -> str:
    # print('Enemy plays {}, player throws {}'.format(enemy_key.get(enemy_move), player_key.get(player_move)))

    if enemy_move == 'Rock': # rock
        if player_move == 'Rock':
            return 'draw'
        elif player_move == 'Paper':
            return 'win'
        else:
            return 'loss'

    elif enemy_move == 'Paper': # paper
        if player_move == 'Rock':
            return 'loss'
        elif player_move == 'Paper':
            return 'draw'
        else:
            return 'win'

    else: # scizzors
        if player_move == 'Rock':
            return 'win'
        elif player_move == 'Paper':
            return 'loss'
        else:
            return 'draw'

def calculate_round_points(outcome: str, player_move: str) -> int:
    # print("outcome: {}, player_move: {}".format(outcome, player_move))
    return points_key_outcome.get(outcome) + points_key_move.get(player_move)

if __name__ == '__main__':
    # pt1()
    pt2()