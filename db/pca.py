import csv
import numpy as np
import scipy.linalg as la
import warnings

warnings.filterwarnings('error')

students = {}
classes = {}
i = 0

# Store data from csv in dictionaries
with open('enrolmenty.csv', 'rt') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    if len(row) == 0:
      continue
    student = row[0]
    class_name = row[1] + row[2]
    if class_name == "DeptNumber":
      continue
    if class_name in classes:
      idx = classes[class_name]
    else:
      classes[class_name] = i
      idx = i
      i += 1

    if student in students:
      students[student].append(idx)
    else:
      students[student] = [idx]

# Populate 2D array with data from dictionaries
matrix = []

class_list = sorted(classes, key=lambda x: classes[x])
# print classes
for student in students:
  offered = len(classes.keys())

  mean = 0

  # This might be "mean centering" on students; uncomment
  taken = len(students[student])
  mean = taken / offered
  row = [-mean] * offered
  for class_id in students[student]:
    row[class_id] += 1
  matrix.append(row)
# print(matrix[0])

# Test data
# matrix = [[.69,.49],[-1.31,-1.21],[.39,.99],[.09,.29],[1.29,1.09],[.49,.79],[.19,-.31],[-.81,-.81],[-.31,-.31],[-.71,-1.01]]
# matrix = [[0.00, 0.00, 0.23, 0.00, 0.00, 0.10, 0.00, 0.00, 0.46], 
#           [0.00, 0.17, 0.00, 0.00, 0.00, 0.07, 0.35, 0.35, 0.00], 
#           [0.28, 0.14, 0.00, 0.28, 0.28, 0.06, 0.00, 0.00, 0.00],
#           [0.00, 0.00, 0.69, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]]

U, s, V = la.svd(matrix)

# print("u:")
# print(U)
# print("s:")
# print(s)
# print("V:")
# print(V)
'''
# Zero out all but first k values of s
k = 5
for i in range(k, len(s)):
  s[i] = 0

dim_m = len(U)
dim_n = len(V)
dim_min = min(dim_m, dim_n)

# S = np.zeros((dim_m, dim_n), dtype=complex)
# S[:dim_min, :dim_min] = np.diag(s)

# Reconstruct matrix
# m_prime = np.dot(U, np.dot(S, V))
m_prime= np.dot(np.dot(U,la.diagsvd(s,len(matrix),len(V))),V)
# print("m_prime:")
# print(m_prime)

# Test cosine similarity
# m_prime = [ [3562, 3034, 2992, 2730, 2503, 2499],
#             [2165, 2246, 2062, 1859, 2174, 1276],
#             [4256, 4189, 3283, 2876, 2873, 2356],
#             [746, 724, 523, 488, 506, 421],
#             [135, 295, 140, 72, 136, 47],
#             [160, 117, 660, 511, 714, 376],
#             [1314, 1938, 1903, 1860, 2213, 1330],
#             [198, 897, 338, 89, 123, 128],
#             [1566, 1249, 1464, 1708, 2062, 849] ]

# U, s, V = la.svd(m_prime)            
# dim_m = len(U)
# dim_n = len(V)
# dim_min = min(dim_m, dim_n)
# m_prime = np.asarray(m_prime)

### Create course similarity matrix ###

# First, set c_raw up as M^T M.
c_raw = np.dot(m_prime.T, m_prime)

# Get the diagonal. (Note: can remove small numbers w/code below.)
cdiag_sqrt = np.sqrt(np.diag(c_raw))

# Repeat into a matrix.
cdiag_vector = cdiag_sqrt.reshape(cdiag_sqrt.shape[0],1)
cnorms = np.repeat(cdiag_vector,cdiag_sqrt.shape[0],1)

# Next, divide row-wise and column-wise by the norms
with np.errstate(invalid='ignore'):
  intermediate = np.divide(c_raw, cnorms)
  c_complex = np.divide(intermediate, cnorms.T)

# Zero out the NaN entries.
c_complex[~np.isfinite(c_complex)] = 0

# Initialize similarity matrix
sim = np.zeros((dim_n**2,3))

row_count = 0
for i in range(len(c_complex)):
  for j in range(len(c_complex[i])):
    # Cosine similarity after discarding imaginary component 
    cos_similarity = np.real(c_complex[i][j])
    # populate col 1 with from_class
    sim[row_count][0] = i
    # populate col 2 with to_class
    sim[row_count][1] = j
    # populate col 3 with cosine similarity
    sim[row_count][2] = cos_similarity
    # increment row counter
    row_count += 1

# print("sim:")
# print(sim)

### Done: Create course similarity matrix ###

# Save to csv
np.savetxt("simz.csv", sim, fmt="%1.6f", delimiter=",")
'''