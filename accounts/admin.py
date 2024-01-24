from django.contrib import admin
from . import models
from tution.models import ApplicantForTutor
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# class AdminApprouval(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         info = ApplicantForTutor.objects.get(user=request.user)
#         obj.save()
#         if info.admin_approval:
#             obj.tutors.user = obj.user
#             obj.tutors.save()
#             email_subject = "Applicant Confirmation"
#             email_body = render_to_string('applicant.html', {'user': obj.user})
#             email = EmailMultiAlternatives(email_subject, '', to=[obj.user.email])
#             email.attach_alternative(email_body, "text/html")
#             email.send()
#             obj.admin_approval = False

admin.site.register(models.UserInformation)

