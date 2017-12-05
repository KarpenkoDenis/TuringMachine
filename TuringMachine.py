# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:35:23 2017

@author: Flame
"""
from enum import Enum
from colorama import Fore
#from colorama import init
#init(autoreset=False)

EMTY_SYMBOL = '*'

def paint(string, pointer):
    out = ""
    for i in range(len(string)):
        if i == pointer:
            out = out  + Fore.RED + string[i]  + Fore.RESET 
        else:
            out = out + string[i]
    return out 


class Tape:
    def __init__(self,tape): 
        self.tape= EMTY_SYMBOL + tape + EMTY_SYMBOL
        self.pointer=1    # указатель на крайний левый не пустой символ
    def __str__(self):
        return paint(self.tape, self.pointer)
    def change_curr_symbol(self, newS):
        self.tape = self.tape[:self.pointer] + newS  \
                             + (self.tape[self.pointer+1:] if self.pointer+1<len(self.tape) else "")
    def curr_symbol(self):
        return self.tape[self.pointer]
    def move_to(self, to):
        if Move.Right==to:
            self.pointer+=1
        if Move.Left==to:
            self.pointer-=1


class Move(Enum):
    Left=1
    Right=2
    Stay=3
    
class Q:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return 'q'+str(self.n)
    def __eq__(self, other):
        return self.n == other.n

class Rule:
    def __init__(self, Q, S, next_Q, next_S, pos):
        self.Q=Q
        self.S=S
        self.next_Q=next_Q
        self.next_S=next_S
        self.pos=pos
      
    def __str__(self):
        return  str(self.Q)  + ", " + self.S + " -> " + \
                str(self.next_Q)  + ", "  + self.next_S  + ", "  + str(self.pos.name)
                

class TuringMachine:
    def __init__(self, rules, curr_Q, final_Q): 
        self.rules= rules
        self.curr_Q= curr_Q
        self.final_Q= final_Q
    def __str__(self):
        out = ""
        for r in self.rules:
            out = out  + str(r) + '\n'
        return out
    def check(self, tape):
        print(tape, " - ", self.curr_Q )
        while self.curr_Q != self.final_Q:
#            print(self.curr_Q, '!=', self.final_Q)
            for r in self.rules:
#                print(r)
#                print("Сравнение: ", self.curr_Q, r.Q)
#                print("Сравнение: ", tape.curr_symbol(), r.S)
                if self.curr_Q == r.Q and tape.curr_symbol() == r.S:
                    tape.change_curr_symbol(r.next_S)
                    tape.move_to(r.pos)
                    self.curr_Q= r.next_Q
                    print(tape, " - ", self.curr_Q )
                    break
#                print("Сравнение: ", self.rules.index(r), self.rules[len(self.rules)-1])
                if r == self.rules[len(self.rules)-1]: # собственно вылeт, если вообще не нашли правил
                    return False
        return True





