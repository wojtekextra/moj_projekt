#!/bin/bash
source venv/bin/activate
python3 -m black --check --exclude '/venv/|/build/|/dist/' .