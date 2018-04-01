# import numpy as np
import string

# print('='*11)
T = int(input())
# print('T =',T)
for t in range(T):
    N = int(input())
    # print('N =',N)
    senators = input().split()
    senators = [int(s) for s in senators]
    # senators = np.array(senators)
    party = string.ascii_uppercase[:N]
    # print('party',party)

    result = []
    # # numpy version
    # while(senators.sum()):
    #     # print('senators1',senators)
    #     first_index = senators.argmax()
    #     # print(first_index)
    #     senators[first_index] -= 1
    #     # print('senators2',senators)
    #     second_index = senators.argmax()
    #     # print(second_index)
    #     senators[second_index] -= 1
    #     # print('senators3',senators)
    #     remaining = sum(senators) or 1
    #     percentage = senators / remaining
    #     # print('percentage',percentage)
    #     majority = (percentage > 0.5).any()
    #     # print('majority',majority)
    #     if majority:
    #         senators[second_index] += 1
    #         result.append(party[first_index])
    #     else:
    #         result.append(party[first_index]+party[second_index])
    #     # print('result',result)

    # vanilla version
    while(sum(senators)):
        # print('senators1',senators)
        first_index = senators.index(max(senators))
        # print(first_index)
        senators[first_index] -= 1
        # print('senators2',senators)
        second_index = senators.index(max(senators))
        # print(second_index)
        senators[second_index] -= 1
        # print('senators3',senators)
        remaining = sum(senators) or 1
        percentage = [s/remaining for s in senators]
        # print('percentage',percentage)
        majority = False
        for p in percentage:
            if p > 0.5:
                majority = True
                break
        # print('majority',majority)
        if majority:
            senators[second_index] += 1
            result.append(party[first_index])
        else:
            result.append(party[first_index]+party[second_index])
        # print('result',result)


    # print('exit while')
    print('Case #{}: {}'.format(t+1,' '.join(result)))