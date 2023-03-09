import sys
import getopt


def parse_args() -> tuple[dict[str, bool], str, str]:
    arg_dict: dict[str, bool] = {
        "verbose": False,
        "user_name": False,
        "password": False,
    }
    user_name: str = ""
    password: str = ""
    opts: list[tuple[str, str]] = getopt.getopt(
        sys.argv[1:], "vu:p:", ["verbose", "user_name", "password"]
    )[0]
    print(opts)
    for opt, arg in opts:
        if opt == "-v":
            arg_dict["verbose"] = True
        if opt == "-u":
            arg_dict["user_name"] = True
            user_name = arg
        if opt == "-p":
            arg_dict["password"] = True
            password = arg

    if arg_dict["verbose"]:
        print("Verbose mode on")
    return arg_dict, user_name, password
