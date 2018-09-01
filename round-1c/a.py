# print('='*11)
import math

def new_word_f(columns_list,letters_to_go,this_key,word_so_far):
    if letters_to_go == 1:
        return word_so_far+this_key

    if '$' in word_so_far:
        return word_so_far+'$'

    if not columns_list[-letters_to_go][this_key]:
        return word_so_far+'$'
    else:
        for v in columns_list[-letters_to_go][this_key]:
            return new_word_f(columns_list,letters_to_go-1,v,word_so_far+this_key)

T = int(input())
for t in range(T):
    # print('case',t+1)
    N,L = list(map(int,input().split()))
    # print(N,L)

    words = []
    for n in range(N):
        words.append(input())

    # print(words)

    if L == 1:
        # print('L=1')
        print('Case #{}: -'.format(t+1)) # print result
        continue

    # L > 1
    # create columns of unique letters
    columns_list = [{} for i in range(L)]
    for word in words:
        for idx in range(len(word)):
            columns_list[idx][word[idx]] = []
    # print(columns_list)
    # print(list(columns_list[0].keys()))

    # populate possible connections
    for col_idx in range(L-1):
        for k,v in columns_list[col_idx].items():
            columns_list[col_idx][k] = list(columns_list[col_idx+1].keys())
    # print(columns_list)

    # remove connections
    for word in words:
        for idx in range(len(word)-1):
            try:
                columns_list[idx][word[idx]].remove(word[idx+1])
            except:
                pass
    # print(columns_list)

    # find a possible new word
    new_word = '-'
    # if L == 2:
    #     for k,v in columns_list[0].items():
    #         if v:
    #             new_word = k+v[0]
    # else:
    #     for k,v in columns_list[0].items():
    #         new_word = new_word_f(columns_list,L,k,'')
    #         if not '$' in new_word:
    #             break

    for k,v in columns_list[0].items():
        new_word = new_word_f(columns_list,L,k,'')
        # print(new_word)
        if not '$' in new_word and len(new_word) == L:
            break

    if not '$' in new_word and len(new_word) == L:
        result = new_word
    else:
        result = '-'

    print('Case #{}: {}'.format(t+1,result)) # print result
