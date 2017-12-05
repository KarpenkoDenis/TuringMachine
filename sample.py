# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:32:45 2017

@author: Flame
"""



from main import check

"""
from TuringMachine import Rule, Q, Move, TuringMachine, Tape
from TuringMachine import EMTY_SYMBOL as empty
# тест на машине, которая заменяет все единички на нолики
r1 = Rule(Q(1),'1',Q(1),'0', Move.Right)
r2 = Rule(Q(1),empty,Q(2),empty, Move.Stay)
print(TuringMachine([r1, r2], Q(1), Q(2)))
t1000 = TuringMachine([r1, r2], Q(1), Q(2))
print( "Right" if t1000.check(Tape('11111')) else "Wrong")

# правила для задания из ИДЗ8 под номером 3"""



check('101, 11111')