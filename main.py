def on_button_pressed_a():
    global Operator
    Operator += 1
    music.play_tone(262, music.beat(BeatFraction.EIGHTH))
    if Operator == 1:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        basic.pause(500)
        basic.clear_screen()
    else:
        if Operator == 2:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . . . .
            """)
            basic.pause(500)
            basic.clear_screen()
        else:
            if Operator == 3:
                basic.show_leds("""
                    # . . . #
                                        . # . # .
                                        . . # . .
                                        . # . # .
                                        # . . . #
                """)
                basic.pause(500)
                basic.clear_screen()
            else:
                if Operator == 4:
                    basic.show_leds("""
                        . . # . .
                                                . . . . .
                                                # # # # #
                                                . . . . .
                                                . . # . .
                    """)
                    basic.pause(500)
                    basic.clear_screen()
                else:
                    if Operator == 5:
                        basic.show_leds("""
                            . . # . .
                                                        . # . # .
                                                        # . . . #
                                                        . . . . .
                                                        . . . . .
                        """)
                        basic.pause(500)
                        basic.clear_screen()
                    else:
                        Operator = 1
                        basic.show_leds("""
                            . . # . .
                                                        . . # . .
                                                        # # # # #
                                                        . . # . .
                                                        . . # . .
                        """)
                        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global a, b
    music.play_tone(262, music.beat(BeatFraction.EIGHTH))
    if c == 0:
        a += -1
        basic.show_number(a)
    if c == 1:
        b += -1
        basic.show_number(b)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    global c
    basic.clear_screen()
    music.play_tone(262, music.beat(BeatFraction.EIGHTH))
    c += 1
    if c == 2:
        if Operator == 1:
            basic.show_number(a + b)
        else:
            if Operator == 2:
                basic.show_number(a - b)
            else:
                if Operator == 3:
                    basic.show_number(a * b)
                else:
                    if Operator == 4:
                        basic.show_number(a / b)
                    else:
                        basic.show_number(a ** b)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    global a, b
    music.play_tone(262, music.beat(BeatFraction.EIGHTH))
    if c == 0:
        a += 1
        basic.show_number(a)
    if c == 1:
        b += 1
        basic.show_number(b)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_logo_pressed():
    control.reset()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

c = 0
b = 0
a = 0
Operator = 0
Operator = 0
a = 0
b = 0
c = 0
music.play_tone(262, music.beat(BeatFraction.EIGHTH))
basic.show_string("START")