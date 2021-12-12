// pages/user/user.js
import Notify from "@vant/weapp/notify/notify";

Page({
  data: {
    user_icon_path: "/images/icons/empty_user.png",

    loading: true,
    username: "",
    email: "",
    account_birth: "",
    like_count: 0,
    comment_count: 0,
    collection_count: 0,
  },
  logout() {
    const app = getApp();
    app.logout();
    wx.reLaunch({
      url: "/pages/login/login",
    });
  },
  choose_icon() {
    wx.chooseImage({
      count: 1,
      success: (res) => {
        const temp_path = res.tempFilePaths[0];
        wx.saveFile({
          tempFilePath: temp_path,
          success: (r) => {
            const saved_path = r.savedFilePath;
            wx.uploadFile({
              filePath: saved_path,
              name: 'image',
              url: getApp().global_data.global_domain + '/api/v1.0/save_user_icon',
              formData: {
                'mask': getApp().global_data.global_user_token
              },
              success: (res) => {
                Notify({
                  type: "success",
                  message: "上传成功"
                });
                this.setData({
                  user_icon_path: res.data.path
                })
              },
              fail() {
                Notify({
                  type: "danger",
                  message: "上传失败"
                });
              }
            })
          },
          fail() {
            Notify({
              type: "danger",
              message: "上传失败"
            });
          }
        })
      },
    })
  },
  onReady() {
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
            email: user_data.email,
            account_birth: user_data.account_birth.slice(0, -12),
            like_count: user_data.like_count,
            comment_count: user_data.comment_count,
            collection_count: user_data.collection_count,
          })
        }
      }
    })
  }
});