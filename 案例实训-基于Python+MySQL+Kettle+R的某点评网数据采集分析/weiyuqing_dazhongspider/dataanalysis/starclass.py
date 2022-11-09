from pyecharts import Bar
from spider import dbconnect
# 统计一个城市各星级饭店数量函数
def starshopCount(City):
    #连接数据库
    mysql_db = dbconnect.DBHelper()
    mysql_db.connectDatabase();
   #查询有哪些星级,返回唯一不同的星级
    starsql = "SELECT DISTINCT(shopPower) from dazhongoutput ;"
    data = mysql_db.select(starsql)  #返回所有查询记录行，每一行是一个元组，所有行的元组再组装成一个元组data
    list_code = []
    for i in data:
        #选择该城市某个星级按照商铺ID统计商铺数量
        countsql = '''SELECT COUNT(shopId) from dazhongoutput where shopPower=%s and city="%s";''' % (i[0], City)
        countstar_city = mysql_db.select(countsql)
        #将所有星级和饭店数量放于list_code列表
        for m in countstar_city:
            list_code.append([i[0], m[0]])
    print(list_code)
    #返回商铺星级、数量
    return list_code

# 所有城市各星级饭店统计函数
def mianStar():
    #调用starshopCount(City)统计出下述城市各星级饭店数量
    shop1 = starshopCount("广州")
    shop2 = starshopCount("杭州")
    shop3 = starshopCount("南京")
    shop4 = starshopCount("成都")
    shop5 = starshopCount("武汉")
    shop6 = starshopCount("济南")
    shop7 = starshopCount("南宁")
    shop8 = starshopCount("合肥")
    shop9 = starshopCount("昆明")
    shop10 = starshopCount("西安")
    shop11 = starshopCount("北京")
    shop12 = starshopCount("上海")
    shop13 = starshopCount("深圳")
    shop14 = starshopCount("天津")
    shop15 = starshopCount("重庆")
    shop16 = starshopCount("青岛")
    shop17 = starshopCount("威海")
    shop18 = starshopCount("长春")
    shop19 = starshopCount("大连")
    shop20 = starshopCount("贵阳")

    #定义X轴和Y轴显示数据列表，开始为NULL
    list_x = []
    list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10,list_y11, list_y12, list_y13, list_y14, list_y15, list_y16, list_y17, list_y18, list_y19, list_y20 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    #数据列表赋值,zip将所有城市星级饭店列表，打包为一个包含多个元组的zip迭代对象，多变量循环
    for data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20 in zip(
            shop1, shop2, shop3, shop4, shop5, shop6, shop7, shop8, shop9, shop10,
            shop11, shop12, shop13, shop14, shop15, shop16, shop17, shop18, shop19, shop20
            ):
        #提取星级，建立X轴列表
        if data1[0] == '30':
            list_x.append("三星级")
        elif data1[0] == '35':
            list_x.append("三星半")
        elif data1[0] == '40':
            list_x.append("四星级")
        elif data1[0] == '45':
            list_x.append("四星半")
        else:
            list_x.append("五星级")
        #20城市不同星级饭店数量
        list_y1.append(data1[1])
        list_y2.append(data2[1])
        list_y3.append(data3[1])
        list_y4.append(data4[1])
        list_y5.append(data5[1])
        list_y6.append(data6[1])
        list_y7.append(data7[1])
        list_y8.append(data8[1])
        list_y9.append(data9[1])
        list_y10.append(data10[1])
        list_y11.append(data11[1])
        list_y12.append(data12[1])
        list_y13.append(data13[1])
        list_y14.append(data14[1])
        list_y15.append(data15[1])
        list_y16.append(data16[1])
        list_y17.append(data17[1])
        list_y18.append(data18[1])
        list_y19.append(data19[1])
        list_y20.append(data20[1])
    print(list_x, list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10,
              list_y11, list_y12, list_y13, list_y14, list_y15, list_y16, list_y17, list_y18, list_y19, list_y20
              )
         # 饭店星级排行画图
    plotstar(list_x, list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10,
             list_y11, list_y12, list_y13, list_y14, list_y15, list_y16, list_y17, list_y18, list_y19, list_y20
             )

# 饭店星级排行画图函数
def plotstar(list_x, list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10,
             list_y11, list_y12, list_y13, list_y14, list_y15, list_y16, list_y17, list_y18, list_y19, list_y20):
    attr = list_x
    #设置柱状图大小标题,可根据实际数据情况统计
    starbar = Bar("20个大中城市饭店星级统计", "数据来源于大众点评TOP100",width=1300,height=500)
    ##添加柱状图数据和配置项，标记最大值和最小值，最右侧设置工具栏，可对图进行更多操作，图例位置
    starbar.add("广州", attr, list_y1, mark_point=["max", "min"])
    starbar.add("杭州", attr, list_y2, mark_point=["max", "min"])
    starbar.add("南京", attr, list_y3, mark_point=["max", "min"])
    starbar.add("成都", attr, list_y4, mark_point=["max", "min"])
    starbar.add("武汉", attr, list_y5, mark_point=["max", "min"])
    starbar.add("济南", attr, list_y6, mark_point=["max", "min"])
    starbar.add("南宁", attr, list_y7, mark_point=["max", "min"])
    starbar.add("合肥", attr, list_y8, mark_point=["max", "min"])
    starbar.add("昆明", attr, list_y9, mark_point=["max", "min"])
    starbar.add("西安", attr, list_y10, mark_point=["max", "min"])
    starbar.add("北京", attr, list_y11, mark_point=["max", "min"])
    starbar.add("上海", attr, list_y12, mark_point=["max", "min"])
    starbar.add("深圳", attr, list_y13, mark_point=["max", "min"])
    starbar.add("天津", attr, list_y14, mark_point=["max", "min"])
    starbar.add("重庆", attr, list_y15, mark_point=["max", "min"])
    starbar.add("青岛", attr, list_y16, mark_point=["max", "min"])
    starbar.add("威海", attr, list_y17, mark_point=["max", "min"])
    starbar.add("长春", attr, list_y18, mark_point=["max", "min"])
    starbar.add("大连", attr, list_y19, mark_point=["max", "min"])
    starbar.add("贵阳", attr, list_y20, mark_point=["max", "min"], is_more_utils=True, legend_top='bottom')
#生成html文件数据可视化展示
    starbar.render("20个大中城市饭店星级排名.html")

if __name__ == '__main__':
    mianStar()