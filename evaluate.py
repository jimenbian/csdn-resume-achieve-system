#-*- coding: UTF-8 -*- 
from __future__ import division
from math import e


def get_score(visit_times,origin_articles,comments):
      visit_times_int=int(visit_times)
      origin_articles_int=int(origin_articles)
      comments_int=int(comments)
      a1=comments_int/(1+origin_articles_int)
      a2=visit_times_int*a1
      a3=e**(-a2/200000)
      a4=1/(1+a3)
      return float(a4*100)


#print get_score('158140','130','225')
