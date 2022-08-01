# Integration_Security_Tool
## Description
This tool will add security to the ISSG of a selected Integration. It will read date from the integration, determine what security is needed and will at the ISSG to the required domains. If an ISU or ISSG is not found on the integration it will create and add to the Integration

## TODO
### Functionality
- [ ] User input Integration ID
- [ ] Get Integration System
- [ ] If ISU and ISSG Found
    - [ ] Extract ISU
    - [ ] Get ISU
    - [ ] Extract ISSG
    - [ ] Get ISSG
- [ ] If ISU or ISSG not Found
    - [ ] Create ISU
    - [ ] Create ISSG
- [ ] Determine Required Security
    - [ ] EIB
        - [ ] Run 'Report Field Security Report'
            - [ ] Workday Delivered Fields
            - [ ] Calculated Fields?
            - [ ] If report doesn't yet exist create it
        - [ ] Extract domains from Report Response
        - [ ] Aggregate required domains (Don't duplicate)
    - [ ] Connector
        - [ ] TBD Placeholder
    - [ ] Studio
        - [ ] TBD Placeholder
- [ ] Add ISSG to Security
    - [ ] get current Security Domain Config
    - [ ] Add ISSG to current config (Do not overwrite anything!!!)
    - [ ] Submit Security Domain