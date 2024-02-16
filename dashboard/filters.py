import django_filters
from .models import Question

class QuestionFilter(django_filters.FilterSet):
    question_text = django_filters.CharFilter(field_name='question_text', lookup_expr='exact')

    class Meta:
        model = Question
        fields = ['question_text']