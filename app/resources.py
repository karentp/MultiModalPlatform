from import_export import resources
from .models import *

class SegmentationResource(resources.ModelResource):
    class Meta:
        model = Segmentation