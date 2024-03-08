# Delete all compiled Python files
clean:
	@echo "🧹 Cleaning up..."
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	@echo "✨ Clean up complete!"

# Lint using Ruff
lint:
	@echo "🔍 Linting..."
	ruff . --fix
	djhtml .
	@echo "✨ Linting complete!"

# Check using Django's system-check
check:
	@echo "🔍 Running system checks..."
	python manage.py check
	python manage.py check --deploy
	python manage.py check --tag security
	@echo "✨ All checks done!"

# Update dependencies and pre-commit
update:
	@echo "🔄 Updating dependencies and pre-commit..."
	poetry update
	pre-commit autoupdate
	@echo "✨ Update complete!"

# Collect static files
collect:
	@echo "📦 Collecting static files..."
	python manage.py collectstatic --no-input
	@echo "✨ Static files collected!"

# Run tests
test:
	@echo "🧪 Running tests..."
	python manage.py test
	@echo "✨ Running tests complete!"

# Setup project with dependencies
setup:
	poetry install
	pre-commit install
	pre-commit run --all-files
	@echo "✨ Project setup complete!"

# Run server
run:
	python manage.py runserver
