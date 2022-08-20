# sheetdb.py v0.15
sheetdb.py is a python package that make it easier for developer to use [Google Sheet](https://www.google.com/sheets/about/) as a database. Google Sheet has some limitations but even with these limitation, it can be a great database for prototyping.

⚠️ **Note that this project is still under development! Expect breaking changes.**

## Limitations of Google Sheets

| Read Requests [🔗](https://developers.google.com/sheets/api/limits) | Quotas |
| :---         |     :---:      |
| Per minute per user per project | Unlimited |
| Per minute per project | 300 |
| Per minute per user per project | 60|

| Write Requests [🔗](https://developers.google.com/sheets/api/limits) | Quotas |
| :---         |     :---:      |
| Per minute per user per project | Unlimited |
| Per minute per project | 300 |
| Per minute per user per project | 60|

[🔗](https://workspaceupdates.googleblog.com/2022/03/ten-million-cells-google-sheets.html#:~:text=We've%20increased%20the%20cell,%2C%20existing%2C%20and%20imported%20files.) Google sheets has a limit of ten million cells.

## Supported Datatypes
- string
- integer
- float

## Project Development Plans
[🔗 Project Development Plans](https://github.com/users/SarwinR/projects/1)
