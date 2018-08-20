import numpy
#tạo một ma trận có gia trị random từ 1 đến 100 cỡ 100x100
base_matrix = numpy.random.random_integers(0, 100, (100,100))

print('MA TRẬN ĐƯỢC SINH RA LÀ')
print(base_matrix)

print('ĐỊNH THỨC CỦA MA TRẬN')
#định thức của ma trận gốc
print(numpy.linalg.det(base_matrix))

#ma trận chuyển vị của ma trận gốc	
print('MA TRẬN CHUYỂN VỊ CỦA MA TRẬN LÀ')
print(numpy.matrix.transpose(base_matrix))
# lấy ra trị riêng và vector riêng của ma trận

print('TRỊ RIÊNG CỦA MA TRẬN LÀ')
print(numpy.linalg.eig(base_matrix)[0])


print('VECTOR RIÊNG CỦA MA TRẬN LÀ')
print(numpy.linalg.eig(base_matrix)[1])

import pandas as pd 
df = pd.DataFrame(base_matrix)
df.to_csv("output1.csv")

f= open('ouput1.txt', 'w')
for line in base_matrix:
	f.write(str(line) + "\n")