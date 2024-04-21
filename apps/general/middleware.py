from django.utils import translation 


class LanguageMiddleware:
    def __init__(self, get_response):
      self.get_response = get_response

    def __call__(self, request):
        old_currency = request.session.get("currency")
        currency = request.GET.get("currency", old_currency)
        if currency != '1':
            currency = '2'
        request.session['currency'] = currency

        old_language = request.session.get('language')
        language = request.GET.get('language', old_language)
        if language != 'uz':
            language = 'ru'
        request.session['language'] = language 
        language_code = language
        translation.activate(language_code)

        response = self.get_response(request)
        return response