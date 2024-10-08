help:
	@grep -E '^[a-zA-Z_0-9]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

watch: ## watches the directory for changes and executes instructions
	python -m watch

example: vite ## runs the example project

vite: ## runs the vite project
	cd example/vite && npm run dev