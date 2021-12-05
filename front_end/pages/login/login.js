import Notify from "@vant/weapp/notify/notify";

Page({
  data: {
    user_name: "",
    user_password: "",
  },

  checkEmpty() {
    const data_object = this.data;
    const is_empty =
      data_object.user_name === "" || data_object.user_password === "";
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
        url: "https://thurec.whiteffire.cn/api/v1.0/login",
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
            setTimeout(this.loginSuccessful, 500);
            const app = getApp();
            const user_data = res.data.user;
            app.global_data.global_user_info.email = user_data.email;
            app.global_data.global_user_info.like_count = user_data.like_count;
            app.global_data.global_user_info.account_birth = user_data.account_birth;
            app.global_data.global_user_info.username = user_data.user_name;
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
