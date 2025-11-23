# Item Inventory App (Name WIP)

## Description
- User can add items to a personal database to help keep inventory for their personal belongings or to help keep their online shops organized. (Think ebay sellers)

## Requirements

### Useful Docs
- https://go-upc.com/docs
- https://www.barcodelookup.com/
- https://www.youtube.com/watch?v=IOhZqmSrjlE

### Functional Requirements
- Allow user to manually input data such as name of item, price of item, type of item, quantity of item, date added, barcode number
- Data types:
    - name: string
    - price: float 
    - type: string
    - quantity: int
    - date: ISO date format
    - barcode number: int
- Bar code usable. User can use camera to scan barcode to help with adding of item. When bar code is used, user is then moved to a page to fill out information that isn't auto filled by scanning bar code
- Allow user to manually input barcode
- User's items are displayed in card like fashion with photo of item over name, price, etc.
- Saves items either locally or via database

### Non-functional Requirements 
- User can export item list to csv to allow them to view items in spreadsheet application
- User can make account to make database accessible from any device 
- Have an option to mark item as sold and have stats that keep track of money spent and money made through items 


### Functionality not required


### Limitations