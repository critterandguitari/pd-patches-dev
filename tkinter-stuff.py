from Tkinter import * 
     
sliderw = 50
sliderh = 300
slider1x = 200
slider1y = 10

def onCanvasRelease(event):
    print 'release', event.x, event.y, event.widget
   # canv.itemconfigure(obj2, fill='yellow')
    
def onObjectClick(event):
    print  event.widget.find_closest(event.x, event.y)[0]
    canv.itemconfigure(event.widget.find_closest(event.x, event.y)[0], fill='blue')
    
def onObjectRelease(event):
    print  event.widget.find_closest(event.x, event.y)[0]
    canv.itemconfigure(event.widget.find_closest(event.x, event.y)[0], fill='yellow')
    
def movingSlider(event):
    newy = event.y
    if newy > (slider1y + sliderh) :
        newy = (slider1y + sliderh)
    if newy < slider1y :
        newy = slider1y
    val = sliderh - (newy - slider1y)
    print val
    canv.coords(slider1bg, slider1x, slider1y, slider1x + sliderw, newy)
     
root = Tk()
canv = Canvas(root, width=400, height=400)
obj1 = canv.create_rectangle(  100,   100, 150, 250, fill="yellow")

slider1 = canv.create_rectangle(  slider1x, slider1y, slider1x + sliderw, slider1y + sliderh, fill="red")
slider1bg = canv.create_rectangle(  slider1x, slider1y, slider1x + sliderw, slider1y + sliderh, fill="black")


canv.bind('<ButtonRelease-1>', onCanvasRelease)                

canv.tag_bind(obj1, '<Button-1>', onObjectClick)   
canv.tag_bind(obj1, '<ButtonRelease-1>', onObjectRelease)   

canv.tag_bind(slider1, '<B1-Motion>', movingSlider)
canv.tag_bind(slider1bg, '<B1-Motion>', movingSlider)
 
canv.pack()
root.mainloop()

