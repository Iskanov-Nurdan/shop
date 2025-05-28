from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Home, Testimonial, BlogPost, Contact

from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def index_view(request):
    home = Home.objects.first()
    testimonials = Testimonial.objects.all()
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    contact_info = Contact.objects.first()
    context = {
        'home': home,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'contact_info': contact_info,
    }
    return render(request, 'index-3.html', context)



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=f'Новое сообщение от {name}',
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('base:index')  # Перенаправление на главную страницу
        except Exception as e:
            return HttpResponse(f"Ошибка отправки письма: {str(e)}")

    return render(request, 'index-3.html')  # Можно оставить для GET-запросов, но лучше перенаправить