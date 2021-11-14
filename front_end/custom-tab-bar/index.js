Component({
  data: {
    active: 0,
    is_login: false,
  },
  setIsLogin(loginStatus){
    console.log("changed");
    this.data.isLogin = loginStatus;
  },
  onChange(event) {
    this.setData({ active: event.detail });
    if (this.data.isLogin){
      // 跳转 for login 模式
      wx.switchTab({
        url: '/pages/register/register',
      })
    }else{
      // 跳转 for 已经登录模式
      
    }

  },
});
