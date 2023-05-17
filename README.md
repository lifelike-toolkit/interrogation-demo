# interrogation-demo
A game where you can interrogate a suspect and figure out how to get a confession by intimidating the suspect, either through playing bad cop, or calling out their lies. Made with Lifelike

# Setup Process
1. Clone the project from github with `git clone https://github.com/lifelike-toolkit/interrogation-demo.git` (or however really, this is the https method). I will assume you have git.
2. From the terminal, run `pip install -r requirements.txt` to install all dependencies. If you don't have pip, or python, here is the guide to install [python](https://realpython.com/installing-python/) (should come with pip by default), and [pip](https://pip.pypa.io/en/stable/installation/) (python is required, so this is only really if you somehow did not install pip with python)
3. Get an OpenAI API key from [their website](https://platform.openai.com/) and save it somewhere. For the game to be stable you need to be on the paid plan, since the current implementation involves more requests than a free tier is allowed to make in 1 minute. 
4. Create .venv file, where you must set `OPENAI_API_KEY={the key you saved from step 3}`
5. Run `python game.py` (`python3 game.py` for some people) and enjoy

# How to Play
Read the DinnerPartyCaseFile.md file for instructions.
In the actual game, you can say and ask whatever to Jason, the suspect. The goal is to question him, find out his motive and force him to confess to murder.
**Important:** If you want to make Jason talk about something, do not ask "Can you describe" or "Would you describe". Instead, give him commands, like "describe the victim".
