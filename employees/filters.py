import django_filters


from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    designacao = django_filters.CharFilter(field_name='designacao', lookup_expr='iexact')
    emp_nome = django_filters.CharFilter(field_name='emp_nome', lookup_expr='icontains')
    #id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='do EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='para EMP ID')



    class Meta:
        model = Employee
        fields = ['designacao', 'emp_nome', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, nome, value):
        if nome == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif nome == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset