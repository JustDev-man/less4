def checker(function):
    def check(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems {exc}")
            result = ""
        else:
            print(f"No problems. Result - {result}")
        return result
    return check

@checker
def calculate(expresssion):
    return eval(expresssion)

inpexp = str(input("Enter a expression - "))
calculate(inpexp)
