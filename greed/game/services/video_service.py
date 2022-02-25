import pyray

class VideoService:

    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):

        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    
    def close_window(self):

        pyray.close_window()

    
    def clear_buffer(self):

        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

    
    def draw_actor(self):

        pass

    
    def flush_buffer(self):

        pyray.end_drawing

    
    def get_cell_size(self):

        return self._cell_size

    
    def get_height(self):

        return self._height

    
    def get_width(self):

        return self._width

    
    def is_window_open(self):

        return not pyray.window_should_close()

   
    def open_window(self):

        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

   
    def _draw_grid(self):
        
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)
