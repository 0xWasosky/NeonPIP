import subprocess


install = "pip install "
delete = "pip uninstall "
update = "pip install --upgrade"

load_libs = subprocess.getoutput("pip freeze").splitlines()

