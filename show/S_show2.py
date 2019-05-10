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
   def pie_radius() -> Pie:
       salary_base = ['6k以下', '7k-10k', '11k-15k', '16k-20k', '21k-30k', '30k以上']
       salary_num_py = [9, 29, 33, 71, 111, 47]
       c = (
           Pie()
               .add(
               "",
               [list(z) for z in zip(salary_base, salary_num_py)],
               radius=["40%", "75%"],
           )
               .set_global_opts(
               title_opts=opts.TitleOpts(title="Python工程师薪资"),
               legend_opts=opts.LegendOpts(
                   orient="vertical", pos_top="15%", pos_left="2%"
               ),
           )
               .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
       )
       return c


   @C.funcs
   def pie_radius() -> Pie:
       salary_base = ['6k以下', '7k-10k', '11k-15k', '16k-20k', '21k-30k', '30k以上']
       salary_num_java = [7, 52, 70, 46, 71, 54]
       c = (
           Pie()
               .add(
               "",
               [list(z) for z in zip(salary_base, salary_num_java)],
               radius=["40%", "75%"],
           )
               .set_global_opts(
               title_opts=opts.TitleOpts(title="Java工程师薪资"),
               legend_opts=opts.LegendOpts(
                   orient="vertical", pos_top="15%", pos_left="2%"
               ),
           )
               .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
       )
       return c


   Page().add(*[fn() for fn, _ in C.charts]).render("s2.html")