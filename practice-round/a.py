import logging
logger = logging.getLogger('out')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('out.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.debug('='*11)

t = int(input())
for _ in range(t):
    a,b = input().split()
    a,b = int(a),int(b) # range (a,b]
    n = int(input())
    for _ in range(n):
        # nums = list(range(a+1,b+1))
        # guess = nums[(len(nums)+1)//2-1]
        guess = (a+b+1)//2
        print(guess,flush=True)
        reply = input()
        if reply == 'CORRECT':
            break
        elif reply == 'TOO_BIG':
            b = guess - 1
        elif reply == 'TOO_SMALL':
            a = guess
