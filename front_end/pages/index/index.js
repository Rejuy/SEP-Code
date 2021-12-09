Page({
  data: {
    // 后续可以通过 onLoad 函数获取数据
    swiper_data: [{
        id: 1,
        url: "../notice/notice",
        path: "../../images/swiper/notice.png"
      },{
        id:2,
        url: "../notice/notice",
        path: "../../images/swiper/topic.png"
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