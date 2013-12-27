#coding: utf-8
from annoying.decorators import render_to, ajax_request

from .models import Job
from .forms import JobForm


@render_to("jobs_home.html")
def jobs_home(request):
    """ Render Job opportunities home page. """
    jobs = Job.objects.filter(active=True, aproved=True)
    form = JobForm()
    return {'jobs': jobs, 'form': form}


@ajax_request
def new_job(request):
    """ Add a new job"""
    if request.POST:
        form = form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return {'success': True}
        else:
            return {'success': False, 'errors': form.errors.keys()}
    return {'success': False, 'error': 'Request not valid'}
