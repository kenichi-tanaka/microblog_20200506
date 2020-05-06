from django.test import TestCase, Client


class BlogTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('/')

        # stauts code => 200 OK
        # stauts code => 302 Redirect
        # stauts code => 404 Not Found
        self.assertEqual(res.status_code, 200)
        
