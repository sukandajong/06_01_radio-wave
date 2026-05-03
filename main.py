def on_received_string(receivedString):
    if receivedString == "F":
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)

    elif receivedString == "B":
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)

    elif receivedString == "R":
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)

    elif receivedString == "L":
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)

    else:
        basic.show_icon(IconNames.SQUARE)

radio.on_received_string(on_received_string)

joy_y = 0
joy_x = 0
pins.digital_write_pin(DigitalPin.P0, 1)
radio.set_group(1)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_UP)
is_active = False

def on_forever():
    global is_active, joy_x, joy_y
    if pins.digital_read_pin(DigitalPin.P13) == 0:
        is_active = True
        basic.show_string("ON")
        basic.show_icon(IconNames.HEART)
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        is_active = False
        basic.show_string("OFF")
    if is_active:
        joy_x = pins.analog_read_pin(AnalogReadWritePin.P2)
        joy_y = pins.analog_read_pin(AnalogReadWritePin.P1)
        if joy_y < 400:
            radio.send_string("F")
            basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
                """)
        elif joy_y > 600:
            radio.send_string("B")
            basic.show_leds("""
                . . # . .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
                """)
        elif joy_x < 400:
            radio.send_string("R")
            basic.show_leds("""
                . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
                """)
        elif joy_x > 600:
            radio.send_string("L")
            basic.show_leds("""
                . . # . .
                . # . . .
                # # # # #
                . # . . .
                . . # . .
                """)
        else:
            radio.send_string("S")
            basic.show_icon(IconNames.HEART)
basic.forever(on_forever)

def on_forever2():
    global is_active, joy_x, joy_y
    if pins.digital_read_pin(DigitalPin.P14) == 0:
        is_active = True
        basic.show_string("ON")
        basic.show_icon(IconNames.HEART)
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        is_active = False
        basic.show_string("OFF")
    if is_active:
        joy_x = pins.analog_read_pin(AnalogReadWritePin.P2)
        joy_y = pins.analog_read_pin(AnalogReadWritePin.P1)
        if joy_y < 400:
            radio.send_string("F")
            basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
                """)
        elif joy_y > 600:
            radio.send_string("B")
            basic.show_leds("""
                . . # . .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
                """)
        elif joy_x < 400:
            radio.send_string("R")
            basic.show_leds("""
                . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
                """)
        elif joy_x > 600:
            radio.send_string("L")
            basic.show_leds("""
                . . # . .
                . # . . .
                # # # # #
                . # . . .
                . . # . .
                """)
        else:
            radio.send_string("S")
            basic.show_icon(IconNames.HEART)
basic.forever(on_forever2)
