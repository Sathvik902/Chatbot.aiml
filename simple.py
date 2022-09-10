
import aiml
import time
time.clock = time.time

Kernel = aiml.Kernel()
Kernel.learn("std-startup.xml")
Kernel.respond("load aiml b")


while True:
    input_text = input(">Welcome to the chatbot:   ")
    response = Kernel.respond(input_text)
    print("Bot> "+response)