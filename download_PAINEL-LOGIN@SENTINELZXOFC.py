import os
import time
import subprocess
import re

# dev: @sentinelzxofc

def zx_animation():
    os.system('clear')
    print("\033[1;32mverificado arena...\033[0m")
    time.sleep(1)
    print("\033[1;32mExecutando...\033[0m")
    time.sleep(1)

    for i in range(1, 6):
        print("\033[1;33mAcessando servidor\033[0m")
        for j in range(1, 4):
            print("\033[1;33m.\033[0m", end='', flush=True)
            time.sleep(0.2)
        print()

    print("\033[1;32mConexão estabelecida!\033[0m")
    time.sleep(1)
    os.system('clear')

print("\033[1;32mIniciando verificação do diretório...\033[0m")

def verifica_diretorio(diretorio):
    while not os.path.isdir(diretorio):
        print("\033[1;31mO diretório '{}' não existe.\033[0m".format(diretorio))
        print("\033[1;32mDigite o local da pasta onde deseja executar (exemplo: /sdcard/pasta):\033[0m")
        diretorio = input()
    return diretorio

# Inicialize a variável 'diretorio'
diretorio = input("\033[1;32mDigite o local da pasta onde deseja executar (exemplo: /sdcard/pasta):\033[0m\n")

# Verifique o diretório
diretorio = verifica_diretorio(diretorio)

zx_animation()

try:
    os.chdir(diretorio)
except Exception as e:
    print(f"\033[1;31mErro ao mudar para o diretório: {e}\033[0m")
    exit(1)

subprocess.run(["pkg", "update", "-y"])

packages = ["python-pip", "python", "python3", "php", "curl", "aria2", "unzip", "wget", "file"]

for package in packages:
    subprocess.run(["pkg", "install", "-y", "--allow-downgrades", package])

URL = "https://www.mediafire.com/file/nqv1wl2dz3pymx3/PAINEL-LOGIN%2540SENTINELZXOFC.zip/file"

output = subprocess.run(["curl", "-s", URL], capture_output=True, text=True)
REAL_URL = re.search(r'(?<=href=")https://download[^"]*', output.stdout).group()

subprocess.run(["aria2c", "-o", "PAINEL-LOGIN@SENTINELZXOFC.zip", REAL_URL])

if not os.path.exists("PAINEL-LOGIN@SENTINELZXOFC.zip"):
    print("\033[1;31mErro: Arquivo não baixado.\033[0m")
    exit(1)

subprocess.run(["unzip", "-o", "PAINEL-LOGIN@SENTINELZXOFC.zip", "-d", "./"])

os.chdir("PAINEL-LOGIN@SENTINELZXOFC")

os.remove("../PAINEL-LOGIN@SENTINELZXOFC.zip")

time.sleep(1)
time.sleep(1)
time.sleep(1)

os.system('clear')
