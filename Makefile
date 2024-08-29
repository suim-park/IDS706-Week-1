# Install dependencies
install:
	pip install -r requirements.txt

# Lint with pylint
lint:
	pylint **/*.py

# Test with pytest
test:
	pytest

# Format with black
format:
	black .

# Run all commands
all: install lint format test