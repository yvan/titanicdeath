.PHONY: run init migrate upgrade downgrade show stage

run:
	gunicorn titanicdeath.app:app --reload

stage:
	git push stage master

prod:
	git push prod master
