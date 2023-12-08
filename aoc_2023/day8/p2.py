# Advent of Code template by @MathisHammel

import requests

from ..secrets.aoc_secrets import AOC_COOKIE # Put your session cookie in this variable
YEAR = '2023'

def get_input(day):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}/input', headers={'cookie':'session='+AOC_COOKIE})
    return req.text

def get_example(day,offset=0):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}', headers={'cookie':'session='+AOC_COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]

def submit(day, level, answer):
    input(f'You are about to submit the follwing answer:\n>>>>>>>>>>>>>>>>> {answer}\nPress enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer', headers={'cookie':'session='+AOC_COOKIE}, data=data)
    if 'You gave an answer too recently' in response.text:
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        print('VERDICT : INVALID LEVEL')
    else:
        print('VERDICT : OK !')

def ints(s):
    return list(map(int, s.split()))

DAY = 8
PART = 2
s = get_input(DAY).strip().splitlines()




import collections
import math
import sys
sys.setrecursionlimit(10**9)
#import networkx as nx

# Your code here

NETWORK = {}
nodes = []
for i in range(2, len(s)):
    node, elem = s[i].split(' = ')
    NETWORK[node] = elem[1:-1].split(', ')
    if node[-1] == 'A':
        nodes.append(node)



D = {'L': 0, 'R': 1}
MOVES  = s[0]



ans = 1


for node in nodes:
    res = 0
    while node[-1]!= 'Z':
        d = MOVES[res%len(MOVES)]
        node = NETWORK[node][D[d]]
        res += 1
    
    ans = math.lcm(ans, res)

submit(DAY, PART, ans)