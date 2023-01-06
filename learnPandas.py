from logging import currentframe
from numpy.core.fromnumeric import sometrue
import pandas as pd
import mysql.connector
import datetime
from pymongo import MongoClient
import matplotlib.pyplot as plt



#Simon notes
#use a for loop with largest list len - current list len and fill with null to make sure all lists are same size
current_time = datetime.datetime.now()
str_current_time = str(current_time.month) + '/' +  str(current_time.day) + '/' + str(current_time.year) + ' ' + str(current_time.hour) + 'h:' + str(current_time.minute) + 'm:' + str(current_time.second) + 's'

# plist = pd.Series(1, 2, "string", True)

#create a dict and feed it into a dataframe
data = {
    'apples': [3, 2, 0, 1], #the lists are called series
    'oranges': [0, 3, 7, 2] #each list must be the same length
    }

purchases = pd.DataFrame(data)
# print(purchases)
# print(purchases.loc[0]) #use the auto index to locate
# print(purchases.loc[0,'apples']) #grab a single field from an item
# purchases.loc[0,'apples'] = 5 #updating a value in the dataframe in a specific field
# print(purchases.loc[0,'apples'])

#create a dataframe with an index
people_purchases = pd.DataFrame(data, index=["Simon", "Marc", "Easterly", "Jakob"])#index list size must match series size
#print(people_purchases)
#print(people_purchases.loc["Marc"]) #locate an item in the datafram using user defined index
#print(people_purchases.loc["Marc", 'oranges']) #locate a field in the dataframe using user defined index and and key
#people_purchases.loc["Marc", 'oranges'] = 25 #locate a field in the dataframe using user defined index and and key and update it
#print(people_purchases.loc["Marc", 'oranges'])

csv_read = pd.read_csv("Python\Python Files\simple_CSV.csv") #importing csv file as a dataframe
print(csv_read)

# csv_read_index_col = pd.read_csv("Python\Python Files\simple_CSV.csv", index_col=0) #importing csv file as a dataframe using column 0 as the index
# print(csv_read_index_col)

# json_read = pd.read_json("Python\Python Files\simple_JSON.json") #load a json file into a dataframe, automatically uses headers
# print(json_read)

mydb = mysql.connector.connect(user='root', password='test',
                              host='127.0.0.1', database="python_db")
mycursor = mydb.cursor()
#print(mydb)
# table = pd.read_sql_query("SELECT * FROM test_crud_table;", mydb) #create a dataframe using a sql table
# print(table)
#table = pd.read_sql_query("SELECT * FROM test_crud_table;", mydb, index_col='Id') #create a dataframe using a sql table and setting the index column to a column name
#print(table)
# print(table.loc[1, 'FirstName'])
#table.loc[1, 'FirstName'] = 'Simon'
#print(table.loc[1, 'FirstName'])
# print(table[table.eq(' LAMBERT').any(1)]) #find all columns where any field contains specific value
# print(table.loc[(table['FirstName'] == ' VERA')]) #find all columns where specific field is a specific value

#purchases.to_csv("Python/Python Files/fruit_CSV_out.csv") #write a dataframe to a csv file
#purchases.to_json("Python/Python Files/fruit_JSON_out.json") #write a dataframe to a json file
#print(str_current_time)
#mycursor.execute("drop table if exists simple_people; CREATE TABLE simple_people (Id INT PRIMARY KEY, FirstName VARCHAR(50), LastName VARCHAR(50), HireYear Int)")
#mycursor.execute("""LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\python_db\\simple_CSV.csv' INTO TABLE simple_people FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '/n' IGNORE 1 ROWS;""")

myclient = MongoClient('localhost', 27017)
mydb = myclient['employee_database']
mycol = mydb["employees"]
my_new_col = mydb["new_employees"]
new_db = myclient['db']
restaurants = new_db['restaurants']
#employee_table = pd.DataFrame(mydb.employee.find({})) #create a dataframe using  a mongo table
# print(employee_table)
# my_new_col.insert_many(employee_table.to_dict('records')) #load the dataframe back into mongo and makes sure they are records




# time to do some more data viewing and manipulation -----------------------------------------------

#temp_df = employee_table #creating a temporary dataframe to manipulate so i dont break mine

#going to use the mongo dataframe for this because of its size, but any dataframe would work

# print(employee_table.head()) #prints the first five items of a dataframe by default but can take in a paramater to show a different amount
# print(employee_table.head(2))

# print(employee_table.tail()) #prints the last five items of a dataframe by default but can take in a paramater to show a different amount
# print(employee_table.tail(10))

#employee_table_size = str(len(employee_table))
#print(employee_table_size)
# new_employee_vals = {'_id' : 'cool_id', 'id' : employee_table_size, 'first_name' : 'Simon', 'last_name' : 'silverman', 'hire_date' : '2003'} #creating a key that does not already exist will give a null value to all previous items
# employee_table = employee_table.append(new_employee_vals, ignore_index='true') #put a new row onto the end of the series | ignore index forces it to use the same index as the rest of the dataframe 
# print(employee_table.tail(2))

#print(len(employee_table)) #gets the length of the dataframe
#print(employee_table.info()) #returns the properties of your dataframe
#print(employee_table.shape) #returns (rows, columns)

#duplicate handling
# print(temp_df.shape)
# temp_df = temp_df.append(employee_table)
# print(temp_df.shape)
# print(temp_df.loc[temp_df['id'] == '1']) #see that there is duplicate
# temp_df.drop_duplicates(inplace=True, keep='first') #inplace means you do not have to redifine the dataframe var | keep has first, last, and False. first will keep the first of each duplicate, last will keep the last, and false will drop all, defaults to first
# print(temp_df.shape)#size has dropped down
# print(temp_df.loc[temp_df['id'] == '1']) #see that the duplicates are gone

