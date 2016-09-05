# Linear Algebra 1.1):
import numpy as np

A = np.array([[1,2,3],[2,7,4]])   # matrix
print
print 'Matrix A:'
print A    # output matrix
print
print 'Dimension of matrix A:',A.shape       # output dimensions
print

# Output for 1.1):
# >>> runfile('/Users/swatisharma/Documents/LA1p1.py', wdir='/Users/swatisharma/Documents')
#
# Matrix A =
# [[1 2 3]
#  [2 7 4]]
#
# Dimension of matrix A: (2, 3)
#__________________________________________________________________

# Linear Algebra 1.2):
import numpy as np

B = np.array([[1,-1],[0,1]])   # matrix
print
print 'Matrix B ='
print B    # output matrix
print
print 'Dimension of matrix B:',B.shape       # output dimensions
print

# Output for 1.2):
# >>> runfile('/Users/swatisharma/Documents/LA1p2.py', wdir='/Users/swatisharma/Documents')
#
# Matrix B =
# [[ 1 -1]
#  [ 0  1]]
#
# Dimension of matrix B: (2, 2)
#__________________________________________________________________

# Linear Algebra 1.3):
import numpy as np

C = np.array([[5,-1],[9,1],[6,0]])   # matrix
print
print 'Matrix C ='
print C    # output matrix
print
print 'Dimension of matrix C:',C.shape       # output dimensions
print

# Output for 1.3):
# >>> runfile('/Users/swatisharma/Documents/LA1p3.py', wdir='/Users/swatisharma/Documents')
#
# Matrix C =
# [[ 5 -1]
#  [ 9  1]
#  [ 6  0]]
#
# Dimension of matrix C: (3, 2)
#______________________________________________________________________

# Linear Algebra 1.4):
import numpy as np

D = np.array([[3,-2,-1],[1,2,3]])   # matrix
print
print 'Matrix D ='
print D    # output matrix
print
print 'Dimension of matrix D:',D.shape       # output dimensions
print

# Output for 1.4):
# >>> runfile('/Users/swatisharma/Documents/LA1p4.py', wdir='/Users/swatisharma/Documents')
#
# Matrix D =
# [[ 3 -2 -1]
#  [ 1  2  3]]
#
# Dimension of matrix D: (2, 3)
#_____________________________________________________________________

# Linear Algebra 1.5):
# Linear Algebra 1.5):
import numpy as np

u = np.array([[6,2,-3,5]])   # matrix
print
print 'Matrix u ='
print u    # output matrix
print
print 'Dimension of matrix u:',u.shape       # output dimensions
print

# Output for 1.5):
# >>> runfile('/Users/swatisharma/Documents/LA1p5.py', wdir='/Users/swatisharma/Documents')
#
# Matrix u =
# [[ 6  2 -3  5]]
#
# Dimension of matrix u: (1, 4)
#__________________________________________________________________

# Linear Algebra 1.6):
import numpy as np

w = np.array([[1],[8],[0],[5]])   # matrix
print
print 'Matrix w ='
print w    # output matrix
print
print 'Dimension of matrix w:',w.shape       # output dimensions
print

# Output for 1.6):
# >>> runfile('/Users/swatisharma/Documents/LA1p6.py', wdir='/Users/swatisharma/Documents')
#
# Matrix w =
# [[1]
#  [8]
#  [0]
#  [5]]
#
# Dimension of matrix w: (4, 1)
#_____________________________________________________________________
# Linear Algebra 2.1):
import numpy as np

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

matsum = u + v

print
print 'u + v = ',matsum
print

# Output for 2.1):
# >>> runfile('/Users/swatisharma/Documents/LA2p1TEST.py', wdir='/Users/swatisharma/Documents')
#
# u + v =  [ 9  7 -4  9]
#____________________________________________________________________

# Linear Algebra 2.2):
import numpy as np

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

matdiff = u - v


print
print 'u - v = ',matdiff
print

# Output for 2.2):
# >>> runfile('/Users/swatisharma/Documents/LA2p1TEST.py', wdir='/Users/swatisharma/Documents')
#
# u - v =  [ 3 -3 -2  1]
#_____________________________________________________________________

# Linear Algebra 2.3):
import numpy as np

u = np.array([6,2,-3,5])
alpha = 6

matmul = 6*u


print
print 'alpha(u) = ',matmul
print

# Output for 2.3):
# >>> runfile('/Users/swatisharma/Documents/LA2p1TEST.py', wdir='/Users/swatisharma/Documents')
#
# alpha(u) =  [ 36  12 -18  30]
#_____________________________________________________________________

# Linear Algebra 2.4):
import numpy as np

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

matdot = np.dot(u,v)


print
print 'u dot v = ',matdot
print

# Output for 2.4):
# >>> runfile('/Users/swatisharma/Documents/LA2p1TEST.py', wdir='/Users/swatisharma/Documents')
#
# u dot v =  51
________________________________________________________________________

