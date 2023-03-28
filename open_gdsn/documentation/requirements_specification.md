# OpenGDSN Requirement Specification

This application should allow fetching and submitting product information XML messages using GS1 Global Data Synchronisation Network (GS1 GDSN). Also viewing and modifying CatalogueItemNotification (CIN) messages should be possible.

More information about GS1 GDSN available here:
[https://www.gs1.org/gdsn](https://www.gs1.org/gdsn)

Specifications and implementation guidelines are available here:
[https://www.gs1.org/standards/gdsn](https://www.gs1.org/standards/gdsn)

## Roles

Application is planned to work as single user desktop application. No multiple users or user roles will be implemented in first phase.

It must be possible to define multiple companies with different roles. Data receiver (DR) company role allows subscribing and receiving product information. Data source (DS) role allows submitting and withdrawing product information.

## Connection

In first phase the information will be sent and received to data pool using FTPS connection. Information here:
[https://gs1.fi/sites/default/files/2020-10/GS1_Finland_Synkka_Data_Pool_FTPS_Connectivity_Guide.pdf](https://gs1.fi/sites/default/files/2020-10/GS1_Finland_Synkka_Data_Pool_FTPS_Connectivity_Guide.pdf)

Future development should also investigate AS2 connection possibilities:
[https://gs1.fi/sites/default/files/2020-10/GS1%2BFinland_Synkka_Data_Pool_AS2_Connectivity_Guide.pdf](https://gs1.fi/sites/default/files/2020-10/GS1%2BFinland_Synkka_Data_Pool_AS2_Connectivity_Guide.pdf)

## User Interface

#### DS Trade Item List View

* Data table type view
* Showing list of existing trade items
* Column used for sorting should be selectable
* Search/filter functionality
* From every row, there must be possible to move to trade item edit view
* Import function to allow importing exiting XML CIN messages

#### DS Trade Item Edit View

* Hierarchical view for XML data structure
* Allow adding, removing and modifying nodes
* Implement XSD validation
* Receiver selection

#### DR Trade Item List View

* Similar data table as for DS
* Showing list of received trade items
* From every row, there must be possible to move to trade item read-only view

#### DR Trade Item Read-Only View

* Hierarchical read-only view for XML data structure

#### DR Subscription View

* Manage subscriptions for companies

#### Company management view

* Add, modify and remove companies
* All companies must have following information:
  * Name
  * Global Location Number (GLN)
  * Connection settings
  * Role: DS and/or DR
