from core.gunicorn.logger import GunicornLogger


def get_app_options(
    host: str,
    port: int,
    workers: int,
    timeout: int,
    log_level: str,
) -> dict:
    return {
        "accesslog": "-",
        "errorlog": "-",
        "bind": f"{host}:{port}",
        "loglevel": log_level,
        "logger_class": GunicornLogger,
        "worker_class": "uvicorn.workers.UvicornWorker",
        "workers": workers,
        "timeout": timeout,
    }
