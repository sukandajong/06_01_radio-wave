def on_received_string(receivedString):
    if receivedString == "C":
        basic.show_icon(IconNames.HEART)
    elif receivedString == "W":
        basic.show_icon(IconNames.NO)
radio.on_received_string(on_received_string)

is_active = False
radio.set_group(1)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_UP)

def on_forever():
    global is_active
    if pins.digital_read_pin(DigitalPin.P13) == 0:
        is_active = True
        basic.show_icon(IconNames.HEART)
        radio.send_string("C")
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        basic.show_icon(IconNames.NO)
        radio.send_string("W")
basic.forever(on_forever)
