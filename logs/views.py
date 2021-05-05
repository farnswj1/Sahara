from django_filters.views import FilterView
from django.contrib.auth.mixins import UserPassesTestMixin
from .filters import LogFilter

# Create your views here.
class LogListView(UserPassesTestMixin, FilterView):
    template_name = "logs/list.html"
    context_object_name = "logs"
    filterset_class = LogFilter
    paginate_by = 15
    extra_context = {"title": "Logs"}
    
    def test_func(self):
        return self.request.user.is_superuser