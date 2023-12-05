from turtle import Screen

class Window:
    def __init__(self):
        self.color = 'black'
        self.screen = Screen()
        self.screen.bgcolor(self.color)
        self.screen.setup(width=800, height=600)
        self.screen.title('Pong')

