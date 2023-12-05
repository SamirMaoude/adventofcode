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
PART = 2
s = get_input(DAY).strip().splitlines()

import collections
import math
from pprint import pprint
#import networkx as nx

def intersection(a, b): return max(a[0], b[0]), min(a[1], b[1])

# Your code here
ans = 0

pairs = list(map(int, s[0].split(': ')[1].split()))


seeds = []
for i in range(0, len(pairs), 2): seeds += [(pairs[i], pairs[i]+pairs[i+1]-1)]



N = len(s)

i = 2
while i < N:

    i +=1
    changed = set()

    while i < N and len(s[i])>0:
        
        dest, source, ran = map(int, s[i].split())
        idx = 0

        while idx <len(seeds):
            # print(idx, seeds, changed)
            seed = seeds[idx]
            inter = intersection((source, source+ran-1), seed)

            if inter[0] <= inter[1] and not seed in changed:
                v = dest+inter[0]-source, dest+inter[1]-source
                changed.add(v)

                if inter == seed:
                    seeds[idx] = v
                else:
                    ok = False
                    if seed[0] <= inter[0] - 1:
                        ok = True
                        seeds +=  [(seed[0], inter[0] - 1)]

                    if inter[1] + 1 <= seed[1]:
                        ok = True
                        seeds += [(inter[1] + 1, seed[1])]
                    if ok:
                        seeds.pop(idx)
                        idx -= 1
            idx += 1

        i += 1
    
    seeds = list(set(seeds).union(changed))
    
    i += 1


seeds.sort()

ans = seeds[0][0]
submit(DAY, PART, ans)