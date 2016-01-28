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
  course = request.GET.get('course')
  number = request.GET.get('number')
  excl = int(request.GET.get('excl'))

  ### PCA ###
  scores = {}
  # get key for given course
  code = course.upper() + str(number)
  # subtract 1 since Course table is zero indexed
  course_key = Course.objects.filter(code__startswith=code).first().unique_id - 1
  # create a query set
  sims = Similarity.objects.filter(from_class=course_key).exclude(to_class=course_key)
  for sim in sims:
    score = sim.score
    # add 1 back since Course table is zero indexed
    to_unique_id = sim.to_class + 1
    to_code = Course.objects.filter(unique_id=to_unique_id).first().code
    regex = re.compile(r'[^\d]+')
    to_number = int(regex.sub('', to_code))
    regex = re.compile(r'[\d]+')
    to_dept = regex.sub('', to_code)
    under_300 = to_number < 300
    exclude_CS = excl and to_dept == 'CPSC'
    # if excl:
    #   continue
    #scores[to_code] = score
    if under_300:
      continue
    scores[to_number] = score
  results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
  ### DONE: PCA ###

  res = {}
  # res['course'] = course.upper()
  res['course'] = course.upper()
  res['number'] = number
  res['results'] = results
  return HttpResponse(json.dumps(res))

# regex = re.compile(r'[^\d]+')
    # to_code = Course.objects.filter(unique_id=sim.unique_id)[0].code
    # to_number = int(regex.sub('', to_code))
    # if to_number >= 300:
    # scores[to_code] = sim.score
    # course = to_code
    # number = sim.score

'''
  # create a query set
  sims = Similarity.objects.filter(from_class=course_key.unique_id).exclude(to_class=course_key.unique_id)
  
  count = 0

  for sim in sims:
    count += 1
    # regex = re.compile(r'[^\d]+')
    to_code = Course.objects.filter(unique_id=sim.unique_id)[0].code
    # to_number = int(regex.sub('', to_code))
    # if to_number >= 300:
    scores[to_code] = sim.score
    course = to_code
    number = sim.score

  results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
'''

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