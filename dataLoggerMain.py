from dlmode import RUN_MODE
import modeselection
import oledScreens


k = modeselection.MODES()         #mode selection through keypad
disp =oledScreens.OLEDSCREENS()

if __name__ == "__main__":
    disp.WelcomeMessage()
    disp.ModesOfDataLogger()
    userDelay1 = 0
    del disp
    while True:
        k.modeSelection()           #Selection of mode through keypad
        userDelay1 = userDelay1+1
        if userDelay1 == 200:
            RUN_MODE()
