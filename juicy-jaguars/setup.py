"""Setup script for Web95."""
import os
import sys
import subprocess


def supports_color():
    """Check if system supports ANSI colour."""
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                  'ANSICON' in os.environ)
    # isatty is not always implemented, #6223.
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return supported_platform and is_a_tty


def install(color=False):
    """Install Web95."""
    if color:
        green = "\u001b[32m\u001b[1m"
        yellow = "\u001b[33m\u001b[1m"
        red = "\u001b[31m\u001b[1m"
        reset = "\u001b[0m"
    else:
        green, yellow, red, reset = "", "", "", ""

    print(yellow+"Cloning Repository...")
    result = subprocess.call(["git", "clone",
                              "https://github.com/Juicy-Jaguars/\
summer-code-jam-2020"])
    result += os.chdir("summer-code-jam-2020/juicy-jaguars")

    if result != 0:
        print(red+"Error cloning Repository. Exiting...")
        sys.exit()

    print(green+"Repository successfully cloned."+reset)
    print()
    print(yellow+"Installing Pipenv..."+reset)
    result = subprocess.call(["pip3", "install", "pipenv"])

    if result != 0:
        print(red+"Error installing Pipenv. Exiting...")
        sys.exit()

    print(green+"Pipenv successfully installed."+reset)
    print()
    print(yellow+"Installing dependencies with Pipenv..."+reset)
    result = subprocess.call(["pipenv", "install"])

    if result != 0:
        print(red+"Error installing Dependencies. Exiting...")
        sys.exit()

    print(green+"Dependencies successfully installed."+reset)
    print()
    print(yellow+"Making migrations...")
    result = subprocess.call([os.path.join("Web95", "manage.py"),
                              "makemigrations"])

    if result != 0:
        print(red+"Error making migrations. Exiting...")
        sys.exit()

    print(green+"Made migrations successfully."+reset)
    print()
    print(green+"Successfully installed. Run with 'pipenv run Web95/manage.py\
 runserver'")


if __name__ == "__main__":
    color = supports_color()
    if os.argv[1] == "install":
        install(color)