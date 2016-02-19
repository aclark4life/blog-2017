all: update build
update:
	git commit -a -m "Update"; git push
build:
	ablog build
serve:
	ablog serve
install:
	virtualenv .; bin/pip install -r requirements.txt
