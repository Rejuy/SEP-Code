// pages/course/course.js
Page({
    data: {
        department_type: [
            { text: '任意院系', value: 0 },
            { text: '体育部', value: 1 },
            { text: '语言中心', value: 2 },
            { text: '软件学院', value: 3 },
        ],
        course_type: [
            { text: '全部课程', value: 0 },
            { text: '体育课', value: 1 },
            { text: '外文课', value: 2 },
            { text: '文化素质课', value: 3 },
            { text: '文化素质核心课', value: 4 },
        ],
        rank_type: [
            { text: '评分排序', value: 0 },
            { text: '热度排序', value: 1 },
            { text: '时间排序', value: 2 },
        ],
        department_value: 0,
        course_value: 0,
        rank_value: 0,

        image_url: "https://learn.tsinghua.edu.cn/b/wlxt/kc/v_kcxx_jskcxx/teacher/showImageById?wlkcid=2021-2022-1142764790&_csrf=d39592c7-bbb0-416a-affb-a39b1ab00ba4",

        current_page: 0,
        total_pages: 0,
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
        TIME_ASCENDING_ORDER: -300
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