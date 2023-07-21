from flask import Flask, request, render_template
import pymysql
from flask import session
app = Flask(__name__)
app.secret_key = 'my-secret-key'
# 连接数据库
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='1111',   # 数据库连接密码
    db='software1',    # 数据库名
    charset='utf8mb4'  # 数据库字符编码
)
def delet_zhaoping(name):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql = "DELETE FROM `jobpostings` WHERE `name`=%s"
            cursor.execute(sql,(name))
            # 获取结果
            results = cursor.fetchall()
            return results
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "查询失败：" + str(e)
def chakan_zhaoping():
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql = "SELECT * FROM jobpostings"
            cursor.execute(sql)
        # 提交事务
            results = cursor.fetchall()
            return results
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "发布失败：" + str(e)
def get_zhaoping(address):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句
            sql = "SELECT * FROM jobpostings WHERE address =%s"
            cursor.execute(sql,(address))
            # 获取结果
            results = cursor.fetchall()
            return results
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "查询失败：" + str(e)
def add_zhaogong(name,address,age,phone,salary,illustrate):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql = "INSERT INTO `jobpostings` (`name`, `address`, `age`,`phonenumber`,`salary`,`illustrate`) VALUES (%s, %s, %s,%s,%s,%s)"
            cursor.execute(sql, (name,address,age,phone,salary,illustrate))
        # 提交事务
        conn.commit()
        return "招聘信息发布成功"
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "发布失败：" + str(e)
#用户信息修改
def updata_user(password,name,age,phonenumber,addres):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql="UPDATE `user1` SET `password`=%s, `name`=%s ,`age`=%s,`phonenumber`=%s,`addres`=%s WHERE `id`=%s"
            cursor.execute(sql, (password,name,age,phonenumber,addres,session['user_id']))
        # 提交事务
        conn.commit()
        return "用户修改成功"
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "修改失败：" + str(e)
#添加用户
def add_user(id,password,name,age,phonenumber,addres):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql = "INSERT INTO `user1` (`id`, `password`, `name`,`age`,`phonenumber`,`addres`,`manager`) VALUES (%s, %s, %s,%s,%s,%s,%s)"
            cursor.execute(sql, (id,password,name,age,phonenumber,addres,0))
            sql="CREATE TABLE "+name+"(name VARCHAR(255),price VARCHAR(255),number int);"
            cursor.execute(sql)
           # 提交事务
        conn.commit()
        # sql="CREATE TABLE %s (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255),price DECIMAL(10, 2));"
        return "用户注册成功"
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "注册失败：" + str(e)
def login(id,password):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句
            sql = "SELECT * FROM user1 WHERE id =%s"
            cursor.execute(sql,(id))
            # 获取结果
            result = cursor.fetchone()
           
            if result is None:
                return "账号不存在或密码错误"
            elif result[1]!=password:
                return "账号不存在或密码错误"
            else:
                # 登录成功，将用户信息存储在session中
                session['user_id'] = result[0]
                session['username'] = result[2]
                session['age'] = result[3]
                session['phone'] = result[4]
                session['address'] = result[5]
                session['manager']=result[6]
                return "登录成功"
    except Exception as e:
        return "登录失败：" + str(e)
# 新增一条记录
def cart(name):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql = "SELECT * FROM"+" "+name;
            cursor.execute(sql)
        # 提交事务
            results = cursor.fetchall()
            
            return results
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "查询购物车数据失败：" + str(e)
def add_product(name, link, price):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql = "INSERT INTO `product` (`name`, `link`, `price`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, link, price))
        # 提交事务
        conn.commit()
        return "新增成功"
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "新增失败：" + str(e)

# 模糊查询记录
def get_likeproducts(name):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句
            
            sql = "SELECT * FROM `product` WHERE `name` LIKE  '%" + name + "%' "
            cursor.execute(sql)
            # 获取结果
            results = cursor.fetchall()
            return results
    except Exception as e:
        return "查询失败：" + str(e)
def get_products(name):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句
            sql = "SELECT * FROM `product` WHERE `name`=%s"
            cursor.execute(sql,(name,))
            # 获取结果
            results = cursor.fetchall()
            return results
    except Exception as e:
        return "查询失败：" + str(e)

# 修改一条记录
def update_product(name, link, price):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql = "UPDATE `product` SET `link`=%s, `price`=%s WHERE `name`=%s"
            cursor.execute(sql, (name, link, price))
        # 提交事务
        conn.commit()
        return "修改成功"
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "修改失败：" + str(e)

# 删除一条记录
def delete_product(name):
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，将参数以元组形式传入
            sql = "DELETE FROM `product` WHERE `name`=%s"
            cursor.execute(sql, (name,))
        # 提交事务
        conn.commit()
        return "删除成功"
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        return "删除失败：" + str(e)

