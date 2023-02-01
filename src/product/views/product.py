from django.views import generic
from product.models import Variant, Product, ProductVariant


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ctxproducts'] = Product.objects.prefetch_related('productvariant_set')

        return context
