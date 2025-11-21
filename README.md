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



2. Screener에 Asset을 추가하세요!

3. Screener를 start 하세요!
