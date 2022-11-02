def whenInABreak():
    print("Hello")
    pause_until(input.button_is_pressed(Button.A))


input.button_is_pressed(Button.A)



def on_forever():
    whenInABreak()
    basic.pause(1000)
    pass
basic.forever(on_forever)
