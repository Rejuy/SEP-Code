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
    if (this.checkEmpty()) {
      Notify({ type: "danger", message: "必填为空" });
    } else {
      wx.request({
        url: "https://thurec.xyz/api/v1.0/login",
        data: {
          user_name: this.data.user_name,
          password: this.data.user_password,
        },
        header: {
          "content-type": "application/json", // 默认值
        },
        method: "POST",
        success: (res) => {
          if (res.data.state === 0) {
            Notify({ type: "success", message: "登录成功" });
            getApp().globalData.g_user_token = res.data.user_mask;
            setTimeout(this.loginSuccessful, 500);
          } else {
            Notify({ type: "danger", message: "登录失败" });
          }
        },
        fail: function (res) {
          Notify({ type: "danger", message: "请求超时" });
        },
      });
    }

    return;
  },
});
