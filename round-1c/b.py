import sys
# Use logger for debugging since stdout is needed to interact with judge
# import logging
# logger = logging.getLogger('out')
# logger.setLevel(logging.DEBUG)
# fh = logging.FileHandler('out.log')
# fh.setLevel(logging.DEBUG)
# logger.addHandler(fh)
# logger.debug('='*11)

T = int(input())
for _ in range(T):
  N = int(input())
  # logger.debug(N)

  lollipops = [1 for i in range(N)]
  wants = [0 for i in range(N)]
  # logger.debug(lollipops)

  count = 0 # count number of interactions with judge
  while(count < N): # limit to 1000 interactions
    count += 1 # update count
    D = list(map(int,input().split()))
    wish = D[1:]
    D = D[0]
    # logger.debug(D)
    # logger.debug(wish)

    if D == 0:
      print(-1)
      sys.stdout.flush()
      continue
    else:
      sold = False
      for w in wish:
        wants[w] += 1
      available = [a*b for a,b in zip(wants,lollipops)]
      minimum = 999999
      min_idx = -1
      for w in wish:
        if available[w] > 0:
          if available[w] < minimum:
            minimum = available[w]
            min_idx = w
        # if lollipops[w] == 1:
        #   lollipops[w] = 0
        #   print(w)
        #   sys.stdout.flush()
        #   sold = True
        #   break
      if min_idx > -1:
        print(min_idx)
        sys.stdout.flush()
        lollipops[min_idx] = 0
        sold = True
      if not sold:
        print(-1)
        sys.stdout.flush()
    # logger.debug(lollipops)



# print('end')