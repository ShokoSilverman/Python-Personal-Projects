import mwxml
import time
import pyodbc 
cursor = conn.cursor()
start_time = time.asctime(time.localtime(time.time()))

FILE_TO_PARSE = r'C:\Users\ssilverman\OneDrive - Neumont College of Computer Science\Desktop\Classes\Q5\Persistence Projects\customers.xml'

dump = mwxml.Dump.from_file(open(FILE_TO_PARSE, encoding='utf-8', errors='replace'))
for Customer in dump:
    print(Customer.text)


end_time =  time.asctime(time.localtime(time.time()))
print('start time: ' + start_time)
print('end time: ' + end_time)