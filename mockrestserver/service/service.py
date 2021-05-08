from fastapi import FastAPI
import uvicorn

from mockrestserver.service.hadler import Handler

class Service:

    def __init__(self, ctx):
        self.ctx = ctx
        self.app = FastAPI(debug=True)
        self.populate_handlers()

    def populate_handlers(self):
        for endpoint in self.ctx.endpoints():
            method = endpoint.get("method", "get").lower()
            handle = Handler(endpoint.get("resp"))
            path = endpoint.get("path")
            if method == "get":
                self.app.get(path)(handle.callback_handler)
            elif method == "post":
                self.app.post(path)(handle.callback_handler)
            elif method == "put":
                self.app.put(path)(handle.callback_handler)
            elif method == "delete":
                self.app.delete(path)(handle.callback_handler)

    def run(self):
        uvicorn.run(self.app, host="0.0.0.0", port=5000, log_level="info")
