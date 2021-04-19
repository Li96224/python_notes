'''

1.华为外包 mm基线
   （1）用什么方法设计用例

   答：边界值、等价类、场景法

   （2）接口工具都用什么，post,get区别，关联怎么用

    postman/python+requests
    GET产生一个TCP数据包；POST产生两个TCP数据包。
    长的说：
    对于GET方式的请求，浏览器会把http header和data一并发送出去，服务器响应200（返回数据）；
    而对于POST，浏览器先发送header，服务器响应100 continue，浏览器再发送data，服务器响应200 ok（返回数据）

    get传输有数据大小有限制 post没有限制

    postman只支持写js代码 可以在Test里面写js代码，将token设置为全局变量，其他需要调用的接口在传参时直接输入变量即可
    //把json字符串转化为对象
    var data=JSON.parse(responseBody);

    //获取data对象的utoken值。
    var token=data.utoken;

    //设置成全局变量
    pm.globals.set("token", token);

    python+requests的话也是直接通过设置token作为相关的变量即可
    如果是需要使用本地同一个cookie 可以使用Session会话
    #session会话.requests中每次请求都是独立的.那么就会产生cookie不能共享的问题


   （3）py 切片取字符串2-4，怎么取，py+ui 加一条数据怎么判断数据增加成功，列表怎么倒排

    变量名[1:5]    #上标为1表示从第二位的值开始取 下标为5表示只取到第4位的值 因为下标默认不取的 步长不填默认为1

    可以使用unittest里面自带的断言方法来判断新增的值得元素是否出现在相应的页面上
    或者可以使用python来连接数据库 通过sql语句查询返回的结果来断言是否新增成功

    列表倒叙 可以使用切边 上标下标直接默认为空 步长为-1从末尾开始取
    或者使用列表自带的排序函数 listvar.sort(reverse=True) 默认为reverse=False(为正序)
    或者使用列表自带的反转函数 listvar.reverse()

   （4）查找数据前五行

    select * from student limit 5   关键字limit限制

   （5）linux常用命令

    cd切换路径 切换到日志文件的路径
    tail从末尾的方式打开文件
    tail -f 10 日志文件名称 实时读日志读十行


2.字节跳动 外包 影像相关
    （1）逻辑题：给你一个天平，2g、7g砝码，怎么3次把140g盐分为50g 90g
    （2）采样率具体是指什么
    （3）音视频质量算法
    （4）http与https有什么区别
    （5）tcp三次握手
    （6）纯音频质量测试方法
    （7）抖音点击+拍一段视频并发布成功，设计用例

'''