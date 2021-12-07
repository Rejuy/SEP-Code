// pages/user/user.js
import Notify from "@vant/weapp/notify/notify";

Page({
  data: {
    user_icon_path: "/images/icons/empty_user.png",

    loaded: true,
    username: "",
    email: "",
    account_birth: "",
    comment_count: 0,
    like_count: 0,
    content_count: 0,
    collection_count: 0,
  },
  logout() {
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
    this.setData({
      username: app.global_data.global_user_info.username,
      email: app.global_data.global_user_info.email,
      account_birth: app.global_data.global_user_info.account_birth.slice(0, -12),
      collection_count: app.global_data.global_user_info.collection_count,
      content_count: app.global_data.global_user_info.content_count,
      like_count: app.global_data.global_user_info.like_count,
      comment_count: app.global_data.global_user_info.comment_count,
    })
    let curr_app = getApp();
    wx.request({
      url: curr_app.global_data.global_domain + '/api/v1.0/get_user_icon',
      data: {
        mask: curr_app.global_data.global_user_token
      },
      method: "POST",
      success: (res) => {
        if (res.data.state === 0) {
          this.setData({
            user_icon_path: curr_app.global_data.global_domain + "/" + res.data.path,
          });
        }
      }
    })
  }
});