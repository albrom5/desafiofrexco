import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker

from desafioFrexco.core.models import User


class CreateUserPostValid(APITestCase):
    def setUp(self):
        data = {
            'username': 'tester',
            'birth_date': '2000-10-01',
            'password': 'test_pass'
        }
        self.response = self.client.post('/create_user/', data)

    def test_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_user_created(self):
        self.assertTrue(User.objects.exists())

    def test_user_data(self):
        user = User.objects.all().first()
        self.assertEqual(user.username, 'tester')
        self.assertEqual(user.birth_date, datetime.date(2000, 10, 1))

    def test_auto_generate_random_password(self):
        data = {
            'username': 'testerwithautopass',
            'birth_date': '2010-10-01',
        }
        self.client.post('/create_user/', data)
        user = User.objects.get(username='testerwithautopass')
        self.assertEqual(user.username, 'testerwithautopass')
        self.assertTrue(user.password)


class CreateUserPostInvalid(APITestCase):
    def test_user_without_username(self):
        data = {
            'birth_date': '2000-10-01',
            'password': 'test_pass'
        }
        response = self.client.post('/create_user/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.exists())
        self.assertIn('username', response.data.serializer.errors.keys())


    def test_user_without_birth_date(self):
        data = {
            'username': 'tester',
            'password': 'test_pass'
        }
        response = self.client.post('/create_user/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.exists())
        self.assertIn('birth_date', response.data.serializer.errors.keys())


class ListUsers(APITestCase):
    def setUp(self):
        users = baker.make('core.User', _quantity=100)

    def test_get_user_list_json(self):
        response = self.client.get('/users_json/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 100)
        self.assertEqual(response.headers['Content-Type'],
                         'application/json')

    def test_get_user_list_csv(self):
        response = self.client.get('/users_csv/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 100)
        self.assertEqual(response.headers['Content-Type'],
                         'text/csv; charset=utf-8')

    def test_get_user_list_xlsx(self):
        response = self.client.get('/users_xlsx/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 100)
        self.assertEqual(response.headers['Content-Type'],
                         'application/xlsx; charset=utf-8')
