Page({
    data: {
        // 用户选择输入的文本
        user_text: "",
        // 用户选择上传的图片
        image_selected: [],
        // 展开的公告栏标号
        active_number: '1'
    },

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
        // this.data.image_selected.forEach((temporary_path, index) => {
        //     wx-wx.uploadFile({
        //         filePath: temporary_path,
        //         name: 'user_feedback_image',
        //         url: 'url',
        //         formData: {},
        //         header: header,
        //         timeout: 0,
        //         success: (result) => {
        //             console.log(result);
        //             if(index === this.data.image_selected.length - 1) {
        //                 // 全部图片已经上传，配合文本一起传递至后端
        //             }
        //         },fail: (error) => {
        //             console.log(error);
        //         },complete: (res) => {
      
        //         },
        //       })
        // });

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