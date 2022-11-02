function whenInABreak() {
    console.log("Hello")
    pauseUntil(function button(): boolean {
        return false
    })
}

basic.forever(function on_forever() {
    whenInABreak()
    basic.pause(1000)
    
})
