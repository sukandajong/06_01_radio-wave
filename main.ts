radio.onReceivedString(function (receivedString) {
    if (receivedString == "F") {
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    } else if (receivedString == "B") {
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    } else if (receivedString == "R") {
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    } else if (receivedString == "L") {
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    } else {
        basic.showIcon(IconNames.Square)
    }
})
let joy_y = 0
let joy_x = 0
let is_active = false
pins.digitalWritePin(DigitalPin.P0, 1)
radio.setGroup(1)
pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
pins.setPull(DigitalPin.P16, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        is_active = true
        basic.showString("ON")
        basic.showIcon(IconNames.Heart)
    } else if (pins.digitalReadPin(DigitalPin.P16) == 0) {
        is_active = false
        basic.showString("OFF")
    }
    if (is_active) {
        joy_x = pins.analogReadPin(AnalogReadWritePin.P2)
        joy_y = pins.analogReadPin(AnalogReadWritePin.P1)
        if (joy_y < 400) {
            radio.sendString("F")
            basic.showLeds(`
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
                `)
        } else if (joy_y > 600) {
            radio.sendString("B")
            basic.showLeds(`
                . . # . .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
                `)
        } else if (joy_x < 400) {
            radio.sendString("R")
            basic.showLeds(`
                . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
                `)
        } else if (joy_x > 600) {
            radio.sendString("L")
            basic.showLeds(`
                . . # . .
                . # . . .
                # # # # #
                . # . . .
                . . # . .
                `)
        } else {
            radio.sendString("S")
            basic.showIcon(IconNames.Heart)
        }
    }
})
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P14) == 0) {
        is_active = true
        basic.showString("ON")
        basic.showIcon(IconNames.Heart)
    } else if (pins.digitalReadPin(DigitalPin.P16) == 0) {
        is_active = false
        basic.showString("OFF")
    }
    if (is_active) {
        joy_x = pins.analogReadPin(AnalogReadWritePin.P2)
        joy_y = pins.analogReadPin(AnalogReadWritePin.P1)
        if (joy_y < 400) {
            radio.sendString("F")
            basic.showLeds(`
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
                `)
        } else if (joy_y > 600) {
            radio.sendString("B")
            basic.showLeds(`
                . . # . .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
                `)
        } else if (joy_x < 400) {
            radio.sendString("R")
            basic.showLeds(`
                . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
                `)
        } else if (joy_x > 600) {
            radio.sendString("L")
            basic.showLeds(`
                . . # . .
                . # . . .
                # # # # #
                . # . . .
                . . # . .
                `)
        } else {
            radio.sendString("S")
            basic.showIcon(IconNames.Heart)
        }
    }
})
