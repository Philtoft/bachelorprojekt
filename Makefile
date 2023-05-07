clean:
	py3clean .
	rm -rf .ipynb_checkpoints/
	rm -rf wandb
	rm -rf model
	rm *.log
install:
	pip install -r requirements.txt