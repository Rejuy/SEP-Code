Page({
    data: {
        loading: true,
        user_icon_path: "",
        collection_list: [],
        num_collection: 0,

        loading: true,
    },
    back: function () {
        wx.reLaunch({
            url: '/pages/user/user',
        })
    },

    onReady: function () {
        const app = getApp();
        wx.request({
            url: app.global_data.global_domain + '/api/v1.0/get_user_favorites',
            data: {
                mask: app.global_data.global_user_token
            },
            method: "POST",
            success: (res) => {
                const type = [,"课程","餐饮","出行"]
                const url = [,"/images/icons/course.png","/images/icons/food.png","/images/icons/place.png"]
                this.setData({
                    collection_list: res.data.favorites.map((v)=>({...v, desc:type[v.class], url:url[v.class]})),
                    loading: false
                });
            }
        })
    }
})