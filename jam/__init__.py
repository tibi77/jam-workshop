from FoxDot import *

Clock.bpm = 120
Scale.default = Scale.minor
Root.default = var([0, -2, -3], 16)

# LAYERS
## Atmosphere
p1 >> swell([0,2,4], dur=16, sus=14,
            amp=0.3, chop=2, pan=linvar([-0.4,0.4],64),
            room=0.7, verb=0.9, lpf=linvar([800, 3000],128))

## Kick + Groove
d1 >> play("x   ", sample=2, dur=1, amp=0.9)
h1 >> play(" - -", dur=1/2, sample=3, amp=0.5, pan=0.3)
d2 >> play("..o.", dur=1/4, amp=0.3, sample=4, pan=-0.2)

## Hypnotic Bass
b1 >> dbass(var([0,None,-2,None],8), dur=2, sus=1.5,
            amp=0.6, lpf=500, room=0.3)

## Textures + Details
fx >> play("V", dur=PDur(3,8), sample=5, amp=0.3,
            room=0.5, verb=0.7, pan=linvar([-0.5,0.5],64))
l1 >> bell(P[0, None, 3, None, 7].rotate(1),
             dur=var([4,8],[16,32]), sus=3,
             amp=0.2, lpf=1200)

# STRUCTURE FUNCTIONS
def intro():
    d1.amp=0.4; h1.amp=0; d2.amp=0; b1.amp=0
    print("INTRO: Just atmosphere")

def groove():
    h1.amp=0.4; d2.amp=0.3; b1.amp=0.4
    print("GROOVE: Kick, hats, bass enter")

def deep_roll():
    b1.amp=0.7; h1.amp=0.5; l1.amp=0.15; fx.amp=0.4
    p1.lpf=linvar([1000, 4000],128)
    print("DEEP ROLL: Bass and textures intensify")

def breakdown():
    d1.amp=0; h1.amp=0.2; d2.amp=0.1; b1.amp=0.2
    p1.amp=0.2; l1.amp=0
    print("BREAKDOWN: Stripped back")

def peak():
    d1.amp=1; h1.amp=0.6; d2.amp=0.4; b1.amp=0.8
    l1.amp=0.25; fx.amp=0.5
    print("PEAK: Full hypnotic groove")

def outro():
    d1.amp=0.2; h1.amp=0.1; d2.amp=0; b1.amp=0.1
    p1.amp=0.1; fx.amp=0.1; l1.amp=0
    print("OUTRO: Slowly fading out")

p1 >> blip(
    P[0, 4, 7, 11, 9, 7].stutter([4, 2, 2, 1, 1, 2]),
    dur=PDur(5, 8),
    sus=0.3,
    amp=var([0.9, 1.2], 16),
    lpf=linvar([1200, 4000], 32),
    vib=12,
    slide=2,
    echo=0.5,
    echotime=0.25,
    oct=5,
    pan=PWhite(-0.7, 0.7)
)

# SCHEDULED FLOW (like a DJ set timeline)
Clock.schedule(intro, Clock.now() + 0)
Clock.schedule(groove, Clock.now() + 64)
Clock.schedule(deep_roll, Clock.now() + 128)
Clock.schedule(breakdown, Clock.now() + 192)
Clock.schedule(peak, Clock.now() + 256)
Clock.schedule(outro, Clock.now() + 384)

Go()