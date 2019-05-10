# coding=utf-8

import random



from example.commons import Collector, Faker

from pyecharts import options as opts

from pyecharts.charts import Bar3D, Page
"""
Created on 19-5-09
@title: ''
@author: XuChao
"""
# Bar3D 就是测试了一下
if __name__ == "__main__":

  C = Collector()
  city_nms_top10 = ['北京', '上海', '深圳', '成都', '广州', '杭州', '武汉', '南京', '苏州', '郑州']
  city_nums_top10 = [149, 95, 77, 22, 17, 17, 16, 13, 7, 5]

  @C.funcs
  def bar3d_base() -> Bar3D:
      data = [(i, j, random.randint(0, 1)) for i in range(6) for j in range(24)]
      c = (
          Bar3D()
          .add(
              "",
              [[d[1], d[0], d[2]] for d in data],
              xaxis3d_opts=opts.Axis3DOpts(city_nms_top10, type_="category"),
              yaxis3d_opts=opts.Axis3DOpts(city_nums_top10, type_="category"),
              zaxis3d_opts=opts.Axis3DOpts(type_="value"),
          )
          .set_global_opts(
              visualmap_opts=opts.VisualMapOpts(max_=20),
              title_opts=opts.TitleOpts(title="Bar3D-Python工程师"),
          )
      )
      return c

  Page().add(*[fn() for fn, _ in C.charts]).render("c3.html")