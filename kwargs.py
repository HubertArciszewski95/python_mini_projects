def calculate(**kwargs):

    # Here i make all calculation
    if kwargs.get("operation") is "add":
        result = kwargs.get("first") + kwargs.get("second")

    elif kwargs.get("operation") is "substract":
        result = kwargs.get("first") - kwargs.get("second")

    elif kwargs.get("operation") is "multiply":
        result = kwargs.get("first") * kwargs.get("second")

    elif kwargs.get("operation") is "divide":
        result = kwargs.get("first") / kwargs.get("second")

    # This function is making result of calculation float or int
    def is_float():
        if kwargs.get("make_float"):
            return float(result)
        else:
            return int(result)

    # This function is printing default message or provided message
    def output():
        if kwargs.get("message"):
            return f"{kwargs.get('message')} {is_float()}"
        else:
            return f"The result is {is_float()}"
    return output()


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=6, second=3))
