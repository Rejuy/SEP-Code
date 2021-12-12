Page({
  data: {
    loading: true,
    user_icon_path: "",
    comment_list: [],
    num_comment: 0,

    loading: true,
  },
  back: function () {
    wx.reLaunch({
      url: '/pages/user/user',
    })
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
            num_comment: user_data.comment_count,
          })
          wx.request({
            url: app.global_data.global_domain + '/api/v1.0/get_comment_by_id',
            method: "POST",
            data: {
              mask: app.global_data.global_user_token,
              offset: 0,
              size: this.data.num_comment,
            },
            success: (res) => {
              this.setData({
                comment_list: res.data.comments
              })
              this.setData({
                loading: false
              })
            }
          })
        }
      }
    })
  }

})