from django.http import HttpResponse

def test_text(request):
    text_data = open("./media/test_text.txt", "rb").read()
    response = HttpResponse(content_type='text')
    response['Content-Disposition'] = 'attachment; filename="test_text.txt"'
    return response