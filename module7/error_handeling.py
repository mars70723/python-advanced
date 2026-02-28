# try:
#     result=10/0
# except ZeroDivisionError:
#     print("Opss! Tried to divide by zero!")
#
#
# fruits = {
#     "apple": 5,
#     "orange": 3,
#     "banana": 7
# }
# try:
#     print(fruits["cherry"])
# except KeyError:
#     print("The key does not match in the dictionary")
#
#
# text = "this is not a number"
# try:
#     text_to_int = int(text)
# except Exception as e:
#     print("An error ocurred", e)
#
#
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("Division by 0")
# else:
#     print("Division successful. Result=", result)
#
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("We have an error, we cant divine by 0")
# finally:
#     print("Finally block executed")
#
#
# def devide_numbers(a,b):
#     try:
#         result = a/b
#         print("The result is: ",result)
#     except ZeroDivisionError:
#         print("You tried to divide by 0")
#     except Exception as e:
#         print("Invalid type for division")
#     except Exception as e:
#         print("Unexpected error", e)
# devide_numbers(10,2)
# devide_numbers(10,0)

def challange(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        raise ValueError("Invalid operator")
try:
    number1 = float(input("shtyp numrin 1: "))
    number2 = float(input("shtyp numrin 2: "))
    operator = input("Enter an operator (+,-,*,/): ")
    result = challange(number1, number2, operator)
    print("The result of the operations is", result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("You tried to divide by 0")
except Exception as e:
    print("Theres an error", e)
finally:
    print("The code was executed")













