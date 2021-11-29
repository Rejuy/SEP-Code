Component({
  properties: {
    is_login: {
      type: Boolean,
      value: false,
    },
    current_page: {
      type: String,
      value: ""
    }
  },
  methods:{
  onChange(event) {
    if (!this.data.is_login) {
      // 跳转 for login 模式
      switch (event.detail) {
        case "login":
          getCurrentPages().pop().onLoad();
          wx.reLaunch({
            url: "/pages/login/login",
          });
          break;
        case "register":
          getCurrentPages().pop().onLoad();
          wx.reLaunch({
            url: "/pages/register/register",
          });
          break;
        default:
          console.error("Unknown active, check custom-tab-bar.js");
          break;
      }
    } else {
      // is_login = true
      switch (event.detail) {
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
        case "course":
          wx.reLaunch({
            url: "/pages/course/course",
          });
          break;
        case "food":
            wx.reLaunch({
              url: "/pages/food/food",
            });
            break;
            case "place":
              wx.reLaunch({
                url: "/pages/place/place",
              });
              break;
        default:
          console.error("Unknown active, check custom-tab-bar.js");
          break;
      }
    }
  }
  },
});
