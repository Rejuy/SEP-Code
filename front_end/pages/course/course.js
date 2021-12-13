import Toast from '@vant/weapp/toast/toast';


Page({
    data: {
        department_type: [
            { text: '任意院系', value: 0 },
            { text: '车辆学院', value: 1 },
            { text: '材料学院', value: 2 },
            { text: '电机系', value: 3 },
            { text: '电子系', value: 4 },
            { text: '法学院', value: 5 },
            { text: '工物系', value: 6 },
            { text: '公管学院', value: 7 },
            { text: '工业工程系', value: 8 },
            { text: '航院', value: 9 },
            { text: '化学系', value: 10 },
            { text: '化工系', value: 11 },
            { text: '环境学院', value: 12 },
            { text: '机械系', value: 13 },
            { text: '经管学院', value: 14 },
            { text: '金融学院', value: 15 },
            { text: '建筑学院', value: 16 },
            { text: '计算机系', value: 17 },
            { text: '交叉信息院', value: 18 },
            { text: '集成电路学院', value: 19 },
            { text: '美术学院', value: 20 },
            { text: '马克思主义学院', value: 21 },
            { text: '能动系', value: 22 },
            { text: '求真书院', value: 23 },
            { text: '清华-伯克利深圳学院', value: 24 },
            { text: '日新书院', value: 25 },
            { text: '软件学院', value: 26 },
            { text: '人文学院', value: 27 },
            { text: '数学系', value: 28 },
            { text: '水利系', value: 29 },
            { text: '社科学院', value: 30 },
            { text: '生命学院', value: 31 },
            { text: '苏世民书院', value: 32 },
            { text: '土木系', value: 33 },
            { text: '体育部', value: 34 },
            { text: '土水学院', value: 35 },
            { text: '外文系', value: 36 },
            { text: '物理系', value: 37 },
            { text: '未央书院', value: 38 },
            { text: '新雅书院', value: 39 },
            { text: '行健书院', value: 40 },
            { text: '新闻学院', value: 41 },
            { text: '训练中心', value: 42 },
            { text: '医学院', value: 43 },
            { text: '药学院', value: 44 },
            { text: '语言中心', value: 45 },
            { text: '艺教中心', value: 46 },
            { text: '致理书院', value: 47 },
            { text: '自动化系', value: 48 },
            { text: '其他开课单位', value: 49 },
        ],
        course_type: [
            { text: '全部课程', value: 0 },
            { text: '专业课', value: 1 },
            { text: '数理课', value: 2 },
            { text: '外文课', value: 3 },
            { text: '实验课', value: 4 },
            { text: '体育课', value: 5 },
            { text: '思政课', value: 6 },
            { text: '文核课', value: 7 },
            { text: '文素课', value: 8 },
        ],
        rank_type: [
            { text: '评分排序', value: 0 },
            { text: '热度排序', value: 1 },
            { text: '时间排序', value: 2 },
        ],
        
        schedule_for_create: ['春季学期', '夏季学期', '秋季学期', '春、秋季学期'],
        type_for_create: ['专业课', '数理课', '外文课', '实验课', '体育课', '思政课', '文核课', '文素课'],
        department_for_create: ['车辆学院','材料学院','电机系','电子系','法学院','工物系','公管学院','工业工程系','航院','化学系','化工系','环境学院','机械系','经管学院','金融学院','建筑学院','计算机系','交叉信息院','集成电路学院','美术学院','马克思主义学院','能动系','求真书院','清华-伯克利深圳学院','日新书院','软件学院','人文学院','数学系','水利系','社科学院','生命学院','苏世民书院','土木系','体育部','土水学院','外文系','物理系','未央书院','新雅书院','行健书院','新闻学院','训练中心','医学院','药学院','语言中心','艺教中心','致理书院','自动化系','其他开课单位'],

        search_value: '',
        department_value: 0,
        course_value: 0,
        rank_value: 0,

        edit_course_credit: 0,
        edit_course_schedule: '',
        edit_course_type: '',
        edit_course_department: '',

        image_url: "https://learn.tsinghua.edu.cn/b/wlxt/kc/v_kcxx_jskcxx/teacher/showImageById?wlkcid=2021-2022-1142764790&_csrf=d39592c7-bbb0-416a-affb-a39b1ab00ba4",

        current_page: 0,
        total_pages: 0,
        show_popup: false,

        courses_list: [
            { id: 1, name: '软件工程', teacher: '刘强', department: '软件学院', type: '专业课', star: 5.0, score: 10.0, tag: 'TOP1', color: '#228B22'},
            { id: 2, name: '概率论与数理统计', teacher: '梁恒', department: '数学系', type: '数理课', star: 4.0, score: 8.1, tag: '', color: '#000000'},
            { id: 3, name: '美国社会与文化', teacher: 'TULP RUSSELL ALAN', department: '语言中心', type: '外文课', star: 4.5, score: 9.5, tag: 'TOP15', color: '#FFA500' },  
            { id: 4, name: '物理实验B(2)', teacher: '梁昌林', department: '物理系', type: '实验课', star: 0.0, score: 0.4, tag: '', color: '#8B4513' },  
            { id: 5, name: '二年级男生散手', teacher: '马勇志', department: '体育部', type: '体育课', star: 3.5, score: 7.3, tag: '', color: '#9400D3' },    
            { id: 7, name: '不朽的艺术：走进大师与经典', teacher: '孙晶', department: ' 人文学院', type: '文核课', star: 5.0, score: 9.7, tag: 'TOP8', color: '	#0000FF' },   
            { id: 8, name: '亲密关系：爱情、婚姻与心理学', teacher: '廖江群', department: '社科学院', type: '文素课', star: 4.0, score: 8.2, tag: '', color: '#FF1493' },   
        ]
    },

    marco: {
        PAGE_CAPACITY: 8,
        SCORE_DESCENDING_ORDER: 100,
        POPULARITY_DESCENDING_ORDER: 200,
        TIME_DESCENDING_ORDER: 300,
        SCORE_ASCENDING_ORDER: -100,
        POPULARITY_ASCENDING_ORDER: -200,
        TIME_ASCENDING_ORDER: -300,
    },

    onSearch: function(result) {
        this.setData({
            search_value: result.detail
        });
    },

    closePopup: function() {
        this.setData({
            show_popup: false
        });
    },

    publishRecommendation: function() {
        this.setData({
            show_popup: true
        })
    },

    editCourseSchedule: function(event) {
        const { value } = event.detail;
        this.setData({
            edit_course_schedule: value
        });
        Toast.success('设置成功');
        console.log(this.data.edit_course_schedule);        
    },

    editCourseType: function(event) {
        const { value } = event.detail;
        this.setData({
            edit_course_type: value
        });
        Toast.success('设置成功');
        console.log(this.data.edit_course_type);
    },

    editCourseDepartment: function(event) {
        const { value } = event.detail;
        this.setData({
            edit_course_department: value
        });
        Toast.success('设置成功');
        console.log(this.data.edit_course_department);
    },

    cancelPicker: function() {
        Toast.fail('请重新选择');
    },

    courseTypeSelected: function(result) {
        this.setData({
            course_value: result.detail
        });        
        console.log("course_value ", this.data.course_value);
    },

    departmentTypeSelected: function(result) {
        this.setData({
            department_value: result.detail
        });     
        console.log("department_value ", this.data.department_value);
    },

    rankTypeSelected: function(result) {
        this.setData({
            rank_value: result.detail
        });
        console.log("rank_value ", this.data.rank_value);  
    },

    viewCourseItem: function() {
        wx.navigateTo({
          url: '../course_item/course_item',
        })
    },

    getCourseList: function() {
        let begin = this.data.current_page * PAGE_CAPACITY;
        let end = begin + PAGE_CAPACITY;

        wx.request({
          url: 'url',
          method: 'GET',  
          data: {
              begin: begin,
              end: end,
              course_type: this.data.course_value,
              course_department: this.data.department_value,
              course_order: this.marco.SCORE_DESCENDING_ORDER
          },
          dataType: JSON,
          enableCache: true,
          enableHttp2: true,
          enableQuic: true,
          header: {
            "content-type": "application/json"
          },
          timeout: 0,
          success: (result) => {
              console.log(result);
              // 在此处完成开课院系和int的转换, type = hash_table[i]
          }, fail: (error) => {
              console.log(error);
          }, complete: (res) => {},
        })
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {
        if(this.data.current_page >= this.data.total_pages) {
            console.log("已无下一页数据");
        }else {
            this.data.current_page ++;
            // 更新 coursers_list
        }
    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})