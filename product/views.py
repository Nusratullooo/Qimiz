from django.contrib import messages
from django.http import HttpResponseRedirect
from product.form import CommentForm
from product.models import Comment


def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            data.save()
            messages.success(request, "Message is successfully saved !")
        return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
