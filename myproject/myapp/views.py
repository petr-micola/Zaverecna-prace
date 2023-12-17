from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserForm


@login_required
def view_profile(request):
    user_profile = request.user
    return render(request, 'profile/view_profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    user_profile = request.user  # Assuming the user is authenticated
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # Update the existing user's profile information
            form.save()
            return redirect('view_profile')
    else:
        # If it's a GET request, create a form with the current user's data
        form = CustomUserForm(instance=user_profile)

    # Your custom logic for displaying the edit profile page
    return render(request, 'profile/edit_profile.html', {'form': form})
