from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',

    # ex: /page/about/
    url(r'^$', views.blogs, name='blogs'),
    url(
        r'^blog/view/(?P<slug>[^\.]+)',
        'blog.views.view_post',
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+)',
        'blog.views.view_category',
        name='view_blog_category'),
)