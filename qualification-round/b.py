# print('='*11)

T = int(input())
for t in range(T):
    # print('case',t+1)
    N = int(input())
    V = input().split()
    V = [int(v) for v in V]
    # print('N',N)
    # print('V',V)

    even = V[::2] # extract even indices
    odd = V[1::2] # extract odd indices
    # print('even',even)
    # print('odd',odd)

    even_sorted = sorted(even) # sort it, assume sort is O(n log n)
    # print('even_sorted',even_sorted)
    odd_sorted = sorted(odd) # sort it, assume sort is O(n log n)
    # print('odd_sorted',odd_sorted)
    
    V[::2] = even_sorted # reconstruct V
    V[1::2] = odd_sorted # reconstruct V
    # print('V',V)

    result = -1 # default to OK
    for i in range(len(V)-1): # iterate from front
        if V[i] > V[i+1]: # definition based on question, if current is larger than next element
            result = i # result is this index
            break

    print('Case #{}: {}'.format(t+1,result if result >= 0 else 'OK'))
