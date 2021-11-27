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

        image_url: "https://z3.ax1x.com/2021/11/28/omzV6x.jpg"
    },

    rangeSelected: function(result) {
        this.setData({
            range_value: result.detail
        });
        let tmp_value = this.data.range_value;
        
        if(tmp_value == 1) {
            let inside_food_type = [
                { text: '任意食堂', value: 0 },
                { text: '桃李园', value: 1 },
                { text: '紫荆园', value: 2 },
                { text: '玉树园', value: 3 },
                { text: '清芬园', value: 4 },
            ];
            this.setData({
                uncertain_range: false,
                food_type: inside_food_type
            });            
        }else if(tmp_value == 2) {
            let outside_food_type = [
                { text: '任意类型', value: 0 },
                { text: '汉堡披萨', value: 1 },
                { text: '龙虾烧烤', value: 2 },
                { text: '香锅火锅', value: 3 },
                { text: '米线拉面', value: 4 },
            ];
            this.setData({
                uncertain_range: false,
                food_type: outside_food_type
            });   
        }else {
            let default_food_type = [
                { text: '任意类型', value: 0 },
            ];
            this.setData({
                uncertain_range: true,
                food_type: default_food_type
            });   
        }
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