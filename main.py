import os
import socket
import getpass

user = getpass.getuser()


message = input("What is your message?: ")
type = input("Send through whole server or this chat?\n"+
  "W for whole server C for just the chat :"
  )

if (type=="W" or type=="w"):
  os.system(f"echo Public Message from {user}: {message} | wall -n")
else: 
  print("not available")
if (type=="C" or type=="c"):
    forwardUser = input("Who are you sending this private message too \n" + 
                       "Type username if you know \n" +
                       "Or type w to see who is available \n" +
                        ": "
                       )
    if (forwardUser=="w"):
        os.system("who")
        second = input(f"Who would you like to message?")
        os.system(f"echo Private message from {user}: {message} | write {second}")

    else:
        os.system(f"echo Private message from {user}: {message} | write {forwardUser}")
print("Thankyou bye!!")
