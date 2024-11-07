from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Badge


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag = 0;
        for form in self.forms:
            if form.cleaned_data['is_main']:
                main_tag = main_tag + 1
                if main_tag > 1:
                    raise ValidationError('Не может быть два главных тэга')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Badge)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']