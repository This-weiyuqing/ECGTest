import pymysql
# 数据库操作类，这个类用于连接数据库、插入数据、查询数据
class DBHelper():
    #定义构造函数，self实例变量属性
    def __init__(self):
        self.host = 'localhost'  # MySQL服务器地址
        self.port = 3306         # MySQL服务器端口号
        self.user = 'root'       #用户名
        self.passwd = 'shuidilab@123'   #密码
        self.db = 'testdazhong'  #数据库名称
    # 定义连接到数据库的方法
    def connectDatabase(self):
        #创建连接对象
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn
    # 插入数据
    def insert(self, sql, *params):  # 注意这里params要加*,因为传递过来的是元组，*表示参数个数不定
        conn = self.connectDatabase()
        #创建游标对象
        cur = conn.cursor()
        #执行sql语句
        cur.execute(sql, params)
        #注意要commit，提交
        conn.commit()
        cur.close()
        conn.close()
    # 查询数据
    def select(self, sql):
        conn = self.connectDatabase()
        cur = conn.cursor()
        try:
            # 执行SQL语句
            cur.execute(sql)
            conn.commit()
            # 获取所有记录列表
            results = cur.fetchall()
            return results
        except:
            print("Error: unable to fecth data")
        cur.close()
        conn.close()