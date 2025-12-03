# create the venv
# criar o venv
python -m venv .venv
source .venv/bin/activate

# install something to the venv
# instalar algo no venv
.venv/bin/python -m pip install pathlib

# freeze and install reqs
# congelar e instalar requisitos
pip freeze > requirements.txt
