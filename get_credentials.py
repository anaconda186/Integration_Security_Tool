import maskpass


def get_credentials(arg_dict, user_name_arg, password_arg) -> dict[str, str]:
    credentials: dict[str, str] = {
        "user_name": "",
        "password": "",
        "tenant": "invisors_dpt1",
        "data center": "wd2",
    }
    if arg_dict["user_name"]:
        credentials["user_name"] = user_name_arg
    else:
        user_name: str = input("Input User Name: ")
        credentials["user_name"] = user_name

    if arg_dict["password"]:
        credentials["password"] = password_arg
    else:
        password: str = maskpass.askpass(prompt="Input password: ", mask="*")
        credentials["password"] = password

    return credentials
