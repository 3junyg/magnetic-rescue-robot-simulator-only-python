import desktop_app

from smooth_perception_renderer import draw_smooth_perception


class SmoothPerceptionApp(desktop_app.DesktopSimulationApp):
    def redraw(self) -> None:
        original_draw_board = desktop_app.draw_board
        desktop_app.draw_board = draw_smooth_perception
        try:
            super().redraw()
        finally:
            desktop_app.draw_board = original_draw_board


if __name__ == "__main__":
    SmoothPerceptionApp().show()

