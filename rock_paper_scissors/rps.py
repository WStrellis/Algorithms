#!/usr/bin/python

import sys

# length of returned list is n**3


# def calc_permutations(n, word, combo=None):
#     if combo == None:
#         combo = []
#     if len(combo) == n:
#         return combo
#     else:
#         combo.append(word)
#         r = calc_permutations(n, 'rock', combo)
#         p = calc_permutations(n, 'paper', combo)
#         s = calc_permutations(n, 'scissors', combo)
#         return [r, p, s]


# def rock_paper_scissors(n):
#     return [calc_permutations(n, x) for x in ['rock', 'paper', 'scissors']]

def calc_permutations(n, word, master, previous=None):
    if previous == None:
        previous = []
    new_arr = previous[:]
    new_arr.append(word)
    if len(new_arr) == n:
        master.append(new_arr)
        return
    else:
        calc_permutations(n, 'rock', master, new_arr)
        calc_permutations(n, 'paper', master, new_arr)
        calc_permutations(n, 'scissors', master, new_arr)


def rock_paper_scissors(n):
    master = []
    if n == 0:
        return [master]
    else:
        calc_permutations(n,  'rock', master,)
        calc_permutations(n, 'paper', master)
        calc_permutations(n, 'scissors', master)
    return master


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
