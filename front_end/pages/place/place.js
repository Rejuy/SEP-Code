import Toast from '@vant/weapp/toast/toast';
import Dialog from '@vant/weapp/dialog/dialog';


Page({
    data: {
        range : [
            { text: '任意地点', value: 0 },
            { text: '校内地点', value: 1 },
            { text: '校外地点', value: 2 },
        ],

        type: [
            { text: '任意场所', value: 0 },
            { text: '自习场所', value: 1 },
            { text: '锻炼场所', value: 2 },
            { text: '会议场所', value: 3 },
            { text: '娱乐场所', value: 4 },
        ],

        order: [
            { text: '评分排序', value: 0 },
            { text: '热度排序', value: 1 },
            { text: '时间排序', value: 2 },
        ],

        image_url: "https://mmbiz.qpic.cn/mmbiz_jpg/HhoEMZZMsiaQgcfIVLkACUh2wiaMRyVkiaaxScRDXzvmA4erdq8HzhF34JzQzH7PsjdZRtgcn51XdE93IIiaCZNqUw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1",

        range_table: ['校内地点', '校外地点'],
        type_table: ['自习场所', '锻炼场所', '会议场所', '娱乐场所'],
        color_table: ['#800080', '#FF69B4', '#000080', '#228B22'],

        search_value: '',
        range_value: 0,
        type_value: 0,
        order_value: 0,

        edit_place_name: '',
        edit_place_position: '',
        edit_opening_hours: '',
        edit_range_value: 0,
        edit_place_type: 0,
        place_range_title: '选择范围',
        place_type_title: '选择类型',

        total_pages: 0,
        current_page: 0,
        show_popup: false,

        places_list: []
    },

    marco: {
        PAGE_CAPACITY: 8,
        INSIDE_CAMPUS: 1,
        OUTSIDE_CAMPUS: 2,

        DEFAULT_RANGE_TITLE: '选择范围',
        DEFAULT_TYPE_TITLE: '选择类型',
    },

    onLoad: function () {
        this.getPlaceList();
    },

    onReachBottom: function () {
        if(this.data.current_page >= this.data.total_pages) {
            console.log("已无下一页数据");
        }else {
            this.setData({
                current_page: this.data.current_page + 1
            })
            this.getPlaceList();
        }
    },

    getPlaceList: function() {
        const app = getApp();
        let begin = this.data.current_page * this.marco.PAGE_CAPACITY;
        let end = begin + this.marco.PAGE_CAPACITY - 1;

        wx.request({
          url: app.global_data.global_domain + '/api/v1.0/get_places_list',
          method: 'POST',  
          data: {
              begin: begin,
              end: end,
              like: this.data.search_value,
              place_scope: this.data.range_value,
              place_type: this.data.type_value,
              place_order: this.data.order_value
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
              let array_length = rtn.places.length;
              for(let i = 0; i < array_length; i ++) {
                  let tmp_range_value = rtn.places[i].scope - 1;
                  let tmp_type_value = rtn.places[i].type - 1;
                  rtn.places[i].color = this.data.color_table[tmp_type_value];
                  rtn.places[i].type = this.data.type_table[tmp_type_value];
                  rtn.places[i].range = this.data.range_table[tmp_range_value];
              }
              this.data.places_list.push.apply(this.data.places_list, rtn.places);
              this.data.total_pages = Math.ceil(rtn.total_places / this.marco.PAGE_CAPACITY) - 1;
              this.setData({
                  places_list: this.data.places_list,
                  total_pages: this.data.total_pages,
              })
          }, fail: (error) => {
              console.log(error);
          }, complete: (res) => {},
        })
    },

    onSearch: function(result) {
        this.setData({
            current_page: 0,
            places_list: [],
            search_value: result.detail,
        });
        this.getPlaceList();
    },

    rangeSelected: function(result) {
        this.setData({
            current_page: 0,
            places_list: [],
            range_value: result.detail,
        });      
        this.getPlaceList();
    },

    typeSelected: function(result) {
        this.setData({
            current_page: 0,
            places_list: [],
            type_value: result.detail,
        });      
        this.getPlaceList();
    },    

    orderSelected: function(result) {
        this.setData({
            current_page: 0,
            places_list: [],
            order_value: result.detail,
        });   
        this.getPlaceList();   
    },

    showPopup: function() {
        this.setData({
            show_popup: true
        })
    },

    closePopup: function() {
        this.setData({
            show_popup: false
        });
    },

    editPlaceRange: function(event) {
        const { value } = event.detail;
        this.setData({
            place_range_title: value
        });
        if(value == '校内地点') {
            this.setData({
                edit_range_value: this.marco.INSIDE_CAMPUS,
            })
        }else {
            this.setData({
                edit_range_value: this.marco.OUTSIDE_CAMPUS,
            })
        }
        Toast.success('设置成功');
        console.log(this.data.edit_range_value);            
    },

    editPlaceType: function(event) {
        const { value, index } = event.detail;
        this.setData({
            edit_place_type: index + 1,
            place_type_title: value
        });
        Toast.success('设置成功');
        console.log(this.data.edit_place_type);
    },

    cancelPlaceRange: function() {
        this.setData({
            edit_range_value: 0,
            place_range_title: this.marco.DEFAULT_RANGE_TITLE,
        });
        Toast.fail('请重新选择');
    },

    cancelPlaceType: function() {
        this.setData({
            edit_place_type: this.marco.DEFAULT_TYPE_TITLE,
            place_type_title: this.marco.DEFAULT_TYPE_TITLE
        });
        Toast.fail('请重新选择');        
    },

    submitNewContent: function() {
        Dialog.confirm({
            title: '确认提交？',
            message: '请仔细检查所填信息是否真实有效，多次提交无用的内容会浪费他人的时间，并可能导致您的账号信用受到影响。',
          }).then(() => {
              // on confirm
              let tmp_place_name = this.data.edit_place_name;
              let tmp_place_position = this.data.edit_place_position;
              let tmp_opening_hours = this.data.edit_opening_hours;
              if(tmp_place_name == '' || tmp_place_position == '' || tmp_opening_hours == '') {
                  Toast.fail('缺少关键内容');
                  return;
              }
              let tmp_range_value = this.data.edit_range_value;
              let tmp_place_type = this.data.edit_place_type;
              if(tmp_range_value === 0 || tmp_place_type === 0) {
                  Toast.fail('缺少关键内容');
                  return;
              } 

              const app = getApp();
              
              wx.request({
                url: app.global_data.global_domain + '/api/v1.0/add_item',
                method: 'POST',
                data: {
                    "mask": app.global_data.global_user_token,
                    "class": 3, 
                    "info": {
                        "name": this.data.edit_place_name,
                        "position": this.data.edit_place_position,
                        "hours": this.data.edit_opening_hours,
                        "scope": this.data.edit_range_value,
                        "type": this.data.edit_place_type, 
                  }                  
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
                  if(rtn.status == 2) {
                      Toast.success('请等待审核');
                  }else {
                      Toast.fail('发布失败');
                  }
                },
                fail: (error) => {
                    console.log(error);
                    Toast.fail('发布失败');
                },
                complete: (res) => {},
              })  
            }).catch(() => {
              // on cancel
            });
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