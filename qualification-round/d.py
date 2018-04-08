# print('='*11)
import math

# face_diag = round(math.sqrt(2),6)
# face_diag = math.sqrt(2)
face_diag = 1.414213 # assume 6 decimal as given in question, to maintain precision

T = int(input())
for t in range(T):
    # print('case',t+1)
    A = float(input())
    # print('A',A)

    if A <= 1.414213: # constrain to 1D rotation
        angle = math.asin(A / face_diag) - math.pi / 4 # get angle required
        a = math.cos(angle) / 2 # resolve trigo
        b = math.sin(angle) / 2
        c = -b
        d = a

        print('Case #{}:'.format(t+1))
        print('{} {} {}'.format(a,b,0))
        print('{} {} {}'.format(c,d,0))
        print('{} {} {}'.format(0,0,0.5))
    # else: # did not solve for 2D rotation


