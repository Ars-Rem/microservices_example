from cleanapi import BaseHandler
url_tail = "/ex.json"
class Handler(BaseHandler):
    async def get(self):
        self.set_status(200)
        self.write({"status": "working"})
