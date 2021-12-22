// pages/search/search.js
Page({
    data: {
        image_table: [
            "https://learn.tsinghua.edu.cn/b/wlxt/kc/v_kcxx_jskcxx/teacher/showImageById?wlkcid=2021-2022-1142764790&_csrf=d39592c7-bbb0-416a-affb-a39b1ab00ba4",
            "https://z3.ax1x.com/2021/12/03/odK6aD.jpg",
            "https://mmbiz.qpic.cn/mmbiz_jpg/HhoEMZZMsiaQgcfIVLkACUh2wiaMRyVkiaaxScRDXzvmA4erdq8HzhF34JzQzH7PsjdZRtgcn51XdE93IIiaCZNqUw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1",
        ],

        total_pages: 0,
        current_page: 0,
        search_value: '',

        // 记得处理下 id, 这次 id 可能有重复, 需要识别是什么类型的，然后改成字符串 eg: id + class
        content_list: [],
    },

    marco: {
        PAGE_CAPACITY: 8,
    },

    // 生命周期函数--监听页面加载
    onLoad: function (options) {
        this.setData({
            search_value: options.search_value
        })
        this.getContentList();
    },

    // 页面上拉触底事件的处理函数
    onReachBottom: function () {
        if(this.data.current_page >= this.data.total_pages) {
            console.log("已无下一页数据");
        }else {
            this.setData({
                current_page: this.data.current_page + 1
            })
            this.getContentList();
        }
    },

    getContentList: function () {
        const app = getApp();
        let begin = this.data.current_page * this.marco.PAGE_CAPACITY;
        let end = begin + this.marco.PAGE_CAPACITY - 1;

        wx.request({
          url: app.global_data.global_domain + '/api/v1.0/global_search',
          method: 'POST',  
          data: {
              like: this.data.search_value,
              begin: begin,
              end: end,
          },
          dataType: JSON,
          enableCache: true,
          enableHttp2: true,
          enableQuic: true,
          header: {
            "content-type": "application/json"
          },
          timeout: 0,
          success: (result) => {
              let rtn = JSON.parse(result.data);
              let array_length = rtn.items.length;
              for(let i = 0; i < array_length; i ++) {
                  switch(rtn.items[i].class) {
                      case 1:
                          rtn.items[i].range = "课程推荐";
                          rtn.items[i].type = "课程卡片";
                          rtn.items[i].image = this.data.image_table[0];
                          break;
                      case 2:
                          rtn.items[i].range = "餐饮推荐";
                          rtn.items[i].type = "餐饮卡片";
                          rtn.items[i].image = this.data.image_table[1];
                          break;
                      case 3:
                          rtn.items[i].range = "出行推荐";
                          rtn.items[i].type = "出行卡片";
                          rtn.items[i].image = this.data.image_table[2];
                          break;
                      default:
                          console.log("search.js : fail to match");
                  }
              }
              this.data.content_list.push.apply(this.data.content_list, rtn.items);
              this.data.total_pages = Math.ceil(rtn.count / this.marco.PAGE_CAPACITY) - 1;
              this.setData({
                  content_list: this.data.content_list,
                  total_pages: this.data.total_pages,
              })
          }, fail: (error) => {
              console.log(error);
          }, complete: (res) => {},
        })
    },

    // 生命周期函数--监听页面初次渲染完成
    onReady: function () {

    },

    // 生命周期函数--监听页面显示
    onShow: function () {

    },

    // 生命周期函数--监听页面隐藏
    onHide: function () {

    },

    // 生命周期函数--监听页面卸载
    onUnload: function () {

    },

    // 页面相关事件处理函数--监听用户下拉动作
    onPullDownRefresh: function () {

    },

    // 用户点击右上角分享
    onShareAppMessage: function () {

    }
})