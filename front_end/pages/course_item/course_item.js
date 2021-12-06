// pages/course_item/course_item.js
Page({
    data: {
        loading: true,
        course_name: '实验室科研探究',
        course_credit: 1,
        course_teacher: '汤彬',
        course_schedule: '春、秋季学期',
        course_department: '训练中心',
        course_type: '文化素质核心课程',
        image_url: "https://learn.tsinghua.edu.cn/b/wlxt/kc/v_kcxx_jskcxx/teacher/showImageById?wlkcid=2021-2022-1142764790&_csrf=d39592c7-bbb0-416a-affb-a39b1ab00ba4",
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        console.log('ready');
        this.setData({
            loading: false,
        })
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

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})