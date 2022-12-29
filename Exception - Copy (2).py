def div():
    try:
        input_1=int(input())
        input_2=int(input())
        return input_1/input_2
    except ZeroDivisionError:
        print("denominator is zero")
    except ValueError:
        print("hello")

print(div())