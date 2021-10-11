JUPYTER_PATH="$(jupyter --paths | head -n 2| tail -1 | cut -d# -f2 | xargs)"
cp -f ./jupyter_setup/jupyter_notebook_config.py "$JUPYTER_PATH/jupyter_notebook_config.py"

git config --global core.attributesfile .gitattributes
git config --global filter.dropoutput_ipynb.clean "python ./jupyter_setup/ipynb_output_filter.py"
git config --global filter.dropoutput_ipynb.smudge cat
