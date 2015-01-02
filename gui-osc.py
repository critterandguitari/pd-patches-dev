#from Tkinter import * 
import Tkinter 
import os
import socket
import subprocess

import random

from pythonosc import osc_message_builder
from pythonosc import udp_client

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

#pd = subprocess.Popen(["/Applications/Pd-0.46-4.app/Contents/MacOS/Pd", "/Users/owen/pd-patches-dev/patches/mother.pd"])

# TODO :  make helper module, include functions like these :
def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

class Slider:
    def __init__(self, canvas, name, x0, y0, w, h, callback):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0 + w
        self.y1 = y0 + h
        self.height = h
        self.callback = callback
        self.sliderid = canvas.create_rectangle( self.x0, self.y0, self.x1, self.y1, fill="red")
        self.sliderbgid = canvas.create_rectangle( self.x0, self.y0, self.x1, self.y1, fill="black")
        canvas.tag_bind(self.sliderid, '<B1-Motion>', self.moveit)
        canvas.tag_bind(self.sliderbgid, '<B1-Motion>', self.moveit)
        canvas.tag_bind(self.sliderid, '<Button-1>', self.moveit)
        canvas.tag_bind(self.sliderbgid, '<Button-1>', self.moveit)
        
    def moveit(self, event):
        newy = event.y
        if newy > (self.y0 + self.height) :
            newy = (self.y0 + self.height)
        if newy < self.y0 :
            newy = self.y0
        val = self.height - (newy - self.y0)
        self.callback(self.name, float(val) / self.height)
        event.widget.coords(self.sliderbgid, self.x0, self.y0, self.x1, newy)

class Key:
    def __init__(self, canvas, name, x0, y0, w, h, callback):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0 + w
        self.y1 = y0 + h
        self.callback = callback
        self.buttonid = canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill="yellow")
        canvas.tag_bind(self.buttonid, '<Button-1>', self.onclick)   
        canvas.tag_bind(self.buttonid, '<ButtonRelease-1>', self.onrelease)
    
    def onclick(self, event):  
        self.callback(self.name, 1)
        canv.itemconfigure(self.buttonid, fill='blue')  
        
    def onrelease(self, event):
        self.callback(self.name, 0)
        canv.itemconfigure(self.buttonid, fill='yellow')   

class ClickPatch:
    global pd
    def __init__(self, canvas, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.textid = canvas.create_text(x, y, font="Purisa", text=self.name)
        canvas.tag_bind(self.textid, '<ButtonRelease-1>', self.onclick)
    def onclick(self, event):
        print self.name
        pd.kill()
        pd = subprocess.Popen(["/Applications/Pd-0.46-4.app/Contents/MacOS/Pd", "/Users/owen/pd-patches-dev/patches/mother.pd", self.name])
        
#oh my god why didnt he ... what?


def onchange(name, val) :
    print  str(name) + ": " + str(val)
    sock.sendto(str(name) + " " + str(val) + ";\n", (UDP_IP, UDP_PORT))


#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
                     
                     
client = udp_client.UDPClient(UDP_IP, UDP_PORT)
msg = osc_message_builder.OscMessageBuilder(address = "/filter")
msg.add_arg(random.random())
msg = msg.build()
client.send(msg)

root = Tkinter.Tk()
canv = Tkinter.Canvas(root, width=800, height=600)

kx = -80
ky = -50

button1 =  Key(canv, 'key 1', 100 + kx, 500 + ky, 40, 100, onchange)
button2 =  Key(canv, 'key 2', 125 + kx, 390 + ky, 40, 100, onchange)
button3 =  Key(canv, 'key 3', 150 + kx, 500 + ky, 40, 100, onchange)
button4 =  Key(canv, 'key 4', 175 + kx, 390 + ky, 40, 100, onchange)
button5 =  Key(canv, 'key 5', 200 + kx, 500 + ky, 40, 100, onchange)
button6 =  Key(canv, 'key 6', 250 + kx, 500 + ky, 40, 100, onchange)
button7 =  Key(canv, 'key 7', 275 + kx, 390 + ky, 40, 100, onchange)
button8 =  Key(canv, 'key 8', 300 + kx, 500 + ky, 40, 100, onchange)
button9 =  Key(canv, 'key 9', 325 + kx, 390 + ky, 40, 100, onchange)
button10 = Key(canv, 'key 10', 350 + kx, 500 + ky, 40, 100, onchange)
button11 = Key(canv, 'key 11', 375 + kx, 390 + ky, 40, 100, onchange)
button12 = Key(canv, 'key 12', 400 + kx, 500 + ky, 40, 100, onchange)
button13 = Key(canv, 'key 13', 450 + kx, 500 + ky, 40, 100, onchange)
button14 = Key(canv, 'key 14', 475 + kx, 390 + ky, 40, 100, onchange)
button15 = Key(canv, 'key 15', 500 + kx, 500 + ky, 40, 100, onchange)
button16 = Key(canv, 'key 16', 525 + kx, 390 + ky, 40, 100, onchange)
button17 = Key(canv, 'key 17', 550 + kx, 500 + ky, 40, 100, onchange)
button18 = Key(canv, 'key 18', 575 + kx, 390 + ky, 40, 100, onchange)
button19 = Key(canv, 'key 19', 600 + kx, 500 + ky, 40, 100, onchange)
button20 = Key(canv, 'key 20', 650 + kx, 500 + ky, 40, 100, onchange)
button21 = Key(canv, 'key 21', 675 + kx, 390 + ky, 40, 100, onchange)
button22 = Key(canv, 'key 22', 700 + kx, 500 + ky, 40, 100, onchange)
button23 = Key(canv, 'key 23', 725 + kx, 390 + ky, 40, 100, onchange)
button24 = Key(canv, 'key 24', 750 + kx, 500 + ky, 40, 100, onchange)

auxbutton = Key(canv, 'aux', 500, 100, 50, 50, onchange)

slider1 = Slider(canv, 's1',  20, 10, 80, 265, onchange)
slider2 = Slider(canv, 's2', 120, 10, 80, 265, onchange)
slider3 = Slider(canv, 's3', 220, 10, 80, 265, onchange)
slider4 = Slider(canv, 's4', 320, 10, 80, 265, onchange)



canv.pack()

root.mainloop()

