# Crear un programa que genere una contraseña fuerte. 
# El programa debe pedir el número de caracteres que va a tener la contraseña.
# La contraseña tendrá mayusculas, minúsculas, números y símbolos.
# El programa debe poder ejecutarse desde la bash de la computadora.
# El programa debe copiarse automáticamente al portapapeles.


#El comentario de la línea 10 debe ser el primero del archivo cuando se guarde en la carptea local.

#!/usr/bin/env python3
import os
import secrets
import shutil
import string
import subprocess

MIN_LEN = 9
SIMBOLOS = "!@#$%^&*()-_=+[]{};:,.?"


def gen_contr(n):
    grup = [string.ascii_lowercase, string.ascii_uppercase, string.digits, SIMBOLOS]
    tods = "".join(grup)
    
    pwd = [secrets.choice(g) for g in grup]
    pwd += [secrets.choice(tods) for _ in range(n - len(pwd))]
    secrets.SystemRandom().shuffle(pwd)
    return "".join(pwd)


def copi(text):
    coman = [["xclip", "-selection", "clipboard"], ["xsel", "--clipboard", "--input"]]
    if os.environ.get("WAYLAND_DISPLAY"):
        coman.insert(0, ["wl-copy"])
    for cmd in coman:
        if shutil.which(cmd[0]):
            try:
                subprocess.run(cmd, input=text.encode(), check=True)
                return True
            except subprocess.CalledProcessError:
                continue
    return False


def main():
    while True:
        try:
            nun_carac = int(input(f"Escribe la cantidad de caracteres (mínimo {MIN_LEN}): "))
            if nun_carac >= MIN_LEN:
                break
            print(f"Debe ser al menos {MIN_LEN}.")
        except ValueError:
            print("Escribe un número entero.")

    pwd = gen_contr(nun_carac)
    print(f"\nLa contraseña es: {pwd}\n")

    if copi(pwd):
        print("Copiada al portapapeles.")
    else:
        print("No se pudo copiar.")


if __name__ == "__main__":
    main()