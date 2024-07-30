# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import *
class Game(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        base.camLens.setFov(50)
     
game = Game()
game.run()