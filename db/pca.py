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
matrix = [
    # ['id'] + sorted(classes, key=lambda x: classes[x])
]

for student in students:
    # row = [student] + [0] * len(classes.keys())
    row = [0] * len(classes.keys())
    for class_id in students[student]:
        # row[class_id + 1] = 1
        row[class_id] = 1
    matrix.append(row)

# Perform SVD
U, s, V = numpy.linalg.svd(matrix)

# print U.shape
# print V.shape
# print s.shape

# Zero out all but first k values of s
k = 5

for i in range(k, len(s)):
    s[i] = 0

S = numpy.zeros((486, 666), dtype=complex)
S[:486, :486] = numpy.diag(s)

# Reconstruct matrix
m_prime = numpy.dot(U, numpy.dot(S, V))

# Create course similarity matrix
c = [[0]*666]*666

for row in range(len(c)):
    print '.',
    for col in range(len(c)):
        rcol = m_prime[:,row]
        ccol = m_prime[:,col]
        
        dot = numpy.dot(rcol,ccol)
        l1 = numpy.linalg.norm(rcol)
        l2 = numpy.linalg.norm(ccol)
        mag = l1 * l2
        # print type(dot)
        # print type(mag)
        # print row
        # print col
        # print dot
        # print mag
        if mag == 0:
            sim = 0
        else:
            sim = numpy.asscalar(dot/mag)
        c[row][col] = sim
        print row, col, sim

print c[0][0]
print c[0]