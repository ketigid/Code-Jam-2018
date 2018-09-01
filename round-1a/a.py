print('='*11)
import math

T = int(input())
for t in range(T):
    # print('case',t+1)
    R,C,H,V = list(map(int,input().split()))
    # print(R,C,H,V)

    # create the waffle matrix
    waffle = []
    for r in range(R):
        ln = input() # read a line
        ln2 = [1 if ele == '@' else 0 for ele in ln] # convert to 1's and 0's
        waffle.append(ln2)
    # print(waffle)

    # iterate through the rows to compute sums
    row_sum = []
    for r in range(R):
        s = sum(waffle[r][:]) # sum of row
        row_sum.append(s) # track the sum of each row
    row_sum_sum = sum(row_sum) # track the total number of chips
    # print(row_sum_sum)

    # transpose the waffle matrix
    waffle_T = [[1 if waffle[r][c] else 0 for r in range(R)] for c in range(C)]

    # iterate through the cols to compute sums
    col_sum = []
    for c in range(C):
        s = sum(waffle_T[c][:]) # sum of col
        col_sum.append(s) # track the sum of each col
    col_sum_sum = sum(col_sum) # track the total number of chips, should be same as row_sum_sum
    # print(col_sum_sum)

    result = -1 # initialize the result to IMPOSSIBLE
    row_chips = row_sum_sum // (H+1) # integer division to find number of chips per waffle row section
    # print('row_chips',row_chips)
    
    if row_sum_sum == 0 and col_sum_sum == 0: # edge case of zero chips
        result = 1 # POSSIBLE
    elif row_sum_sum % (H+1) != 0 or col_sum_sum % (V+1) != 0: # if either H or V cuts results in non-integer value
        result = -1 # IMPOSSIBLE
    else: # otherwise start iterations
        row_flag = True # validity flag for row
        col_flag = True # validity flag for col
        count = 0 # count number of chips so far in this cut
        row_cuts = [0] # track index of row cuts
        for idx in range(len(row_sum)): # iterate through row sum
            count += row_sum[idx] # increment count by row sum element
            if count > row_chips: # if count exceeds the number of chips required in a row section, it means that it is impossible to cut
                result = -1 # IMPOSSIBLE
                row_flag = False # flag to stop processing row
                break # break out of row loop
            elif count == row_chips: # if count equals number of chips required for a row section, then this cut is valid
                row_cuts.append(idx+1) # store the cut index
                count = 0 # reset count

        if row_flag: # continue only if row cuts are all valid
            running_sum = [0 for _ in col_sum] # track col sum of chips in a row cut
            col_cuts = [0] # track index of col cut
            for idx in range(len(row_cuts)-1): # iterate over row cuts
                row_slice = waffle[row_cuts[idx]:row_cuts[idx+1]] # get the row cut section
                for a_slice in row_slice: # sum over the row cut section
                    running_sum = [a+b for a,b in zip(running_sum,a_slice)] # zip and sum
                col_chips = row_chips // (V+1) # integer division to find number of chips per waffle col section based on the number of chips in a row section
                if row_chips % (V+1) != 0: # if the col cut is invalid
                    result = -1 # IMPOSSIBLE
                    col_flag = False # flag to stop processing col
                    break # break out of row cuts loop
                running_count = 0 # count number of chips so far in this col cut
                if len(col_cuts) == 1: # if the col cuts has not been defined by the first row section yet
                    for cs_idx in range(len(running_sum)): # iterate over the col sum of chips in the first row section
                        running_count += running_sum[cs_idx] # increment running count by col sum element
                        if running_count > col_chips: # if running count exceeds the number of chips required in a col, it means that it is impossible to cut
                            result = -1 # IMPOSSIBLE
                            col_flag = False # flag to stop processing col
                            break # break out of col sum loop
                        elif running_count == col_chips: # if running count equals number of chips required, store this cut index
                            col_cuts.append(cs_idx+1) # store this col cut index
                            running_count = 0 # reset running count
                else: # if col cuts has already been established
                    for running_idx in range(len(col_cuts)-1): # iterate over the col cuts
                        col_slice = running_sum[col_cuts[running_idx]:col_cuts[running_idx+1]] # get the chips in this col cut
                        if sum(col_slice) != col_chips: # check if sum of col slice is the number of col chips required
                            result = -1 # IMPOSSIBLE
                            col_flag = False # flag to stop processing col
                            break # break out of col cut loop

                if col_flag == False: # if any col cut failed
                    break # break out of row section loop

                running_sum = [0 for _ in col_sum] # reset running sum

        if row_flag and col_flag: # check that both row and col flag passes
            result = 1 # POSSIBLE

    print('Case #{}: {}'.format(t+1,'POSSIBLE' if result >= 0 else 'IMPOSSIBLE')) # print result
