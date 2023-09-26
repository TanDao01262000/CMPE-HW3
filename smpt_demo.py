from socket import *

msg = "\r\nI love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (use the free SMTP server) and call it mailserver
mail_server = "smtp.freesmtpservers.com"

# Create a socket called clientSocket and establish a TCP connection with mailserver
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((mail_server, 25))

recv = client_socket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from the server.')

# Send HELO command and print server response.
hello_command = 'HELO Alice\r\n'
client_socket.send(hello_command.encode())
recv1 = client_socket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from the server.')

# Send MAIL FROM command and print server response.
mail_from_command = "MAIL FROM: <tankhanhdao@example.com>\r\n"  # Replace with your sender's email address
recv2 = client_socket.recv(1024).decode()
print(recv2)
if recv2[:2] != '250':
    print('250 reply not received from the server')

# Send RCPT TO command and print server response.
rcpt_to_command = "RCPT TO: <tankhanhdao@example.com>\r\n"  # Replace with your receiver's email address
client_socket.send(rcpt_to_command.encode())
recv3 = client_socket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from the server')

# Send DATA command and print server response.
data_command = 'DATA\r\n'
client_socket.send(data_command.encode())
recv4 = client_socket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from the server')

# Send message data.
client_socket.send(msg.encode())

# Message ends with a single period.
client_socket.send(endmsg.encode())

# Send QUIT command and get server response.
quit_command = 'QUIT\r\n'
client_socket.send(quit_command.encode())
recv5 = client_socket.recv(1024).decode()
print(recv5)
if recv5[:3] != '221':
    print('221 reply not received from the server')

client_socket.close()
