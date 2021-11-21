// pages/login/login.js
import Notify from "vant-weapp/notify/notify";

Page({
  data: {
    user_name: "",
    user_password: "",
  },

  checkEmpty() {
    const data_obj = this.data;
    const isEmpty = data_obj.user_name === "" || data_obj.user_password === "";
    return isEmpty;
  },
  loginSuccessful() {
    const app = getApp();
    app.globalData.g_active = "home";
    app.globalData.g_is_login = true;
    wx.reLaunch({
      url: "/pages/index/index",
    });
  },
  login() {
    // post request to backend
    // TODO: finish login check
    Notify({ type: "success", message: "登录成功" });
    setTimeout(this.loginSuccessful, 500);
    return;
    wx.request({
      url: "http://49.233.1.189:5000/api/v1.0/login",
      data: {
        user_name: this.data.user_name,
        password: this.data.user_password,
      },
      header: {
        "content-type": "application/json", // 默认值
      },
      method: "POST",
      success: (res) => {
        if (res.data.state == 0) {
          Notify({ type: "success", message: "登录成功" });
          setTimeout(loginSuccessful, 500);
        }
      },
      fail: function (res) {
        console.log(res);
        Notify({ type: "danger", message: "请求超时" });
      },
    });
  },
});
