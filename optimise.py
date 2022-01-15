import os, os.path, subprocess, json

path = "."
mydata = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith((".jpg", ".jpeg", "png"))]
#https://stackoverflow.com/questions/57982945/how-to-apt-get-install-in-a-github-actions-workflow

results = []

for file in mydata:
    a = os.stat(file).st_size
    if file.endswith((".jpg", ".jpeg")):
        command = "jpegoptim"
    elif file.endswith((".png",)):
        command = "optipng"
    result = subprocess.run([command, file], shell=False, capture_output=True)
    b = os.stat(file).st_size
    print(a, b)
    if a <= b:
        continue # wasn't worth it
    results.append([result.stdout.decode('utf-8'), result.stderr.decode('utf-8'), file, a, b])

print(json.dumps(results))
if results != []: sys.exit(36)
