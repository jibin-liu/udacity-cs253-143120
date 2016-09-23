import webapp2
from unit2.rot13 import Rot13
from unit2.sign_up import SignUp, Welcome

form = """
<form method="post" action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.write(q)

        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(self.request)

app = webapp2.WSGIApplication([
                              ('/', MainPage),
                              ('/testform', TestHandler),
                              ('/unit2/rot13', Rot13),
                              ('/unit2/signup', SignUp),
                              ('/unit2/signup/welcome', Welcome)
                              ], debug=True)
