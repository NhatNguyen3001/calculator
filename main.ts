input.onButtonPressed(Button.A, function () {
    Operator += 1
    music.playTone(262, music.beat(BeatFraction.Eighth))
    if (Operator == 1) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.pause(500)
        basic.clearScreen()
    } else {
        if (Operator == 2) {
            basic.showLeds(`
                . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
                `)
            basic.pause(500)
            basic.clearScreen()
        } else {
            if (Operator == 3) {
                basic.showLeds(`
                    # . . . #
                    . # . # .
                    . . # . .
                    . # . # .
                    # . . . #
                    `)
                basic.pause(500)
                basic.clearScreen()
            } else {
                if (Operator == 4) {
                    basic.showLeds(`
                        . . # . .
                        . . . . .
                        # # # # #
                        . . . . .
                        . . # . .
                        `)
                    basic.pause(500)
                    basic.clearScreen()
                } else {
                    if (Operator == 5) {
                        basic.showLeds(`
                            . . # . .
                            . # . # .
                            # . . . #
                            . . . . .
                            . . . . .
                            `)
                        basic.pause(500)
                        basic.clearScreen()
                    } else {
                        Operator = 1
                        basic.showLeds(`
                            . . # . .
                            . . # . .
                            # # # # #
                            . . # . .
                            . . # . .
                            `)
                        basic.clearScreen()
                    }
                }
            }
        }
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    music.playTone(262, music.beat(BeatFraction.Eighth))
    if (c == 0) {
        a += -1
        basic.showNumber(a)
    }
    if (c == 1) {
        b += -1
        basic.showNumber(b)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    music.playTone(262, music.beat(BeatFraction.Eighth))
    c += 1
    if (c == 2) {
        if (Operator == 1) {
            basic.showNumber(a + b)
        } else {
            if (Operator == 2) {
                basic.showNumber(a - b)
            } else {
                if (Operator == 3) {
                    basic.showNumber(a * b)
                } else {
                    if (Operator == 4) {
                        basic.showNumber(a / b)
                    } else {
                        basic.showNumber(a ** b)
                    }
                }
            }
        }
    }
})
input.onGesture(Gesture.TiltRight, function () {
    music.playTone(262, music.beat(BeatFraction.Eighth))
    if (c == 0) {
        a += 1
        basic.showNumber(a)
    }
    if (c == 1) {
        b += 1
        basic.showNumber(b)
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    control.reset()
})
let c = 0
let b = 0
let a = 0
let Operator = 0
Operator = 0
a = 0
b = 0
c = 0
music.playTone(262, music.beat(BeatFraction.Eighth))
basic.showString("START")
