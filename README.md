# LIONS Database Analysis Tools

## Getting Started
The software contained in this package was written for Python 3.7. You will need

To get started, from your terminal, run the Makefile:

```
make
```

This will install the required Python packages for this package. Next, you must activate the virtual environment, which will make it so the Python binary you're running contains the required packages.

```
source venv/bin/activate
```

Finally, you're ready to go.

## Downloading the data
Downloading the most recent data from LIONS is made simple with the download.py file.

From the top level directory of this package, simply run:

```
python -m lions.download
```
This will download the entire LIONS dump into the data directory

If you would only like to download certain disks, you can add the optional argument '-s' or '--select' to the end, as follows:

```
python -m lions.download --select DISK01
```

## Parsing the data
Provided in parse.py is the parser for each table in the LIONS database, which will give you the SQL formatting of table, and a list of the rows themselves. This is useful if you'd like to perform any kind of analysis.

The following will give you every case in Python list format (warning: takes a long time and a massive amount of space)

```
from lions.parse import *

sql, data = gs_case()
```

If you only want certain columns, you can add the optional argument 'columns' to any of the functions:

```
from lions.parse import *

sql, data = gs_case(columns=['DISTRICT', 'ID', 'LEAD_CHARGE'])
```

## Initializng the database
The package contains a file that will initialize a PostgreSQL database. After running the database program in the background on localhost, running the following script will recreate LIONS in its entirety, for you to query as you please. Note that this script is not compatible if the database running has authentication enabled.

```
python -m lions.sqlize
```

This script can take a very long time to complete. If you'd only to insert a few tables, comment out the lines in the code you don't wish to run.
