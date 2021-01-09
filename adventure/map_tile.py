class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def room_text(self):
        raise NotImplementedError


class StartingRoom(MapTile):
    def room_text(self):
        return "A damp, dark cavern with the only light source being a lone torch."