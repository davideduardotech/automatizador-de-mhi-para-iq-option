from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("script.py", base=base)]

packages = ["iqoptionapi","colorama"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Automatizador MHI",
    options = options,
    version = "1.0",
    description = 'Automatizador(Iq Option) pra estrátegia MHI pra lucrar(R$) 100% no automático',
    executables = executables
)