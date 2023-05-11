import asyncio
import os
import tornado.web

app_port = os.environ.get("APP_PORT", 8888)
environmental_var= os.environ
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(str(environmental_var))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(app_port)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())