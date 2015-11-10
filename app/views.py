from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
logger.debug('VVVV')

# Create your views here.
def search(request):
  return render(request, 'search.html', {})

def query(request):
	course = request.GET.get('course')
	number = request.GET.get('number')
	logger.debug('XXX')
	logger.info("BHABHABH")
	print('hello')
	# logging.info('ZZZ' + number)
