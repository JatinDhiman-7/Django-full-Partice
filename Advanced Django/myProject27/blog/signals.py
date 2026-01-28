from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Blog

#Triggrred before saving a blog
@receiver(pre_save,sender=Blog)
def before_blog_save(sender,instance,**kwargs):
    print(f"About to save blog [pre-save]: {instance.title}")

#Triggered after saving a blog
@receiver(post_save,sender=Blog)
def after_Blog_save(sender,instance,created,**kwargs):
    if created:
        print(f"New Blog created[Post-save]:{instance.title}")
    else:
        print(f'Blog updated[Post-save]:{instance.title}')