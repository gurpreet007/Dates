## Usage of dates.py program

### What it does
1. Find out the number of days between two datetime parameters.
2. Find out the number of weekdays between two datetime parameters.
3. Find out the number of complete weeks between two datetime parameters.
4. Accept a third parameter to convert the result of (1, 2 or 3) into one of seconds, minutes, hours, years.
5. Allow the specification of a timezone for comparison of input parameters from different timezones.

### pytz module
This program uses pytz module for conversion between timezones.
pytz comes as default with Python on Mac OS X, for Cent OS please follow the below steps (as root):
```sh
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py
# pip install pytz
```
### Invocation
Run as:
```sh
$ python dates.py <options>
```
or
```sh
$ chmod u+x dates.py
$ ./dates.py <options>
```


### Datetime format
The default datatime format is "%Y-%m-%d %H:%M:%S", e.g. "2017-12-23 17:59:59". This is controlled by the FMT constant near the top the program.

### Timezones
The program takes TZ timezones in the style *continent*/*city* as mentioned in the TZ column of [this Wikipedia page](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) e.g. "Australia/Adelaide"

### Valid options

**--dt1**
This is the first datetime string

**--dt2**
This is the second datetime string

**--tz1**
This is the timezone for first datetime (dt1), UTC is used as default

**--tz2**
This is the timezone for second datetime (dt2), UTC is used as default

**-q**
Show time difference in (s)econds, (m)inutes, (h)ours or (y)ears


### Example Usage
Show number of days, total weeks and week days between two dates
```sh
./dates.py --dt1="2017-08-08 00:00:00" --dt2="2017-08-17 00:00:00"
```
Show number of days, total weeks and week days between two dates in different time zones
```sh
/dates.py --dt1="2017-08-08 00:00:00" --dt2="2017-08-17 00:00:00"  --tz2="Australia/Adelaide"  --tz1="Asia/Kolkata"
```
Show number of hours between two datetimes in different timezones
```bash
./dates.py --dt1="2017-08-08 00:00:00" --dt2="2017-08-08 00:00:00" -q h --tz1="Australia/Adelaide"  --tz2="Asia/Kolkata"
```
