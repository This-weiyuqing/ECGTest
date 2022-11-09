import json
import random
import requests
import dbconnect
# 城市列表
listcity = [["上海", "fce2e3a36450422b7fad3f2b90370efd71862f838d1255ea693b953b1d49c7c0"],
            ["北京", "d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0"],
            ["广州", "e749e3e04032ee6b165fbea6fe2dafab71862f838d1255ea693b953b1d49c7c0"],
            ["深圳", "e049aa251858f43d095fc4c61d62a9ec71862f838d1255ea693b953b1d49c7c0"],
            ["天津", "2e5d0080237ff3c8f5b5d3f315c7c,4a508e25c702ab1b810071e8e2c39502be1"],
            ["杭州", "91621282e559e9fc9c5b3e816cb1619c71862f838d1255ea693b953b1d49c7c0"],
            ["南京", "d6339a01dbd98141f8e684e1ad8af5c871862f838d1255ea693b953b1d49c7c0"],
            ["苏州", "536e0e568df850d1e6ba74b0cf72e19771862f838d1255ea693b953b1d49c7c0"],
            ["成都", "c950bc35ad04316c76e89bf2dc86bfe071862f838d1255ea693b953b1d49c7c0"],
            ["武汉", "d96a24c312ed7b96fcc0cedd6c08f68c08e25c702ab1b810071e8e2c39502be1"],
            ["重庆", "6229984ceb373efb8fd1beec7eb4dcfd71862f838d1255ea693b953b1d49c7c0"],
            ["西安", "ad66274c7f5f8d27ffd7f6b39ec447b608e25c702ab1b810071e8e2c39502be1"],
            ["青岛", "9874ff91c8b50ad831ea897b0cd5315b71862f838d1255ea693b953b1d49c7c0"],
            ["济南", "4be7d758168826991eb4b3e779fdf41571862f838d1255ea693b953b1d49c7c0"],
            ["威海", "fb5f85ca4c696d61c6e7a7e6c19b2f4530aacdebee4c4c9365dc18972daccaf7"],
            ["长春", "261f655c7a9713696580432624721cd871862f838d1255ea693b953b1d49c7c0"],
            ["大连", "21f56d987e57bd3e8df308351e3f4b9171862f838d1255ea693b953b1d49c7c0"],
            ["佛山", "4e5d3a805c4f1ed6059c7074e5e86adf30aacdebee4c4c9365dc18972daccaf7"],
            ["贵阳", "7ae3d5049e1c200ed6b2db0ac51604ba30aacdebee4c4c9365dc18972daccaf7"],
            ["合肥", "94af1388885f0b7483fdf72cba086a6030aacdebee4c4c9365dc18972daccaf7"],
            ["呼和浩特", "d64d5919fc236699402122b5770b4a6f71862f838d1255ea693b953b1d49c7c0"],
            ["昆明", "45159d85c35f742c1f2635d6ea6fa3ae30aacdebee4c4c9365dc18972daccaf7"],
            ["兰州", "b201713f2fb5f7235b6e2a6de8faf6a630aacdebee4c4c9365dc18972daccaf7"],
            ["南宁", "ff6f15347ab16f86ffb34e2700c4870930aacdebee4c4c9365dc18972daccaf7"],
            ["秦皇岛", "ca02d37fa01b0f9613555237517e19ff71862f838d1255ea693b953b1d49c7c0"],
            ["沈阳", "eec1fb195780b91fc9dd065409c1d28471862f838d1255ea693b953b1d49c7c0"],
            ["太原", "293e6160d971fe48ebbed1c8033bd9ed71862f838d1255ea693b953b1d49c7c0"],
            ["唐山", "2ae2237467ce4784b1705be502b0315271862f838d1255ea693b953b1d49c7c0"],
            ["无锡", "51ff28145b3f63e2f9ec4b2a34e8850c71862f838d1255ea693b953b1d49c7c0"],
            ["扬州", "02eeb7a9021c215641f3ec0e3cede50b71862f838d1255ea693b953b1d49c7c0"],
            ["珠海", "cf609e6234aca7061ab6a47e8d906e8c30aacdebee4c4c9365dc18972daccaf7"],
            ["安庆", "35e4c8f1738ecc8ad87b613926a9d6dd1eebfd971c239635bc3b5e190325c01c"],
            ["安阳", "d217beb464e7778289c854eafe2fdab21eebfd971c239635bc3b5e190325c01c"],
            ["保定", "2dfe97d8557f1cccc3484afc2dc54e9c71862f838d1255ea693b953b1d49c7c0"],
            ["蚌埠", "1b3e2c870e22cb1c98035d64f71b82361eebfd971c239635bc3b5e190325c01c"],
            ["北海", "d0490e0c48a4225ee85d2a0ec802ab131eebfd971c239635bc3b5e190325c01c"],
            ["滨州", "7ed4b634645044dc1c746c8a1afb14481eebfd971c239635bc3b5e190325c01c"],
            ["保山", "a589b29ec2067666fca30ea28844e70c1eebfd971c239635bc3b5e190325c01c"],
            ["宝鸡", "701cef49e3c2f39394ce006c0b9945b21eebfd971c239635bc3b5e190325c01c"],
            ["北安", "5ac6152df84456d942f1a69afe59c3fa1eebfd971c239635bc3b5e190325c01c"],
            ["承德", "ad798bb841d96db01ce329855213a02ad97945289578b7557a191d6c125161e7"],
            ["沧州", "76de7d4c29a0660101822920a658ecded97945289578b7557a191d6c125161e7"],
            ["大庆", "a18c61815481274c318a383a902247ef71862f838d1255ea693b953b1d49c7c0"],
            ["丹东", "ad2b737489102d91905e887d5eb4d838d97945289578b7557a191d6c125161e7"],
            ["东营", "cb6678ec79300273ed82ba7f7c09ccc11eebfd971c239635bc3b5e190325c01c"],
            ["德州", "475860687e32c17b501eb86d7e8966d21eebfd971c239635bc3b5e190325c01c"],
            ["鄂尔多斯", "8255b0e7540dbba8157071204385cd65d97945289578b7557a191d6c125161e7"],
            ["抚顺", "4c4a091ef17e08597fd6a7c6bc0aab23d97945289578b7557a191d6c125161e7"],
            ["聊城", "e34386f82b808950f4a1f859113352fd1eebfd971c239635bc3b5e190325c01c"],
            ["连云港", "c2687c56fb887be66d324c728ab95c2571862f838d1255ea693b953b1d49c7c0"]
            ]
