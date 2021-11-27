// pages/register/register.js
import Notify from "vant-weapp/notify/notify";

Page({
  /**
   * Page initial data
   */
  data: {
    username: "",
    email: "",
    password: "",
    confirm_password: "",
  },
  checkEmpty() {
    // returns true if empty
    const data_obj = this.data;
    const isEmpty =
      data_obj.username === "" ||
      data_obj.email === "" ||
      data_obj.password === "" ||
      data_obj.confirm_password === "";
    return isEmpty;
  },
  register() {
    if (this.checkEmpty()) {
      Notify({ type: "danger", message: "必填为空" });
    } else if (this.data.password != this.data.confirm_password) {
      Notify({ type: "danger", message: "密码不一致" });
    } else {
      // attempt register
      console.log(this.data)
      wx.request({
        url: "http://thurec.xyz/api/v1.0/register",
        data: {
          user_name: this.data.username,
          email: this.data.email,
          password: this.data.password,
        },
        header: {
          "content-type": "application/json", // 默认值
        },
        method: "POST",
        success: function (res) {
          if (res.data === 0) {
            Notify({ type: "success", message: "邮件已发送，请查看邮箱" });
          }else{
            Notify({ type: "danger", message: "信息异常"})
          }
        },
        fail: function () {
          Notify({ type: "danger", message: "请求超时" });
        },
      });
    }
  },
});
