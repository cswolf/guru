from django.shortcuts import render
from django.http import HttpResponse
from .models import Enrolment
from .models import Course
from .models import Similarity
import json
import re

# Create your views here.
def search(request):
  return render(request, 'search.html', {})

def query(request):
  course = request.GET.get('course').upper()
  number = request.GET.get('number')
  excl = int(request.GET.get('excl'))

  ### PCA ###
  scores = {}
  # get key for given course
  code = course + str(number)
  # subtract 1 since Course table is zero indexed
  # course_key = Course.objects.filter(code__startswith=code).first().unique_id - 1
  course_key = -1
  keys = {}
  for c in Course.objects.all():
    c_key = c.unique_id
    c_code = c.code
    if c_code.startswith(code):
      course_key = c_key
    keys[c_key] = c_code
  if course_key < 0:
    res = {}
    res['course'] = course
    res['number'] = number
    res['results'] = results
    return HttpResponse(json.dumps(res))
  # create a query set
  sims = Similarity.objects.filter(from_class=course_key).exclude(to_class=course_key)
  regex = re.compile(r'[^\d]+')
  for sim in sims:
    score = sim.score
    # add 1 back since Course table is zero indexed
    to_unique_id = sim.to_class + 1
    # Load Course key table in array instead
    # to_code = Course.objects.filter(unique_id=to_unique_id).first().code
    to_code = keys[to_unique_id]
    to_number = int(regex.sub('', to_code))
    under_300 = to_number < 300
    exclude_CS = excl and to_code.startswith('CPSC')
    if under_300 or exclude_CS:
      continue
    scores[to_code] = score
  results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
  ### DONE: PCA ###

  res = {}
  res['course'] = course
  res['number'] = number
  res['results'] = results
  return HttpResponse(json.dumps(res))

  ### Frequency counting ###
  # counts = {}
  # # all student ids from enrolments with given class
  # givenClassIds = [enrolment.id for enrolment in Enrolment.objects.filter(dept=course).filter(number=number).filter(number__gte=300)]
  # # for each student who took the given class
  # for id in givenClassIds:
  #   # create a query set of other classes that student took
  #   classesWith = Enrolment.objects.exclude(dept=course, number=number).filter(id=id).filter(number__gte=300)
  #   # keep count of these classes
  #   for c in classesWith:
  #     name = c.dept + str(c.number)
  #     if name in counts.keys():
  #       counts[name] += 1
  #     else:
  #       counts[name] = 1
  # # sort by descending count
  # results = sorted(counts.items(), key=lambda x: x[1], reverse=True)
  ### DONE: Frequency counting ###