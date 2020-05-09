.PHONY: etl force_deploy

etl:
	(\
		. venv/bin/activate; \
		. env.sh; \
		python -m etl; \
	)

force_deploy:
	date +"%D %T" >> force_deploy
