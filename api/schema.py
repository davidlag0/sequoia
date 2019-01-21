from django.db.models import Q
import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from api.models import Store, Account, Category, SubCategory
from api.models import TransactionStatus, Transaction, Tag


class StoreType(DjangoObjectType):
    class Meta:
        model = Store


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class SubCategoryType(DjangoObjectType):
    class Meta:
        model = SubCategory


class TransactionStatusType(DjangoObjectType):
    class Meta:
        model = TransactionStatus


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class Query(graphene.ObjectType):
    all_stores = graphene.List(StoreType)
    all_accounts = graphene.List(AccountType)
    all_categories = graphene.List(CategoryType)
    all_subcategories = graphene.List(SubCategoryType)
    all_transactionstatus = graphene.List(TransactionStatusType)
    all_transactions = graphene.List(TransactionType)
    all_tags = graphene.List(TagType)

    store = graphene.Field(StoreType, id=graphene.Int(),
                           name=graphene.String())

    stores = graphene.List(StoreType,
                           search=graphene.String(),
                           id=graphene.Int(),
                           name=graphene.String())

    @login_required
    def resolve_all_stores(self, info, **kwargs):
        return Store.objects.all()

    @login_required
    def resolve_store(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Store.objects.get(pk=id)
        if name is not None:
            return Store.objects.get(name=name)
        return None

    @login_required
    def resolve_stores(self, info, search=None, **kwargs):
        result = Store.objects.all()
        print("result:", result)

        if search:
            print("search:", search)
            filter = (Q(id__icontains=search) | Q(name__icontains=search))
            result = result.filter(filter)

        print("before return")
        return result

    @login_required
    def resolve_all_accounts(self, info, **kwargs):
        return Account.objects.all()

    @login_required
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    @login_required
    def resolve_all_subcategories(self, info, **kwargs):
        return SubCategory.objects.all()

    @login_required
    def resolve_all_transactionstatus(self, info, **kwargs):
        return TransactionStatus.objects.all()

    @login_required
    def resolve_all_transactions(self, info, **kwargs):
        return Transaction.objects.all()

    @login_required
    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()


class CreateStore(graphene.Mutation):
    """GraphQL API Mutation for Store."""

    store = graphene.Field(StoreType)

    class Arguments:
        """Fields required for Store mutation."""

        name = graphene.String(required=True)

    @login_required
    def mutate(self, info, name):
        """Mutation Function."""
        store = Store(name=name)
        store.save()
        return CreateStore(store=store)


class StoreMutation(graphene.ObjectType):
    """GraphQL API Mutations."""

    create_store = CreateStore.Field()
