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

DAY = 5
PART = 1
s = get_input(DAY).strip().splitlines()

import collections
import math
from pprint import pprint
#import networkx as nx

# Your code here
ans = 0
seeds = list(map(int, s[0].split(': ')[1].split()))



N = len(s)

i = 2
while i < N:
    
    i +=1
    changed = set()

    while i < N and len(s[i])>0:
        
        dest, source, ran = map(int, s[i].split())
        
        for idx, seed in enumerate(seeds):
            if source <= seed < source+ran and not idx in changed:
                changed.add(idx)
                seeds[idx] = dest+seed-source
        i += 1
    i += 1

ans = min(seeds)

# print(ans)
submit(DAY, PART, ans)