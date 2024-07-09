from pynput.keyboard import Controller

keyboard = Controller()

class Control:
    def startControlling(self,distance,slope):
        if 120 <= distance <= 220:
            keyboard.release('s')
            keyboard.press('w')
            print("w")
        elif 20 <= distance <= 115:
            keyboard.release('w')
            keyboard.press('s')
            print("s")

        if -0.41 < slope < -0.25:
            keyboard.release('d')
            keyboard.press('a')
            print("a")
        elif 0.15 < slope < 0.40:
            keyboard.release('a')
            keyboard.press('d')
            print("d")

