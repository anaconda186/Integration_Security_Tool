import web_request
import xml.etree.ElementTree as ET
from parse_args import parse_args
from get_credentials import get_credentials


def main() -> int:
    arg_dict, user_name, password = parse_args()
    credentials: dict[str, str] = get_credentials(arg_dict, user_name, password)
    security_group_id: str = input(
        "What Security Group would you like to look at? Enter Integration Security Group Unconstrgained ID: "
    )
    security_group: dict[str, str] = {"security_group": security_group_id}
    response: ET.Element = web_request.get_security_group(security_group, credentials)
    isu_name: str | None = None
    for element in response.iter():
        isu_element: ET.Element | None = element.find(
            ".//{urn:com.workday/bsvc}Integration_System_User_Reference"
        )
        if isu_element is not None:
            isu_name: str | None = isu_element.attrib[
                "{urn:com.workday/bsvc}Descriptor"
            ]
            break
    if isu_name is None:
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