#用户代理，是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等#
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"]
#设置随机选择用户代理#
head = {
'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 从列表中随机获取1个
}
flag = 0   #总条数
code = 0   #当前条数

# 定义爬虫函数（调用解析函数）#
def cinfoSpider(citylist):
    city = citylist[0]
    url = citylist[1]
    #爬虫地址#
    cbase_url = "http://dp01.ds.quancube.cn/mylist/ajax/shoprank?rankId="+url
    #get请求获取网页数据#
    html = requests.get(cbase_url, headers=head)
    #调用cfindFood函数解析#
    cfindinfo(city=city, data=str(html.text))

# 定义解析页面函数#
def cfindinfo(city,data):
    global flag,code
    #连接mysql数据库#
    mysql_db = dbconnect.DBHelper()
    mysql_db.connectDatabase();
    #解析返回的JSON数据#
    for data in json.loads(data)["shopBeans"]:
        flag +=1
        # 商铺名称
        shopName = data["shopName"]
        # 商品编号
        shopId = data["shopId"]
        # 商铺星级
        shopPower = data["shopPower"]
        # 所在商区
        mainRegionName = data["mainRegionName"]
        # 分类名称
        mainCategoryName = data["mainCategoryName"]
        # 口味评分
        tasteScore = data["score1"]
        # 环境评分
        environmentScore = data["score2"]
        # 服务评分
        serviceScore = data["score3"]
        # 人均消费
        avgPrice = data["avgPrice"]
        # 详细地址
        shopAddress = data["address"]
        # 商铺网址
        shopUrl = "http://dp01.ds.quancube.cn/shop/"+shopId
        # 商铺图片
        defaultPic = data["defaultPic"]

        phoneNO =data["phoneNo"]
        #tianjiadianhuahao
        #将解析数据插入数据库#
        #定义sql语句#
        sql = '''insert into dazhonginfo_copy(city, shopName, shopId, shopPower, mainRegionName, mainCategoryName, tasteScore, environmentScore, serviceScore, avgPrice, shopAddress, shopUrl, defaultPic,phoneNo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        #插入这些参数的数据#
        params = (city, shopName, shopId, shopPower, mainRegionName, mainCategoryName, tasteScore, environmentScore, serviceScore, avgPrice, shopAddress, shopUrl, defaultPic,phoneNO)
        try:
            mysql_db.insert(sql,*params)
            code +=1
            print("----- 插入:", code, "条------")
        except:
            print("已存在不再重复插入！！")
    print("总条数：", flag)

if __name__ == '__main__':
    #循环执行对每个城市网页的爬虫#
    for city_data in listcity:
        cinfoSpider(city_data)