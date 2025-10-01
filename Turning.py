# sphero edu – compare turning style (A=sharp, B=smooth)

COND     = "A"   # "A" or "B"
SPEED    = 90    # 0–255
PRE      = 0.5   # straight before turn (sec)  ← per request
TURN_T   = 1.0   # turn duration (sec)
AFTER    = 0.5   # straight after turn (sec)
PAUSE    = 1

async def smooth_turn(start_hdg, end_hdg, speed, total_s, steps=12):
    # step headings to form a smooth arc
    step = (end_hdg - start_hdg) / steps
    dt   = total_s / steps
    hdg  = start_hdg
    for _ in range(steps):
        hdg += step
        await roll(hdg, speed, dt)

async def sharp_turn(to_heading, speed, total_s):
    # snap to new heading, move for total_s
    await roll(to_heading, speed, total_s)

async def start_program():
    # cue
    set_main_led({ "r": 0, "g": 80, "b": 255 })
    await delay(1)
    await scroll_matrix_text("A: sharp 90" if COND=="A" else "B: smooth 90",
                             { "r": 255, "g": 255, "b": 255 }, 30, True)
    await delay(PAUSE)
    await speak("Three, two, one, go.", False)
    await delay(0.5)

    # straight pre-turn (identical)
    await roll(0, SPEED, PRE)
    await delay(0.2)

    # turn (only difference)
    if COND == "A":
        await sharp_turn(90, SPEED, TURN_T)
    else:
        await smooth_turn(0, 90, SPEED, TURN_T, steps=12)

    await delay(0.2)

    # straight post-turn (identical)
    await roll(90, SPEED, AFTER)

    # end
    await speak("End of run.", False)
    set_main_led({ "r": 255, "g": 255, "b": 255 })
    await delay(PAUSE)
    exit_program()
