for i in range(65,91):
    alpha=chr(i)
    with open(str(alpha),'x') as file:
        file.write(int(alpha)+32)