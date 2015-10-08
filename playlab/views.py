from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required, login_required
#from .models import Profile
from .forms import UserProfileForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required
def profile(request, username):
    user = Profile.objects.filter(username=username)
    form = UserProfileForm(instance=request)
    return render(request, 'profile.html', user)
    
    
@login_required
def dashboard(request, username):
    """
    User settings view, handles changing of user settings and
    entry distribution (eventually)
    """
    
    if request.method == 'POST': # If the form has been submitted...
        
        form = UserProfileForm(request.POST, instance=request.user) # A form bound to the POST data

        if form.is_valid(): # All validation rules pass
            form.save ()

            return render_to_response('profile_update_success.html',
                                      {},
                                      context_instance=RequestContext(request))

    else:
        #profile_info = Question.objects.order_by('-pub_date')[:5]
        #output = ', '.join([p.question_text for p in latest_question_list])
        #return HttpResponse(output)
        #get userinfo
        
        
        # create unbound form with initial values generated
        # from the user's profile data given by the Auth back
        
        
        #form = UserProfileForm() 
        #form = UserProfileForm(instance=request)
        #form = UserProfileForm(instance=request.user)
        #~ for k,v in form.items():
            #~ print k,v
        return render ( request, 'profile.html', { 'form': form, } )
    #~ return render_to_response('profile.html',
                                      #~ request.user,
                                      #~ context_instance=RequestContext(request))
