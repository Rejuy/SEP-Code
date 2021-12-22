Page({
    data: {
        loading: true,
        show_popup: false,

        place_name: '',
        place_position: '',
        opening_hours: '07:00-22:00',
        place_range: '',
        place_type: '',

        place_score: 0.0,
        place_star: 0.0,
        negative_radio: 10,
        neutral_radio: 30,
        positive_radio: 60,

        user_text: '',
        user_rate: 0.0,

        image_url: '',
        total_pages: 0,
        current_page: 0,
        comment_list: [
            { id: 1, user: '平台测试组', star: 4.5, date: '2021.12.11', likes: 998, complete: true , brief_text: '一教环境相当好，电源充足，一度是个不错的好去处，但因为有社团在三楼开活动，也不是那么香了。'},
            { id: 2, user: '卢本伟', star: 5.0, date: '2021.12.07', likes: 213, complete: true , brief_text: '从今天起，这座广场就叫做卢本伟广场！'},            
        ]
    },

    marco: {
        PAGE_CAPACITY: 8,
    },

    onLoad: function (options) {
        let content = JSON.parse(decodeURIComponent(options.content));
        console.log(content);
        this.setData({
            image_url: content.image,
            place_name: content.name,
            place_position: content.position,
            place_range: content.range,
            place_type: content.type,
            place_score: content.score.toFixed(1),
            place_star: content.star.toFixed(1),
            loading: false,
        })
    },

    // 页面上拉触底事件的处理函数
    onReachBottom: function () {

    },

    showPopup: function() {
        this.setData({
            show_popup: true
        })        
    },

    closePopup: function() {
        this.setData({
            show_popup: false
        })
    },

    userRate: function(event) {
        this.setData({
            user_rate: event.detail,
        });        
    },

    InputText: function(result) {
        this.setData({
            user_text: result.detail.value
        })
    },

    clearText: function() {
        this.setData({
            user_text: ""
        })
    },

    giveLikes: function (options) {
        console.log(options);
    },

    viewDetails: function (options) {
        console.log("hit");
    },

    // 生命周期函数--监听页面初次渲染完成
    onReady: function () {

    },

    // 生命周期函数--监听页面显示
    onShow: function () {

    },

    // 生命周期函数--监听页面隐藏
    onHide: function () {

    },

    // 生命周期函数--监听页面卸载
    onUnload: function () {

    },

    // 页面相关事件处理函数--监听用户下拉动作
    onPullDownRefresh: function () {

    },

    // 用户点击右上角分享
    onShareAppMessage: function () {

    }
})