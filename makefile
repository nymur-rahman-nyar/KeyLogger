push: 
	git add .
	git commit -m "$(filter-out $@,$(MAKECMDGOALS))" # adding message 
	git push origin main