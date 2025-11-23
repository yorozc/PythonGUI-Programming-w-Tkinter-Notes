==================================
 ABQ Data Entry Program specification
==================================

Description 
------------
This program faciliatates entry of laboratory observations into a CSV file 

Requirements
------------
Functional Requirements:
    * Allow all relevant, valid data to be entered, as per the data dictionary
    * Append entered data to the CSV file:
    - The CSV fiel must have a filename of abq_data_record_CURRENTDATE.csv, where CURRENTDATA is the date of the laboratory observations 
        in ISO format (Year-month-day).
    - The CSV file must include all fields listed in the data dictionary 
    - The CSV headers will avoid cryptic abbreviations. 
    * Enforce correct datatypes per fields

Non-functional Requirements: 
    * Enforce reasonable limits on data entered, per the data dict.
    * Auto-fill data to save time.
    * Suggest likely correct values. 
    * Provide a smooth and efficient workflow.
    * Store data in a format easily understandable by Python.

Functionality Not Required 
--------------------------
The program does not need to: 

    * Allow editing of data 
    * Allow deletion of data 
Users can perform both actions in LibreOffice if needed

Limitations
-----------

The program must:

    * Be efficiently operable by keyboard-only users 
    * Be accessible to color blind users. 
    * Run on Debian GNU/Linux 
    * Run acceptably on a low-end PC 