Page({
    data: {
        // 用户选择输入的文本
        user_text: "",
        // 用户选择上传的图片
        image_selected: [],
        // 展开的公告栏标号
        active_number: '1'
    },

    images_url: [],

    changeCollapse: function(event) {
        this.setData({
            active_number: event.detail
        })
    },

    addImage: function() {
        wx-wx.chooseImage({
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
        const {index} = result.currentTarget.dataset;
        let {image_selected} = this.data;
        image_selected.splice(index, 1);
        this.setData({
            image_selected
        })
    },

    handleText: function(result) {
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
        let text_length = this.data.user_text.length;
        // 输入框合法性检查
        if(text_length < 50) {
            wx.showToast({
              title: '文本不足50',
              icon: 'error',
              mask: true
            })
            return;
        }

        // 将用户反馈上传至服务器
        this.data.image_selected.forEach((temporary_path) => {
            wx-wx.uploadFile({
              filePath: temporary_path,
              name: 'image',
              url: 'http://49.233.123.127:8000/api/v1.0/save_images',
              formData: {},
              timeout: 0,
              success: (result) => {
                  // console.log(result);
                  let str = 'http://49.233.123.127:8000/' + result.data;
                  this.images_url.push(str);
              },
              fail: (error) => {
                  console.log(error);
              },
              complete: (res) => {
                  // console.log(this.images_url);
              },
            })
        });

        let that = this;
        wx.request({
          url: 'http://49.233.123.127:8000/api/v1.0/post_user_feedback',
          method: 'POST',
          data: {
              images_url: that.images_url,
              user_text: that.data.user_text
          },
          header: {
            "content-type": "application/json"
          },
          success:function(result) {
            console.log(that.images_url);
          },
          fail:function(error) {
              console.log(that.images_url);
          },
          complete: function(res) {

          }
        })

        wx.showToast({
          title: '提交成功',
          icon: 'success'
        })
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