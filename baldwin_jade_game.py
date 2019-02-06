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
from sys import exit
from textwrap import dedent
import random
import death

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
        exit(1)

class Home(Scene):

    def enter(self):
        print(dedent("""
            You wake up in a dark room. "It's been 33 days since the nuclear explosion" you think to yourself.

            You see a light shining in through the door. What do you do,
            investigate or ignore it?
            """))

        insert = input("~ ")

        if insert == "investigate":
            print(dedent("""
                You see a strange figure standing at the door... Quickly you open
                the door and start to make a run for it. While running you notice a
                small shack with a rotting corpse guarding its entrance. Your only
                chance of surviving is to hide inside the shack.
                """))
            return 'weaponroom'

        elif insert == "ignore it":
            print(dedent("""
                You think nothing of the light and fall back asleep.

                suddenly you are woken up by an infected ripping apart your body, slurping on your intestines like a freezy pop.
                """))
            return death.death()

        else:
            print("I dont know what that means...")
            return 'home'

class WeaponRoom(Scene):    # wanted to make weapons a pickup but was unable to figure out how.

    def enter(self):
        print(dedent("""
            As you enter the shack to catch your breath the infected you were
            running from walks past. After ensuring safety you notice a
            sword hanging on the wall and a pistol lying on the counter.

            Which weapon do you choose?
            """))

        insert = input("~ ")

        if insert == 'sword':
            print(dedent("""
                You decide on the sword as your weapon of choice. Good Luck!

                As you pull the sword slowly off the wall, you see a reflection that frightens you.
                the infected has returned. You act fast and slice it up with your new trusty sword.
                Good choice!
                """))
            return 'thetrap'

        elif insert == 'pistol':
            print(dedent("""
                You have chosen the pistol. As you grab the pistol to load it, the infected bursts down
                the doors and runs at you like a banshee. Unfortunatly you only have 3 shots in the pistol
                and miss all three. The infected then proceeds to rip your head off and you die.
                """))
            return death.death()

        else:
            print("I dont know what that means...")
            return 'weaponroom'

class TheTrap(Scene):

    def enter(self):
        print(dedent("""
            After escaping the shack with your sword you continue your journey.
            while walking you spot a crashed ship. Running towrds it full of joy
            you trip and fall flat on your face. As you stand back up you notice that you're surrounded
            by infected.

            fight or run away?
            """))

        insert = input("~ ")

        if insert == 'fight':
            print(dedent("""
                You decide to fight off the infected. Slashing and slicing through multiple
                enemys with your trusty sword. After fighting off the infected you find parts
                to fix the crashed ship. Now your goal is to rebuild The ship.
                """))
            return 'rebuild'

        elif insert == 'run away':
            print(dedent("""
                While trying to escape the infected one catches you offguard
                and stabs you in the chest with its claws.

                you died
                """))
            return

        else:
            print("I dont know what that means...")
            return 'thetrap'

class Rebuild(Scene):

    def enter(self):
        print(dedent("""
            You make it back to the crashed ship and start your repairs.
            While making some last adjustments, an infected jumps out of
            a bush and startles you.

            what do you do?
            """))

        insert = input("~ ")

        if insert == 'fight':
            print(dedent("""
                While fighting the infected, it smacks your sword out of your hand
                you fall to your knees and the infected rips your head off

                you have died.
                """))
            return death.death()

        elif insert == 'run away':
            print(dedent("""
                while running you trip and bang your head on a tree stump.
                The infected snaps you in half like a kit kat.

                you have died
                """))
            return death.death()

        elif insert == 'shit pants':
            print(dedent("""
                you shit your pants! as the infected get closer it catches the
                smell of your brew. It now has ultimate cringe face and runs runs
                away in fear.
                """))
            return 'escapeship'

        else:
            print("I dont know what that means...")
            return 'rebuild'

class EscapeShip(Scene):

    def enter(self):
        print(dedent("""
            After cleaning yourself up you make it to the Ship and fly away from planet zafaris.


            YOU WIN!
            """))

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('escapeship')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene_enter()


class Map(object):

    scenes = {
    'home': Home(),
    'weaponroom': WeaponRoom(),
    'thetrap': TheTrap(),
    'rebuild': Rebuild(),
    'escapeship': EscapeShip(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('home')
a_game = Engine(a_map)
a_game.play()
