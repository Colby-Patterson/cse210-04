from hashlib import new
import random
from game.casting.artifact import Artifact
from game.shared.point import Point

class Director:
    """satisfy python"""

    def __init__(self, keyboard_service, video_service):

        self._keyboard_service = keyboard_service
        self._video_service = video_service


    def start_game(self, cast):

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        
        robot = cast.get_first_actor('robots')
        speed = self._keyboard_service.get_direction()
        robot.set_speed(speed)

    def _do_updates(self, cast):
        
        banner = cast.get_first_actor('banners')
        robot = cast.get_first_actor('robots')
        artifacts = cast.get_actors('artifacts')

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.change_position(max_x, max_y)
 
        value = random.randint(0,1)
        x = random.randint(0, 60) * 15
        y = 15
        new_artifact = Artifact()
        new_artifact.set_speed(Point(0, 15))
        new_artifact.set_position(Point(x, y))
        new_artifact.set_size(15)
        if value == 0:
            new_artifact.set_value(-1)
            new_artifact.set_text("O")
        elif value == 1:
            new_artifact.set_value(1)
            new_artifact.set_text("*")
        cast.add_actor('artifacts', new_artifact)

        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                value = artifact.get_value()
                score = robot.get_score()
                new_score = score + value
                robot.set_score(new_score)
                banner.set_text(f"Score: {new_score}")
            
            artifact.change_position(max_x, max_y)

            

    def _do_outputs(self, cast):

        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
