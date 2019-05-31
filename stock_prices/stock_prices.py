#!/usr/bin/python

import argparse

def find_max_profit(prices):
# need a high an a low for a sale
# buy before sell
# find the max difference = high - low
	max = None
	low = prices[0]
	high = prices[0]
	for p in prices:
		if p > low:
			low = p
			high = None
		if high is None or p > high:
			high = p
		if max is None or high - low > max:
			max = high - low
	return max

if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))