# Linear Algebra 2.5):
import numpy as np

u = np.array([6,2,-3,5])

matmag = np.linalg.norm(u)


print
print '||u|| = ',matmag

# Output for 2.5):
# >>> runfile('/Users/swatisharma/Documents/LA2p5.py', wdir='/Users/swatisharma/Documents')
#
# ||u|| =  8.60232526704
#______________________________________________________________________

# Linear Algebra 3.1):
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
C = np.array([[5,-1],[9,1],[6,0]])

matsum = A + C
print
print 'A + C =', matsum

# Output for 3.1): NOT POSSIBLE!
# >>> runfile('/Users/swatisharma/Documents/LA3p1.py', wdir='/Users/swatisharma/Documents')
#
# ValueError: operands could not be broadcast together with shapes (2,3) (3,2) 
#_______________________________________________________________

# Linear Algebra 3.2):
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
C = np.array([[5,-1],[9,1],[6,0]])
CTr = np.transpose(C)

matdiff = A - CTr
print
print 'A - CTranspose ='
print matdiff

# Output for 3.2):
# >>> runfile('/Users/swatisharma/Documents/LA3p2.py', wdir='/Users/swatisharma/Documents')
# 
# A - CTranspose =
# [[-4 -7 -3]
#  [ 3  6  4]]
#______________________________________________________

# Linear Algebra 3.3):
import numpy as np

C = np.array([[5,-1],[9,1],[6,0]])
CTr = np.transpose(C)
D = np.array([[3,-2,-1],[1,2,3]])

matsum = CTr + (3*D)
print
print 'CTranspose + 3D ='
print matsum

# Output for 3.3):
# >>> runfile('/Users/swatisharma/Documents/LA3p3.py', wdir='/Users/swatisharma/Documents')
# 
# CTranspose + 3D =
# [[14  3  3]
#  [ 2  7  9]]
#____________________________________________

# Linear Algebra 3.4):
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])

matmul = B.dot(A)
print
print 'BA ='
print matmul
print

# Output for 3.4):
# >>> runfile('/Users/swatisharma/Documents/LA3p4.py', wdir='/Users/swatisharma/Documents')
#
# BA =
# [[-1 -5 -1]
#  [ 2  7  4]]
#_____________________________________________

# Linear Algebra 3.5):
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
ATr = np.transpose(A)
B = np.array([[1,-1],[0,1]])

matmul = B.dot(ATr)
print
print 'B(A Transpose) =', matmul
print

# Ouptput for 3.5):  NOT POSSIBLE!
# >>> runfile('/Users/swatisharma/Documents/LA3p5.py', wdir='/Users/swatisharma/Documents')
#
# ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)
#_____________________________________________

# Linear Algebra 3.6):
import numpy as np

B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])

matmul = B.dot(C)
print
print 'BC =', matmul
print

# Output for 3.6): NOT POSSIBLE!
# >>> runfile('/Users/swatisharma/Documents/LA3p6.py', wdir='/Users/swatisharma/Documents')
#
# ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)
#_______________________________________________

# Linear Algebra 3.7):
import numpy as np

B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])

matmul = C.dot(B)
print
print 'CB ='
print matmul
print

# Output for 3.7):
# >>> runfile('/Users/swatisharma/Documents/LA3p7.py', wdir='/Users/swatisharma/Documents')
#
# CB =
# [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]
#_________________________________________

# Linear Algebra 3.8):
import numpy as np

B = np.array([[1,-1],[0,1]])

#matmul1 = B.dot(B)
#matmul2 = matmul1.dot(matmul1)
matpow = np.linalg.matrix_power(B,4)
print
print 'B^4 ='
print matpow
print

# Output for 3.8):
# >>> runfile('/Users/swatisharma/Documents/LA3p8.py', wdir='/Users/swatisharma/Documents')
#
# B^4 =
# [[ 1 -4]
#  [ 0  1]]
#________________________________________________

# Linear Algebra 3.9):
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
ATr = np.transpose(A)

matmul = A.dot(ATr)
print
print 'A(A Transpose) ='
print matmul
print

# Output for 3.9):
# >>> runfile('/Users/swatisharma/Documents/LA3p9.py', wdir='/Users/swatisharma/Documents')
#
# A(A Transpose) =
# [[14 28]
#  [28 69]]
#____________________________________________________

# Linear Algebra 3.10):
import numpy as np

D = np.array([[3,-2,-1],[1,2,3]])
DTr = np.transpose(D)

matmul = DTr.dot(D)
print
print '(D Transpose)D ='
print matmul
print

# Output for 3.10):
># >> runfile('/Users/swatisharma/Documents/LA3p10.py', wdir='/Users/swatisharma/Documents')
#
# (D Transpose)D =
# [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]











