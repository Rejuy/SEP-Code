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

    random_list: []
  },

    //生命周期函数--监听页面加载
    onLoad: function () {
      const app = getApp();

      wx.request({
        url: app.global_data.global_domain + '/api/v1.0/get_random_list',
        method: 'GET',
        data: {},
        dataType: JSON,
        enableCache: true,
        enableHttp2: true,
        enableQuic: true,
        timeout: 0,
        success: (result) => {
          let rtn = JSON.parse(result.data).content;
          rtn[0].image = rtn[1].image = rtn[2].image = 'https://s3.bmp.ovh/imgs/2021/12/a955c9c5cdd8f7b7.jpg';

          this.setData({
            random_list: rtn
          })
        },
        fail: (res) => {},
        complete: (res) => {},
      })
    },

  onSearch: function(result) {
    this.setData({
        search_value: result.detail
    });
    wx.redirectTo({
      url: '../search/search?search_value=' + this.data.search_value,
    })
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

  viewItem: function(event) {
    let tmp_url = '';
    let index = event.currentTarget.dataset.index;

    switch(index){
        case 0:
            tmp_url = '../course_item/course_item?content=';
            break;
        case 1:
            tmp_url = '../food_item/food_item?content=';
            this.data.random_list[index].range = this.data.random_list[index].scope;
            break;
        case 2:
            tmp_url = '../place_item/place_item?content=';
            this.data.random_list[index].range = this.data.random_list[index].scope;
            break;
        default:
            console.log("index.js error");
    }

    let content = JSON.stringify(this.data.random_list[index]);

    wx.navigateTo({
        url: tmp_url + encodeURIComponent(content),
    })
  }
})