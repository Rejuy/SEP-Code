// pages/user/user.js
Page({
  data: {
    loaded: true,
    username: "User"
  },
  logout() {
    wx.reLaunch({
      url: "/pages/login/login",
    });
  },
});
