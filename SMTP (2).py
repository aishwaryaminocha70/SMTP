from socket import *
def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"
   #mailserver = 'smtp.gmail.com'
   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   # Fill in start
   clientSocket = socket(AF_INET,SOCK_STREAM)
   clientSocket.connect(smtp_client(mailserver))
   # Fill in end
   recv = clientSocket.recv(1024).decode()
   if recv[:3] != '220':
      #print('220 reply not received from server.')
      # Send HELO command and print server response.
      heloCommand = 'HELO Alice\r\n'
      clientSocket.send(heloCommand.encode())
      recv1 = clientSocket.recv(1024).decode()
      #print(recv1)
   if recv1[:3] != '250':
      #print('250 reply not received from server.')
      #Send MAIL FROM command and print server response.
      #Fill in start
      mailFrom = "MAIL FROM: <bubbamcbubba99@gmail.com> \r\n"
      clientSocket.send(mailFrom.encode())
      recv2 = clientSocket.recv(1024).decode
      #print("After MAIL FROM command: "+recv2)
   if recv2[:3] != '250':
      # Fill in end
      # Send RCPT TO command and print server response.
      # Fill in start
      rcptTo = "RCPT TO: <willmcwork@outlook.com> \r\n"
      clientSocket.send(rcptTo.encode())
      recv3 = clientSocket.recv(1024).decode
      #print("After RCPT TO command: "+recv3)
   if recv3[:3] != '250':
      # Fill in end
      # Send DATA command and print server response.
      # Fill in start
      data = "DATA\r\n"
      clientSocket.send(data.encode())
      recv3 = clientSocket.recv(1024).decode
   if recv3[:3] != '250':
      # Fill in end
      # Send message data.
      # Fill in start
      clientSocket.send(msg.encode())
      # Fill in end
      # Message ends with a single period.
      # Fill in start
      endmsg ='\r\n.\r\n'
      clientSocket.send(endmsg.encode())
      recv4 = clientSocket.recv(1024).decode
   if recv4[:3] != '250':
      # Fill in end
      # Send QUIT command and get server response.
      # Fill in start
      clientSocket.send("QUIT\r\n".encode())
      message=clientSocket.recv(1024).decode
      #print (message)
      clientSocket.close()
      # Fill in end
if __name__ == '__main__':
   smtp_client(port=1025, mailserver='127.0.0.1')
