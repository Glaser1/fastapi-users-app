from gunicorn.app.base import BaseApplication
from fastapi import FastAPI


class Application(BaseApplication):
    def __init__(self, application: FastAPI, options: dict):
        self.options = options
        self.application = application
        super().__init__()

    def load(self):
        return self.application

    @property
    def config_options(self) -> dict:
        return {k: v for k, v in self.options.items() if k in self.cfg.settings and v is not None}

    def load_config(self):
        for k, v in self.config_options.items():
            self.cfg.set(k.lower(), v)
