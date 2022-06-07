input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("Haneen")
})
let x = 1
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    x += 2
    basic.showNumber(x)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showNumber(randint(0, 10))
})
