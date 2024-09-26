
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(recipient__profile__campus=request.user.profile.group)
