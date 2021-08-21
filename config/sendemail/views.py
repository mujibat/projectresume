#sendemail/views.py
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

class ContactView(FormView):
    template_name = 'sendemail/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('sendemail:success')

def form_valid(self, form):
    #calls the custom send method
    form.send
    return super().form_valid(form) 
    
class ContactSuccessView(TemplateView):
    template_name = 'sendemail/success.html'
        
                            
# Create your views here.
