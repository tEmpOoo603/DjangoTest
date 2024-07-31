from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from goods.models import Products

def q_search(query:str):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector('name','description')
    query = SearchQuery(query)
    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")

    # return Products.objects.filter(description__search=query)

    # q_objects = Q()
    # keywords = [ word for word in query.split() if len(word)>2 ]
    #
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #     return Products.objects.filter(q_objects)