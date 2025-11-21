# Christmas Tree on Terminal
Display animated ASCII Christmas Tree directly on your terminal!

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
asset.py에서 나머지 asset을 찾을 수 있어요.<br>
어떤 asset들은 list 형태의 layer로 표현되어있어요.

## Blink System
### Blink Option
`permanet` color always applied!<br>
`random` color에 들어가는 색상 list 중 랜덤하게 선택해요.<br>
`twinkle` color에 들어가는 색상 list를 iterate하면서 toggle해요.<br>
### Interval
`blink_rate` 몇 단위마다 blink를 수행할지 정해요 (fps와 단위 같음)<br>
`blink_init_rate` 몇 단위 이후에 blink를 시작할지 정해요. (fps와 단위 같음)<br>
`reverse=True` 처음에 '꺼짐' 상태로 시작해요.<br>

