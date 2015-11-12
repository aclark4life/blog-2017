all: update build serve
update:
	yapf -i conf.py; flake8 conf.py
	git commit -a -m "Update"; git push
build:
	ablog build
serve:
	ablog serve
