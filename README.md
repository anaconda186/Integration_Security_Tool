# Integration_Security_Tool
## Description
This tool will migrate a user defined ISSG and its attached ISU from the source tenant to the destination tenant

## TODO
### Functionality
- [ ] Get ISSG
    - [X] Parse User Arguments
    - [ ] Get Security Group Web Service
- [ ] Parse ISSG
    - [ ] Extract ISU
    - [ ] Extract Security Domains
- [ ] Check Destination Tenant 
    - [X] Get ISU (Web Service)
    - [X] Get ISSG (Web Service)
    If Not Found
    - [ ] Create ISU (Web Service)
    - [ ] Create ISSG (Web Service)
- [ ] Add ISSG to Security
    - [ ] get Security Domain Config (Web Service) from Source Tenant
    - [ ] Add ISSG to Security Domain Config (Do not overwrite anything!!!) in Destination
        - [X] Submit Security Domain (Web Service)