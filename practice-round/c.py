# print('='*11)
T = int(input())
for t in range(T):
    ln = input().split()
    D,N = [int(l) for l in ln]
    K,S = [],[]
    for _ in range(N):
        ln = input().split()
        k,s = [int(l) for l in ln]
        K.append(k)
        S.append(s)
    # print(K,S)
    times = [(D-k)/s for k,s in zip(K,S)]
    # print(times)
    time = max(times)
    # print(time)
    result = D / time
    print('Case #{}: {}'.format(t+1,result))