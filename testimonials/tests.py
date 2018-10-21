from django.test import TestCase
from django.test import Client
from django.conf.urls import url
from django.http import HttpRequest
from django.urls import reverse
from .models import Testimonial
from .views import get_testimonials
from .forms import TestimonialPostForm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render




class TestimonialsPageTests(TestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get('/testimonials/')
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonials.html')

    @staff_member_required
    def create_or_edit_testimonial(self, request, testimonial_id):
        testimonial = get_object_or_404(TestimonialPostForm, id=testimonial_id)
    
        if request.POST:
            form = TestimonialPostForm(request.POST, instance=testimonial)
    
            if form.is_valid():
                form.save()
                return redirect('testimonial_detail', testimonial.id)
        else:
            form = TestimonialPostForm(instance=testimonial)
    
        return render(request, "testimonialpostform.html")