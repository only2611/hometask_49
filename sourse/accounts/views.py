from django.contrib.auth import login, authenticate, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import MyUserCreationForm, UserChangeForm, ProfileChangeForm, PasswordChangeForm
from accounts.models import Profile


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('trecker:p-view')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


class RegisterView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = MyUserCreationForm


    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('trecker:p-view')
        return next_url


def logout_view(request):
    logout(request)
    return redirect('trecker:p-view')



class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "profile.html"
    paginate_by = 5
    paginate_orphans = 0


    def get_context_data(self, **kwargs):
        paginator = Paginator(self.get_object().projects.all(), self.paginate_by, self.paginate_orphans)
        page_number = self.request.GET.get('page', 1)
        page_object = paginator.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context['page_obj'] = page_object
        context['projects'] = page_object.object_list
        context['is_paginated'] = page_object.has_other_pages()
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'change_user.html'
    profile_form_class = ProfileChangeForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'profile_form' not in context:
            context['profile_form'] = self.profile_form_class(instance=self.get_object().profile)
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        profile_form = self.profile_form_class(instance=self.object.profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_valid(form, profile_form)


    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form, profile_form):
        form.save()
        profile_form.save()
        return redirect("accounts:profile", self.object.pk)


    def form_invalid(self, form, profile_form):
        return self.render_to_response(self.get_context_data(form=form,profile_form=profile_form))


class ChangePasswordView(UpdateView):
    model = User
    form_class = PasswordChangeForm
    template_name = "change_password.html"


    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk":self.request.user.pk})


    def form_valid(self, form):
        result = super().form_valid()
        update_session_auth_hash(self.request, self.object)
        return result



