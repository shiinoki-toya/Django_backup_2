from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import trn_scraping_details,testdata_for_select,Item
from django.db import connection
from django_tables2 import SingleTableView
from .tables import ItemTable  # 目次5で選んだ列column



#sample 追加####################
def lists(request):
    
#     sample_list = Sample.objects.all()
#     form = SampleForm(request.POST or None)
#     context = {
#         'sample_list':sample_list,
#         'form':form,
#     }
#     if request.method == 'POST':
#         if form.is_valid():

#             # create()の場合
#             Sample.objects.create(**form.cleaned_data)

# # # save()の場合
# #             sample = Sample(**form.cleaned_data)
# #             sample.save

#             return render(request, 'lists.html', context)
    return render(request, 'lists.html')


################################

@login_required
def home(request):
    # data = db_select()
    sc_app_data = {
    'app': 'Django',
    'num': range(10),
    # 'inf': data,
    }
    # context={'db_inf':db_select}
    return render(request, 'scapp/home.html', sc_app_data)

@login_required
def select(request):
    context = {
        'test_list': testdata_for_select.objects.all(),
    }
    
    return render(request, 'scapp/select.html',context)

class DetailView(SingleTableView):
    table_class = ItemTable
    template_name = 'scapp/detail.html'  # テーブル表示するhtml画面

    def get_queryset(self):
        # 1, 全レコードを可視化するならall()
        return Item.objects.all()
        
        # 2, 例えばpk(数値型)を用いて特定の数レコードを可視化するならfilter()
        # pk = self.kwargs.get('pk')
        # return Item.objects.filter(id__lte=pk).filter(id__gte=pk-5)


def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/sc_app/home/')

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'login_app/signup.html', param)


def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next == 'None':
                    return redirect(to='/sc_app/home/')
                else:
                    return redirect(to=next)
    else:
        form = LoginForm()
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }

    return render(request, 'login_app/login.html', param)

def logout_view(request):
    logout(request)

    return render(request, 'login_app/logout.html')

@login_required
def user_view(request):
    user = request.user

    params = {
        'user': user
    }

    return render(request, 'login_app/user.html', params)

@login_required
def other_view(request):
    users = User.objects.exclude(username=request.user.username)

    params = {
        'users': users
    }

    return render(request, 'login_app/other.html', params)