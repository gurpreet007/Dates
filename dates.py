#!/usr/bin/python
import sys
import getopt
from datetime import datetime, timedelta
import pytz

#valid datatime format
#change this if different format is desired
FMT = "%Y-%m-%d %H:%M:%S"

#Converts time in the specified timezone to UTC time
def TZtoUTC(strLocTime, strTz):
    pytzone = pytz.timezone(strTz)
    locTime = datetime.strptime(strLocTime, FMT)
    return pytzone.localize(locTime).astimezone(pytz.utc)
    
def usage():
    print "Valid Options: --dt1, --dt2, --tz1, --tz2, -q"
    print "DateTime format ", FMT, " e.g. ", datetime.strftime(datetime.now(),FMT)


#Return the number of weekdays between two dates
def GetWeekdays(time1, time2):
    #find starting and ending dates
    if time2 > time1:
        endDt = time2
        startDt = time1
    else:
        endDt = time1
        startDt = time2

    #set numWeekDays to 0
    numWeekDays = 0

    #check each day for a weekday till we reach end date
    while(startDt < endDt):
        if startDt.isoweekday() in [1,2,3,4,5]:
            numWeekDays += 1
        startDt = startDt + timedelta(1)

    #return numWeekDays
    return numWeekDays

#start here
if __name__ == '__main__':
    #get the command line options and their values
    try:
        opts, args = getopt.getopt(sys.argv[1:],"q:",["dt1=","dt2=","tz1=","tz2="])
    except getopt.GetoptError as err:
        #wrong option specified
        #so print usage info and exit
        print str(err)
        usage()
        sys.exit(2)

    #initialize variables
    dt1 = ""
    dt2 = ""
    #assume UTC if not timezone is specified
    tz1="UTC"
    tz2="UTC"
    #results will vary depending on if -q is specified or not
    q=""

    #get values from args
    for o, v in opts:
        if o == "--dt1":
            dt1 = v
        elif o == "--dt2":
            dt2 = v
        elif o == "--tz1":
            tz1 = v
        elif o == "--tz2":
            tz2 = v
        elif o == "-q":
            q = v
        else:
            #should never happen
            assert False, "unhandled exception in getopts"

    #show error if dt1 and dt2 are not given
    if dt1=="" or dt2=="":
        print "Enter dates to compare (--dt1 and --dt2)"
        usage()
        sys.exit(2)
    #convert datetimes to UTC
    try:
        time1 = TZtoUTC(dt1, tz1)
        time2 = TZtoUTC(dt2, tz2)
    except ValueError as err:
        print "Error converting time. ", err
        sys.exit(2)

    #find time difference between two datetimes in UTC
    if time1 == time2:
        print "Both datetimes are same. Nothing to do."
        sys.exit(0)
    else:   
        delta = abs(time2 - time1)

    #if -q option is not specified then
    #find the number of days
    if q=="":
        numTotDays = delta.days
        numCompWeeks = numTotDays/7
        numWeekdays = GetWeekdays(time1, time2)
        print "Total Days = ",numTotDays
        print "Complete Weeks = ", numCompWeeks
        print "Number of Weekdays = ", numWeekdays
    #if -q is specified then print datetime difference in
    #desired unit (seconds, minutes, hours or years)
    elif q in ['s','m','h','y']:
        if q == "s":
            print "Seconds: ", delta.total_seconds()
        elif q == "m":
            print "Minutes: ", delta.total_seconds()/60
        elif q == "h":
            print "Hours: ", delta.total_seconds()/3600
        elif q == "y":
            #secs in 1 year = secs in 1 hour * 24 hours * 365 days (approx)
            print "Years: ", delta.total_seconds()/(3600*24*365)
    else:
        print "q must be one of s,m,h,y"
