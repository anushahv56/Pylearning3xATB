def allowed_python_class(name):
    match name:
        case "pramod":
            print("pramod is allowed")
        case "shubam":
            print("shubam is allowed")
        case _:
            print("not allolwed")
allowed_python_class("pramod")
