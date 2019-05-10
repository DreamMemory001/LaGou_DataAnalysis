# coding=utf-8
from example.commons import Collector
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType


"""
Created on 19-5-09
@title: ''
@author: XuChao
"""

# 词云
if __name__ == "__main__":

    C = Collector()

    words = [("上海",555), ("东莞",65512), ("中山",444), ("乌鲁木齐",5655), ("佛山",4454), ("北京",989) ,("南京",9748), ("南昌",545) ,("厦门",4544), ("合肥",45645) ,("大连",5656565) ,("天津", 545),("宁波",4545) ,("广州",565959) ,("成都",5448) ,("拉萨",45454),
             ("无锡",474), ("日照",4554), ("杭州",9999),
             ("武汉",44787) ,("沈阳",54878),("河源",5458),("泉州",5599), ("泰安",548), ("济南",4878), ("深圳",548474), ("烟台",54545),("福州",5748),("苏州",4548), ("西安", 5454545),("贵阳",3333), ("郑州",659), ("重庆",65655), ("长沙",89777), ("青岛",55455)]
    @C.funcs
    def wordcloud_base() -> WordCloud:
        c = (
            WordCloud()
            .add("", words, word_size_range=[20, 100])
            .set_global_opts(title_opts=opts.TitleOpts(title="城市词云图"))
        )
        return c

    Page().add(*[fn() for fn, _ in C.charts]).render("w1.html")