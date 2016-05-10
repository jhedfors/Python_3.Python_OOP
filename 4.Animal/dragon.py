from animal import Animal
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health-=10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "This is a dragon"
        return self
dragon = Dragon('Frank')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
