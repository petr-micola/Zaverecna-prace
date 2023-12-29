from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserForm

def quiz(request):
    return render(request, 'quiz/quiz.html')

@login_required
def view_account(request):
    user_profile = request.user
    return render(request, 'account/view_account.html', {'user_profile': user_profile})


@login_required
def edit_account(request):
    user_profile = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_account')
    else:
        form = CustomUserForm(instance=user_profile)

    return render(request, 'account/edit_account.html', {'form': form})
