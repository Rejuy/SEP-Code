import Toast from '@vant/weapp/toast/toast';
import Dialog from '@vant/weapp/dialog/dialog';
import Notify from '@vant/weapp/notify/notify';


Page({
    data: {
        range: [
            { text: '全部餐饮', value: 0 },
            { text: '校内餐饮', value: 1 },
            { text: '校外餐饮', value: 2 },
        ],
        
        type: [
            { text: '任意类型', value: 0 },
        ],

        order: [
            { text: '评分排序', value: 0 },
            { text: '热度排序', value: 1 },
            { text: '时间排序', value: 2 },
        ],

        range_table: ['校内餐饮', '校外餐饮'],
        outside_type_table: ['汉堡披萨','龙虾烧烤','香锅火锅','米线拉面','日韩料理','简餐便当','各类饮品',],
        outside_color_table: ['#FF976A', '#8A2BE2','#FF0000','#696969','#800000','#DAA520','#FF00FF',],
        inside_type_table: ['家园','甲所','寓园','融园','澜园','荷园','北园','南园','桃李园','紫荆园','清芬园','听涛园','观畴园','玉树园','芝兰园','丁香园','熙春园','清真食堂',],
        image_table: ["https://inews.gtimg.com/newsapp_bt/0/13750087100/1000", "https://z3.ax1x.com/2021/12/03/odK6aD.jpg"],

        search_value: '',
        range_value: 0,
        type_value: 0,
        order_value: 0,
        uncertain_range: true,

        edit_food_name: '',
        edit_food_position: '',
        edit_business_hours: '',
        edit_range_value: 0,
        edit_food_type: 0,
        food_range_title: '选择范围',
        food_type_title: '选择类型',

        total_pages: 0,
        current_page: 0,
        show_popup: false,

        food_list: []
    },

    marco: {
        PAGE_CAPACITY: 8,
        INSIDE_CAMPUS: 1,
        OUTSIDE_CAMPUS: 2,

        THU_PURPLE: '#82318E',
        DEFAULT_RANGE_TITLE: '选择范围',
        DEFAULT_TYPE_TITLE: '选择类型',
    },

    onLoad: function () {
        this.getFoodList();
    },

    onReachBottom: function () {
        if(this.data.current_page >= this.data.total_pages) {
            console.log("已无下一页数据");
        }else {
            this.setData({
                current_page: this.data.current_page + 1
            })
            this.getFoodList();
        }
    },

    getFoodList: function() {
        const app = getApp();
        let begin = this.data.current_page * this.marco.PAGE_CAPACITY;
        let end = begin + this.marco.PAGE_CAPACITY - 1;

        wx.request({
          url: app.global_data.global_domain + '/api/v1.0/get_food_list',
          method: 'POST',  
          data: {
              begin: begin,
              end: end,
              like: this.data.search_value,
              food_scope: this.data.range_value,
              food_type: this.data.type_value,
              food_order: this.data.order_value
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
              let array_length = rtn.food.length;
              for(let i = 0; i < array_length; i ++) {
                  let tmp_range_value = rtn.food[i].scope;
                  let tmp_type_value = rtn.food[i].type - 1;

                  if(tmp_range_value == 1) {
                      rtn.food[i].color = this.marco.THU_PURPLE;
                      rtn.food[i].type = this.data.inside_type_table[tmp_type_value];
                  }else {
                      rtn.food[i].color = this.data.outside_color_table[tmp_type_value];
                      rtn.food[i].type = this.data.outside_type_table[tmp_type_value];
                  }
                  rtn.food[i].range = this.data.range_table[tmp_range_value - 1];
                  rtn.food[i].image = this.data.image_table[tmp_range_value - 1];
              }
              this.data.food_list.push.apply(this.data.food_list, rtn.food);
              this.data.total_pages = Math.ceil(rtn.total_food / this.marco.PAGE_CAPACITY) - 1;
              this.setData({
                  food_list: this.data.food_list,
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
            food_list: [],
            search_value: result.detail
        });
        this.getFoodList();
    },

    rangeSelected: function(result) {
        this.setData({
            current_page: 0,
            food_list: [],
            range_value: result.detail,
        });
        let tmp_value = this.data.range_value;
        if(tmp_value == this.marco.INSIDE_CAMPUS) {
            let inside_food_type = [
                { text: '任意食堂', value: 0 },
                { text: '家园', value: 1 },
                { text: '甲所', value: 2 },
                { text: '寓园', value: 3 },
                { text: '融园', value: 4 },
                { text: '澜园', value: 5 },
                { text: '荷园', value: 6 },
                { text: '北园', value: 7 },
                { text: '南园', value: 8 },
                { text: '桃李园', value: 9 },
                { text: '紫荆园', value: 10 },
                { text: '清芬园', value: 11 },
                { text: '听涛园', value: 12 },
                { text: '观畴园', value: 13 },
                { text: '玉树园', value: 14 },
                { text: '芝兰园', value: 15 },
                { text: '丁香园', value: 16 },
                { text: '熙春园', value: 17 },
                { text: '清真食堂', value: 18 },
            ];
            this.setData({
                uncertain_range: false,
                type: inside_food_type,
            });            
        }else if(tmp_value == this.marco.OUTSIDE_CAMPUS) {
            let outside_food_type = [
                { text: '任意类型', value: 0 },
                { text: '汉堡披萨', value: 1 },
                { text: '龙虾烧烤', value: 2 },
                { text: '香锅火锅', value: 3 },
                { text: '米线拉面', value: 4 },
                { text: '日韩料理', value: 5 },
                { text: '简餐便当', value: 6 },
                { text: '各类饮品', value: 7 },
            ];
            this.setData({
                uncertain_range: false,
                type: outside_food_type,
            });   
        }else {
            let default_food_type = [
                { text: '任意类型', value: 0 },
            ];
            this.setData({
                uncertain_range: true,
                type: default_food_type,
            });   
        }
        this.getFoodList();
    },

    typeSelected: function(result) {
        this.setData({
            current_page: 0,
            food_list: [],
            type_value: result.detail,
        });      
        this.getFoodList();
    },    

    orderSelected: function(result) {
        this.setData({
            current_page: 0,
            food_list: [],
            order_value: result.detail,
        });   
        this.getFoodList();   
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

    editFoodNameTips: function() {
        Notify({ type: 'primary', message: '必要时可以简写' });
    },

    editFoodPositionTips: function() {
        Notify({ type: 'primary', message: '校内餐饮注明大概方位即可' });
    },

    editFoodHoursTips: function() {
        Notify({ type: 'primary', message: '标准格式： 08:00 - 23:00' });
    },

    editFoodRange: function(event) {
        const { value } = event.detail;
        this.setData({
            food_range_title: value
        });
        if(value == '校内餐饮') {
            this.setData({
                edit_range_value: this.marco.INSIDE_CAMPUS,
                food_type_title: this.marco.DEFAULT_TYPE_TITLE
            })
        }else {
            this.setData({
                edit_range_value: this.marco.OUTSIDE_CAMPUS,
                food_type_title: this.marco.DEFAULT_TYPE_TITLE
            })
        }
        Toast.success('设置成功');
        console.log(this.data.edit_range_value);
    },

    editFoodType: function(event) {
        const { value, index } = event.detail;
        this.setData({
            edit_food_type: index + 1,
            food_type_title: value
        });
        Toast.success('设置成功');
        console.log(this.data.edit_food_type);
    },

    cancelFoodRange: function() {
        this.setData({
            edit_range_value: 0,
            edit_food_type: this.marco.DEFAULT_TYPE_TITLE,
            food_range_title: this.marco.DEFAULT_RANGE_TITLE,
        });
        Toast.fail('请重新选择');
    },

    cancelFoodType: function() {
        this.setData({
            edit_food_type: this.marco.DEFAULT_TYPE_TITLE,
            food_type_title: this.marco.DEFAULT_TYPE_TITLE
        });
        Toast.fail('请重新选择');        
    },

    submitNewContent: function() {
        Dialog.confirm({
            title: '确认提交？',
            message: '请仔细检查所填信息是否真实有效，多次提交无用的内容会浪费他人的时间，并可能导致您的账号信用受到影响。',
          }).then(() => {
              // on confirm
              let tmp_food_name = this.data.edit_food_name;
              let tmp_food_position = this.data.edit_food_position;
              let tmp_business_hours = this.data.edit_business_hours;
              if(tmp_food_name == '' || tmp_food_position == '' || tmp_business_hours == '') {
                  Toast.fail('缺少关键内容');
                  return;
              }
              let tmp_range_value = this.data.edit_range_value;
              let tmp_food_type = this.data.edit_food_type;
              if(tmp_range_value === 0 || tmp_food_type === 0) {
                Toast.fail('缺少关键内容');
                return;
              }

              const app = getApp();
              
              wx.request({
                url: app.global_data.global_domain + '/api/v1.0/add_item',
                method: 'POST',
                data: {
                    "mask": app.global_data.global_user_token,
                    "class": 2, 
                    "info": {
                        "name": this.data.edit_food_name,
                        "position": this.data.edit_food_position,
                        "hours": this.data.edit_business_hours,
                        "scope": this.data.edit_range_value,
                        "type": this.data.edit_food_type, 
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

    viewFoodItem: function(event) {
        let index = event.currentTarget.dataset.index;
        let content = JSON.stringify(this.data.food_list[index]);
        wx.navigateTo({
          url: '../food_item/food_item?content=' + encodeURIComponent(content),
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