# print('='*11)
import math

T = int(input())
for t in range(T):
    # print('case',t+1)
    N,P = list(map(int,input().split()))
    # print(N,P)

    cookies = []
    P_base = 0
    for n in range(N):
        W,H = list(map(int,input().split()))
        cookie = {}
        cookie['W'] = W # int
        cookie['H'] = H # int
        cookie['diag'] = math.sqrt(W*W+H*H)
        cookie['theta_bar'] = math.atan(H/W)
        cookie['perimeter'] = 2*(W+H) # int
        P_base += cookie['perimeter']
        cookie['R'] = 2*cookie['diag'] # max perimeter that can be introduced by cutting
        cookie['L'] = 2*min(W,H) # int; min perimeter that can be introduced by cutting
        cookies.append(cookie)
    P_to_go = P - P_base
    # print('P_to_go',P_to_go)

#              L|0|1|2|3|...
# --------------|-|-|-|-|...
# cookie0{L0,R0}|0|*|*|*|...
# cookie1{L1,R1}|0|*|*|*|...
# cookie2{L2,R2}|0|*|*|*|...

    # # attempt to do dynamic programming
    # table = [[(0,0) for _ in range(P_to_go+1)] for _ in range(N)] # initialize table to all 0's
    # for i in range(N): # iterate over number of cookies
    #     for j in range(1,P_to_go+1): # iterate over P_to_go
    #         if i == 0: # first cookie
    #             if cookies[i]['L'] <= j:
    #                 l = cookies[i]['L']
    #                 r = cookies[i]['R']
    #                 table[i][j] = (l,r) # storing as a tuple to track L used up to this element
    #         else: # subsequent cookies
    #             if cookies[i]['L'] <= j: # check if this cookie can be cut
    #                 # compute (l1,r1)
    #                 l1 = cookies[i]['L']
    #                 r1 = cookies[i]['R']
    #                 if (j-l) >= 0: # check if index exists in previous row
    #                     tl,tr = table[i-1][j-l] # retrieve values
    #                     l1 += tl # add to l1
    #                     r1 += tr # add to r1
    #                 # compute (l2,r2); this is just the value directly above
    #                 l2,r2 = table[i-1][j]
    #                 # compare (l1,r1) and (l2,r2)
    #                 if r1 > r2: # if set 1 has higher value
    #                     table[i][j] = (l1,r1)
    #                 elif r1 < r2: # if set 2 has higher value
    #                     table[i][j] =  (l2,r2)
    #                 elif l1 > l2: # values are equal, if set 2 is lighter
    #                     table[i][j] =  (l2,r2)
    #                 elif l1 < l2: # values are equal, if set 1 is lighter
    #                     table[i][j] = (l1,r1)
    #                 else: # both value and weight equal, choose set 1
    #                     table[i][j] = (l1,r1)
    #             else:
    #                 table[i][j] = table[i][j-1] # just get the value on the left

    # # for ele in table:
    # #     print(ele)

    # l,r = table[-1][-1] # get bottom right corner value
    # result = P_base + (r if r < P_to_go else P_to_go) # add value to P_base if value is less than P_to_go



    # attempting dynamic programming recursively
    import functools
    @functools.lru_cache(maxsize=2^32)
    def table(i,j):
        # terminating condition
        if j == 0 or i < 0:
            return 0

        # retrieve info for this cookie
        l = cookies[i]['L']
        r = cookies[i]['R']
        if l <= j:
            a = r + table(i-1,j-l)
            b = table(i-1,j)
            return max(a,b)
        else:
            return table(i,j-1)

    v = table(N-1,P_to_go+1)
    result = P_base + (v if v < P_to_go else P_to_go)

    print('Case #{}: {}'.format(t+1,result))

