from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page
"""
Created on 19-5-09
@title: ''
@author: XuChao
"""

# 直方图
if __name__ == "__main__":

    C = Collector()

    @C.funcs
    def bar_base() -> Bar:
        salary_base = ['6k以下', '7k-10k', '11k-15k', '16k-20k', '21k-30k', '30k以上']
        salary_num_java = [7, 52, 70, 46, 71, 54]
        salary_num_py = [9,29,33,71,111,47]
        c = (
            Bar()
                .add_xaxis(salary_base)
                .add_yaxis("Python工程师薪资",salary_num_py )
                .add_yaxis("Java工程师薪资",salary_num_java)
                .set_global_opts(title_opts=opts.TitleOpts(title="薪资直方图", subtitle="数据由拉勾网提供"))
        )
        return c


    Page().add(*[fn() for fn, _ in C.charts]).render("s1.html")