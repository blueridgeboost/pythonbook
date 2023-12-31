###
### Makefile for building and pushing site
###

GITHUB_PAGES_BRANCH=gh-pages
DESTINATION = docs


develop: 
	sleep 1 && echo "Opening local browser..." &&  open http://localhost:1313/pythonbook &
	hugo server --config hugo.toml --buildDrafts --watch --destination $(DESTINATION)

html: 
	hugo --config hugo.toml --destination $(DESTINATION)

github: html 
	git add -A :/; git commit -m "Rebuilt site" ; git push

.PHONY: html develop
