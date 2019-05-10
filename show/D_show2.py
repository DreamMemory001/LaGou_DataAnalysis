# coding=utf-8
from example.commons import Collector, Faker

from pyecharts import options as opts

from pyecharts.charts import Page, Pie

"""
Created on 19-5-09
@title: ''
@author: XuChao
"""
# 饼图
if __name__ == "__main__":

   C = Collector()

   @C.funcs
   def pie_rosetype() -> Pie:
       num_people_py = [37, 240, 1, 22]
       degree = ['大专', '本科', '硕士', '不限']
       v = degree
       c = (
           Pie()
               .add(
               "",
               [list(z) for z in zip(v, num_people_py)],
               radius=["30%", "75%"],
               center=["25%", "50%"],
               rosetype="radius",
               label_opts=opts.LabelOpts(is_show=False),
           )
               .add(
               "",
               [list(z) for z in zip(v, num_people_py)],
               radius=["30%", "75%"],
               center=["75%", "50%"],
               rosetype="area",
           )
               .set_global_opts(title_opts=opts.TitleOpts(title="Python工程师对学历要求"))
       )
       return c



   @C.funcs
   def pie_rosetype() -> Pie:
       num_people_java = [44, 239, 2, 15]
       degree = ['大专', '本科', '硕士', '不限']
       v = degree
       c = (
           Pie()
               .add(
               "",
               [list(z) for z in zip(v, num_people_java)],
               radius=["30%", "75%"],
               center=["25%", "50%"],
               rosetype="radius",
               label_opts=opts.LabelOpts(is_show=False),
           )
               .add(
               "",
               [list(z) for z in zip(v, num_people_java)],
               radius=["30%", "75%"],
               center=["75%", "50%"],
               rosetype="area",
           )
               .set_global_opts(title_opts=opts.TitleOpts(title="Java工程师对学历要求"))
       )
       return c


   Page().add(*[fn() for fn, _ in C.charts]).render("d2.html")