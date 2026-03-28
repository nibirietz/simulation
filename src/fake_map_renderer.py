from game_map import GameMap


class FakeMapRenderer:
    def render(self, game_map: GameMap, move_counter: int):
        pass

    def is_pause(self) -> bool:
        return False

    def is_exit(self) -> bool:
        return False
