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
        num_people_py = [37, 240, 1, 22]
        # java
        num_people_java = [44,239,2,15]
        degree = ['大专', '本科', '硕士', '不限']

        c = (
            Bar()
                .add_xaxis(degree)
                .add_yaxis("java", num_people_java)
                .add_yaxis("python",num_people_py)
                .set_global_opts(title_opts=opts.TitleOpts(title="对学历要求", subtitle="数据由拉勾网提供"))
        )
        return c

    Page().add(*[fn() for fn, _ in C.charts]).render("d1.html")