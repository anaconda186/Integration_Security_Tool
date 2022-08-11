import web_request
import xml.etree.ElementTree as ET


def main() -> int:
    IntegrationID: str = input(
        "What integration would you like to look at? Enter Integration System ID: "
    )
    password: str = input("Input Password: ")
    userName: str = input("Input UserName: ")
    integration: dict[str, str] = {"id": IntegrationID}
    credentials: dict[str, str] = {
        "username": userName,
        "password": password,
        "tenant": "invisors_dpt1",
        "data center": "wd2",
    }
    response: ET.Element = web_request.getIntegrationSystem(integration, credentials)
    ISUName: str | None = None
    for element in response.iter():
        ISUElement: ET.Element | None = element.find(
            ".//{urn:com.workday/bsvc}User_Name"
        )
        if ISUElement is not None:
            ISUName: str | None = ISUElement.text
            print(ISUName)
            print(element)
            break
    if ISUName is None:
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
