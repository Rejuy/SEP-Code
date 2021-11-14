// pages/login/login.js
import Notify from "vant-weapp/notify/notify";

Page({
  data: {
    user_name: "",
    user_password: "",
  },

  login() {
    // post request to backend
    const loginSuccessful = ()=> {
      const tabbar = this.getTabBar();
      tabbar.setData({ is_login: true });
      wx.switchTab({
        url: "/pages/index/index",
      });
    }
    
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
        console.log(res.data.state);
        if (res.data.state == 0) {
          console.log("suc");
          Notify({ type: 'success', message: '登录成功' });
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
