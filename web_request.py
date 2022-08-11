import requests
import xml.etree.ElementTree as ET


def create_isu(integration: dict[str, str], credentials: dict[str, str]) -> str:
    request: str = f"""<?xml version="1.0" encoding="utf-8"?>
    <env:Envelope
        xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
        <env:Header>
            <wsse:Security env:mustUnderstand="1">
                <wsse:UsernameToken>
                    <wsse:Username>{credentials["username"]}@{credentials["tenant"]}</wsse:Username>
                    <wsse:Password
                        Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{credentials["password"]}</wsse:Password>
                </wsse:UsernameToken>
            </wsse:Security>
        </env:Header>
        <env:Body>
            <wd:Put_Integration_System_User_Request
                xmlns:wd="urn:com.workday/bsvc"
                wd:version="v36.2">
                <wd:Integration_System_Reference>
                    <wd:ID wd:type="Integration_System_ID">{integration["Name"].replace(' ','_')}</wd:ID>
                </wd:Integration_System_Reference>
                <wd:Integration_System_User_Data>
                    <wd:Integration_System_Reference>
                        <wd:ID wd:type="Integration_System_ID">{integration["Name"].replace(' ','_')}</wd:ID>
                    </wd:Integration_System_Reference>
                    <wd:User_Name>ISU {integration["Name"]}</wd:User_Name>
                    <wd:Password>{integration["Password"]}</wd:Password>
                    <wd:Require_New_Password_At_Next_Sign_In>false</wd:Require_New_Password_At_Next_Sign_In>
                    <wd:Session_Timeout_Minutes>10</wd:Session_Timeout_Minutes>
                    <wd:Do_Not_Allow_UI_Sessions>true</wd:Do_Not_Allow_UI_Sessions>
                </wd:Integration_System_User_Data>
            </wd:Put_Integration_System_User_Request>
        </env:Body>
    </env:Envelope>"""
    return request


def create_issg(integration: dict[str, str], credentials: dict[str, str]) -> str:
    request: str = f"""<?xml version="1.0" encoding="utf-8"?>
    <env:Envelope
        xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
        <env:Header>
            <wsse:Security env:mustUnderstand="1">
                <wsse:UsernameToken>
                    <wsse:Username>{credentials["username"]}@{credentials["tenant"]}</wsse:Username>
                    <wsse:Password
                        Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{credentials["password"]}</wsse:Password>
                </wsse:UsernameToken>
            </wsse:Security>
        </env:Header>
        <env:Body>
            <wd:Put_Integration_System_Security_Group__Unconstrained__Request xmlns:wd="urn:com.workday/bsvc"
                wd:Add_Only="0" wd:version="v23.2">
                <wd:Integration_System_Security_Group__Unconstrained__Data wd:ID="ISSG_{integration["Name"].replace(' ','_')}">
                    <wd:Name>ISSG {integration["Name"]}</wd:Name>
                    <wd:Comment>Security Group for Integration with ID {integration["Name"].replace(' ','_')}</wd:Comment>
                    <wd:Inactive>0</wd:Inactive>
                    <wd:Integration_System_User_Reference>
                            <wd:ID wd:type="System_User_ID">ISU {integration["Name"]}</wd:ID>
                        </wd:Integration_System_User_Reference>
                </wd:Integration_System_Security_Group__Unconstrained__Data>
            </wd:Put_Integration_System_Security_Group__Unconstrained__Request>
        </env:Body>
    </env:Envelope>"""
    return request


