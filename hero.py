class Hero():
    def __init__(self,hp,att,name):
        self.hp=hp
        self.att=att
        self.name=name

    def beattack(self,enemy):
        self.hp-=enemy.att
    
    def attack(self,enemy):
        enemy.beattack(self)
    
    def heal(self):
        self.hp+=1

class Shooter(Hero):
    def __init__(self,hp,att,name):
        super().__init__(hp,att,name)

    def attack(self,enemy):
        super().attack(enemy)
        super().attack(enemy)

class Archmage(Hero):   
    def __init__(self,hp,att,mp,name):
        super().__init__(hp,att,name)
        self.mp=mp

    def heal(self):
        self.mp-=1
        super().heal()
        super().heal()

class Warrior(Hero):   
    def __init__(self,hp,att,defe,name):
        super().__init__(hp,att,name)
        self.defe=defe

    def beattack(self,enemy):
        if self.defe>enemy.att:
            self.defe-=enemy.att
        else:
            x=enemy.att-self.defe
            self.hp-=x
            self.defe=0
def heroChoice():
    h=open("hero.txt","w")
    print("1: Shooter, 2: Archmage, 3: Warrior")
    x=int(input())
    if x==1:
        h.writelines(["Shooter","\n"])
        print("input name")
        name=input()
        h.writelines([name,"\n"])
        print("input hp")
        hp=input()
        h.writelines([hp,"\n"])
        print("input att")
        att=input()
        h.write(att)
    elif x==2:
        h.writelines(["Arcgmage","\n"])
        print("input name")
        name=input()
        h.writelines([name,"\n"])
        print("input hp")
        hp=input()
        h.writelines([hp,"\n"])
        print("input att")
        att=input()
        h.writelines([att,"\n"])
        print("input mp")
        mp=input()
        h.write(mp)
    else:
        h.writelines(["Warrior","\n"])
        print("input name")
        name=input()
        h.writelines([name,"\n"])
        print("input hp")
        hp=input()
        h.writelines([hp,"\n"])
        print("input att")
        att=input()
        h.writelines([att,"\n"])
        print("input defe")
        defe=input()
        h.write(defe)
    h.close()

heroChoice()

h=open("hero.txt","r")
config=h.readlines()

s=Shooter(100,5,"Joe")

if config[0]=="Shooter\n":
    name=config[1].replace("\n","")
    hp=int(config[2].replace("\n",""))
    att=int(config[3])
    bot=Shooter(hp,att,name)

if config[0]=="Archmage\n":
    name=config[1].replace("\n","")
    hp=int(config[2].replace("\n",""))
    att=int(config[3].replace("\n",""))
    mp=int(config[4])
    bot=Archmage(hp,att,mp,name)

if config[0]=="Warrior\n":
    name=config[1].replace("\n","")
    hp=int(config[2].replace("\n",""))
    att=int(config[3].replace("\n",""))
    defe=int(config[4])
    bot=Warrior(hp,att,defe,name)

s.attack(bot)
'''
h=open("hero.txt","r")
h2=open("hero2.txt","w")
h2.write(h.read())
h2.close()
h.close()
'''
h=open("hero.txt","r+")
cfg=h.readlines()
if cfg[0]=="Shooter\n":
    cfg[2]=str(bot.hp)+"\n"
    print(cfg)
    h.close()
    h=open("hero.txt","w")
    h.writelines(cfg)