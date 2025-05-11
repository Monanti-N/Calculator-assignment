class SecretStash:
    def __init__(self):
        self.__chocolate = 42

    def take_chocolate(self):
        if self.__chocolate > 0:
            self.__chocolate -= 1
            print("One Chocolate taken!")  
        else:
            print("No chocolates left!")
            
