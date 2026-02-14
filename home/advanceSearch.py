from django.db.models import F
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField 
from django.contrib.postgres.fields import DateRangeField, DateTimeRangeField, IntegerRangeField, DecimalRangeField
from django.utils import timezone
import uuid
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from django.db.models import JSONField
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from .addressType import AddressField
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank
)
from django.contrib.postgres.search import TrigramSimilarity
from appInstanceData import AppInstance



query = SearchQuery("delhi electrician")

qs = AppInstance.objects.annotate(
    search=SearchVector("address", weight="A"),
    rank=SearchRank(SearchVector("address"), query)
).filter(rank__gt=0.1).order_by("-rank")






qs = AppInstance.objects.annotate(
    similarity=TrigramSimilarity("address", "delhi main brnch")
).filter(similarity__gt=0.2).order_by("-similarity")








query = SearchQuery("delhi electrician")

qs = AppInstance.objects.annotate(
    search=SearchVector("address"),
    rank=SearchRank(F("search"), query),
    similarity=TrigramSimilarity("address", "delhi electrician")
).filter(
    rank__gt=0.05
).order_by("-rank", "-similarity")
