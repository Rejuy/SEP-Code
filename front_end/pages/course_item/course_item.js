Page({
    data: {
        loading: true,
        show_popup: false,

        course_name: '',
        course_credit: 0,
        course_teacher: '',
        course_schedule: '春、秋季学期',
        course_department: '',
        course_type: '',

        course_score: 0.0,
        course_star: 0.0,
        negative_radio: 30,
        neutral_radio: 20,
        positive_radio: 50,

        user_text: '',
        user_rate: 0.0,
        image_selected: [],

        schedule_table: ['', '春季学期', '夏季学期', '秋季学期', '春、秋季学期'],

        image_url: "https://learn.tsinghua.edu.cn/b/wlxt/kc/v_kcxx_jskcxx/teacher/showImageById?wlkcid=2021-2022-1142764790&_csrf=d39592c7-bbb0-416a-affb-a39b1ab00ba4",

        comment_list: [
            { id: 1, user: '平台测试组', star: 3.5, date: '2021.12.06', likes: 998, complete: false , brief_text: '这课给人的感觉就是完全O什么K啊，自动PF，上够8个单元就稳吃1学分文核了。不过找实验室的过程确实痛苦面具啊'},
            { id: 2, user: '哥谭噩梦', star: 1.5, date: '2021.10.07', likes: 213, complete: true , brief_text: '我好不容易心动一次，你却让我输得这么彻底，哈哈哈哈哈，焯！'},            
        ]
    },

    marco: {
        PAGE_CAPACITY: 8,
    },

    onLoad: function (options) {
        let content = JSON.parse(options.content);
        
        this.setData({
            course_name: content.name,
            course_teacher: content.teacher,
            course_department: content.department,
            course_type: content.type,
            course_score: content.score.toFixed(1),
            course_star: content.star.toFixed(1),
            loading: false,
        })
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

    addImage: function() {
        wx.chooseImage({
          count: 9,
          sizeType: ['original', 'compressed'],
          sourceType: ['album', 'camera'],
          success: (result) => {
              this.setData({
                  image_selected: [...this.data.image_selected, ...result.tempFilePaths]
              })
          }, fail: (error) => {
              console.log(error);
          },complete: (result) => {

          },
        })
    },

    removeImage: function(result) {
        const { index } = result.currentTarget.dataset;
        let { image_selected } = this.data;
        image_selected.splice(index, 1);
        this.setData({
            image_selected
        })
    },

    giveLikes: function (options) {
        console.log(options);
    },

    viewFullContent: function (event) {
        console.log(event.currentTarget.dataset.index);
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

    // 页面上拉触底事件的处理函数
    onReachBottom: function () {

    },

    // 用户点击右上角分享
    onShareAppMessage: function () {

    }
})