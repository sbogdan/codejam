#!/usr/bin/env python3
class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def solve(combine, oppose, invoke):
    comb = {}
    for c in combine:
        comb[(c[0], c[1])] = c[2]
        comb[(c[1], c[0])] = c[2]

    op = set()
    for o in oppose:
        op.add((o[0], o[1]))
        op.add((o[1], o[0]))

    st = []
    for i in invoke:
        st.append(i)
        # combine 
        if len(st) > 1 and (st[-1], st[-2]) in comb:
            st[-2:] = [comb[(st[-1], st[-2])]]
        # destroy
        if any([(x, st[-1]) in op for x in st]):
            st = []
    return repr(st).replace("'", "")


for _ in range(int(input())):
    datum = input().split()
    
    crt, x = 1, int(datum[0])
    combine = datum[crt:crt+x]
    crt, x = crt+x+1, int(datum[crt+x])
    oppose = datum[crt:crt+x]
    invoke = datum[crt+x+1]
    Mouth.answer(solve(combine, oppose, invoke))
