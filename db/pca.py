import csv
import numpy
import warnings

warnings.filterwarnings('error')

students = {}
classes = {}
i = 0

# Store data from csv in dictionaries
with open('enrolmentx.csv', 'rt') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    student = row[1]
    class_name = row[2] + row[3]
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
  # taken = len(students[student])
  # mean = taken / offered
  row = [-mean] * offered
  for class_id in students[student]:
    row[class_id] += 1
  matrix.append(row)

# Perform SVD
U, s, V = numpy.linalg.svd(matrix)

# Zero out all but first k values of s
k = 5
for i in range(k, len(s)):
  s[i] = 0

dim_m = len(U)
dim_n = len(V)
dim_min = min(dim_m, dim_n)

S = numpy.zeros((dim_m, dim_n), dtype=complex)
S[:dim_min, :dim_min] = numpy.diag(s)

# Reconstruct matrix
m_prime = numpy.dot(U, numpy.dot(S, V))

### Create course similarity matrix ###

# First, set c_raw up as M^T M.
c_raw = numpy.dot(m_prime.T, m_prime)

# Get the diagonal. (Note: can remove small numbers w/code below.)
cdiag_sqrt = numpy.sqrt(numpy.diag(c_raw))

# Repeat into a matrix.
cdiag_vector = cdiag_sqrt.reshape(cdiag_sqrt.shape[0],1)
cnorms = numpy.repeat(cdiag_vector,cdiag_sqrt.shape[0],1)

# Next, divide row-wise and column-wise by the norms
with numpy.errstate(invalid='ignore'):
  intermediate = numpy.divide(c_raw, cnorms)
  c_complex = numpy.divide(intermediate, cnorms.T)

# Zero out the NaN entries.
c_complex[~numpy.isfinite(c_complex)] = 0

# Initialize similarity matrix
sim = numpy.zeros((dim_n**2,3))

row_count = 0
for i in range(len(c_complex)):
  for j in range(len(c_complex[i])):
    # Cosine similarity after discarding imaginary component 
    cos_similarity = numpy.real(c_complex[i][j])
    # populate col 1 with from_class
    sim[row_count][0] = i
    # populate col 2 with to_class
    sim[row_count][1] = j
    # populate col 3 with cosine similarity
    sim[row_count][2] = cos_similarity
    # increment row counter
    row_count += 1

### Done: Create course similarity matrix ###

# Save to csv
numpy.savetxt("sim.csv", sim, fmt="%1.6f", delimiter=",")
