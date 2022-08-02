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
