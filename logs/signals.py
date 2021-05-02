from django.db.models.signals import post_save, post_delete
from inventory.models import Item, Category
from users.models import User
from django.dispatch import receiver
from .models import Log

@receiver(post_save, sender=Item)
def save_item(sender, instance, created, **kwargs):
    action = "Create" if created else "Update"
    Log.objects.create(model_name="Item", model_id=instance.id, action=action)


@receiver(post_save, sender=Category)
def save_category(sender, instance, created, **kwargs):
    action = "Create" if created else "Update"
    Log.objects.create(model_name="Category", model_id=instance.id, action=action)


@receiver(post_save, sender=User)
def save_user(sender, instance, created, **kwargs):
    if created:
        Log.objects.create(model_name="User", model_id=instance.id, action="Create")


@receiver(post_delete, sender=Item)
def delete_item(sender, instance, **kwargs):
    Log.objects.create(model_name="Item", model_id=instance.id, action="Delete")


@receiver(post_delete, sender=Category)
def delete_category(sender, instance, **kwargs):
    Log.objects.create(model_name="Category", model_id=instance.id, action="Delete")
