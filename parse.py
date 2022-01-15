import subprocess

a = subprocess.run(["python3", "optimise.py"], capture_output=True).stdout

import json
a = json.loads(a)

for i in a:
    print(f"{i[2]} should be optimised! (Old: {i[3] / 1024} KiB, new: {i[4] / 1024} KiB)")
