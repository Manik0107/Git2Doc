#!/bin/bash
# Backend server startup script
export PYTHONPATH=.
uvicorn api.main:app --reload --port 8000
