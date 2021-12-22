// app.js
App({
  global_data: {
    global_domain: 'https://thurec.xyz',
    global_user_token: "", // user login token
  },
  logout: function(){
    this.global_user_token = ""
  }
});