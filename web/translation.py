from modeltranslation.translator import TranslationOptions, translator
from .models import News, Medicine


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = {
        'ru': ('title', 'content',), 
        'en': ('title', 'content',), 
        'default': ('title', 'content',)
    }
    fallback_languages = {
        'ru': ('title', 'content',), 
        'en': ('title', 'content',), 
        'default': ('title', 'content',)
    }
    
    
class MedicineTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = {
        'ru': ('name', 'description',), 
        'en': ('name', 'description',), 
        'default': ('name', 'description',)
    }
    fallback_languages = {
        'ru': ('name', 'description',), 
        'en': ('name', 'description',), 
        'default': ('name', 'description',)
    }
    
translator.register(News, NewsTranslationOptions)
translator.register(Medicine, MedicineTranslationOptions)
