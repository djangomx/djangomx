#coding: utf-8
from annoying.decorators import render_to
from .forms import ContactForm


@render_to("contact_home.html")
def contact_home(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return {'form': form}
