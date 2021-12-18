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

        search_value: '',
        range_value: 0,
        type_value: 0,
        order_value: 0,

        edit_place_name: '',
        edit_place_position: '',
        edit_opening_hours: '',
        edit_range_value: 0,
        edit_place_type: '',
        place_range_title: '选择范围',
        place_type_title: '选择类型',

        current_page: 0,
        total_pages: 0,
        show_popup: false,

        place_list: [
            { id: 1, name: '第一教室楼', position: '清华大学西南方向', range: '校内地点', type: '自习场所', star: 4.0, score: 8.3, tag: 'TOP3', color: '#07C160'},    
            { id: 2, name: '邺架轩', position: '清华大学李文正图书馆下沉广场', range: '校内地点', type: '自习场所', star: 3.5, score: 7.2, tag: '', color: '#07C160'},        
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
        const { value } = event.detail;
        this.setData({
            edit_place_type: value,
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
              if(tmp_range_value == 0 || tmp_place_type == this.marco.DEFAULT_TYPE_TITLE) {
                Toast.fail('缺少关键内容');
                return;
            }              
            }).catch(() => {
              // on cancel
            });
    },

    onLoad: function (options) {

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

    // 页面上拉触底事件的处理函数
    onReachBottom: function () {

    },

    // 用户点击右上角分享
    onShareAppMessage: function () {

    }
})