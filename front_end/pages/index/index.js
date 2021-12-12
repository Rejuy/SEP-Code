Page({
  data: {
    // 后续可以通过 onLoad 函数获取数据
    swiper_data: [{
        id: 1,
        url: "../notice/notice",
        path: "https://s3.bmp.ovh/imgs/2021/12/8cc8d6aa502879af.jpg"
      },{
        id: 2,
        url: "../notice/notice",
        path: "https://s3.bmp.ovh/imgs/2021/12/d4d723c1a40f1385.jpg"
      }
    ]
  },

  /*
   * 生命周期函数--监听页面加载
  */
  onLoad: function (options) {
    
  },

  /*
   * 生命周期函数--监听页面初次渲染完成
  */
  onReady: function () {
    if (getApp().global_data.global_user_token === ""){
      // not logged in
      wx.reLaunch({
        url: '/pages/login/login',
      })
    }
  },
})