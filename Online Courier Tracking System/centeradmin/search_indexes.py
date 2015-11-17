__author__ = 'srikanth'
import datetime
from haystack import indexes
from centeradmin.models import Parcel_Data

class ParcelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    P_ID = indexes.CharField(model_attr='P_ID')

    content_auto = indexes.EdgeNgramField(model_attr='P_ID')

    def get_model(self):
        return Parcel_Data

    def index_queryset(self, using=None):
        return self.get_model().objects.all()