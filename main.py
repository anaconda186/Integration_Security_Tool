import sys
import getopt
import web_request
import xml.etree.ElementTree as ET


def main() -> int:
    opts: list[tuple[str, str]] = getopt.getopt(sys.argv[1:], "v", ['verbose'])[0]
    verbose: bool = False
    print(opts)
    for opt, arg in opts:
        if opt == '-v':
            verbose = True
    if verbose:
        print('Verbose mode on')
    SecurityGroupID: str = input(
        "What Security Group would you like to look at? Enter Integration Security Group Unconstrained ID: "
    )
    password: str = input("Input Password: ")
    userName: str = input("Input UserName: ")
    securityGroup: dict[str, str] = {"securityGroup": SecurityGroupID}
    credentials: dict[str, str] = {
        "username": userName,
        "password": password,
        "tenant": "invisors_dpt1",
        "data center": "wd2",
    }
    response: ET.Element = web_request.getSecurityGroup(securityGroup, credentials)
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
