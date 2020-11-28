"""
Question Link: https://cses.fi/problemset/task/1083
"""

def main():
	limit = int(input())
	numbers = [int(number) for number in input().split(' ')]
	xor = 0
	for number in range(1,limit+1):
		xor^=number
	for number in numbers:
		xor^=number
	print(xor)

if __name__ == '__main__':
	main()