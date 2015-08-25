from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('main.py', 'Console', targetName = 'blackout')
]

setup(name='blackout',
      version = '1.0',
      description = "A text adventure tribute to Five Nights At Freddy's.",
      options = dict(build_exe = buildOptions),
      executables = executables)
