import Notify from "@vant/weapp/notify/notify";

Page({
  data: {
    user_name: "",
    user_password: "",
  },

  checkEmpty() {
    const data_object = this.data;
    const is_empty = data_object.user_name === "" || data_object.user_password === "";
    return is_empty;
  },
  loginSuccessful() {
    const app = getApp();
    app.global_data.global_active = "home";
    app.global_data.global_is_login = true;
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
        url: "http://thurec.xyz/api/v1.0/login",
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
            //getApp().globalData.global_user_token = res.data.user_mask;
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
