# print('='*11)
T = int(input())
# print('T',T)
for t in range(T):
    ln = input().split()
    N,K = [int(l) for l in ln]
    # print('N',N)
    # print('K',K)

    spaces = {N:1}

    k = K
    while(k>0):
        max_space_key = max(spaces.keys())
        max_space_value = spaces[max_space_key]
        spaces.pop(max_space_key)
        K_left = (max_space_key - 1) // 2
        if K_left in spaces:
            spaces[K_left] += max_space_value
        else:
            spaces[K_left] = max_space_value
        K_right = max_space_key // 2
        if K_right in spaces:
            spaces[K_right] += max_space_value
        else:
            spaces[K_right] = max_space_value
        k -= max_space_value

    # slow way
    # for k in range(K):
    #     max_space_key = max(spaces.keys())
    #     max_space_value = spaces[max_space_key]
    #     if spaces[max_space_key] == 1:
    #         spaces.pop(max_space_key)
    #     else:
    #         spaces[max_space_key] -= 1
    #     K_left = (max_space_key - 1) // 2
    #     if K_left in spaces:
    #         spaces[K_left] += 1
    #     else:
    #         spaces[K_left] = 1
    #     K_right = max_space_key // 2
    #     if K_right in spaces:
    #         spaces[K_right] += 1
    #     else:
    #         spaces[K_right] = 1

    print('Case #{}: {} {}'.format(t+1,max(K_left,K_right),min(K_left,K_right)))

# print('exited')