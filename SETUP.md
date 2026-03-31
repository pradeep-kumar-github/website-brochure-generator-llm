This setup is for Mac people!

- **Clone the repo :**

https://github.com/pradeep-kumar-github/website-brochure-generator-llm#


- **Install Anaconda environment :**

Download Anaconda from https://docs.anaconda.com/anaconda/install/mac-os/
After installing, you'll need to open a fresh, new Terminal to be able to use it (and you might even need to restart).

Setup the environment:
- Open a new Terminal (Applications > Utilities > Terminal)
- Navigate to the "project root directory" using `cd ~/Documents/Projects/website-brochure-generator-llm` (replace this path as needed with the actual path to the llm_engineering directory, your locally cloned version of the repo). Do `ls` and check you can see subdirectories.

- Download conda, open terminal and run: curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
- Install conda, open terminal and run: bash Miniconda3-latest-MacOSX-arm64.sh
- Check if installed: now open new terminal and run : conda --version

Go to project directory again:
make sure environment.yml is being cloned/copied from the github prject repo (website-brochure-generator-llm)
- Create the environment: `conda env create -f environment.yml`
- Wait for a few minutes for all packages to be installed - in some cases, this can literally take 20-30 minutes if you've not used Anaconda before, and even longer depending on your internet connection. Important stuff is happening! 
- You have now built an isolated, dedicated AI environment for engineering LLMs, running vector datastores, and so much more! You now need to activate it using this command: `conda activate llms`  
You should see `(llms)` in your prompt, which indicates you've activated your new environment.


- **Start Jupyter Lab :**

- In the Terminal window, from within the `llm_engineering` folder, type: `jupyter lab`
...and Jupyter Lab should open up in a browser. If you've not seen Jupyter Lab before, I'll explain it in a moment! Now close the jupyter lab browser tab, and close the Terminal, and move on to next Part.


- **Last Part :**