# 处理网页表单请求
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        action = request.form['action'] # 获取表单提交的操作类型
        if action == 'add': # 如果是新增操作
            name = request.form['name'] # 获取表单提交的名称字段
            link = request.form['link'] # 获取表单提交的链接字段
            price = request.form['price'] # 获取表单提交的价格字段
            result = add_product(name, link, price) # 调用新增函数
            return result # 返回结果
        elif action == 'query': # 如果是查询操作
            name = request.form['name'] # 获取表单提交的名称字段
            results = get_products(name) # 调用查询函数
            return render_template('index.html', results=results) # 返回查询结果
        elif action == 'update': # 如果是修改操作
            name = request.form['name'] # 获取表单提交的名称字段
            link = request.form['link'] # 获取表单提交的链接字段
            price = request.form['price'] # 获取表单提交的价格字段
            result = update_product( name, link, price) # 调用修改函数
            return result # 返回结果
        elif action == 'delete': # 如果是删除操作
            name = request.form['name'] # 获取表单提交的记录ID
            result = delete_product(name) # 调用删除函数
            return result # 返回结果
        elif action=='querry1':
            name = request.form['name'] # 获取表单提交的名称字段
            results = get_likeproducts(name) # 调用查询函数
            return render_template('模糊查询.html', results=results) # 返回查询结果 
        elif action=='add_user' :
            username = request.form.get('username')
            password = request.form.get('password')
            nickname = request.form.get('nickname')
            age = request.form.get('age')
            phone = request.form.get('phone')
            address = request.form.get('address')
            result=add_user(username,password,nickname,age,phone,address)
            return result
        elif action=='login':
            username = request.form.get('username')
            password = request.form.get('address')
            result=login(username,password)
            return result
        elif action=='updata_user':
            password = request.form.get('password')
            nickname = request.form.get('nickname')
            age = request.form.get('age')
            phone = request.form.get('phone')
            address = request.form.get('address')
            result=updata_user(password,nickname,age,phone,address)
            return result
        elif action=='cart':
            result=cart(session['username'])
            return render_template('cart.html', results=result)
        elif action=='add_zhaoping':
            name=request.form.get('username')
            address=request.form.get('address')
            age=request.form.get('age')
            phone=request.form.get('phone')
            salary=request.form.get('salary')
            shuoming=request.form.get('shuoming')
            result=add_zhaogong(name,address,age,phone,salary,shuoming)
            return result
        elif action=='get_zhaoping':
            address=request.form.get('address')
            result=get_zhaoping(address)
            return render_template('查询信息查看.html', results=result)
        elif action=='delet_fabu':
            name=request.form.get('username')
            result=delet_zhaoping(name)
            return render_template('删除招聘.html')
    else:
        if 'user_id' not in session:
            return render_template('首页.html')
        else:
            return render_template('首页.html')
         # 如果是GET请求，返回网页表单
@app.route('/denglv', methods=['GET', 'POST'])
def denglv():
    return render_template('登录.html')
@app.route('/zhuye', methods=['GET', 'POST'])
def zhuye():
    return render_template('主页.html')
@app.route('/zhuce', methods=['GET', 'POST'])
def zhuce():
       return render_template('注册.html')
@app.route('/userupdata', methods=['GET', 'POST'])

def userupdata():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('用户修改.html') # 如果是GET请求，返回网页表单
@app.route('/tianjia', methods=['GET', 'POST'])

def tianjia():
    if 'user_id' not in session:
        return render_template('登录.html') 
    if session['manager']=='0':
        return "您不是管理员无法访问此页面"
    if session['manager']=='1':
         return render_template('添加商品.html') # 如果是GET请求，返回网页表单

@app.route('/yonghu', methods=['GET', 'POST'])

def yonghu():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        user_id = session.get('user_id')
        username = session.get('username')
        age = session.get('age')
        phone = session.get('phone')
        address = session.get('address')
        is_manager = session.get('manager')

    # 构建渲染页面所需的数据
        context = {
        'user_id': user_id,
        'username': username,
        'age': age,
        'phone': phone,
        'address': address,
        'is_manager': is_manager
            }
        if is_manager=='0':
            return render_template('用户界面.html', **context) # 如果是GET请求，返回网页表单
        else:
            return render_template('用户界面.html', **context)
@app.route('/er', methods=['GET', 'POST'])

def er():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('2.html')
@app.route('/san', methods=['GET', 'POST'])

def san():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('3.html')
@app.route('/si', methods=['GET', 'POST'])

def si():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('4.html')
@app.route('/wu', methods=['GET', 'POST'])

def wu():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('5.html')
@app.route('/secon', methods=['GET', 'POST'])

def secon():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('98.html')
@app.route('/last', methods=['GET', 'POST'])
def last():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('99.html')
@app.route('/chaxun', methods=['GET', 'POST'])

def chaxun():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('模糊查询.html')
@app.route('/cartl', methods=['GET', 'POST'])

def cartl():
    if 'user_id' not in session:
        return render_template('登录.html') 
    else:
        return render_template('cart.html')
@app.route('/about', methods=['GET', 'POST'])

def about():
        return render_template('about.html')       
@app.route('/guan', methods=['GET', 'POST'])

def guan():
    if 'user_id' not in session:
        return render_template('登录.html') 
    if session['manager']=='0':
        return "您不是管理员无法访问此页面"
    if session['manager']=='1':
         return render_template('index.html')   
@app.route('/fabu', methods=['GET', 'POST'])
def fabu():
        if 'user_id' not in session:
            return render_template('登录.html') 
        else:
            return render_template('招聘发布.html')
@app.route('/zhaopingchakan', methods=['GET', 'POST'])
def zhaopingchakan():
        if 'user_id' not in session:
            return render_template('登录.html') 
        else:
            print(session['user_id'])
            result=chakan_zhaoping()
            return render_template('招聘信息查看.html',results=result)
@app.route('/zhaopingchaxun', methods=['GET', 'POST'])
def zhaopingchaxun():
        return render_template('查询招聘信息.html')
@app.route('/zhaopingchaxunhou', methods=['GET', 'POST'])
def zhaopingchaxunhou():
        if 'user_id' not in session:
            return render_template('登录.html') 
        else:
            return render_template('招聘信息.html')
@app.route('/zhaopingshanchu', methods=['GET', 'POST'])
def zhaopingshanchu():
        if 'user_id' not in session:
            return render_template('登录.html') 
        if session['manager']=='0':
            return "您不是管理员无法访问此页面"
        else:
            return render_template('删除招聘.html')
if __name__ == '__main__':
    app.run(debug=True) # 启动程序，开启调试模式