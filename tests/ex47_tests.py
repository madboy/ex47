from nose.tools import *
from ex47.game import Room

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_room():
    gold = Room("GoldRoom",
            """Gold in room""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Room in center")
    north = Room("North", "Room in north")
    south = Room("South", "Room in south")

    center.add_paths({'north': north, 
        'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You start here")
    west = Room("Tree", "In the woods")
    down = Room("Dungeon", "Dark indeed")

    start.add_paths({'west': west,
        'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
