# https://codecombat.com/play/level/cursed-wonderglade
# Wonderglade has changed since our last visit.
# Ogres cursed it and we should defeat them.
# The burl still is collecting gems, so don't touch them.
# Also don't attack the burl.

while True:
    # Find the nearest item.
    # Collect it (if it exists) only if its type isn't "gem".
    #item = hero.findNearestItem()
    item = hero.findNearest(hero.findItems())
    if(item and item.type!='gem'):
        hero.moveXY(item.pos.x, item.pos.y)
    # Find the nearest enemy.
    # Attack it if it exists and its type isn't "burl".
    #enemy = hero.findNearestEnemy()
    enemy = hero.findNearest(hero.findEnemies())
    if(enemy and enemy.type!='burl'):
        hero.attack(enemy)
    pass
