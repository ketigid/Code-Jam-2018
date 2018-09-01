# print('='*11)
import math

def round(x):
    if (x % 1 >= 0.5):
        return math.ceil(x)
    else:
        return math.floor(x)

def process(langs,to_go,idx,N,max_so_far):
    if not to_go:
        pct_ls = [round(lang/N*100) for lang in langs]
        print(pct_ls)
        pct_sum = sum(pct_ls)
        if pct_sum > max_so_far:
            return pct_sum
        else:
            return max_so_far
    else:
        print(list(set(langs)))
        for idx2 in list(set(langs)):
            langs2 = list(langs)
            langs2[langs2.index(idx2)] += 1
            max_so_far = process(langs2,to_go-1,idx2,N,max_so_far)
        return max_so_far

T = int(input())
for t in range(T):
    # print('case',t+1)
    N,L = list(map(int,input().split()))
    # print(N,L)
    C = list(map(int,input().split()))
    # print(C)

    num_responded = sum(C)
    # print('responded:',num_responded)
    num_not_responded = N - num_responded
    # print('not responded:',num_not_responded)

    ls = list(C) # make a copy
    for i in range(num_not_responded):
        ls.append(0)
    # print(C,ls)

    result = process(ls,num_not_responded,0,N,0)

    print('Case #{}: {}'.format(t+1,result)) # print result
