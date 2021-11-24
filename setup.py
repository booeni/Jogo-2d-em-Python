from os import name
import cx_Freeze
executables = [cx_Freeze.Executable(
    script="primeiroJogo.py", icon="assets/icone.ico")]
 
 
cx_Freeze.setup(
    name="Superman dead",
    options={"build_exe": {"packages": ["pygame"],
        "include_files":["assets"]
    }},
    executables=executables
)
