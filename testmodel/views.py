from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import JCBook,JCPerson


class TestModelView(ListView):
    template_name = 'dbform_oo.html'
    model=JCBook
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TestModelView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['owners'] = JCPerson.objects.all()
        return context

    def get_queryset(self):
        if self.args and self.args[0]:
            self.owner = get_object_or_404(JCPerson, id=self.args[0])
        else:
            self.owner = JCPerson.objects.all()
        return JCBook.objects.filter(owner= self.owner)


    def get(self, request, *args, **kwargs):
        if "addBookOwner_oo" in request.path:
            self.addBookOwner(request)
            redirect(super().get(request, args, kwargs))
        elif "addBook_oo" in request.path:
            self.addBook(request)
            redirect(super().get(request, args, kwargs))
        return super().get(request, args, kwargs)


    def addBook(self, request):
        request.encoding = 'utf-8'
        if 'name' in request.GET:
            bookName = request.GET['name']
            if not bookName:
                return HttpResponse('书名不应为空')

            ownerId = request.GET['owner']
            owner = JCPerson.objects.get(id=ownerId)
            bookId = 0
            for var in JCBook.objects.order_by("id"):
                if bookId < var.id:
                    bookId = var.id
            bookId += 1
            book = JCBook(id=bookId, name=request.GET['name'], owner=owner)
            book.save()

    def addBookOwner(self, request):
        request.encoding = 'utf-8'
        if 'name' in request.GET:
            bookOwner = request.GET['name']
            if not bookOwner:
                return HttpResponse('书籍拥有者不应为空')

            owner = JCPerson.objects.filter(name=bookOwner)
            if owner:
                return HttpResponse('书籍拥有者' + bookOwner + '已存在')
            ownerId = 0
            for var in JCPerson.objects.order_by("id"):
                if ownerId < var.id:
                    ownerId = var.id
            ownerId += 1
            person = JCPerson(id=ownerId, name=bookOwner)
            person.save()


    #def post(self, request):

