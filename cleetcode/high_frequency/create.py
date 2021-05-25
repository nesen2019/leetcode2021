import os
from cleetcode import HandleAddPlan

lst = [
    2
]

if __name__ == '__main__':
    for i in lst:
        hap = HandleAddPlan()
        hap.add_problem01(str(i))
