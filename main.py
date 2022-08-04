import web_request


def main():
    IntegrationID = input(
        "What integration would you like to look at?(Enter INTSYS ID)"
    )
    integration = {"id": IntegrationID}
    credentials = {
        "data": {
            "username": "jhardy-impl",
            "password": "Straw_bag!90",
            "tenant": "GMS",
            "data center": "Testing",
        }
    }
    print(web_request.getIntSys(integration, credentials["data"]))


if __name__ == "__main__":
    main()
