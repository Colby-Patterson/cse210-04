class Director:

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

        banner.set_text('')
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.change_position(max_x, max_y)

        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_postion()):
                message = artifact.get_value()
                banner.set_text(message)

    def _do_outputs(self, cast):

        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
