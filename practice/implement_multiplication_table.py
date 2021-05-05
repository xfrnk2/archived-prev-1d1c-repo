# result = [i for i in zip([n for n in range(2, 10)], [n for n in range(1, 10)])]
# print(result)
#
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')

result = '\n'.join([f'{j} * {i} = {i*j}' for j in range(2, 10) for i in range(1, 10)])

print(result)