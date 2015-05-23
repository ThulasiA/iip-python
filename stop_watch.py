# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
x = 0
y = 0
st_run = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    A = t//600
    #B = (t//100)
    #C = t//10
    D = t%10    
    BC = (t // 10) % 60
   
    if BC < 10: 
       BC1 = "0" + str(BC)
    else:
       BC1 = str(BC)
    return str(A) + ":" + BC1 + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():        
    global st_run     
    timer.start()
    st_run = True    
    
def stop():        
    global x
    global y 
    global st_run
    if st_run:   
       timer.stop()
       y += 1    
       if (t%10) == 0:
          x += 1
    
def reset():
    global t
    global x
    global y
    global st_run
    timer.stop()
    t = 0
    y = 0 
    x = 0
    st_run = False

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [110,150], 30, "White")
    canvas.draw_text((str(x) + "/" + str(y)), [250,50], 25, "Green")

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()