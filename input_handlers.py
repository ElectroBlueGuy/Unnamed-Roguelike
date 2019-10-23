import tcod as libtcod

def handle_keys(key):
    # movement
    if key.vk == libtcod.KEY_KP8:
            return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_KP2:
            return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_KP4:
            return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_KP6:
            return {'move': (1, 0)}
    
    if key.vk == libtcod.KEY_ENTER and libtcod.KEY_ALT:
        # Full screen
        return {'fullscreen': True}
    
    elif key.vk ==libtcod.KEY_ESCAPE:
        # Exit
        return {'exit': True}

    return {}
