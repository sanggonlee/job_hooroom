.PHONY: etl

etl:
	(\
		. venv/bin/activate; \
		. env.sh; \
		python -m etl; \
	)
