from django.shortcuts import render

# Create your views here.
def root(req):
    return render(req, 'first_app/main.html')

def contact(req):
    context = {}
    if req.method == 'POST':
        text = req.POST['inp_text']
        context['text'] = text

    return render(req, 'first_app/contact.html',context)