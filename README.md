## library-cli

a Python CLI book management tool


### Requirements
* Python 3.10+

### Installation

- clone this repo\
`git clone git@github.com:abe511/library-cli.git`

- go to the app directory\
`cd library-cli`

- run\
`python main.py`

- run with custom database file name\
`python main.py <your_db_filename>`

### Test

`python -m unittest discover tests`

### Usage


#### Navigate using main menu

press number keys from `1` to `6` to run commands:

`1` - **add** a book\
type in the **Title**, **Author** and the **Year** of the book and press `Enter`\
press `Enter` once again to go to the main menu

`2` - **remove** the book\
type in the **ID** of the book and press `Enter`

`3` - **search** the book\
provide the **Title** or **Author** or **Year** of the book, or any combination of these to find the books matching the criteria\
*providing incorrect year input will not affect search results since all field are optional*

`4` - **show** all books\
generates a table of all the books stored in the db

`5` - **change status** of a book\
provide the **ID** of the book to change it's status\
choose between statuses by pressing corresponding keys: `1` or `2` and press `Enter`

`6` - **exit**
