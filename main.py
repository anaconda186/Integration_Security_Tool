import web_request


def main():
    IntegrationID = input(
        "What integration would you like to look at?(Enter INTSYS ID)"
    )
    password: str = input("input Password: ")
    userName: str = input("input UserName: ")
    integration: dict[str, str] = {"id": IntegrationID}
    credentials: dict[str, str] = {
        "username": userName,
        "password": password,
        "tenant": "invisors_dpt1",
        "data center": "wd2",
    }
    response = web_request.getIntegrationSystem(integration, credentials)
    userName = response[
        (response.find("<wd:User_Name>") + 14) : response.find("</wd:User_Name>")
    ]
    print(userName)


if __name__ == "__main__":
    main()
