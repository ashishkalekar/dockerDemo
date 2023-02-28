import requests
import unittest

class TestWebsiteLoad(unittest.TestCase):

    def test_website_load(self):
        url = 'https://atg.world/'
        print(f'Sending request to {url}...')
        response = requests.get(url)
        print(f'Response status code: {response.status_code}')
        self.assertEqual(response.status_code, 200, msg='Website failed to load properly')

if __name__ == '__main__':
    unittest.main()


#import requests
#def test_website_load():
 #   url = 'https://atg.world/'
  #  response = requests.get(url)
   # return response.status_code == 200

#if test_website_load():
 #   print('Website loaded successfully')
#else:
 #   print('Website failed to load')

