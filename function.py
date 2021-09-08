def convert():
    file1 = input("Give first file path")
    file2 = input("Give second file path")
    with open(file1, 'r') as a:
        data_a = a.read
    with open(file2, 'r') as a:
        data_b = a.read
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as a:
        a.write(data_a)

convert()