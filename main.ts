radio.onReceivedString(function (receivedString) {
    if (receivedString == "C") {
        basic.showIcon(IconNames.Heart)
    } else if (receivedString == "W") {
        basic.showIcon(IconNames.No)
    }
})
let is_active = false
radio.setGroup(1)
pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
pins.setPull(DigitalPin.P16, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        is_active = true
        basic.showIcon(IconNames.Heart)
        radio.sendString("C")
    } else if (pins.digitalReadPin(DigitalPin.P16) == 0) {
        basic.showIcon(IconNames.No)
        radio.sendString("W")
    }
})
