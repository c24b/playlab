from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required, login_required
from .models import Profile


# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required
def profile(request, username):
    
    user = Profile.objects.filter(username=username)
    print user.__dict__.items()
    return render(request, 'profile.html', user)
    
    
@login_required
def dashboard(request, username):
    """
    User settings view, handles changing of user settings and
    entry distribution (eventually)
    """

    if request.method == 'POST': # If the form has been submitted...

        form = UserProfileForm(request.POST, instance=request.user.profile) # A form bound to the POST data

        if form.is_valid(): # All validation rules pass
            form.save ()

            return render_to_response('profile_update_success.html',
                                      {},
                                      context_instance=RequestContext(request))

    else:
        # create unbound form with initial values generated
        # from the user's profile
        form = UserProfileForm (instance=request.user.profile)

    return render ( request, 'profile.html', { 'form': form, } )
