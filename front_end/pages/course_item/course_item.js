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

        negative_radio: 30,
        neutral_radio: 20,
        positive_radio: 50,

        image_url: "https://learn.tsinghua.edu.cn/b/wlxt/kc/v_kcxx_jskcxx/teacher/showImageById?wlkcid=2021-2022-1142764790&_csrf=d39592c7-bbb0-416a-affb-a39b1ab00ba4",

        comment_list: [
            { id: 1, user: '平台测试组', star: 3.5, date: '2021.12.06', likes: 998, complete: false , brief_text: '这课给人的感觉就是完全O什么K啊，自动PF，上够8个单元就稳吃1学分文核了。不过找实验室的过程确实痛苦面具啊'},
            { id: 2, user: '哥谭噩梦', star: 1.5, date: '2021.10.07', likes: 213, complete: true , brief_text: '我好不容易心动一次，你却让我输得这么彻底，哈哈哈哈哈，焯！'},            
        ]
    },

    onLoad: function (options) {
        this.setData({
            loading: false,
        })
    },

    giveLikes: function (options) {
        console.log(options);
    },

    viewDetails: function (options) {
        console.log("hit");
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