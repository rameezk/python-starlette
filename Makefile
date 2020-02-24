build:
	docker build -t python-starlette .

run: build
	docker run -p 5000:5000 python-starlette

run-detached: build
	docker run -d -p 5000:5000 python-starlette
