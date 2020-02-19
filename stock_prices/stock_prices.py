#!/usr/bin/python

import argparse
import math

# if prices[outer_index] > prices[inner_index]:


def find_max_profit(prices):
    max_diff = -math.inf
    outer_index = len(prices) - 1
    while outer_index > 0:
        inner_index = outer_index - 1
        while inner_index > -1:
            price_diff = prices[outer_index] - prices[inner_index]
            if price_diff > max_diff:
                max_diff = price_diff
            inner_index -= 1
        outer_index -= 1
    return max_diff


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
