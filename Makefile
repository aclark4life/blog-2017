all: build serve
build:
	ablog build
install:
	virtualenv .; bin/pip install -r requirements.txt
push:
	git commit -a -m "Update"; git push
serve:
	ablog serve
