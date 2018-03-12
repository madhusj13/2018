import argparse,re,datetime
from time import strptime
import pytz
strptime('Feb','%b').tm_mon

def convert_timezone(line):
        regex = re.compile('(\d+:\d+:\d+)\s+')
        datetimeFormat = '%H:%M:%S'
        old_timezone = pytz.timezone("GMT")
        new_timezone = pytz.timezone("US/Pacific")
        new_line = regex.sub(\
                        lambda m: m.group().replace(m.group(0), '%s ' %(old_timezone.localize(datetime.datetime.strptime(\
                        m.group(1), datetimeFormat)).astimezone(new_timezone).strftime('%H:%M:%S'))), line)  
        new_line = re.sub('\+[0-9]{1,5}', '-8000', new_line)     
        return new_line
        
def parse_logfile(file,key):
    """
    Reads the log file
    parses the logfile for the key
    counts the number of line where the key appears in the log file
    Computes the mean between each timestamp
    finally converts all the time stamps from UTC to PST
    """

    count = 0
    datetimeFormat = '%m %d %H:%M:%S'
    diff = 0 
    temp = None


    with open(file,'r') as f:
        for line in f:
            if re.search(key.lower(),line.lower()):
                count += 1
                match_object = re.search('([a-zA-Z]{1,4})\s+(\d+)\s+(\d+:\d+:\d+)',line)
                if match_object:
                    time_stamp = '%s %s %s' %(
                        strptime(match_object.group(1), '%b').tm_mon,
                        match_object.group(2),
                        match_object.group(3),
                    )
                    if temp:
                        diff += (datetime.datetime.strptime(time_stamp, datetimeFormat) - \
                        datetime.datetime.strptime(temp, datetimeFormat)).total_seconds()
                        print (diff)
                    temp = time_stamp             
                    print (convert_timezone(line))

    print ('count is %s' %count)
    print ('The average delay between each log occurence is %s' %float(diff/(count-1)))

if __name__=='__main__':
    """
    usage: parse_logfile.py [-h] key filename

    Enter a keyword

    positional arguments:
    key         keyword to parse
    filename    location of the logfile
    """
    parser = argparse.ArgumentParser(description='Enter a keyword')
    parser.add_argument('key', 
                    help='keyword to parse')
    parser.add_argument('filename', 
                    help='location of the logfile')
    args = parser.parse_args()
    parse_logfile(args.filename,args.key)

