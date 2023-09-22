###
### Makefile for building and pushing site
###

GITHUB_PAGES_BRANCH=gh-pages
# THEME = brb


develop: 
	sleep 1 && echo "Opening local browser..." &&  open http://localhost:1313/pythonbook &
	hugo server  --buildDrafts --watch 

html: 
	hugo  

github: html 
	git add -A :/; git commit -m "Rebuilt site" ; git push

.PHONY: html develop
