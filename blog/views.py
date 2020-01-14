from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post.html', {})
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')