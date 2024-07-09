from pynput.keyboard import Controller

keyboard = Controller()

class Control:
    def startControlling(self,distance,slope):
<<<<<<< HEAD
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
=======
        keyPressed = False
        keyPressed_lr = False
        recentKey = None

        if 110 <= distance <= 210:
            PressKey(W)
            recentKey = W
            print('Press W')
            keyPressed = True
            self.current_key_pressed.add(W)
        elif 20 <= distance <= 110:
            PressKey(S)
            recentKey = S
            print('Press S')
            keyPressed = True
            self.current_key_pressed.add(S)

        if -0.40 < slope < -0.25:
            PressKey(A)
            print('Press <--')
            self.current_key_pressed.add(A)
            keyPressed = True
            keyPressed_lr = True
>>>>>>> 45303c9c16d7cd2e9444dd164d2a8766fe5cbeb8
        elif 0.15 < slope < 0.40:
            keyboard.release('a')
            keyboard.press('d')
            print("d")

