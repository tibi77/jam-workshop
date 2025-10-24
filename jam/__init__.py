from FoxDot import *

# GLOBAL SETTINGS
Clock.bpm = 128  # energetic club tempo
Scale.default = Scale.harmonicMinor  # dark but driving
Root.default = var([0, 2, -1, -3], 8)

# SUPER SAW PAD (epic atmosphere)
p1 >> saw(
    [0, 4, 7, 11],
    dur=8,
    sus=8,
    chop=4,
    amp=0.5,
    lpf=linvar([800, 4000], 32),
    room=0.6,
    verb=0.7,
    pan=linvar([-0.5, 0.5], 16),
)

# FAST ARPEGGIO (keeps energy alive)
p2 >> pluck(
    P[0, 2, 4, 7].arp([0, 1, 2, 3]).every(6, "mirror"),
    dur=PDur(3, 8),
    sus=0.2,
    amp=0.9,
    chop=4,
    echo=0.25,
    echotime=0.25,
    lpf=1200,
    pan=PSine(8),
)

# FAST ARPEGGIO (keeps energy alive)
a1 >> pluck(
    P[0, 2, 4, 7].arp([0, 1, 2, 3]),  # Ascending by index
    dur=1 / 4,
    sus=0.3,
    amp=0.9,
    chop=2,
    echo=0.25,
    echotime=0.5,
    lpf=var([1200, 2400], 8),
    pan=PSine(16),
)


# BASSLINES
# Punchy sub bass
s1 >> bass(
    var([0, -1, 0, -3], [4, 4, 4, 4]), dur=1 / 2, sus=0.4, amp=1.3, lpf=900, drive=0.3
)

# Growly mid-bass for texture
m1 >> sawbass(
    P[0, 2, -1, None], dur=2, sus=1.5, amp=0.8, lpf=700, distort=0.3, crush=8
)

# DRUMS — strong club groove
d1 >> play("x-ox xoxo", dur=1 / 2, amp=1.2)
h1 >> play("-(-=)-", dur=1 / 4, amp=0.6, pan=0.4)
c1 >> play("  *   * ", sample=2, dur=1 / 2, amp=0.9)

# FX / GLITCH
fx >> play("V[--]V ", dur=1, amp=0.6).every(8, "stutter", 4, dur=3)


# ENERGY BUILDS
def build():
    a1.amp = 1.2
    h.amp = 1
    c.amp = 1.2
    p1.chop = 8


def drop():
    s.amp = 1.6
    # midbass.amp = 1.2
    d1.amp = 1.4
    fx.amp = 0.9


# Clock.schedule(build, Clock.now() + 16)
# Clock.schedule(drop, Clock.now() + 32)

# Random fills & variations
# Group(drum, hats, clap).every(16, "shuffle")
# Group(arp1, theme).every(12, "mirror")

# END: keep script alive
print("Loaded: foxdot_energy_anthem.py — run, tweak, and let the room move!")
Go()
