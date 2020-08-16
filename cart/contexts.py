from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from merchandise.models import Merchandise


def cart_content(request):

    cart_items = []
    total = 0
    merchandise_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            merchandise = get_object_or_404(Merchandise, pk=item_id)
            total += item_data * merchandise.price
            merchandise_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'merchandise': merchandise,
            })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'merchandise_count': merchandise_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context



# merchandise = get_object_or_404(Merchandise, pk=item_id)
#         total += quantity * merchandise.price
#         merchandise_count += quantity
#         cart_items.append({
#             'item_id': item_id,
#             'quantity': quantity,
#             'merchandise': merchandise,
#         })