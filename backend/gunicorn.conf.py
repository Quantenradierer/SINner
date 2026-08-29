bind = "0.0.0.0:8010"
workers = 6
timeout = 120

# log to the container's stdout/stderr so `docker compose logs` sees them
accesslog = "-"
errorlog = "-"
