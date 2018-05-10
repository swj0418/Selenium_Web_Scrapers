import konlpy
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.corpus import kolaw


def Analy_1(clist):
    M = kkm.pos(clist)
    for i in M:
        print(int(i[0][:1]))


kkm = Kkma()
lines = []

for line in open('A:/2018_Spring/QData/QData_1.txt', 'r', encoding="UTF-8"):
    lines.append(line)

for idx in range(100):
    Analy_1(lines[idx])



