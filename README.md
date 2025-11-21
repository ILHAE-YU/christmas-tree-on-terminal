# Christmas Tree on Terminal
Display animated ASCII Christmas Tree directly on your terminal! <br>

(Warning! It is designed for a very large terminal size. The recommended terminal dimensions are width 500 and height 200, so you may need to resize or zoom out your terminal to display everything properly.)

![Demo GIF](demo.gif)

## Getting Started!
### 1. Create an Asset
`Asset` represents a single ASCII object (tree, bauble, ribbon, etc.).  
You can assign color, blink style, blink rate, and more.
```python
from asset import Asset, TREE

tree = Asset(
    ascii_chars=TREE,
    blink_style="permanent",   # "permanent" | "random" | "twinkle"
    color=["Green"],
    blink_rate=2, 
    blink_rate_init=0
)
```

### 2. Add Assets to Screener
Use `Screener` to manage the screen buffer and place assets.
```python
from screener import Screener

screen = Screener(width=500, height=200, fps=4)

screen.add_asset(tree, x=50, y=10)
screen.add_asset(star, x=120, y=8)
screen.add_asset(ribbon, x=150, y=60)
```

### 3. Start the Animation!
```python
screen.start()
```

## Built-in Assets
This project include some ready-to-use asset sets!<br>
thanks for [ASCII Art Archieve](https://www.asciiart.eu/)<br>
-TREE<br>
-STAR_TOPPER<br>
-RIBBONS<br>
-BABLES ...<br>
You can find all additional assets inside [asset.py](asset.py).<br>
Some assets are organized as layered lists to allow different colors to be applied to each layer.

## Blink System
### Blink Option
`permanet` — color always applied!<br>
`random` — randomly selects a color from the provided color list at each blink cycle.<br>
`twinkle`— toggles visibility while iterating through the color list in sequence.<br>
### Interval
`blink_rate` — determines how frequently the blink occurs (in the same unit as FPS).<br>
`blink_rate_init` — initial delay before blinking starts (also in FPS units).<br>
`reverse=True`— starts the asset in the “off” state instead of “on”.<br>
