# print('='*11)
import math

T = int(input())
for t in range(T):
    # print('case',t+1)
    D,P = input().split()
    D = int(D)
    # print('D',D)
    # print('P',P)

    S = 1 # damage of 1 S
    reduction = 0 # damage reduction by next hack
    total_damage = 0 # total damage of P
    possible_reduction = {} # dict of damage reductions possible based on position of all S in P
    for p in P:
        # print(p)
        if p == 'C':
            reduction = S # S damage reduction is now possible after this C
            S *= 2 # damage of 1 S is double after this C
        elif p == 'S':
            total_damage += S # track total damage
            if reduction in possible_reduction: # check if key exists
                possible_reduction[reduction] += 1 # increment the counts of this reduction
            elif reduction: # check if reduction is not zero
                possible_reduction[reduction] = 1 # create a key for reduction with count 1
    # print('total_damage',total_damage)
    # print('possible_reduction',possible_reduction)

    damage_to_reduce = total_damage - D # compute min damage to reduce
    result = 0
    while damage_to_reduce > 0: # while we still have damage to reduce
        # print('damage_to_reduce',damage_to_reduce)
        # print('possible_reduction',possible_reduction)
        if not possible_reduction: # check if possible reduction is empty
            result = -1 # IMPOSSIBLE
            break
        max_key = max(possible_reduction) # find maximum key
        # print('max_key',max_key)
        this_reduction = max_key * possible_reduction[max_key] # max reduction possible by moving all S in this section below the previous C
        # print('this_reduction',this_reduction)
        if this_reduction >= damage_to_reduce: # if this is enough to meet our goal
            result += math.ceil(damage_to_reduce / max_key) # accumulate just enough to meet our goal
            damage_to_reduce -= this_reduction # update our goal, it should be negative now, therefore break out of while loop
        else: # if this is not enough to meet our goal
            result += possible_reduction[max_key] # accumulate the number of hacks
            damage_to_reduce -= this_reduction # reduced our goal by the amount of damage prevented
            new_key = max_key // 2 # all these S should move down to the previous section, compute the key
            if new_key in possible_reduction: # check if key exists
                possible_reduction[new_key] += possible_reduction[max_key] # increment the counts of this reduction
            elif new_key: # check if key is not zero
                possible_reduction[new_key] = possible_reduction[max_key] # create a key for reduction with count 1
            possible_reduction.pop(max_key) # pop the key that was used up
        # print('possible_reduction',possible_reduction)

        # damage_to_reduce = 0

    print('Case #{}: {}'.format(t+1,result if result >= 0 else 'IMPOSSIBLE'))
