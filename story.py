# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:23:49 2025

@author: asus
"""
import random
class Hero:
    def __init__(self,name,race,post,skill,characterstics,weapon):
        self.name = name
        self.race = race
        self.post = post
        self.skill = skill
        self.charact = characterstics
        self.weapon = weapon
        
    def backstory(self):
        return ( f"{self.name}, was a hidden talent of small town Rushik." 
                    f"born in family of {self.race} possessed exceptional power of {self.skill}"
                    f" at age of 5, he advanced his skills to best and got hold of legendary weapon {self.weapon}")
    def currenttimeline(self):
        return{ f"{self.name} hid his identity as the legendary {self.post}. "
                   f" but, his {self.charact} mesmorized everyone whereever he went."
                   f" roaming arounds, is a foodie"}

class Sidekick:
    def __init__(self, name, skill, characterstics,importantitem,hero):
        self.name = name
        self.skill = skill
        self.charact = characterstics
        self.item = importantitem
        self.hero = hero
        
    def backstory(self):
        return ( f"{self.name} was saved by {self.hero} when trafficed as a beastmen slave."
                f" Indebeted to {self.hero}, the orphan {self.name} vowed to stay by his side and gain power"
                f" As time went by two of them became friends and our little beastman grew into a {self.charact} with expectional talent in {self.skill}")

class Villan:
    def __init__(self, name, characterstics,enemytype, castlearea):
        self.name = name
        self.charact = characterstics
        self.enemy = enemytype
        self.castle = castlearea
        
    def backstory(self):
        return( f"{self.name} was a lovely crown  prince of empire  when his lovely wife and kids were killed by his stepfather, King Valiz of Dundy, the Empress second husband through polticial marriage"
               f" He was not only a kind prince whom everyone loved but also a powerful {self.enemy}."
               f" but due to schemes of his step father, he was betrayed by crowd and exciled in false pretences ")
    def currenttimeline(self):
        return(f" The desposed crown prince, has gathered army to kill stepfather but in process has been blinded by betryal and is on killing spree"
               f" Lives in {self.castle} , an abandonded and forgotten place which he finds homely due to being abandoned by his nation n mother"
               f" his {self.charact} has grown dark and he cries everynight in despair of killing everyone and in memory of his happy family ")
    
class StoryProgress:
    def __init__(self, goal,storytype,fightscenenmber,mysterynumber,hero,villan,sidekick):
        self.goal = goal
        self.fights=fightscenenmber
        self.mystery=mysterynumber
        self.hero = hero
        self.sidekick = sidekick
        self.villan = villan
        self.storytype = storytype
        self.scenario_list = [
            "A mysterious forest ambush", "A lost scroll in the desert", "An old ghost in the castle",
            "Mercenaries in the lake", "Carriage gets broken", "Falling ceiling in hotel",
            "Poison mushroom eaten by sidekick", "Helping villagers against villain's troops", 
            "Killing King Valiz of Dundy in an accident", "Saving saintess and gaining immunity", 
            "Secret passage under villain’s castle", "Fight with mages at a ballroom party",
            "Saving a cat and discovering villain’s family portrait"
        ]
        
    def mysteryscenes(self):
        legendaryitem=0
        for i in range(self.mystery):
            legendaryitem+=1
            print(f" Mystery #{i+1} a legendary item was discovered")
        return f'total legandary items : {legendaryitem}'
    
    def fightiterators(self): 
        for i in range(self.fights):
            scenario_shuffle = iter(random.sample(self.scenario_list, len(self.scenario_list)))
            for j in range(random.randint(1, self.mystery)):
                scenariotype = next(scenario_shuffle)
                print(f"Fight #{i+1}: {scenariotype}")
            
            if random.random() < 0.3 and hasattr(self.sidekick, "item"):
                destroyed_item = self.sidekick.item
                del self.sidekick.item
                return f"{self.sidekick.name} broke down as his precious item '{destroyed_item}' got destroyed."

    def ending(self):
        return f"'{self.villan.name}' has let go of all vengeance. The shadow of the villain fades into the past."
        
        