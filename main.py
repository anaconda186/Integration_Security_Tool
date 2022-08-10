import web_request


def main():
    IntegrationID = input(
        "What integration would you like to look at?(Enter INTSYS ID)"
    )
    password = input("inputPassword")
    integration = {"id": IntegrationID}
    credentials = {
        "data": {
            "username": "jhardy-impl",
            "password": password,
            "tenant": "invisors_dpt1",
            "data center": "wd2",
        }
    }
    response = web_request.getIntSys(integration, credentials["data"])
    userName = response[
        response.find("<wd:User_Name>") + 14 : response.find("</wd:User_Name>")
    ]
    print(userName)


if __name__ == "__main__":
    main()
