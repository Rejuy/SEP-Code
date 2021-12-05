// pages/user/user.js
Page({
  data: {
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
  }
});