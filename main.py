import requests

update = str(requests.get("https://raw.githubusercontent.com/TheGreatMaximus98/PythonGame/main/main.py").content).replace("b'", "").replace("'", "").replace("\\n\\n", "\n").removesuffix("\\n")
with open("main.py", "w") as f:
    f.write(update)
