from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Testimonial
from .forms import TestimonialPostForm
from django.contrib.auth.models import User



def get_testimonials(request):
    """
    Create a view that will return a
    list of Testimonials that were published prior to'now'
    and render them to the 'testimonials.html' template
    """
    testimonials = Testimonial.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "testimonials.html", {'testimonials': testimonials})


def testimonial_detail(request, pk):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'testimonialpost.html'
    template. Or return a 404 error if the
    post is not found
    """
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.save()
    return render(request, "testimonialpost.html", {'testimonial': testimonial})


def create_or_edit_testimonial(request, pk=None):
    testimonial = get_object_or_404(Testimonial, pk=pk) if pk else None
    if request.method == "POST":
        form = TestimonialPostForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            testimonial = form.save()
            return redirect(testimonial_detail, testimonial.pk)
    else:
        form = TestimonialPostForm(instance=testimonial)
    return render(request, 'testimonialpostform.html', {'form': form})