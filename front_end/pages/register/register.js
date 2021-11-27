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
      // TODO: finish register check
      Notify({ type: "success", message: "邮件已发送，请查看邮箱" });
      return;
      wx.request({
        url: "http://127.0.0.1:8080/register",
        data: {
          username: this.data.username,
          email: this.data.email,
          password: this.data.password,
        },
        header: {
          "content-type": "application/json", // 默认值
        },
        method: "POST",
        success: function (res) {
          if (res.data === "yes") {
            Notify({ type: "success", message: "注册成功" });
          }
        },
        fail: function () {
          Notify({ type: "danger", message: "请求超时" });
        },
      });
    }
  },
});
