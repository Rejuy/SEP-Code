// pages/user/user.js
Page({
  data: {},
  logout() {
    const app = getApp();
    app.globalData.g_active = "login";
    app.globalData.g_is_login = false;
    wx.reLaunch({
      url: "/pages/login/login",
    });
  },
});
