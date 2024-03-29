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
      const app = getApp();
      const domain = app.global_data.global_domain;
      let login_domain = domain + '/api/v1.0/login';
      wx.request({
        url: login_domain,
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
            app.global_data.global_user_token = res.data.user_mask;
            /*
            app.global_data.global_user_info.email = user_data.email;
            app.global_data.global_user_info.like_count = user_data.like_count;
            app.global_data.global_user_info.account_birth = user_data.account_birth;
            app.global_data.global_user_info.username = user_data.user_name;
            */
          } else if (res.data.state === 1) {
            Notify({ type: "danger", message: "用户不存在" });
          }else if (res.data.state === 2) {
            Notify({ type: "danger", message: "密码错误" });
          }else if (res.data.state === 3){
            Notify({ type: "danger", message: "用户未激活" });
          }else{
            Notify({ type: "danger", message: "连接失败，请稍后重试" });
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
