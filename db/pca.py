import csv
import numpy
import warnings

warnings.filterwarnings('error')

students = {}
classes = {}
i = 0

# Store data from csv in dictionaries
with open('enrolment.csv', 'rb') as csvfile:
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
print classes
for student in students:
    row = [0] * len(classes.keys())
    for class_id in students[student]:
        row[class_id] = 1
    matrix.append(row)

# Perform SVD
U, s, V = numpy.linalg.svd(matrix)

# Zero out all but first k values of s
k = 5

for i in range(k, len(s)):
    s[i] = 0

S = numpy.zeros((485, 665), dtype=complex)
S[:485, :485] = numpy.diag(s)

# Reconstruct matrix
m_prime = numpy.dot(U, numpy.dot(S, V))

#### Create course similarity matrix ####

# First, set c_raw up as M^T M.
c_raw = numpy.dot(m_prime.T, m_prime)

# Next, pull out the norms

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

# Discard imaginary component and copy into final matrix
c = numpy.zeros((665, 665))
for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j] = numpy.real(c_complex[i][j])

#### Done: Create course similarity matrix ####

numpy.savetxt("sim.csv", c, fmt="%1.6f", delimiter=",")

# print type(c[0][0])
# print c[0][0] > c[0][1]
# print numpy.real(c[0][1])
# print c[0]
# print c[664][664]