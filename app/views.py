from django.shortcuts import render
from django.http import HttpResponse
from .models import Enrolment
import json

# Create your views here.
def search(request):
  return render(request, 'search.html', {})

def query(request):
  course = request.GET.get('course')
  number = request.GET.get('number')
  print('course ' + course)
  print('number ' + number)
  enrolments = Enrolment.objects.filter(id='613').order_by('id');
  results = [enrolment.dept + str(enrolment.number) for enrolment in enrolments]

  counts = {}
  # all enrolments with given class
  givenClassIds = [enrolment.id for enrolment in Enrolment.objects.filter(dept=course).filter(number=number).filter(number__gte=300)]
  for id in givenClassIds:
    classesWith = Enrolment.objects.exclude(dept=course, number=number).filter(id=id).filter(number__gte=300)
    for c in classesWith:
      name = c.dept + str(c.number)
      if name in counts.keys():
        counts[name] += 1
      else:
        counts[name] = 1

  # results = sorted(counts.items(), key=lambda x: x[1]).reverse()
  results = sorted(counts.items(), key=lambda x: x[1], reverse=True)

  res = {}
  res['course'] = course
  res['number'] = number
  res['results'] = results
  return HttpResponse(json.dumps(res))
