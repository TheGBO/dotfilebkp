# create the venv
python -m venv .venv
source .venv/bin/activate
# install something to the venv
.venv/bin/python -m pip install pathlib

# freeze and install reqs
pip freeze > requirements.txt
