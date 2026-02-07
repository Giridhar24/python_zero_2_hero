# Topic of the Day: Production Server (Gunicorn)
#
# Explanation: You’ve been running your API with uvicorn main:app --reload. This is for development (1 worker). In production, you need a robust server manager that can spawn multiple workers to handle thousands of requests. Gunicorn (Green Unicorn) is the standard for Python web apps.
#
# Code: Note: Run pip install gunicorn first.
import uvicorn

# Command Line (Terminal)

# 1. Development (What we used before)
# --reload restarts the server when code changes (Slow)
# uvicorn main:app --reload

# 2. Production (Gunicorn)
# -w 4: Spawn 4 worker processes (Use 1 per CPU core)
# -k uvicorn.workers.UvicornWorker: Use Uvicorn's fast async engine
# -b 0.0.0.0:8000: Bind to all IP addresses (Public)
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 main:app