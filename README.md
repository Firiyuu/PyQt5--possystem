# POS System

POS System for undergraduate thesis.

## Installation

Clone the repository to the pi, make sure that "new" is within /home/pi/. This way the path could be traced as /home/pi/new when connecting to the database and other stuff

To run the barcode scanner

```bash
cd /home/pi/new
sudo python main.py
```
To run the interface

```bash
cd /home/pi/new/env
source bin/activate #this creates a new virtualenv
cd /home/pi/new/paper-dashboard-master
python app.py
```


## Usage

Mouse should be on terminal when scanning.


## License
[MIT](https://choosealicense.com/licenses/mit/)