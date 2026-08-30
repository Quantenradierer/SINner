import os

bind = "0.0.0.0:8010"
workers = int(os.environ.get("GUNICORN_WORKERS", "6"))
timeout = 120

# --reload: restart workers on .py changes. Enabled for local dev via the
# compose override; unset (falsey) on the server.
reload = os.environ.get("GUNICORN_RELOAD") == "1"

# log to the container's stdout/stderr so `docker compose logs` sees them
accesslog = "-"
errorlog = "-"
