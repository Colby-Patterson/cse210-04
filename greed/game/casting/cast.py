class Cast:

    def __init__(self):
        self._actors = {}

    def add_actor(self, group, actor):
        if not group in self._actors.keys():
            self._actors[group] = []

        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        result = []
        if group in self._actors.keys():
            result = self._actors[group].copy()
        return result

    def get_all_actors(self):
        result = []
        for group in self._actors:
            result.extend(self._actors[group])
        return result

    def get_first_actor(self, group):
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        if group in self._actors:
            self._actors[group].remove(actor)