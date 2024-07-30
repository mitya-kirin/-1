# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'abc3.jpg'
        self.colors = [(0.1, 0.99, 0.8, 1), 
                       (0.1, 0.7, 0.45, 1),
                       (0.9, 0.7, 0.11, 1)]
        self.startNew()
        #self.addBlock((0, 10, 0))
    def startNew(self):
        self.land = render.attachNewNode("Land")
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.colorGet(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    def loadLand(self, fname):
        self.clear()
        with open(fname) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for zzz in line:
                    for z0 in range(int(zzz)+1):
                        block = self.addBlock((x, y, z0))
                    x +=1
                y +=1
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def colorGet(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]
