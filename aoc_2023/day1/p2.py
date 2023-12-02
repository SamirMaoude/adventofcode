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

DAY = 1
PART = 2
s = get_input(DAY).strip()

import collections
import math
from collections import defaultdict
#import networkx as nx

# Your code here



def process(s):
    
    d = defaultdict(lambda x: x,{
        'oneight': '18',
        'twone': '21',
        'threeight': '38',
        'fiveight': '58',
        'sevenine': '79',
        'eightwo': '82',
        'eighthree': '83',
        'nineight': '98',
        'one' : '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    })

    for x in list(d.keys()):
        s=s.replace(x, d[x])
    return s

ans = 0
for line in s.splitlines():
    l = [x  for x in process(line.lower()) if x.isdigit()]
    ans += int(l[0]) * 10 + int(l[-1])
   

submit(DAY, PART, ans)