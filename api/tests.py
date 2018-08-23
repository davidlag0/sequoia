from django.test import TestCase
from .models import Store, Account
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class StoreModelTestCase(TestCase):
    """This class defines the test suite for the API Store model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.store_name = "Dummy Store"
        self.store = Store(name=self.store_name)

    def test_model_can_create_a_store(self):
        """Test the Store model can create a store."""
        old_count = Store.objects.count()
        self.store.save()
        new_count = Store.objects.count()
        self.assertNotEqual(old_count, new_count)


class AccountModelTestCase(TestCase):
    """This class defines the test suite for the API Account model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.account_name = "Dummy Account"
        self.account = Account(name=self.account_name)

    def test_model_can_create_an_account(self):
        """Test the Account model can create an account."""
        old_count = Account.objects.count()
        self.account.save()
        new_count = Account.objects.count()
        self.assertNotEqual(old_count, new_count)


class StoreViewTestCase(TestCase):
    """Test suite for the api Store views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        self.data = {'name': 'Dummy Store1'}
        self.response = self.client.post(
            reverse('create_store'),
            self.data,
            format="json")

    def test_api_can_create_store(self):
        """Test the api has store creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_store(self):
        """Test the api can get a given store."""
        store = Store.objects.get()
        response = self.client.get(
            reverse('details_store',
            kwargs={'pk': store.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, store)

    def test_api_can_update_store(self):
        """Test the api can update a given store."""
        store = Store.objects.get()
        change_store = {'name': 'Changed Store'}
        res = self.client.put(
            reverse('details_store', kwargs={'pk': store.id}),
            change_store, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_store(self):
        """Test the api can delete a store."""
        store = Store.objects.get()
        response = self.client.delete(
            reverse('details_store', kwargs={'pk': store.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class AccountViewTestCase(TestCase):
    """Test suite for the api Store views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        self.data = {'name': 'Dummy Account1'}
        self.response = self.client.post(
            reverse('create_account'),
            self.data,
            format="json")

    def test_api_can_create_account(self):
        """Test the api has account creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_account(self):
        """Test the api can get a given account."""
        account = Account.objects.get()
        response = self.client.get(
            reverse('details_account',
            kwargs={'pk': account.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, account)

    def test_api_can_update_account(self):
        """Test the api can update a given account."""
        account = Account.objects.get()
        change_account = {'name': 'Changed Account'}
        res = self.client.put(
            reverse('details_account', kwargs={'pk': account.id}),
            change_account, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_account(self):
        """Test the api can delete an account."""
        account = Account.objects.get()
        response = self.client.delete(
            reverse('details_account', kwargs={'pk': account.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

