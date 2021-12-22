import Toast from '@vant/weapp/toast/toast';
import Dialog from '@vant/weapp/dialog/dialog';
import Notify from '@vant/weapp/notify/notify';


Page({
    data: {
        type: [
            { text: '全部课程', value: 0 },
            { text: '专业课', value: 1 },
            { text: '数理课', value: 2 },
            { text: '外文课', value: 3 },
            { text: '实验课', value: 4 },
            { text: '体育课', value: 5 },
            { text: '思政课', value: 6 },
            { text: '文核课', value: 7 },
            { text: '文素课', value: 8 },
            { text: '实践课', value: 9 },
        ],

        department: [
            { text: '任意院系', value: 0 },
            { text: '车辆学院', value: 1 },
            { text: '材料学院', value: 2 },
            { text: '电机系', value: 3 },
            { text: '电子系', value: 4 },
            { text: '法学院', value: 5 },
            { text: '工物系', value: 6 },
            { text: '公管学院', value: 7 },
            { text: '工业工程系', value: 8 },
            { text: '航院', value: 9 },
            { text: '化学系', value: 10 },
            { text: '化工系', value: 11 },
            { text: '环境学院', value: 12 },
            { text: '机械系', value: 13 },
            { text: '经管学院', value: 14 },
            { text: '金融学院', value: 15 },
            { text: '建筑学院', value: 16 },
            { text: '计算机系', value: 17 },
            { text: '交叉信息院', value: 18 },
            { text: '集成电路学院', value: 19 },
            { text: '美术学院', value: 20 },
            { text: '马克思主义学院', value: 21 },
            { text: '能动系', value: 22 },
            { text: '求真书院', value: 23 },
            { text: '清华-伯克利深圳学院', value: 24 },
            { text: '日新书院', value: 25 },
            { text: '软件学院', value: 26 },
            { text: '人文学院', value: 27 },
            { text: '数学系', value: 28 },
            { text: '水利系', value: 29 },
            { text: '社科学院', value: 30 },
            { text: '生命学院', value: 31 },
            { text: '苏世民书院', value: 32 },
            { text: '土木系', value: 33 },
            { text: '体育部', value: 34 },
            { text: '土水学院', value: 35 },
            { text: '外文系', value: 36 },
            { text: '物理系', value: 37 },
            { text: '未央书院', value: 38 },
            { text: '新雅书院', value: 39 },
            { text: '行健书院', value: 40 },
            { text: '新闻学院', value: 41 },
            { text: '训练中心', value: 42 },
            { text: '医学院', value: 43 },
            { text: '药学院', value: 44 },
            { text: '语言中心', value: 45 },
            { text: '艺教中心', value: 46 },
            { text: '致理书院', value: 47 },
            { text: '自动化系', value: 48 },
            { text: '其他开课单位', value: 49 },
        ],

        order: [
            { text: '评分排序', value: 0 },
            { text: '热度排序', value: 1 },
            { text: '时间排序', value: 2 },
        ],

        image_url: "https://learn.tsinghua.edu.cn/b/wlxt/kc/v_kcxx_jskcxx/teacher/showImageById?wlkcid=2021-2022-1142764790&_csrf=d39592c7-bbb0-416a-affb-a39b1ab00ba4",

        init_flag: true,
        type_table: [],
        department_table: [],
        schedule_table: ['春季学期', '夏季学期', '秋季学期', '春、秋季学期'],
        color_table: ['', '#228B22', '#000000', '#FFA500', '#8B4513', '#9400D3', '#DC143C', '#0000FF', '#FF1493', '#D8BFD8'],

        search_value: '',
        type_value: 0,
        department_value: 0,
        order_value: 0,

        edit_course_name: '',
        edit_course_teacher: '',
        edit_course_credit: 0,
        edit_course_schedule: 0,
        edit_course_type: 0,
        edit_course_department: 0,
        course_schedule_title: '开课时间',
        course_type_title: '课程类型',
        course_department_title: '开课院系',

        total_pages: 0,
        current_page: 0,
        show_popup: false,
        
        courses_list: [],
    },

    marco: {
        PAGE_CAPACITY: 8,
        DEFAULT_SCHEDULE_TITLE: '开课时间',
        DEFAULT_TYPE_TITLE: '课程类型',
        DEFAULT_DEPARTMENT_TITLE: '开课院系',
    },

    onLoad: function () {
        this.getCourseList();
    },

    onReachBottom: function () {
        if(this.data.current_page >= this.data.total_pages) {
            console.log("已无下一页数据");
        }else {
            this.setData({
                current_page: this.data.current_page + 1
            })
            this.getCourseList();
        }
    },

    getCourseList: function() {
        const app = getApp();
        let begin = this.data.current_page * this.marco.PAGE_CAPACITY;
        let end = begin + this.marco.PAGE_CAPACITY - 1;

        wx.request({
          url: app.global_data.global_domain + '/api/v1.0/get_courses_list',
          method: 'POST',  
          data: {
              begin: begin,
              end: end,
              like: this.data.search_value,
              course_type: this.data.type_value,
              course_department: this.data.department_value,
              course_order: this.data.order_value
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
              let array_length = rtn.courses.length;
              for(let i = 0; i < array_length; i ++) {
                  let tmp_type_value = rtn.courses[i].type;
                  let tmp_department_value = rtn.courses[i].department;
                  rtn.courses[i].color = this.data.color_table[tmp_type_value];
                  rtn.courses[i].type = this.data.type[tmp_type_value].text;
                  rtn.courses[i].department = this.data.department[tmp_department_value].text;
              }
              this.data.courses_list.push.apply(this.data.courses_list, rtn.courses);
              this.data.total_pages = Math.ceil(rtn.total_courses / this.marco.PAGE_CAPACITY) - 1;
              this.setData({
                  courses_list: this.data.courses_list,
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
            courses_list: [],
            search_value: result.detail
        });
        this.getCourseList();
    },

    typeSelected: function(result) {
        this.setData({
            current_page: 0,
            courses_list: [],
            type_value: result.detail,
        });      
        this.getCourseList();  
    },

    departmentSelected: function(result) {
        this.setData({
            current_page: 0,
            courses_list: [],
            department_value: result.detail
        });     
        this.getCourseList();  
    },

    orderSelected: function(result) {
        this.setData({
            current_page: 0,
            courses_list: [],
            order_value: result.detail
        });
        this.getCourseList();  
    },

    viewCourseItem: function(event) {
        let index = event.currentTarget.dataset.index;
        let content = JSON.stringify(this.data.courses_list[index]);
        wx.navigateTo({
          url: '../course_item/course_item?content=' + content,
        })
    },

    showPopup: function() {
        if(this.data.init_flag) {
            let tmp_type_table = [...this.data.type];
            let tmp_department_table = [...this.data.department];
            
            tmp_type_table.shift();
            tmp_department_table.shift();

            this.setData({
                init_flag: false,
                type_table: tmp_type_table,
                department_table: tmp_department_table,
            })
        }

        this.setData({
            show_popup: true,
        })
    },

    closePopup: function() {
        this.setData({
            show_popup: false
        });
    },

    editCourseNameTips: function() {
        Notify({ type: 'primary', message: '请尽量与info信息保持一致' });
    },

    editCourseTeacherTips: function() {
        Notify({ type: 'primary', message: '合开课程只需填写主讲教师' });
    },

    editCourseSchedule: function(event) {
        const { value, index } = event.detail;
        this.setData({
            edit_course_schedule: index + 1,
            course_schedule_title: value
        });
        Toast.success('设置成功');
        console.log(this.data.edit_course_schedule);        
    },

    editCourseType: function(event) {
        const { value, index } = event.detail;
        this.setData({
            edit_course_type: index + 1,
            course_type_title: value.text,
        });
        Toast.success('设置成功');
        console.log(this.data.edit_course_type);
    },

    editCourseDepartment: function(event) {
        const { value, index } = event.detail;
        this.setData({
            edit_course_department: index + 1,
            course_department_title: value.text,
        });
        Toast.success('设置成功');
        console.log(this.data.edit_course_department);
    },

    cancelEditSchedule: function() {
        this.setData({
            edit_course_schedule: 0,
            course_schedule_title: this.marco.DEFAULT_SCHEDULE_TITLE
        });
        Toast.fail('请重新选择');
    },

    cancelEditType: function() {
        this.setData({
            edit_course_type: 0,
            course_type_title: this.marco.DEFAULT_TYPE_TITLE
        });
        Toast.fail('请重新选择');
    },

    cancelEditDepartment: function() {
        this.setData({
            edit_course_department: 0,
            course_department_title: this.marco.DEFAULT_DEPARTMENT_TITLE
        });
        Toast.fail('请重新选择');        
    },

    submitNewContent: function() {
        Dialog.confirm({
            title: '确认提交？',
            message: '请仔细检查所填信息是否真实有效，多次提交无用的内容会浪费他人的时间，并可能导致您的账号信用受到影响。',
        }).then(() => {
            // on confirm
            let tmp_course_name = this.data.edit_course_name;
            let tmp_course_teacher = this.data.edit_course_teacher;
            if(tmp_course_name == '' || tmp_course_teacher == '') {
                Toast.fail('缺少关键内容');
                return;
            }
            let tmp_course_schedule = this.data.edit_course_schedule;
            let tmp_course_type = this.data.edit_course_type;
            let tmp_course_department = this.data.edit_course_department;
            if(tmp_course_schedule == 0 || tmp_course_type == 0 || tmp_course_department == 0) {
                Toast.fail('缺少关键内容');
                return;
            }

            const app = getApp();
            
            wx.request({
              url: app.global_data.global_domain + '/api/v1.0/add_item',
              method: 'POST',
              data: {
                  "mask": app.global_data.global_user_token,
                  "class": 1, 
                  "info": {
                      "name": this.data.edit_course_name,
                      "teacher": this.data.edit_course_teacher,
                      "credit": this.data.edit_course_credit,
                      "schedule": this.data.edit_course_schedule,
                      "type": this.data.edit_course_type,
                      "department": this.data.edit_course_department 
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