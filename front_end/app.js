// app.js
App({
  global_data: {
    global_domain: 'https://thurec.whiteffire.cn',
    global_user_token: "", // user login token
    /*
    global_user_info: { // sample user info, dont use
      username: "Andrew",
      email: "adr",
      like_count: 2,
      account_birth: "Sun 14, Nov 2021 12:07:44 GMT",
      collection_count: 3,
      content_count: 4,
      comment_count: 5,
    }
    */
  },
  logout: function(){
    app.global_user_token = ""
  }
});