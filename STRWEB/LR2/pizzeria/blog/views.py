# Create your views here.
import random
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pizza.models import PromoCode

from .forms import ReviewForm
from .models import Post, CompanyInfo, FAQ, Review, LogoCompanies, Vacancy, Employee


def home(request):
    latest_post = Post.objects.order_by('-published_date').first()
    images = ['pizzeria_promo_1.png', 'pizzeria_promo_2.png', 'pizzeria_promo_3.png']  # List of image paths
    random_image = random.choice(images)  # Select a random image from the list
    logo_companies = LogoCompanies.objects.all()
    return render(request, 'blog/home.html', {'latest_post': latest_post,
                                              'random_image': random_image, 'logo_companies': logo_companies})


def about_company(request):
    return render(request, 'blog/about_company.html')


def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/news_post.html', {'post': post})


def news_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/news_list.html', {'posts': posts})


def faq_list(request):
    faqs = FAQ.objects.all().order_by('-added_date')
    return render(request, 'blog/faq_list.html', {'faqs': faqs})


def promo_list(request):
    promos = PromoCode.objects.all().order_by('-is_active')
    for promo in promos:
        promo.discount *= 100
    return render(request, 'blog/promo_list.html', {'promos': promos})


def review_list(request):
    reviews = Review.objects.all().order_by('added_date')
    return render(request, 'blog/reviews.html', {'reviews': reviews})

def test(request):
    return render(request, 'blog/test.html')


def vacancy_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'blog/vacancy.html', {'vacancies': vacancies})


def employee_view(request):
    workers = Employee.objects.all()
    return render(request, 'blog/employee.html', {'workers': workers})


@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Process the form data
            # Assuming you have a Review model to save the review data
            review = form.save(commit=False)
            review.user_name = request.user.first_name  # Assuming you have a user field in your Review model
            review.added_date = datetime.now()
            review.save()
            return redirect('blog:reviews')  # Redirect to a success page after submitting the review
    else:
        form = ReviewForm()

    return render(request, 'submit_review.html', {'form': form})
