// pages/place/place.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        range_type: [
            { text: '任意地点', value: 0 },
            { text: '校内地点', value: 1 },
            { text: '校外地点', value: 2 },
        ],
        place_type: [
            { text: '任意场所', value: 0 },
            { text: '自习场所', value: 1 },
            { text: '锻炼场所', value: 2 },
            { text: '会议场所', value: 3 },
            { text: '娱乐场所', value: 4 },
        ],
        rank_type: [
            { text: '评分排序', value: 0 },
            { text: '热度排序', value: 1 },
            { text: '时间排序', value: 2 },
        ],
        range_value: 0,
        place_value: 0,
        rank_value: 0,

        image_url: "https://mmbiz.qpic.cn/mmbiz_jpg/HhoEMZZMsiaQgcfIVLkACUh2wiaMRyVkiaaxScRDXzvmA4erdq8HzhF34JzQzH7PsjdZRtgcn51XdE93IIiaCZNqUw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1",

        place_list: [
            { id: 1, name: '第一教室楼', position: '清华大学西南方向', range: '校内地点', type: '自习场所', star: 4.0, score: 8.3, tag: 'TOP3', color: '#07C160'},    
            { id: 2, name: '邺架轩', position: '清华大学李文正图书馆下沉广场', range: '校内地点', type: '自习场所', star: 3.5, score: 7.2, tag: '', color: '#07C160'},        
        ]
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