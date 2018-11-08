from django.test import TestCase
from django.contrib.auth.models import User
from .models import Store, Account, Category, SubCategory
from .models import TransactionStatus, Tag, Transaction
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


class CategoryModelTestCase(TestCase):
    """This class defines the test suite for the API Category model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.category_name = "Dummy Category"
        self.category = Category(name=self.category_name)

    def test_model_can_create_a_category(self):
        """Test the Category model can create a category."""
        old_count = Category.objects.count()
        self.category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)


class SubCategoryModelTestCase(TestCase):
    """This class defines the test suite for the API SubCategory model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.subcategory_name = "Dummy SubCategory"
        self.subcategory = SubCategory(name=self.subcategory_name)

    def test_model_can_create_a_subcategory(self):
        """Test the Category model can create a subcategory."""
        old_count = SubCategory.objects.count()
        self.subcategory.save()
        new_count = SubCategory.objects.count()
        self.assertNotEqual(old_count, new_count)


class TransactionStatusModelTestCase(TestCase):
    """This class defines the test suite for the API TransactionStatus model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.transactionstatus_name = "Dummy TransactionStatus"
        self.transactionstatus = TransactionStatus(name=self.transactionstatus_name)

    def test_model_can_create_a_transactionstatus(self):
        """Test the TransactionStatus model can create a transactionstatus."""
        old_count = TransactionStatus.objects.count()
        self.transactionstatus.save()
        new_count = TransactionStatus.objects.count()
        self.assertNotEqual(old_count, new_count)


class StoreViewTestCase(TestCase):
    """Test suite for the api Store views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create_user(username="testuser")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.data = {'name': 'Dummy Store1'}
        self.response = self.client.post(
            reverse('create_store'),
            self.data,
            format="json")

    def test_api_can_create_store(self):
        """Test the api has store creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        response = new_client.get(reverse('details_store',
            kwargs={'pk': 3}), format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

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
        user = User.objects.create_user(username="testuser")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.data = {'name': 'Dummy Account1'}
        self.response = self.client.post(
            reverse('create_account'),
            self.data,
            format="json")

    def test_api_can_create_account(self):
        """Test the api has account creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        response = new_client.get(reverse('details_account',
            kwargs={'pk': 3}), format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

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


class CategoryViewTestCase(TestCase):
    """Test suite for the api Category views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create_user(username="testuser")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.data = {'name': 'Dummy Category1'}
        self.response = self.client.post(
            reverse('create_category'),
            self.data,
            format="json")

    def test_api_can_create_category(self):
        """Test the api has category creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        response = new_client.get(reverse('details_category',
            kwargs={'pk': 3}), format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_category(self):
        """Test the api can get a given category."""
        category = Category.objects.get()
        response = self.client.get(
            reverse('details_category',
            kwargs={'pk': category.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, category)

    def test_api_can_update_category(self):
        """Test the api can update a given category."""
        category = Category.objects.get()
        change_category = {'name': 'Changed Category'}
        res = self.client.put(
            reverse('details_category', kwargs={'pk': category.id}),
            change_category, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_category(self):
        """Test the api can delete a category."""
        category = Category.objects.get()
        response = self.client.delete(
            reverse('details_category', kwargs={'pk': category.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class SubCategoryViewTestCase(TestCase):
    """Test suite for the api SubCategory views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create_user(username="testuser")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.data = {'name': 'Dummy SubCategory1'}
        self.response = self.client.post(
            reverse('create_subcategory'),
            self.data,
            format="json")

    def test_api_can_create_subcategory(self):
        """Test the api has subcategory creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        response = new_client.get(reverse('details_subcategory',
            kwargs={'pk': 3}), format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_subcategory(self):
        """Test the api can get a given subcategory."""
        subcategory = SubCategory.objects.get()
        response = self.client.get(
            reverse('details_subcategory',
            kwargs={'pk': subcategory.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, subcategory)

    def test_api_can_update_subcategory(self):
        """Test the api can update a given subcategory."""
        subcategory = SubCategory.objects.get()
        change_subcategory = {'name': 'Changed SubCategory'}
        res = self.client.put(
            reverse('details_subcategory', kwargs={'pk': subcategory.id}),
            change_subcategory, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_subcategory(self):
        """Test the api can delete a subcategory."""
        subcategory = SubCategory.objects.get()
        response = self.client.delete(
            reverse('details_subcategory', kwargs={'pk': subcategory.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class TransactionStatusViewTestCase(TestCase):
    """Test suite for the api TransactionStatus views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create_user(username="testuser")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.data = {'name': 'Dummy TransactionStatus1'}
        self.response = self.client.post(
            reverse('create_transactionstatus'),
            self.data,
            format="json")

    def test_api_can_create_transactionstatus(self):
        """Test the api has transactionstatus creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        response = new_client.get(reverse('details_transactionstatus',
            kwargs={'pk': 3}), format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_transactionstatus(self):
        """Test the api can get a given transactionstatus."""
        transactionstatus = TransactionStatus.objects.get()
        response = self.client.get(
            reverse('details_transactionstatus',
            kwargs={'pk': transactionstatus.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, transactionstatus)

    def test_api_can_update_transactionstatus(self):
        """Test the api can update a given transactionstatus."""
        transactionstatus = TransactionStatus.objects.get()
        change_transactionstatus = {'name': 'Changed TransactionStatus'}
        res = self.client.put(
            reverse('details_transactionstatus', kwargs={'pk': transactionstatus.id}),
            change_transactionstatus, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_transactionstatus(self):
        """Test the api can delete a transactionstatus."""
        transactionstatus = TransactionStatus.objects.get()
        response = self.client.delete(
            reverse('details_transactionstatus', kwargs={'pk': transactionstatus.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

