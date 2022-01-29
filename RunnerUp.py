'''

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

'''

num = int(input())
scores = list(map(int, input().split(' ')))
winner = max(scores)
lst = []

if len(scores) != num:
    print('length of score is greater than input given')
else:
    for score in scores:
	if winner > score:
	    lst.append(score)

runnerup = max(lst)
print(runnerup)
