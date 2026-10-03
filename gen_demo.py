from PIL import Image, ImageDraw, ImageFont

W, H = 800, 500
BG = (30, 30, 30)
FG = (200, 200, 200)
GREEN = (80, 220, 100)
RED = (255, 100, 100)
CYAN = (80, 200, 255)
DIM = (120, 120, 120)

try:
    font = ImageFont.truetype("consola.ttf", 16)
except Exception:
    font = ImageFont.load_default()

TL, TR, BL, BR, HZ, VT = "+", "+", "+", "+", "-", "|"

scenes = [
    [("PS D:\\> ", CYAN), ('wiply start "Building wiply"', FG)],
    [("", None), (TL + HZ*38 + TR, GREEN), (VT + " > Started: Building wiply        " + VT, FG), (VT + "   ID: a1b2c3d4 | 10:30            " + VT, DIM), (BL + HZ*38 + BR, GREEN)],
    [("PS D:\\> ", CYAN), ('wiply start "Review code"', FG)],
    [("", None), (TL + HZ*38 + TR, GREEN), (VT + " > Started: Review code            " + VT, FG), (VT + "   ID: e5f6g7h8 | 10:31            " + VT, DIM), (BL + HZ*38 + BR, GREEN)],
    [("PS D:\\> ", CYAN), ("wiply status", FG)],
    [("", None), (TL + HZ*38 + TR, CYAN), (VT + " ID     Task                 Elapsed " + VT, CYAN), ("+" + HZ*38 + "+", CYAN), (VT + " a1b2c  Building wiply        2m     " + VT, FG), (VT + " e5f6g  Review code           1m     " + VT, FG), (BL + HZ*38 + BR, CYAN)],
    [("PS D:\\> ", CYAN), ("wiply stop", FG)],
    [("", None), (TL + HZ*38 + TR, RED), (VT + " | Stopped: Review code           " + VT, FG), (VT + " Duration: 1m                      " + VT, FG), (BL + HZ*38 + BR, RED)],
    [("PS D:\\> ", CYAN), ("wiply stats", FG)],
    [("", None), (TL + HZ*30 + TR, CYAN), (VT + " Total time:   3m               " + VT, FG), (VT + " Total tasks:  2                 " + VT, FG), (VT + " Today:        3m                 " + VT, FG), (VT + " Streak:       1 days            " + VT, FG), (BL + HZ*30 + BR, CYAN)],
    [("", None), ("  2026-10-03 " + "#"*20 + " 3m", GREEN), ("", None), ("  Top tasks:", CYAN), ("    Building wiply: 1x", FG), ("    Review code: 1x", FG)],
]

frames = []
for scene in scenes:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    y = 20
    for line, color in scene:
        if color is None:
            y += 10
            continue
        draw.text((20, y), line, fill=color, font=font)
        y += 22
    for _ in range(8):
        frames.append(img)

frames[0].save("demo.gif", save_all=True, append_images=frames[1:], duration=125, loop=0)
print("demo.gif created:", len(frames), "frames")
