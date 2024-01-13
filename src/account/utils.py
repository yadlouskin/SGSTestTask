from django.contrib.auth.mixins import UserPassesTestMixin


class AdminRolePassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists() \
            or self.request.user.is_superuser
