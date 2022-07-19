from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, Scope, ArticleScope


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleScope)
class ArticleScopeAdmin(admin.ModelAdmin):
    pass


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Не определены рубрики')

        count_main = 0
        for form in self.forms:

            if form.cleaned_data['is_main']:
                count_main += 1
            if count_main > 1:
                raise ValidationError('Главная рубрика отмечена более одного раза!')

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]