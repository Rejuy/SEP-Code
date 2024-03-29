// pages/register/register.js
import Notify from "@vant/weapp/notify/notify";

Page({
  /**
   * Page initial data
   */
  data: {
    user_name: "",
    email: "",
    password: "",
    confirm_password: "",
  },
  checkEmpty() {
    // returns true if empty
    const data_obj = this.data;
    const is_empty =
      data_obj.user_name === "" ||
      data_obj.email === "" ||
      data_obj.password === "" ||
      data_obj.confirm_password === "";
    return is_empty;
  },
  register() {
    if (this.checkEmpty()) {
      Notify({ type: "danger", message: "必填为空" });
    } else if (this.data.password != this.data.confirm_password) {
      Notify({ type: "danger", message: "密码不一致" });
    } else {
      // attempt register
      const app = getApp();
      const domain = app.global_data.global_domain;
      let register_domain = domain + "/api/v1.0/register_user_info";
      wx.request({
        url: register_domain,
        data: {
          user_name: this.data.user_name,
          email: this.data.email,
          password: this.data.password,
        },
        header: {
          "content-type": "application/json", // 默认值
        },
        method: "POST",
        success: function (res) {
          if (res.data.state === 0) {
            Notify({
              type: "success",
              message: "邮件已发送，请查看邮箱(可能在垃圾邮件中)",
            });
          } else if (res.data.state === 1) {
            Notify({ type: "danger", message: "邮箱不合法，请检查注册信息" });
          } else if (res.data.state === 2) {
            Notify({
              type: "danger",
              message: "用户名不合法，长度要求 6 到 10",
            });
          } else if (res.data.state === 3) {
            Notify({
              type: "danger",
              message: "密码长度不合法，长度要求 6 到 18",
            });
          } else if (res.data.state === 4) {
            Notify({
              type: "danger",
              message:
                "密码符号类型不足，需包含大小写字母、数字、符号，且必须包含前三者",
            });
          } else if (res.data.state === 5) {
            Notify({
              type: "danger",
              message: "密码包含非法字符，只能包含大小写字母、数字、符号",
            });
          } else if (res.data.state === 6) {
            Notify({ type: "danger", message: "邮箱已存在，请检查注册信息" });
          } else if (res.data.state === 7) {
            Notify({ type: "danger", message: "用户名已存在，请检查注册信息" });
          } else {
            Notify({ type: "danger", message: "连接失败，请稍后重试" });
          }
        },
        fail: function (res) {
          Notify({ type: "danger", message: "请求超时" });
        },
      });
    }
  },
});