#column cleanup
#print(temp_df.columns) #returns all the columns in a dataframe
# temp_df.rename(columns = {
#     '_id' : 'new__id', 'id' : 'new_id', 'first_name' : 'new_first_name', 'last_name' : 'new_last_name', 'hire_date' : 'new_hire_date'
# }, inplace=True) #pass in a dict of old names as the key and new names as the value to rename the columns
# print(temp_df.columns)
# temp_df.columns=['test__id', 'test_id', 'test_first_name', 'test_last_name', 'test_hire_date'] #can also pass in a list of the new column names but it requires the knowledge of what order you want the column names
# print(temp_df.columns)
# temp_df.columns=[col.upper() for col in temp_df] #can use list comprehension to change the column names
# print(temp_df.columns)
# temp_df.columns=[col.lower() for col in temp_df] #can use list comprehension to change the column names
# print(temp_df.columns)

#working with missing values
data_with_nulls = pd.read_csv("Python Files\DataWithNulls.csv", index_col=0)
#print(data_with_nulls.shape)
#print(data_with_nulls)
#print(data_with_nulls.isnull()) #returns rows on a dataframe and shows if they contain nulls (true) or non null (false)
#print(data_with_nulls.loc[4].isnull()) #returns a single row and shows if it has nulls
#print(data_with_nulls.head(3).isnull()) #can be connected to .head or .tail
#print(data_with_nulls.isnull().sum()) #returns the amount nulls in each column in the entire dataframe
#data_without_nulls = data_with_nulls.dropna() #drops all rows with null value
#print(data_without_nulls.shape)
#print(data_without_nulls.isnull().sum()) #shows that it has no nulls
#data_with_nulls.dropna(inplace=True) #inplace can be specified to allow you to drop all nulls within the dataframe
#print(data_with_nulls.shape)
#print(data_with_nulls.isnull().sum()) #shows that it has no nulls
# data_without_nulls = data_with_nulls
# print(data_without_nulls.columns)
# data_without_nulls = data_with_nulls.dropna(axis=1) #drops all columns with null values, can also be done with inplace
# print(data_without_nulls.columns) #shows that no columns are left because all columns had null values
    #imputation (keeping valuable data that has nulls)
#data_with_nulls_age = pd.read_csv("Python\Python Files\Data_With_Nulls_Age.csv", index_col=0)
#print(data_with_nulls_age)
#ages = data_with_nulls_age['age'] #creates a series from the column email
#print(ages)
# print(ages.mean()) #returns the average of a column
# print(ages.sum()) #returns the sum of the column
# print(ages.isnull().sum())
# ages.fillna(ages.mean(), inplace=True) #replaces all null values with the mean of the series
# print(ages.isnull().sum())

#data info
#print(data_with_nulls.describe()) #returns a summary of the dataframe information
# print(data_with_nulls['last_name'].describe()) #returns a summary of a single column in a dataframe
#print(data_with_nulls['last_name'].value_counts().head()) #shows the amount of each val in the column
#print(data_with_nulls['last_name'].value_counts())

#slicing, selecting, extracting
#full_name = data_with_nulls[['first_name', 'last_name']] #creating a subset of a dataframe by specifying multiple columns
#print(full_name)
# print(full_name.loc[3]) #locates using the user given index, this one just happens to already be a number
# print(full_name.iloc[2]) #locates using the pandas given 0 base numerical index
# print(full_name.loc[1:3]) #locates the fields with the user given index with a starting and finishing index
# print(full_name.iloc[0:2]) #locates the fields with the pandas given index with a starting and finishing index, exludes final index
    #conditional selections
# print(data_with_nulls['first_name'] == 'Delmar') #returns the table and shows true if the field matches
# print(data_with_nulls[data_with_nulls['first_name'] == 'Jodie']) #returns all rows that match the given data | works with all operants (>, !=, (== | ==), etc...)
# print(data_with_nulls[data_with_nulls['first_name'] != 'Jodie']) #returns all rows that does not match the given data
# print(data_with_nulls[(data_with_nulls['first_name'] == 'Jodie') | (data_with_nulls['last_name'] == 'Maeer')]) #can se or/and, must be done with |/&
# print(data_with_nulls[data_with_nulls['first_name'].isin(['Jodie', 'Delmar'])]) #consice way to return all rows and check multiple options within a field

#applying functions
def is_old(x):
    if x >= 50:
        return 'old'
    elif x<50:
        return 'young'
    else:
        return 'no age'
# data_with_nulls_age['young_old'] = data_with_nulls_age['age'].apply(is_old) #can add a new column and set the values to be a function return | iterates 
# print(data_with_nulls_age.head(10))
# data_with_nulls_age['young_old'] = data_with_nulls_age['age'].apply(lambda x: 'old' if x>=50 else ('young' if x<50 else 'no age')) #works with lambdas too
# print(data_with_nulls_age.head(10))

#Plotting
#plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) #sets font and plot size for the plot
# movies_df.plot(kind='scatter', x='rating', y='revenue_millions', title='Revenue (millions) vs Rating');
#data_with_nulls_age_no_index = pd.read_csv("Python\Python Files\Data_With_Nulls_Age.csv") #I dont want to manual index on this, I want to call the id field
#data_with_nulls_age_no_index.plot(kind='scatter', x='id', y='age', title='id-age relation') #creates a scatterplot based on two columns in the dataframe
# data_with_nulls_age_no_index['age'].plot(kind='hist', title='ages') #creates a histogram of a series
# data_with_nulls_age_no_index['age'].plot(kind='box', title='ages') #creates a boxplot of a series

#plt.show() #shows the plots









