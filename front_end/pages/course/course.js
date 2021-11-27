// pages/course/course.js
Page({

    /**
     * 页面的初始数据
     */
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
        courses_list: []
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