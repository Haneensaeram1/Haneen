def on_button_pressed_a():
  
    basic.show_string("Haneen")
input.on_button_pressed(Button.A, on_button_pressed_a)

x=1
def on_button_pressed_b():
   global x
   x+=2
   basic.show_number(x)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(randint(0, 10))
input.on_gesture(Gesture.SHAKE, on_gesture_shake) 