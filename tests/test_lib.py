import unittest

from pyaes256 import PyAES256

class Test(unittest.TestCase):
    password = 'Xkju2#%^&^Hg182067!opKKJSiklks8274kj--97'
    text = 'TESTING'
    lib = PyAES256()
    url = ''
    salt = ''
    iv = ''

    def test_encypt_decrypt(self):
        print('Encrypt secret text:', self.text)
        res = self.lib.encrypt(self.text, self.password)
        self.url = res['url']
        self.salt = res['salt']
        self.iv = res['iv']

        decrypt = bytes.decode(self.lib.decrypt(self.url, self.salt, self.iv, self.password))
        print('Decrypt result:', decrypt)
        self.assertEqual(self.text, decrypt)
        
