data = [
    ['100', '200', '300'],
    ['400', '500', '600']
    ]

# С сайта мы получаем именно списки.
numbers = []

data1 = [
    [100, 110, 120],
    [400, 500, 600],
    [150, 130, 140]
    ]

list = []

for row in data:
    for text in row:
        number = int(text)
        numbers.append(number)
print(numbers)

for row in data1:
    for item in row:
        if item > 190:
            list.append(item)
print(list)