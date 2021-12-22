Page({
  data: {
    swiper_data: [
      {
        id: 1,
        url: "../notice/notice",
        path: "https://s3.bmp.ovh/imgs/2021/12/8cc8d6aa502879af.jpg"
      }, 
      {
        id: 2,
        url: "../notice/notice",
        path: "https://s3.bmp.ovh/imgs/2021/12/d4d723c1a40f1385.jpg"
      }
    ],

    search_value: '',

    random_list: [
      { id: 1, type: '课程', image: 'https://s3.bmp.ovh/imgs/2021/12/a955c9c5cdd8f7b7.jpg'},
      { id: 2, type: '餐饮', image: 'https://s3.bmp.ovh/imgs/2021/12/a955c9c5cdd8f7b7.jpg'},
      { id: 3, type: '地点', image: 'https://s3.bmp.ovh/imgs/2021/12/a955c9c5cdd8f7b7.jpg'},
    ]
  },

  onSearch: function(result) {
    this.setData({
        search_value: result.detail
    });
    wx.redirectTo({
      url: '../search/search?search_value=' + this.data.search_value,
    })
  },
  
  //生命周期函数--监听页面加载
  onLoad: function (options) {
    
  },

  // 生命周期函数--监听页面初次渲染完成
  onReady: function () {
    if (getApp().global_data.global_user_token === ""){
      // not logged in
      wx.reLaunch({
        url: '/pages/login/login',
      })
    }
  },
})