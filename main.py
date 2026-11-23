import ctypes
try:
    ctypes.windll.user32.SetProcessDPIAware()  # 윈도우 배율(125%, 150%)로 창이 커지는 것 방지
except Exception:
    pass

from pico2d import open_canvas, close_canvas
import game_framework

import play_mode as start_mode

open_canvas(1600, 600)
game_framework.run(start_mode)
close_canvas()

