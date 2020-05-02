run:
	uvicorn sales_service.main:app --reload

test:
	pipenv run pytest -sx tests/

pyformat:
	black sales_service/.

clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete
	@find . -iname '*.DS_STORE' -delete
	@find . -iname 'db.sqlite3' -delete
	@find . -iname '.coverage' -delete
	@rm -rf cashback-service/.pytest_cache
