Page({

  data: {
    loading: true,
    user_icon_path : "",
  },

  onReady: function () {
    const app = getApp();
    wx.request({
      url: app.global_data.global_domain + '/api/v1.0/get_user_icon',
      data: {
        mask: app.global_data.global_user_token
      },
      method: "POST",
      success: (res) => {
        if (res.data.state === 0) {
          this.setData({
            user_icon_path: app.global_data.global_domain + "/" + res.data.path,
          });
        }
      }
    })
    wx.request({
      url: app.global_data.global_domain + '/api/v1.0/get_user_info',
      data: {
        mask: app.global_data.global_user_token
      },
      method: "POST",
      success: (res) => {
        if (res.data.state === 0) {
          const user_data = res.data.user;
          this.setData({
            loading: false,
            username: user_data.user_name,
          })
        }
      }
    })
  }

})