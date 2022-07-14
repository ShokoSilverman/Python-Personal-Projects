# import Imports.Silver_ODBC as Sil_ODBC
from Imports.Silver_ODBC import SQL_server as Silver_ODBC_SQL_server
from Imports.Silver_ODBC import My_SQL as Silver_My_SQL
from Imports.Silver_ODBC import MongoDB as Silver_MongoDB
from Imports.Silver_ODBC import Neo4j as Silver_Neo4J

# SQL_server = Silver_ODBC_SQL_server(server_name='LAPTOP-L46BVJII', database='sql_test')
# My_SQL = Silver_My_SQL('root', 'test', '127.0.0.1', 'python_db')
# mongo = Silver_MongoDB('localhost',27017, 'testMongoSilver')
neo4j = Silver_Neo4J("bolt://localhost:7687", 'neo4j', 'password')

def main():

    #------------SQL SERVER-----------------

    # SQL_server.test_con()
    # print(SQL_server.query("insert into simple_people Values(9,'Liam', 'Douglas',2022)"))
    # print(SQL_server.query_df("select * from simple_people"))
    # SQL_server.insert_one('simple_people',(3, 'Alex', 'Turro', 2022))
    # bulk_insert_list = [(4, 'Tristyn', 'Kahrs', 2022), (5, 'Robert', 'Brunney', 2022)]
    # SQL_server.insert_many('simple_people', bulk_insert_list, 4)
    # SQL_server.read('simple_people')
    # SQL_server.read('simple_people', ['Id', 'LastName'], 'Id')
    # SQL_server.update('simple_people', {'Id':1}, {'FirstName':"'Grayson'", 'LastName':"'Sudweeks'"})
    # SQL_server.delete('simple_people', {'FirstName':"'David'"})

    #-------------MYSQL------------------------------

    # My_SQL.test_con()
    # print(My_SQL.query("insert into simple_people Values(9,'Liam', 'Douglas',2022)"))
    # print(My_SQL.query_df("select * from simple_people"))
    # My_SQL.insert_one('simple_people',(3, 'Alex', 'Turro', 2022))
    # bulk_insert_list = [(4, 'Tristyn', 'Kahrs', 2022), (5, 'Robert', 'Brunney', 2022)]
    # My_SQL.insert_many('simple_people', bulk_insert_list, 4)
    # My_SQL.read('simple_people')
    # My_SQL.read('simple_people', ["Id", "LastName"], 'Id')
    # My_SQL.update('simple_people', {'Id':1}, {'FirstName':"'Grayson'", 'LastName':"'Sudweeks'"})
    # My_SQL.delete('simple_people', {'FirstName':"'David'"})

    #-----------------Mongo-------------------------------
    
    # mongo.test_con()
    # mongo.insert_one('testCol', {'name':'Simon', 'age':19, 'hireyear':2022})
    # bulk_insert_list = [{'name':'Tobie', 'age':20}, {'name':'Grayson', 'age':19}]
    # mongo.insert_many('testCol', bulk_insert_list)
    # for item in mongo.read('testCol'):
    #     print(item)
    # for item in mongo.read('testCol', {'age':19, 'name':'Simon'}):
    #     print(item)
    # mongo.update_one('testCol', {'name':'Alex'}, {'name':'Tobie'})
    # mongo.update('testCol', {'name':'Tobie'}, {'name':'Alex'})
    # mongo.delete('testCol', {'name':'Tobie', 'age':19})
    # mongo.delete('testCol', {'$or': [{'name':'Tobie'}, {'name': 'Grayson'}]})


    #---------------------Neo4j-----------------------------
    
    neo4j.test_con()

    pass






if __name__ == '__main__':
    main()
    print('---------------------------------\nprogram is complete')