all: update build serve
update:
	git commit -a -m "Update"; git push
build:
	ablog build
serve:
	ablog serve
