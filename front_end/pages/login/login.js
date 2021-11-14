// pages/login/login.js
import Notify from "vant-weapp/notify/notify";

Page({
  /**
   * Page initial data
   */
  data: {
    username: "",
    user_password: "",
  },

  login() {
    // post request to backend
    wx.request({
      url: "http://127.0.0.1:8080/login",
      data: {
        username: this.data.username,
        password: this.data.password,
      },
      header: {
        "content-type": "application/json", // 默认值
      },
      method: "POST",
      success: (res) => {
        if (res.data === "yes") {
          Notify({ type: "success", message: "登录成功" });
          const tabbar = this.getTabBar();
          tabbar.setData({ is_login: true });
          wx.switchTab({
            url: "/pages/index/index",
          });
        }
      },
      fail: function () {
        Notify({ type: "danger", message: "请求超时" });
      },
    });
  },
});
