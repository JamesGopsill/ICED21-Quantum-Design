# ICED21 Quantum Combinatorial Design paper accompanying scripts

This repo features the scripts used in the International Conference on Engineering Design paper "Quantum Combinatorial Design". The paper can be found at: [insert url when released]

## Running the scripts

To run the scripts, you first need python installed on your computer and to download this repository. `cd` into the repository and using the terminal, create a python virtual environment. For example,

`python -m venv .venv`

Start the virtual environment

`source .venv/bin/activate` (MacOS/Linux/WSL) or `.venv/Scripts/activate` (Windows)

You should see `(venv)` at the beginning of your terminal prompt. Then install the requirements.

`pip install -r requirements.txt`

With the requirements installed, you can run the code by simply calling python and the respective file. E.g.

`python no-overlap.py`