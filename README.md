# sheetdb.py
sheetdb.py is a python package that make it easier for developer to use [Google Sheet](https://www.google.com/sheets/about/) as a database. Google Sheet has some limitations but even with these limitation, it can be a great database for prototyping.

⚠️**Note that this project is still under development! Expect breaking changes.**

## Limitation of Google Sheets
### [Read Requests	](https://developers.google.com/sheets/api/limits)
| Description | Quotas |
| :---         |     :---:      |
| Per minute per user per project | Unlimited |
| Per minute per project | 300 |
| Per minute per user per project | 60|

### [Write Requests	](https://developers.google.com/sheets/api/limits)
| Description | Quotas |
| :---         |     :---:      |
| Per minute per user per project | Unlimited |
| Per minute per project | 300 |
| Per minute per user per project | 60|

### [Cell Limit](https://workspaceupdates.googleblog.com/2022/03/ten-million-cells-google-sheets.html#:~:text=We've%20increased%20the%20cell,%2C%20existing%2C%20and%20imported%20files.)
Google sheets has a limit of ten million cells.

## Supported Datatypes
- string
- integer
- float

## To Do List v1
### Table
- [x] Ability to create tables
- [ ] Ability to alter tables
- [ ] Ability to delete tables
- [ ] Ability to select tables

### Data
- [x] Ability to insert data into tables
- [ ] Ability to modify data
- [ ] Ability to delete data from table
- [ ] Ability to query data from table
