#!/bin/bash
source venv/bin/activate
python -m black --check --exclude=venv .