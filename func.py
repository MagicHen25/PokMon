class Role(object):
    def __init__(self, name, blood, weapon, armor):
        self.name = name
        self.blood = blood
        self.weapon = weapon
        self.armor = armor

    def talk(self):
        print("你好，我是 %s, 很高兴见到你~" % self.name)


class PlayerRole(Role):
    def __init__(self, name, blood, weapon, armor, gender, occupation, religion, package):
        super(PlayerRole,self).__init__(name, blood, weapon, armor)
    pass


class BadlyRole(Role):
    pass


class LittleElf(object):
    pass

