#!/bin/bash
# Test script for Smart Document Analyzer

set -e

echo "Running Smart Document Analyzer Tests..."
echo "========================================"

# Run unit tests
echo "Running unit tests..."
python -m pytest tests/ -v --tb=short

# Run tests with coverage
echo ""
echo "Running tests with coverage..."
python -m pytest tests/ --cov=src --cov-report=html --cov-report=term

echo ""
echo "All tests completed successfully!"
echo "Coverage report generated in htmlcov/index.html"
