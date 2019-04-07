"""GraphQL Tests."""

from .models import Store
from django.contrib.auth import get_user_model
from graphql_jwt.testcases import JSONWebTokenTestCase


class StoreGraphQLTestCase(JSONWebTokenTestCase):
    """Test suite for the GraphQL API Store Queries."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = get_user_model().objects.create(username='test')
        self.client.authenticate(self.user)

        self.store_name = "Dummy Store"
        self.store = Store(name=self.store_name)
        self.store.save()

    def test_api_can_create_store(self):
        """Test the GraphQL API has Store creation capability."""
        query = '''
        mutation {
            createStore(name: "Bob") {
                name
            }
        }
        '''

        variables = {
            'name': 'Bob',
        }

        # executed = self.client.execute(query, variables=variables)
        executed = self.client.execute(query)
        print("errors:", executed.errors)
        print("data:", executed.data)
        print("db1:", Store.objects.count())
        print("db2:", Store.objects.get())
        assert executed == {'blop'}

    def test_api_can_get_store(self):

        query = '''
        {
            allStores {
                name
            }
        }
        '''

        variables = {
          'username': self.user.username,
        }

        print("db3:", Store.objects.count())
        executed = self.client.execute(query)
        print("errors:", executed.errors)
        print("data:", executed.data)
        assert executed == {'blop'}
