// pages/user/user.js
Page({
  data: {},
  logout() {
    wx.reLaunch({
      url: "/pages/login/login",
    });
  },
});
