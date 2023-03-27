from constants import POST_PER_PAGE
from django.core.paginator import Paginator


def paginate(request, post_list):
    paginator = Paginator(post_list, POST_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
