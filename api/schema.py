import graphene
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

    @login_required
    def resolve_all_stores(self, info, **kwargs):
        return Store.objects.all()

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
