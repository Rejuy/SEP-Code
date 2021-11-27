// pages/food/food.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        range_type: [
            { text: '全部餐饮', value: 0 },
            { text: '校内餐饮', value: 1 },
            { text: '校外餐饮', value: 2 },
        ],
        food_type: [
            { text: '任意类型', value: 0 },
            { text: '汉堡披萨', value: 1 },
            { text: '龙虾烧烤', value: 2 },
            { text: '香锅火锅', value: 3 },
            { text: '米线拉面', value: 4 },
        ],
        rank_type: [
            { text: '评分排序', value: 0 },
            { text: '热度排序', value: 1 },
            { text: '时间排序', value: 2 },
        ],
        range_value: 0,
        food_value: 0,
        rank_value: 0,
        uncertain_range: true,

        image_url: "https://obohe.com/i/2021/11/27/j1j3qo.jpg"
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

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})