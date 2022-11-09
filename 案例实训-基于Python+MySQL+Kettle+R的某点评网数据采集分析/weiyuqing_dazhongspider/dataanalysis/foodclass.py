from pyecharts import Pie, Page,Bar
from spider import dbconnect

#查询统计某城市菜品分类名
def foodClass(city):
    #连接数据库
    mysql_db = dbconnect.DBHelper()
    mysql_db.connectDatabase();
    fsql = '''SELECT COUNT(mainCategoryName),mainCategoryName from dazhongoutput  where city="%s" GROUP BY mainCategoryName;'''%(city)
    #查询获得菜品分类商店梳理、菜品分类名称数据返回
    listData = mysql_db.select(fsql)
    return listData

#菜品分类画图函数
def plotfoodclass():
    #查询统计济南的菜品分类以及数量
    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClass("济南")]
    [list_address.append(i[1]) for i in foodClass("济南")]
    print(list_address)
    print(list_sum)
    #定义页面
    page = Page()
    #添加饼图的数据和配置项
    fpie1 = Pie("济南菜品分类", title_pos='center')
    fpie1.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    #添加柱状图的数据和配置型项
    fbar1 = Bar("济南菜品分类", "数据来源于大众点评TOP100",title_pos ='center')
    fbar1.add("济南", list_address, list_sum, mark_point=["max", "min"],legend_pos="right")

    # 查询统计青岛的菜品分类以及数量
    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClass("青岛")]
    [list_address.append(i[1]) for i in foodClass("青岛")]
    print(list_address)
    print(list_sum)
    # 添加饼图的数据和配置项
    fpie2 = Pie("青岛菜品分类", title_pos='center')
    fpie2.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    # 添加柱状图的数据和配置型项
    fbar2 = Bar("青岛菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    fbar2.add("青岛", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    # 查询统计威海的菜品分类以及数量
    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClass("威海")]
    [list_address.append(i[1]) for i in foodClass("威海")]
    print(list_address)
    print(list_sum)
    # 添加饼图的数据和配置项
    fpie3 = Pie("威海菜品分类", title_pos='center')
    fpie3.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    # 添加柱状图的数据和配置型项
    fbar3 = Bar("威海菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    fbar3.add("威海", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

   #页面上添加图形
    page.add(fpie1)
    page.add(fbar1)
    page.add(fpie2)
    page.add(fbar2)
    page.add(fpie3)
    page.add(fbar3)

    page.render("山东3大城市菜品分类.html")
if __name__ == '__main__':
    plotfoodclass()