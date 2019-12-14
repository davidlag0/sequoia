"""Model Tests."""

from django.db.utils import IntegrityError
from django.db.models.deletion import ProtectedError
from django.test import TestCase
from api.models import Store, Account, Category, SubCategory
from api.models import TransactionStatus, Transaction, Tag


class StoreModelTestCase(TestCase):
    """This class defines the test suite for the API Store model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.store_name = "Dummy Store"
        Store.objects.create(name=self.store_name)

    def test_model_can_create_a_store(self):
        """Test the Store model can create a store."""
        self.assertEqual(Store.objects.get().name,
                         self.store_name)

    def test_model_fails_with_duplicate_store(self):
        """Test the addition of a second Store with the same name."""
        self.assertRaises(IntegrityError, Store.objects.create,
                          name=self.store_name)

    def test_model_fails_with_blank_store(self):
        """Test the addition of a Store with a blank name."""
        # self.assertRaises(IntegrityError, Store.objects.create, name="")
        Store.objects.create(name="")
        print("bleh:", Store.objects.get(pk=2).name)
        self.assertRaises(IntegrityError, Store.objects.create,
                          name=None)


class AccountModelTestCase(TestCase):
    """This class defines the test suite for the API Account model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.account_name = "Dummy Account"
        Account.objects.create(name=self.account_name)

    def test_model_can_create_an_account(self):
        """Test the Account model can create an account."""
        self.assertEqual(Account.objects.get().name,
                         self.account_name)

    def test_model_fails_with_duplicate_account(self):
        """Test the addition of a second Account with the same name."""
        self.assertRaises(IntegrityError, Account.objects.create,
                          name=self.account_name)


class CategoryModelTestCase(TestCase):
    """This class defines the test suite for the API Category model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.category_name = "Dummy Category"
        Category.objects.create(name=self.category_name)

    def test_model_can_create_a_category(self):
        """Test the Category model can create a category."""
        self.assertEqual(Category.objects.get().name,
                         self.category_name)

    def test_model_fails_with_duplicate_category(self):
        """Test the addition of a second Category with the same name."""
        self.assertRaises(IntegrityError, Category.objects.create,
                          name=self.category_name)


class SubCategoryModelTestCase(TestCase):
    """This class defines the test suite for the API SubCategory model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.subcategory_name = "Dummy SubCategory"
        SubCategory.objects.create(name=self.subcategory_name)

    def test_model_can_create_a_subcategory(self):
        """Test the Category model can create a subcategory."""
        self.assertEqual(SubCategory.objects.get().name,
                         self.subcategory_name)

    def test_model_fails_with_duplicate_subcategory(self):
        """Test the addition of a second SubCategory with the same name."""
        self.assertRaises(IntegrityError, SubCategory.objects.create,
                          name=self.subcategory_name)


class TransactionStatusModelTestCase(TestCase):
    """TransactionStatus Model Tests.

    This class defines the test suite for the API
    TransactionStatus model.
    """

    def setUp(self):
        """Define the test client and other test variables."""
        self.transactionstatus_name = "Dummy TransactionStatus"
        TransactionStatus.objects.create(name=self.transactionstatus_name)

    def test_model_can_create_a_transactionstatus(self):
        """Test the TransactionStatus model can create a transactionstatus."""
        self.assertEqual(TransactionStatus.objects.get().name,
                         self.transactionstatus_name)

    def test_model_fails_with_duplicate_transactionstatus(self):
        """Transactionstatus Duplicate Test.

        Test the addition of a second TransactionStatus with the same name.
        """
        self.assertRaises(IntegrityError, TransactionStatus.objects.create,
                          name=self.transactionstatus_name)


class TransactionModelTestCase(TestCase):
    """Transaction Model Tests.

    This class defines the test suite for the API
    Transaction model.
    """

    def setUp(self):
        """Define the test client and other test variables."""
        # Prepare the Transaction fields.
        self.transaction_date = "2018-11-07T20:12:00-05:00"
        self.original_description = "Test Original Description"
        self.custom_description = "Test Custom Description"
        Transaction.objects.create(
            transaction_date=self.transaction_date,
            original_description=self.original_description,
            custom_description=self.custom_description,
            account=Account.objects.create(name="Test Account"),
            category=Category.objects.create(name="Test Category"),
            transactionstatus=TransactionStatus.objects.create(
                                name="Test TransactionStatus"))

    def test_model_can_create_a_transaction(self):
        """Test the Transaction model can create a transaction."""
        self.assertEqual(Transaction.objects.get().original_description,
                         self.original_description)
        self.assertEqual(Transaction.objects.get().custom_description,
                         self.custom_description)


class TagModelTestCase(TestCase):
    """This class defines the test suite for the API Tag model."""

    def setUp(self):
        """Define the test client and other test variables."""
        # Create a new Transaction and save it as it is necessary to
        # create a transaction as the Tag needs the transaction ID to
        # which it will be linked to.
        self.transaction = Transaction.objects.create(
            transaction_date="2018-11-07T20:12:00-05:00",
            original_description="Test Original Description",
            custom_description="Test Custom Description",
            account=Account.objects.create(name="Test Account"),
            category=Category.objects.create(name="Test Category"),
            transactionstatus=TransactionStatus.objects.create(
                name="Test TransactionStatus"
            )
        )

        self.tag_name = "Test Tag Name"
        self.tag = Tag.objects.create(tag_name=self.tag_name,
                                      transaction_id=self.transaction)

    def test_model_can_create_a_tag(self):
        """Test the Tag model can create a tag correctly."""
        self.assertEqual(self.tag.tag_name, self.tag_name)
        self.assertEqual(self.tag.transaction_id.id, self.transaction.id)

    def test_model_fails_with_duplicate_tag(self):
        """
        Tag Model Tests.

        Test the addition of a second tag with the same name as the first
        tag and tied to the same transaction. This test should fail as
        these two items should make a unique combination.
        """
        self.assertRaises(IntegrityError, Tag.objects.create,
                          tag_name=self.tag_name,
                          transaction_id=self.transaction)

    def test_deleting_tag_keeps_transaction(self):
        """Test that deleting a tag keeps the related transaction."""
        self.tag.delete()
        self.assertEqual(self.transaction.id, 1)

    def test_cannot_delete_transaction_if_tag_linked_to_it(self):
        """
        Test to delete transaction with a tag.

        Test that we cannot delete a transaction if a tag is still
        related to it.
        """
        transaction = Transaction.objects.get()
        self.assertRaises(ProtectedError, transaction.delete)
