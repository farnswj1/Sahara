from django_filters import FilterSet, CharFilter, NumberFilter, ChoiceFilter
from .models import Log

ACTIONS = (
    ("Create", "Create"),
    ("Update", "Update"),
    ("Delete", "Delete"),
)

class LogFilter(FilterSet):
    action = ChoiceFilter("action", label="Action", lookup_expr="exact", choices=ACTIONS)
    model_name = CharFilter("model_name", label="Model Name", lookup_expr="icontains")
    model_id = NumberFilter("model_id", label="Model ID", lookup_expr="exact")

    class Meta:
        model = Log
        fields = ("action", "model_name", "model_id")