// pages/food_item/food_item.js
Page({
    data: {
        loading: true,

        food_name: '汉堡王',
        food_position: '海淀区华清嘉园7号楼',
        business_hours: '07:00-22:00',
        food_range: '校外餐饮',
        food_type: '汉堡披萨',

        negative_radio: 30,
        neutral_radio: 20,
        positive_radio: 50,

        image_url: "https://z3.ax1x.com/2021/12/03/odK6aD.jpg",

        comment_list: [
            { id: 1, user: '平台测试组', star: 2.5, date: '2021.12.11', likes: 998, complete: true , brief_text: '早期满80-40的确是诚意满满，现在配送费上去了，福利却莫得了，差评差评！'},
            { id: 2, user: '老八', star: 5.0, date: '2021.12.07', likes: 213, complete: true , brief_text: '美食界里我老八，万人称我美食家！'},            
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