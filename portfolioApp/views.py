from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from . models import *
from django.contrib import messages
from portfolioApp.email import emailInquiry
import threading
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

# Create your views here.

def home(request):
    try:
        return render(request, "index.html")
    
    except Exception as ex:
        print(ex)



# @csrf_exempt
def contactInquiry(request):
    try:
        if request.method=="POST":
            name = request.POST["your-name"]
            email = request.POST["your-email"]
            subject = request.POST["your-subject"]
            message = request.POST["your-message"]

            contact_inquiry = Contact(
                name=name,
                email=email,
                subject=subject,
                message=message,
                )
            contact_inquiry.save()
            # csrf_token = get_token(request)              ------

            # response = OTPGenerator(["michaeloluwole99@gmail.com"], "SUCCESSFUL LOGIN!!!", """We are pleased you login. Thank you.""")
            # response = ServiceTemplateEmailNotify.delay("michaeloluwole99@gmail.com", "SUCCESS", "index.html", humans)                  #
            # response = emailInquiry(email, "THANK YOU", "index.html", contact_inquiry)                                                  #normal method
            myThread = threading.Thread(target=emailInquiry, args=(email, "THANK YOU", "email.html", contact_inquiry))                    #threading implementation
            myThread.start()

            # OTGGenerator([email], "SUCCESSFUL SUBMISSION OF INQUIRY!!!", """We kindly inform you that your inquiry has been sent to the church for prior attention. We will get back to you shortly. Thank you.""")
            # return render(request, "index.html", {"csrf_token": csrf_token})      --------
            return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
        return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

    except Exception as ex:
        print(ex)




def like_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        post.likes += 1
        post.save()
        return JsonResponse({"success": True, "likes": post.likes})
    return JsonResponse({"success": False, "error": "Invalid request method."}, status=400)
