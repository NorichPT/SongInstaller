from cx_Freeze import setup, Executable

executables = [Executable("main.py"), Executable("music.py")]

setup(name="Songinstaller",
      version="0.1",
      description="MP3",
      executables=executables
      )
