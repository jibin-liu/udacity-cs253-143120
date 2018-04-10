import webapp2
import cgi

form = """
<form method="post">
    <h2>Welcome to New Rot 13. Please enter the text below:</h2>
    <br>
    <textarea name="text" cols="80" rows="20" >%(q)s</textarea>
    <br>
    <input type="submit">
</form>
"""


class Rot13(webapp2.RequestHandler):
    def write_response(self, q=''):
        return self.response.write(form % {'q': q})

    def get(self):
        return self.write_response()

    def post(self):
        user_input = self.request.get('text')
        rot13 = self.rot13_transform(user_input)
        self.write_response(rot13)

    def rot13_transform(self, s):
        # do transform for aphabetic leters
        char_list = list(s)

        for index, char in enumerate(char_list):
            ord_num = ord(char)
            if ord_num >= 65 and ord_num <= 90:  # lowercase
                char_list[index] = chr(ord_num + 13) if ord_num <= 77 else chr(ord_num - 13)
            elif ord_num >= 97 and ord_num <= 122:  # uppercase
                char_list[index] = chr(ord_num + 13) if ord_num <= 109 else chr(ord_num - 13)

        res = ''.join(char_list)

        # then return escaped strings
        return self.escape_html_char(res)

    def escape_html_char(self, s):
        return cgi.escape(s, quote=True)
