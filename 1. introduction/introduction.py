async def start_program():
    # led test
    
    async def precue(color, ms=250):
            set_main_led(color)
            await delay(ms/1000)
            set_main_led({ "r": 255, "g": 255, "b": 255 })

    async def introd():
            await speak("Hello, I'm sphero Pass. Wish you have a good day. How can I help you?", False)
            await scroll_matrix_text("Await instructions:", {'r': 0, 'g': 180, 'b': 255}, 30, False)
            await roll(0, 60, 0.8)
            await roll(45, 60, 0.7)

    # move test
    async def bow():
            # small forward/back to “bow”
            await roll(0, 40, 0.4)
            await roll(180, 40, 0.4)

    async def init():
        set_main_led({ "r": 0, "g": 180, "b": 255 })  # calm cyan

    #init
    await init()
    await delay(0.3)

    # introduction
    await precue({ "r": 255, "g": 200, "b": 0 }, 200)
    await introd()
    await precue({ "r": 255, "g": 80, "b": 80 }, 200)
    await roll(90, 70, 0.8)     
    await delay(0.2)            


    # personality beat + bow
    await precue({ "r": 120, "g": 255, "b": 120 }, 200)
    set_main_led({ "r": 120, "g": 255, "b": 120 })
    await delay(0.2)  
    await speak("I'm still learning—if I turn in circles, I'm thinking hard, not lost!", False)
    await delay(0.3)
    await bow() 
    await delay(0.2)
    
    # ending pose
    await speak("That's my intro. Thank you!", False)
    await scroll_matrix_text("Thanks !", {'r': 255, 'g': 255, 'b': 255}, 25, False)
    set_main_led({ "r": 255, "g": 255, "b": 255 })
    await delay(0.4)

    # await stop_roll()
    exit_program()
