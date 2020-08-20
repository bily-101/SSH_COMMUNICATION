import os
import socket

message = input("What is your message?: ")
type = input("Send through whole server or this chat?\n"+
  "W for whole server C for just the chat :"
  )

if (type=="W"):
  os.system(f"echo {message} | wall")
else: 
  print("not available")

