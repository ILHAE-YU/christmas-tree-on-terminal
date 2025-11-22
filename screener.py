import time
import random

class Screener:

    COLOR_TO_ANSICOLOR = {
        "Black":   "\033[30m",
        "Red":     "\033[31m",
        "Green":   "\033[32m",
        "Yellow":  "\033[33m",
        "Blue":    "\033[34m",
        "Magenta": "\033[35m",
        "Cyan":    "\033[36m",
        "White":   "\033[37m",

        "BrightBlack":   "\033[90m",
        "BrightRed":     "\033[91m",
        "BrightGreen":   "\033[92m",
        "BrightYellow":  "\033[93m",
        "BrightBlue":    "\033[94m",
        "BrightMagenta": "\033[95m",
        "BrightCyan":    "\033[96m",
        "BrightWhite":   "\033[97m",

        "Reset": "\033[0m",
    }

    def __init__(self, width, height, fps=15):
        self.width = width
        self.height = height
        self.buffer = [[' ' for _ in range(width)] for _ in range(height)]
        self.fps = fps
        self.sync = 0
        self.assets = []

    def clear(self):
        self.buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def add_asset(self, asset, x, y):
        self.assets.append((asset, (x, y)))

    def draw_asset(self, asset, x, y):
        asset_height, asset_width = asset.shape()
        blink_rate = asset.blink_rate
        blink_rate_init = asset.blink_rate_init


        if asset.blink_style == "permanent":
            asset.blink_state = 1

        else: 
            if (self.sync + blink_rate_init) % blink_rate == 0:

                if asset.blink_style == "random":
                    asset.blink_state = 1
                    color_nums = list(range(0, len(asset.color)))
                    exclude = asset.color_index
                    if exclude in color_nums:
                        color_nums.remove(exclude)
                    asset.color_index = random.choice(color_nums)

                elif asset.blink_style == "twinkle":
                    asset.blink_state = 1 - asset.blink_state
                    if asset.blink_state != 0:
                        asset.color_index = (asset.color_index + 1) % len(asset.color)

                else:
                    asset.blink_state = 0


        if asset.blink_state == 1:
            color_ansi = Screener.COLOR_TO_ANSICOLOR[asset.color[asset.color_index]]
            
            for row in range(asset_height):
                for col in range(asset_width):
                    if 0 <= y + row < self.height and 0 <= x + col < self.width:
                        ch = asset.ascii_chars[row][col]
                        if ch != ' ':
                            self.buffer[y + row][x + col] = color_ansi + ch + Screener.COLOR_TO_ANSICOLOR["Reset"]

        else:
            for row in range(asset_height):
                for col in range(asset_width):
                    if 0 <= y + row < self.height and 0 <= x + col < self.width:
                        ch = asset.ascii_chars[row][col]
                        if ch != ' ':
                            self.buffer[y + row][x + col] = ch

    def _sync(self):
        self.sync += 1

    def render(self):
        screen_str = "\n".join("".join(row) for row in self.buffer)
        print(screen_str, end="")

    def start(self):
        while True:
            # print("\033[2J\033[H", end="")  
            print("\033[H]", end="")  
            
            self.clear()
            for asset, (x, y) in self.assets:
                self.draw_asset(asset, x, y)
            self.render()
            self._sync()
            time.sleep(1 / self.fps)