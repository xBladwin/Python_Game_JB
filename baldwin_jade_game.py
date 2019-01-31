'''
The year is 2083, after a nuclear appocolypse the world has become
a dangerous place for survival. This game tells the story of one survior
named Josiah, his goal is to fight his way through the infected and make
it to planet zafaris. On his journey he will have to find a weapon
and fight his way to rebuild a space ship to evacuate what's left of earth.

'''

'''
Rooms
home - Starting point of the game
TheTrap - This is a room where Josiah get trapped by the infected and has to fight them off, successfull = parts
WeaponRoom - this is where josiah get to select between a sword or a pistol
Rebuild - where the ship needs to be rebuilt
Escape - the player escapes after a brutal fight, or does he?

Actions
Death - when the player dies
PickUpWeapon - a choice between the sword or the pistol each has different outcomes
pick up ship parts - need to have all parts to escape.
'''


#Map
#   next_scene
#   start_scene
#Engine
#   play
#Scene
#   enter
#   death
#   home
#   TheTrap
#   WeaponRoom
#   Rebuild
#   EscapeShip

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class Home(Scene):

    def enter(self):
        pass

class WeaponRoom(Scene):

    def enter(self):
        pass

class TheTrap(Scene):

    def enter(self):
        pass

class Rebuild(Scene):

    def enter(self):
        pass

class EscapeShip(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('Home')
a_game = Engine(a_map)
a_game.play()
