from itertools import product
suit = ['пик', 'треф', 'бубен', 'червей']
suit.remove(input())

value = ['2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10 ', 'валет ', 'дама ', 'король ', 'туз ']


print(*[i[0] + i[1] for i in product(value, suit)], sep='\n')
# OK
