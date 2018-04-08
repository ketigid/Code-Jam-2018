import sys
# Use logger for debugging since stdout is needed to interact with judge
# import logging
# logger = logging.getLogger('out')
# logger.setLevel(logging.DEBUG)
# fh = logging.FileHandler('out.log')
# fh.setLevel(logging.DEBUG)
# logger.addHandler(fh)
# logger.debug('='*11)

# Helper functions
def sub2ind(array_shape, rows, cols):
    return rows*array_shape[1] + cols

def ind2sub(array_shape, ind):
    rows = (ind // array_shape[1])
    cols = (ind % array_shape[1])
    return (rows, cols)

# Pre-defined rectangle dimensions since A = 20 or 200
rect_dim = {
  20: [3,7], # min number of middle squares
  64: [8,8], # testing purpose
  200: [4,50] # should have picked [3,67] instead...
}
table_shape = [] # get table shape based on input
free_space = [] # tracks number of free neighbours around this point
field = [] # track how the field looks
free_space_shape = [] # shape of free_space

base_row = 100 # offset
base_column = 100 # offset

T = int(input())
for _ in range(T):
  A = int(input())
  table_shape = rect_dim[A]
  field = [[0 for x in range(table_shape[1])] for y in range(table_shape[0])]
  free_space_shape = [x - 2 for x in table_shape]
  free_space = [[9 for x in range(free_space_shape[1])] for y in range(free_space_shape[0])]

  count = 0 # count number of interactions with judge
  while(count < 1000): # limit to 1000 interactions
    count += 1 # update count
    flattened = [item for row in free_space for item in row] # flatten free_space to find max
    max_index = flattened.index(max(flattened)) # get index of max free space
    (r,c) = ind2sub(free_space_shape,max_index) # convert to row and column indices
    # logger.debug(r)
    # logger.debug(c)
    r_adj = r + 1 + base_row # adjust free space to actual field
    c_adj = c + 1 + base_column
    # logger.debug([r_adj,c_adj])
    print(r_adj,c_adj) # interacte with judge
    sys.stdout.flush() # flush is needed

    s = list(map(int,input().split())) # get reply from judge
    # logger.debug(s)
    if s == [-1,-1]: # fail
      break
    elif s == [0,0]: # succeed
      break
    else: # iterate
      i,j = s # destructure
      i_adj = i - base_row # adjust to field space
      j_adj = j - base_column
      # logger.debug(i_adj)
      # logger.debug(j_adj)
      if not field[i_adj][j_adj]: # if field is empty
        field[i_adj][j_adj] = 1 # update field
        for m in [-1,0,1]: # for neighbours around updated field
          for n in [-1,0,1]:
            m_adj = i_adj + m - 1 # convert to free space 
            n_adj = j_adj + n - 1
            if m_adj >= 0 and m_adj < free_space_shape[0] and n_adj >= 0 and n_adj < free_space_shape[1]: # boundary conditions
              free_space[m_adj][n_adj] -= 1 # reduce free space count
    # logger.debug(field)
    # logger.debug(free_space)

