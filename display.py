from asset import Asset, TREE, STAR_TOPPER, RIBBONS, BAUBLES, GIFT_BOX1, GIFT_BOX2, GIFT_BOX3, GIFT_BOX4, WREATH, LOGO
import time
import random
import copy

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

        # Bright colors
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

tree = Asset(
    TREE,
)

star_topper = Asset(STAR_TOPPER,    blink_style = "permanent", color = [ "Yellow"])

ribbon5 = Asset(RIBBONS[1], blink_style = "random",color = [ "Red", "BrightMagenta"],  blink_rate = 4, blink_rate_init = 0)
ribbon1 = Asset(RIBBONS[0], blink_style = "random",color = [ "Red", "BrightMagenta"],  blink_rate = 4, blink_rate_init = 0)
ribbon2 = Asset(RIBBONS[1], blink_style = "random",color = [ "Red", "BrightMagenta"],  blink_rate = 4, blink_rate_init = 0,    reverse=True)
ribbon3 = Asset(RIBBONS[1], blink_style = "random",color = [ "Red", "BrightMagenta"],  blink_rate = 4, blink_rate_init = 0,    reverse=True).mirror_horizontal()
ribbon4 = Asset(RIBBONS[1], blink_style = "random",color = [ "Red", "BrightMagenta"],  blink_rate = 4, blink_rate_init = 0,    reverse=True)
ribbon5 = Asset(RIBBONS[1], blink_style = "random",color = [ "Red", "BrightMagenta"],  blink_rate = 4, blink_rate_init = 0)

BAUBLE_RAND_COLORS = [ "BrightRed", "BrightGreen", "BrightYellow", "BrightBlue", "BrightMagenta", "BrightCyan"]
bauble1 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble2 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble3 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble4 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble5 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble6 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble7 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble8 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble9 =   Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble10 =  Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble11 =  Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble12 =  Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble13 =  Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble14 =  Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)
bauble15 =  Asset(BAUBLES[0],    blink_style = "random",    color = BAUBLE_RAND_COLORS,    blink_rate = 2,    blink_rate_init = 0)

gift_box1           = Asset(GIFT_BOX1[0], blink_style = "permanent", color = [ "Blue"])
gift_box1_ribbon    = Asset(GIFT_BOX1[1], blink_style = "permanent", color = [ "Green"])
gift_box2           = Asset(GIFT_BOX2[0], blink_style = "permanent", color = [ "BrightRed"])
gift_box2_ribbon    = Asset(GIFT_BOX2[1], blink_style = "permanent", color = [ "Cyan"])
gift_box3           = Asset(GIFT_BOX3[0], blink_style = "permanent", color = [ "Green"])
gift_box3_ribbon    = Asset(GIFT_BOX3[1], blink_style = "permanent", color = [ "Red"])
gift_box4           = Asset(GIFT_BOX2[0], blink_style = "permanent", color = [ "White"])
gift_box4_ribbon    = Asset(GIFT_BOX2[1], blink_style = "permanent", color = [ "Red"])
gift_box5           = Asset(GIFT_BOX4[0], blink_style = "permanent", color = [ "BrightMagenta"])
gift_box5_ribbon    = Asset(GIFT_BOX4[1], blink_style = "permanent", color = [ "BrightYellow"])
gift_box6           = Asset(GIFT_BOX1[0], blink_style = "permanent", color = [ "BrightCyan"])
gift_box6_ribbon    = Asset(GIFT_BOX1[1], blink_style = "permanent", color = [ "BrightMagenta"])

wreath              = Asset(WREATH[0], blink_style = "permanent", color = [ "Green"])
wreath_ribbon       = Asset(WREATH[1], blink_style = "permanent", color = [ "Red"])
wreath_artifact     = Asset(WREATH[2], blink_style = "permanent", color = [ "Yellow"])
wreath_artifact2    = Asset(WREATH[3], blink_style = "permanent", color = [ "BrightYellow"])

logo = Asset(LOGO,    blink_style = "random", color = [ "BrightRed", "BrightGreen"], blink_rate=4)


screen = Screener(500, 200, fps=4)
offset_x = 50
offset_y = 10
screen.add_asset(tree, 10 + offset_x, 5 + offset_y)
screen.add_asset(logo, 240 + offset_x, 80 + offset_y)

screen.add_asset(star_topper, 135 + offset_x, 5 + offset_y)

screen.add_asset(ribbon1, 150 + offset_x, 50 + offset_y)
screen.add_asset(ribbon2, 80 + offset_x, 130 + offset_y)
screen.add_asset(ribbon3, 180 + offset_x, 110 + offset_y)
screen.add_asset(ribbon4, 120 + offset_x, 65 + offset_y)
screen.add_asset(ribbon5, 125 + offset_x, 90 + offset_y)

screen.add_asset(bauble1, 140 + offset_x, 25 + offset_y)
screen.add_asset(bauble2, 150 + offset_x, 30 + offset_y)
screen.add_asset(bauble3, 130 + offset_x, 37 + offset_y)
screen.add_asset(bauble4, 160 + offset_x, 40 + offset_y)
screen.add_asset(bauble5, 130 + offset_x, 50 + offset_y)
screen.add_asset(bauble6, 160 + offset_x, 60 + offset_y)
screen.add_asset(bauble7, 170 + offset_x, 70 + offset_y)
screen.add_asset(bauble8, 200 + offset_x, 72 + offset_y)
screen.add_asset(bauble9, 130 + offset_x, 78 + offset_y)
screen.add_asset(bauble10, 175 + offset_x, 84 + offset_y)
screen.add_asset(bauble11, 100 + offset_x, 90 + offset_y)
screen.add_asset(bauble12, 200 + offset_x, 93 + offset_y)
screen.add_asset(bauble13, 145 + offset_x, 100 + offset_y)
screen.add_asset(bauble14, 100 + offset_x, 115 + offset_y)
screen.add_asset(bauble15, 220 + offset_x, 132 + offset_y)

screen.add_asset(wreath, 117 + offset_x, 123 + offset_y)
screen.add_asset(wreath_ribbon, 117 + offset_x, 123 + offset_y)
screen.add_asset(wreath_artifact, 117 + offset_x, 123 + offset_y)
screen.add_asset(wreath_artifact2, 117 + offset_x, 123 + offset_y)

screen.add_asset(gift_box1, 60 + offset_x, 145 + offset_y)
screen.add_asset(gift_box1_ribbon, 60 + offset_x, 145 + offset_y)
screen.add_asset(gift_box2, 95 + offset_x, 137 + offset_y)
screen.add_asset(gift_box2_ribbon, 95 + offset_x, 137 + offset_y)
screen.add_asset(gift_box3, 120 + offset_x, 147 + offset_y)
screen.add_asset(gift_box3_ribbon, 120 + offset_x, 147 + offset_y)
screen.add_asset(gift_box6, 180 + offset_x, 142 + offset_y)
screen.add_asset(gift_box6_ribbon, 180 + offset_x, 142 + offset_y)
screen.add_asset(gift_box5, 190 + offset_x, 150 + offset_y)
screen.add_asset(gift_box5_ribbon, 190 + offset_x, 150 + offset_y)
screen.add_asset(gift_box4, 150 + offset_x, 142 + offset_y)
screen.add_asset(gift_box4_ribbon, 150 + offset_x, 142 + offset_y)

screen.start()