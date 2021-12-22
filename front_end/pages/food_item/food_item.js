import Dialog from '@vant/weapp/dialog/dialog';
import Notify from '@vant/weapp/notify/notify';


Page({
    data: {
        loading: true,
        show_popup: false,

        food_id: 0,
        food_range: '',
        food_type: '',
        food_name: '',
        food_position: '',
        business_hours: '',


        food_score: 0.0,
        food_star: 0.0,
        negative_radio: 30,
        neutral_radio: 20,
        positive_radio: 50,

        user_text: '',
        user_rate: 0.0,

        image_url: '',
        total_pages: 0,
        current_page: 0,
        comments_list: []
    },

    marco: {
        PAGE_CAPACITY: 8,
    },

    onLoad: function (options) {
        let content = JSON.parse(decodeURIComponent(options.content));

        this.setData({
            food_id: content.id,
            image_url: content.image, 
            food_name: content.name,
            food_position: content.position,
            food_range: content.range,
            food_type: content.type,
            food_score: content.score.toFixed(1),
            food_star: content.star.toFixed(1),
            loading: false,
        })

        this.getCommentList();
    },

    onReachBottom: function () {
        if(this.data.current_page >= this.data.total_pages) {
            console.log("已无下一页数据");
        }else {
            this.setData({
                current_page: this.data.current_page + 1
            })
            this.getCommentList();
        }
    },

    getCommentList: function() {
        const app = getApp();
        let begin = this.data.current_page * this.marco.PAGE_CAPACITY;
        let end = begin + this.marco.PAGE_CAPACITY - 1;

        wx.request({
          url: app.global_data.global_domain + '/api/v1.0/get_food_item',
          method: 'POST',  
          data: {
              id: this.data.food_id,
              begin: begin,
              end: end,
          },
          dataType: JSON,
          enableCache: true,
          enableHttp2: true,
          enableQuic: true,
          header: {
            "content-type": "application/json"
          },
          timeout: 0,
          success: (result) => {
              let rtn = JSON.parse(result.data);
              this.data.comments_list.push.apply(this.data.comments_list, rtn.comments);
              this.data.total_pages = Math.ceil(rtn.counts / this.marco.PAGE_CAPACITY) - 1;
              this.setData({
                  business_hours: rtn.hours,
                  negative_radio: rtn.negative,
                  neutral_radio: rtn.neutral,
                  positive_radio: rtn.positive,
                  comments_list: this.data.comments_list,
                  total_pages: this.data.total_pages,
              })
          }, fail: (error) => {
              console.log(error);
          }, complete: (res) => {},
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

    handleSubmit: function() {
        Dialog.confirm({
            title: '确认提交？',
            message: '或许还可以再检查检查~',
        }).then(() => {
            // on confirm
            if(this.data.user_rate == 0) {
                Dialog.confirm({
                    title: '确认评分？',
                    message: '您一定要给它0分吗？',
                }).then(() => {
                    console.log(this.data.user_rate);
                    Notify({ type: 'success', message: '发布成功' });
                })
            }
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