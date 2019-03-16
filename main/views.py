"""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Transaction, Store, Account, Category, SubCategory, Status, Tag

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'latest_transaction_list'

    def get_queryset(self):
        """
        """
        Return the last five transactions.
        """
        """
        return Transaction.objects.filter(
            transaction_date__lte=timezone.now()
        ).order_by('-transaction_date')[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Transaction
    template_name = 'main/detail.html'

    def get_queryset(self):
        return Transaction.objects.filter(transaction_date__lte=timezone.now())


def vote(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    try:
        selected_store = transaction.store_set.get(pk=request.POST['store'])
    except (KeyError, Store.DoesNotExist):
        # Redisplay the transaction form.
        return render(request, 'main/detail.html', {
            'transaction': custom_description,
            'error_message': "You didn't select a store.",
        })
    else:
        #selected_choice.votes = F('votes') + 1
        #selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('main:detail', args=(transaction.id,)))
"""