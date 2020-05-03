from mat import Matrix


m1 = Matrix(data=[[2, 3, 4], [5, 1, -3], [3, -2, 1]])
m2 = Matrix(shape=(4, 5))
m3 = Matrix(data=[[2, -1, 3], [4, 3, -1], [1, -2, 5]])
m4 = Matrix(shape=(9, 9))
m5 = Matrix(shape=(3, 3))
b1 = [13, 7, 15]
# print(m1.check_shape_for_add(m2))
# print(m1.check_shape_for_add(m5))

# print(m1.check_shape_for_mul(m2))
# print(m1.check_shape_for_mul(m3))

# print(m1.check_shape_square())
# print(m2.check_shape_square())

# print(m1 + m3)
# print(m3 + m5)

m1 += m3
# print(m1)
m3 += m5
# print(m3)

# print(m3 - m5)
# print(m1 - m3)

m3 -= m5
# print(m3)
m1 -= m3
# print(m1)

# print(m1 * 2)
# print(m5 * 9)

# print(m3.determinant())
# print(m4.determinant())

# print(m3.is_degenerate())
# print(m4.is_degenerate())

# print(m3.kramer_solution(b1))
# print(m5.kramer_solution(b1))

# print(m3.gauss_solution(b1))
# print(m5.gauss_solution(b1))

print(m3.inverse())
print(m1.inverse())
