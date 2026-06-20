import gifos
import os

t = gifos.Terminal(width=800, height=500, xpad=15, ypad=15, font_size=15)

# Boot sequence
t.gen_text(text="Initializing aryanOS v2.0...", row_num=1)
t.gen_text(text="Loading kernel modules... [OK]", row_num=2)
t.gen_text(text="Mounting file systems... [OK]", row_num=3)
t.gen_text(text="Starting user session...", row_num=4)
t.gen_text(text=" ", row_num=5)
t.gen_text(text="\x1b[1;32mWelcome to Aryan Kumar's Terminal!\x1b[0m", row_num=6)
t.gen_text(text="----------------------------------", row_num=7)
t.gen_text(text=" ", row_num=8)

t.gen_text(text="$ whoami", row_num=9, contin=False)
t.gen_text(text="Aryan Kumar (B.Tech CS 2029)", row_num=10)
t.gen_text(text=" ", row_num=11)

t.gen_text(text="$ cat profile.txt", row_num=12)
t.gen_text(text="> \x1b[32mFocused on ML systems & Deep Learning Math\x1b[0m", row_num=13)
t.gen_text(text="> \x1b[36mGoal: Research Engineer / Data Science\x1b[0m", row_num=14)
t.gen_text(text="> \x1b[33mLocation: New Delhi, India\x1b[0m", row_num=15)
t.gen_text(text=" ", row_num=16)

t.gen_text(text="$ neofetch --stack", row_num=17)
t.gen_text(text="  \x1b[35mResearch & Math\x1b[0m: Linear Algebra, Optimization, Calculus", row_num=18)
t.gen_text(text="  \x1b[34mProgramming\x1b[0m: Python, PyTorch, C, Node.js", row_num=19)
t.gen_text(text=" ", row_num=20)

t.gen_text(text="$ echo $QUOTE", row_num=21)
t.gen_text(text='"C makes it easy to shoot yourself in the foot; C++ makes it harder,', row_num=22)
t.gen_text(text=' but when you do, it blows your whole leg off."', row_num=23)
t.gen_text(text=" ", row_num=24)

t.gen_text(text="$ _", row_num=25)

# Generate GIF
t.gen_gif()

if os.path.exists('output.gif'):
    os.rename('output.gif', 'profile.gif')
