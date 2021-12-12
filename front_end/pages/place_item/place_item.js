// pages/place_item/place_item.js
Page({
    data: {
        loading: true,

        place_name: '第一教室楼',
        place_position: '清华大学西南方向',
        opening_hours: '07:00-22:00',
        place_range: '校内地点',
        place_type: '自习场所',

        negative_radio: 10,
        neutral_radio: 30,
        positive_radio: 60,

        image_url: "https://mmbiz.qpic.cn/mmbiz_jpg/HhoEMZZMsiaQgcfIVLkACUh2wiaMRyVkiaaxScRDXzvmA4erdq8HzhF34JzQzH7PsjdZRtgcn51XdE93IIiaCZNqUw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1",

        comment_list: [
            { id: 1, user: '平台测试组', star: 4.5, date: '2021.12.11', likes: 998, complete: true , brief_text: '一教环境相当好，电源充足，一度是个不错的好去处，但因为有社团在三楼开活动，也不是那么香了。'},
            { id: 2, user: '卢本伟', star: 5.0, date: '2021.12.07', likes: 213, complete: true , brief_text: '从今天起，这座广场就叫做卢本伟广场！'},            
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