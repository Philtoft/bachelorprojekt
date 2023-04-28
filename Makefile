clean:
	py3clean .
	rm -rf .ipynb_checkpoints/
	rm -rf wandb
	rm -rf model
install:
	pip install -r requirements.txt