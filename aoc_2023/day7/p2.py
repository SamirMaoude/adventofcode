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

DAY = 7
PART = 2
s = get_input(DAY).strip()

import collections
import math
import sys
sys.setrecursionlimit(10**9)
#import networkx as nx

CARDS = 'AKQT98765432J'

def maximize(hand, orig='', ind=0):

    if ind > 4 or not 'J' in hand : return rank(hand, orig)
    if hand[ind] != 'J' : return maximize(hand, orig, ind+1)


    mini = rank(hand, orig)
    tmp = list(hand)
    
    
    for x in CARDS:
        tmp[ind] = x
        mini = min(mini, maximize(''.join(tmp), orig, ind+1))

    return mini    

def hand_type(hand):
    s = set(hand)
    l = [hand.count(x) for x in s]
    l.sort(reverse=True)

    if l==[5]: return 0
        
    if l==[4,1]: return 1

    if l == [3, 2]: return 2

    if l == [3, 1 , 1] : return 3

    if l == [2, 2, 1]: return 4
    
    if l == [2, 1, 1, 1]: return 5

    return 6

def rank(hand, orig): return hand_type(hand) , *(CARDS.index(x) for x in orig )

# Your code here
ans = 0

hands = list(map(lambda x : (x.split()[0], int(x.split()[1])), s.splitlines()))
hands.sort(key=lambda x: maximize(x[0], x[0]), reverse=True)


for idx, hand in enumerate(hands):
    # print(hand[1], idx+1)
    ans += (idx+1) * hand[1]

# print(ans)
submit(DAY, PART, ans)