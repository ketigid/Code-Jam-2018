print('='*11)
import math

def get(metal,resources,formulas):
    f1,f2 = formulas[metal]
    ok = 1
    if resources[f1-1] == 0:
        ok,resources = get(f1-1,resources,formulas)
    if ok<0:
        return ok
    if resources[f2-1] == 0:
        ok,resources = get(f2-1,resources,formulas)
    if ok<0:
        return ok
    resources[f1-1] -= 1
    resources[f2-1] -= 1
    resources[metal] += 1
    return ok,resources

T = int(input())
for t in range(T):
    print('case',t+1)
    M = int(input())
    print(M)
    R = []
    for m in range(M):
        R.append(list(map(int,input().split())))
    print(R)
    G = list(map(int,input().split()))
    print(G)

    g = list(G)
    ok,g = get(0,g,R)
    while(ok>0):
        ok,g = get(0,g,R)

    result = g[0]

    print('Case #{}: {}'.format(t+1,result)) # print result
