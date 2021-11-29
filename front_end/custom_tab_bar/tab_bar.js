Component({
  data: {
    active: "login",
    is_login: false,
  },
  methods: {
    onChange(event) {
      const app = getApp();
      this.setData({ active: event.detail });
      app.global_data.global_active = this.data.active;
      if (!this.data.is_login) {
        // 跳转 for login 模式
        switch (this.data.active) {
          case "login":
            wx.reLaunch({
              url: "/pages/login/login",
            });
            break;
          case "register":
            wx.reLaunch({
              url: "/pages/register/register",
            });
            break;
          default:
            console.error("Unknown active, check custom_tab_bar.js");
            break;
        }
      } else {
        // is_login = true
        switch (this.data.active) {
          case "home":
            wx.reLaunch({
              url: "/pages/index/index",
            });
            break;
          case "user":
            wx.reLaunch({
              url: "/pages/user/user",
            });
            break;
          default:
            console.error("Unknown active, check custom-tab-bar.js");
            break;
        }
      }
    },
  },
  lifetimes: {
    attached() {
      this.setData({
        is_login: getApp().global_data.global_is_login,
        active: getApp().global_data.global_active,
      });
    },
  },
});
