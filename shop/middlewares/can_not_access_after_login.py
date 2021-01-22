from django.shortcuts import redirect ,render
def cantAccessAfterLogin(get_response):
  # function aayega yha pr
    def middleware(request):
        user = request.session.get('user')
        if user:
            #dont serve page
            return redirect('index')

        else:
           return get_response(request)

    return middleware