# test if I can use the pindirs + pullup/down to signal
# then could keep it always in input mode, just toggle?

from machine import Pin
import time

@rp2.asm_pio(set_init=rp2.PIO.OUT_HIGH, out_init=rp2.PIO.OUT_HIGH)
def dut():
#    wrap_target()
    set(pins, 0)
    set(pindirs, 1)
    set(pindirs, 0)
    set(pindirs, 1)
    set(pindirs, 0)
    in_(pins, 1)  ## this reads high if external pullup or no connection, low if pulldown ~10k.
#    push()
#    wrap()


# gpio61 = Pin(18, Pin.IN, pull=None)
gpio61 = Pin(18, Pin.IN, pull=Pin.PULL_UP)
time.sleep_ms(1)
mosheen2 = rp2.StateMachine(0, dut, freq=5_000, in_base=gpio61, out_base=gpio61, set_base=gpio61)
# gpio61 = Pin(18, Pin.OPEN_DRAIN)
mosheen2.active(1)
time.sleep_ms(10)
mosheen2.active(0)


