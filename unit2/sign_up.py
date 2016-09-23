import webapp2
import re


form = """
<form method="post">
    <h2>Sign up below:</h2>
    <br>
    <label>
        Username:
        <input type="text" name="username" value="%(username)s">%(user_error)s
    </label>
    <br>
    <label>
        Password:
        <input type="password" name="password">%(pw_error)s
    </label>
    <br>
    <label>
        Verify Password:
        <input type="password" name="verify">%(verify_error)s
    </label>
    <br>
    <label>
        Email(option):
        <input type="text" name="email" value="%(email)s">%(email_error)s
    </label>
    <br>
    <input type="submit">
</form>
"""


class SignUp(webapp2.RequestHandler):
    def render(self, username='', email='', user_error='', pw_error='',
               verify_error='', email_error=''):

        d = {
            'username': username,
            'email': email,
            'user_error': user_error,
            'pw_error': pw_error,
            'verify_error': verify_error,
            'email_error': email_error
        }

        self.response.write(form % d)

    def get(self):
        self.render()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        error_dict = self.validation(username, password, verify, email)
        if error_dict:
            self.render(username=username, email=email, **error_dict)
        else:
            self.redirect('/unit2/signup/welcome?username=' + username)

    def validation(self, username, password, verify, email):
        d = dict()

        if not self.valid_username(username):
            d['user_error'] = 'This is not a valid username'

        if not self.valid_password(password):
            d['pw_error'] = 'This is not a valid password'
        else:
            if not self.verify_password(password, verify):
                d['verify_error'] = 'The passwords entered are not the same'

        if email and not self.valid_email(email):
            d['email_error'] = 'This is not a valid email'

        return d

    def valid_username(self, username):
        user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return user_re.match(username)

    def valid_password(self, pw):
        pw_re = re.compile(r"^.{3,20}$")
        return pw_re.match(pw)

    def verify_password(self, pw1, pw2):
        return True if pw1 == pw2 else False

    def valid_email(self, email):
        email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        return email_re.match(email)


class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if username:
            self.response.write('<h2>Welcome, {}!</h2>'.format(username))
        else:
            self.redirect('/unit2/signup')

