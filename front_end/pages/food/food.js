import Toast from '@vant/weapp/toast/toast';
import Dialog from '@vant/weapp/dialog/dialog';


Page({
    data: {
        range_type: [
            { text: '全部餐饮', value: 0 },
            { text: '校内餐饮', value: 1 },
            { text: '校外餐饮', value: 2 },
        ],
        food_type: [
            { text: '任意类型', value: 0 },
        ],
        rank_type: [
            { text: '评分排序', value: 0 },
            { text: '热度排序', value: 1 },
            { text: '时间排序', value: 2 },
        ],

        range_for_create: ['校内餐饮', '校外餐饮'],
        outside_type_for_create: ['汉堡披萨','龙虾烧烤','香锅火锅','米线拉面','日韩料理','简餐便当','各类饮品',],
        inside_type_for_create: ['家园','甲所','寓园','融园','澜园','荷园','北园','南园','桃李园','紫荆园','清芬园','听涛园','观畴园','玉树园','芝兰园','丁香园','熙春园','清真食堂',],

        search_value: '',
        range_value: 0,
        food_value: 0,
        rank_value: 0,
        uncertain_range: true,

        edit_food_name: '',
        edit_food_position: '',
        edit_business_hours: '',

        edit_range_value: 0,
        edit_food_type: '',

        food_range_title: '选择范围',
        food_type_title: '选择类型',

        image_url: "https://z3.ax1x.com/2021/12/03/odK6aD.jpg",

        current_page: 0,
        total_pages: 0,
        show_popup: false,

        food_list: [
            { id: 1, name: '汉堡王', position: '海淀区华清嘉园7号楼', range: '校外餐饮', type: '汉堡披萨', star: 4.0, score: 8.3, tag: 'TOP15', color: '#FF976A'}, 
            { id: 2, name: '李先生牛肉面大王', position: '海淀区双清苑1号楼', range: '校外餐饮', type: '米线拉面', star: 4.0, score: 8.0, tag: '', color: '#EE0A24'},             
        ]
    },

    marco: {
        PAGE_CAPACITY: 8,
        INSIDE_CAMPUS: 1,
        OUTSIDE_CAMPUS: 2,

        DEFAULT_RANGE_TITLE: '选择范围',
        DEFAULT_TYPE_TITLE: '选择类型',
    },

    onSearch: function(result) {
        this.setData({
            search_value: result.detail
        });
    },

    closePopup: function() {
        this.setData({
            show_popup: false
        });
    },

    publishRecommendation: function() {
        this.setData({
            show_popup: true
        })
    },

    editFoodRange: function(event) {
        const { value } = event.detail;
        this.setData({
            edit_food_range: value,
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
        console.log(this.data.edit_food_type);
    },

    editFoodType: function(event) {
        const { value } = event.detail;
        this.setData({
            edit_food_type: value,
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
              if(tmp_range_value == 0 || tmp_food_type == this.marco.DEFAULT_TYPE_TITLE) {
                Toast.fail('缺少关键内容');
                return;
            }              
            }).catch(() => {
              // on cancel
            });
    },

    rangeSelected: function(result) {
        this.setData({
            range_value: result.detail
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
                food_type: inside_food_type
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
                food_type: outside_food_type
            });   
        }else {
            let default_food_type = [
                { text: '任意类型', value: 0 },
            ];
            this.setData({
                uncertain_range: true,
                food_type: default_food_type
            });   
        }
    },

    viewFoodItem: function() {
        wx.navigateTo({
          url: '../food_item/food_item',
        })
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
        
    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})