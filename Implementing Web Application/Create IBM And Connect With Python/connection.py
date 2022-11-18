import ibm_db


def insertvalues1(USERNAME, EMAIL, MOBILE, PASSWORD):
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=ftx13630;PWD=l4wr4Z1nGI19hj7a;", '', '')
    print("Connected to DB")
    sql = "INSERT INTO verification VALUES('{}', '{}', '{}', '{}')".format(
        USERNAME, EMAIL, MOBILE, PASSWORD)
    ibm_db.exec_immediate(conn, sql)
    print("Number Of Rows Added In Registration: 1")


def insertvalues2(USERNAME, EMAIL, MESSAGE):
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=ftx13630;PWD=l4wr4Z1nGI19hj7a;", '', '')
    print("Connected to DB")
    sql = "INSERT INTO contact VALUES('{}', '{}', '{}')".format(
        USERNAME, EMAIL, MESSAGE)
    ibm_db.exec_immediate(conn, sql)
    print("Number Of Rows Added In Contact: 1")

        

try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=ftx13630;PWD=l4wr4Z1nGI19hj7a;", '', '')
    print("Connected to DB")
    
except:
    print("Not Connected")
