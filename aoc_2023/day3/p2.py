# Advent of Code template by @MathisHammel

import requests
from functools import reduce

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

DAY = 3
PART = 2
s = get_input(DAY).strip()

import collections
import math
#import networkx as nx

# Your code here
ans = 0



L = s.splitlines()

N, M = len(L), len(L[0])

DIR = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def get_gears(i, j):

    gears = set()

    for d in DIR:

        a, b = i + d[0], j + d[1]

        if 0 <= a < N and 0 <= b < M:

            if L[a][b].isdigit():

                gear = L[a][b]

                x = b-1

                while 0<=x:
                    if L[a][x].isdigit():
                        gear = L[a][x] + gear
                        x -= 1
                    else: break

                x = b + 1 

                while x < M:
                    if L[a][x].isdigit():
                        gear += L[a][x]
                        x += 1
                    else: break

                gears.add(int(gear))


    return reduce( lambda x, y: x*y, gears) if len(gears) == 2  else 0




i = 0
for i in range(N):
    for j in range(M):
        if L[i][j] == '*': 
            ans += get_gears(i, j)





# print(ans)
submit(DAY, PART, ans)