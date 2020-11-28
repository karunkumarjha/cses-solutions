"""
Question Link: https://cses.fi/problemset/task/1068/
"""

def main():
	number = int(input())
	string = str(number) + ' '

	while number != 1:
		if number%2 == 0:
			number//=2
		else:
			number*=3
			number+=1
		string+=str(number) + ' '
	print(string)
		


if __name__ == '__main__':
	main()