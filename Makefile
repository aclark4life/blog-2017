all: update build
update:
	-yapf -i conf.py
	-flake8 conf.py
	git commit -a -m "Update"; git push
build:
	ablog build
serve:
	ablog serve
install:
	virtualenv .; bin/pip install -r requirements.txt
