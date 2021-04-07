from django.shortcuts import render, get_object_or_404
from .models import cv
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import loader








# Create your views here.
def homeView(request):
    return render(request, 'cv/cv_home.html')
def detailView(request):
    if request.method == 'POST':
        #Acessing data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        degreeName = request.POST.get('degreeName')
        university = request.POST.get('university')
        skills = request.POST.get('skills')
        shortBio = request.POST.get('shortBio')
        project = request.POST.get('project')
        experience = request.POST.get('experience')
        companyname = request.POST.get('companyname')
        #Adding to model
        new_data = cv(name=name, email=email, phone=phone, country=country,
                                            state=state, city=city, address=address,
                                            degreeName=degreeName,
                                            university=university,skills=skills
                                            ,shortBio=shortBio,project=project,experience=experience,companyname=companyname)
        new_data.save()
        context = {
        'name':name, 'email':email, 'phone':phone, 'country':country,
                                            'state':state, 'city':city, 'address':address,
                                            'degreeName':degreeName,'university':university,
                                            'skills':skills, 'shortBio':shortBio,
                                            'project':project, 'experience':experience, 'companyname':companyname
       }
    else:
        context = {'name': 'no_data found'}
    return render(request, 'cv/cv_detail.html', context)

def render_pdf_view(request):
    user_profile = cv.objects.get()

    template_path = 'cv/pdf.html'
    context = {'user_profile':user_profile}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('we had some errors <pre>'+ html + '</pre>')
    return response
