from product.models import Tag


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        tags = Tag.objects.all()
        context['tags'] = tags

        return context