# https://wd2-impl-services1.workday.com/ccx/service/invisors_dpt1/Core_Implementation_Service/v38.1
def get_security_domain(security: str, credentials: dict[str, str]) -> str:
    request: str = f"""<?xml version="1.0"?>
    <env:Envelope
        xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:wd="urn:com.workday/bsvc">
        xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
        <env:Header>
            <wsse:Security env:mustUnderstand="1">
                <wsse:UsernameToken>
                    <wsse:Username>{credentials["username"]}@{credentials["tenant"]}</wsse:Username>
                    <wsse:Password
                        Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{credentials["password"]}</wsse:Password>
                </wsse:UsernameToken>
            </wsse:Security>
        </env:Header>
        <env:Body>
            <wd:Get_Domain_Security_Policy_Request wd:version="v38.1">
                <wd:Request_References>
                    <wd:Domain_Reference>
                        <wd:ID wd:type="WID">{security}</wd:ID>
                    </wd:Domain_Reference>
                </wd:Request_References>
                <wd:Response_Group>
                    <wd:Include_Reference>true</wd:Include_Reference>
                    <wd:Include_Domain_Security_Policy_Data>true</wd:Include_Domain_Security_Policy_Data>
                </wd:Response_Group>
            </wd:Get_Domain_Security_Policy_Request>
        </env:Body>
    </env:Envelope>"""
    return request


# https://wd2-impl-services1.workday.com/ccx/service/invisors_dpt1/Core_Implementation_Service/v38.1
def put_security_domain(
    security_domain: dict[str, str], credentials: dict[str, str]
) -> str:
    request: str = f"""<?xml version="1.0"?>
    <env:Envelope
        xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:wd="urn:com.workday/bsvc">
        <env:Header>
            <wsse:Security env:mustUnderstand="1">
                <wsse:UsernameToken>
                    <wsse:Username>{credentials["username"]}@{credentials["tenant"]}</wsse:Username>
                    <wsse:Password
                        Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{credentials["password"]}</wsse:Password>
                </wsse:UsernameToken>
            </wsse:Security>
        </env:Header>
        <env:Body>
            <wd:Put_Domain_Security_Policies_Request wd:version="v38.1">
                <wd:Domain_Security_Policy_Data>
                    <wd:Domain_Reference>
                        <!--Zero or more repetitions:-->
                        <wd:ID wd:type="WID">{security_domain["WID"]}</wd:ID>
                    </wd:Domain_Reference>
                    <wd:Domain_Name>Student Data: Academic Data</wd:Domain_Name>
                    <wd:Disabled>1</wd:Disabled>
                    <wd:Notes>Testing</wd:Notes>
                    <wd:Security_Policy_Permission_Data>
                        <wd:Security_Group_Reference>
                            <wd:ID wd:type="WID">eee553af7f5f100b8ff149c37b730000</wd:ID>
                        </wd:Security_Group_Reference>
                        <wd:Security_Operation_Reference>
                            <wd:ID wd:type="Security_Operation_ID">getUpdate_secOp</wd:ID>
                        </wd:Security_Operation_Reference>
                    </wd:Security_Policy_Permission_Data>
                </wd:Domain_Security_Policy_Data>
            </wd:Put_Domain_Security_Policies_Request>
        </env:Body>
    </env:Envelope>"""
    return request


def getIntegrationSystem(
    integration: dict[str, str], credentials: dict[str, str]
) -> ET.Element:

    header: dict[str, str] = {"content-type": "text/xml"}
    request: str = f"""<?xml version="1.0" encoding="utf-8"?>
    <soapenv:Envelope
        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:bsvc="urn:com.workday/bsvc"
        xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
        <soapenv:Header>
            <wsse:Security soapenv:mustUnderstand="1">
                <wsse:UsernameToken>
                    <wsse:Username>{credentials["username"]}@{credentials["tenant"]}</wsse:Username>
                    <wsse:Password
                        Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{credentials["password"]}</wsse:Password>
                </wsse:UsernameToken>
            </wsse:Security>
        </soapenv:Header>
        <soapenv:Body>
            <bsvc:Integration_System_Get bsvc:version="v39.0">
                <bsvc:Integration_System_Reference>
                    <bsvc:System_ID>{integration["id"]}</bsvc:System_ID>
                </bsvc:Integration_System_Reference>
            </bsvc:Integration_System_Get>
        </soapenv:Body>
    </soapenv:Envelope>"""
    r: requests.Response = requests.post(
        "https://wd2-impl-services1.workday.com/ccx/service/invisors_dpt1/Integration/v39.0",
        data=request,
        headers=header,
    )
    print(r.text)
    tree: ET.Element = ET.fromstring(r.text)

    return tree
