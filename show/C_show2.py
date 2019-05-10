# coding=utf-8
from example.commons import Collector, Faker

from pyecharts import options as opts

from pyecharts.charts import Page, Pie

"""
Created on 19-5-09
@title: ''
@author: XuChao
"""
if __name__ == "__main__":

   C = Collector()

   @C.funcs
   def pie_base() -> Pie:
       city_nms_top10 = ['北京', '上海', '深圳', '成都', '广州', '杭州', '武汉', '南京', '苏州', '郑州']
       city_nums_top10 = [149, 95, 77, 22, 17, 17, 16, 13, 7, 5]
       c = (
           Pie()
           .add("", [list(z) for z in zip(city_nms_top10,city_nums_top10)])
           # .add("比例",city_nums_top10)
           .set_global_opts(title_opts=opts.TitleOpts(title="Python岗位分布情况"))
           .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
       )
       return c


   @C.funcs
   def pie_base() -> Pie:
       city_num_java = ["上海", "东莞", "中山", "乌鲁木齐", "佛山", "北京", "南京", "南昌", "厦门", "合肥", "大连", "天津", "宁波", "广州", "成都",
                        "拉萨","无锡", "日照", "杭州","武汉", "沈阳", "河源", "泉州", "泰安", "济南", "深圳", "烟台", "福州", "苏州", "西安", "贵阳", "郑州", "重庆", "长沙", "青岛"]
       people_num_java = [33, 1, 1, 1, 3, 92, 15, 1, 6, 2, 1, 4, 1, 22, 17, 1, 2, 1, 23, 9, 2, 1, 2, 1, 4, 36, 1, 5, 2,1,1, 2, 1, 4, 1]
       c = (
           Pie()
               .add("", [list(z) for z in zip(city_num_java, people_num_java)])
               # .add("比例",city_nums_top10)
               .set_global_opts(title_opts=opts.TitleOpts(title="Java岗位分布情况"))
               .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
       )
       return c
   Page().add(*[fn() for fn, _ in C.charts]).render("c2.html")