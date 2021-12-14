// app.js
App({
  global_data: {
    global_domain: 'https://thurec.xyz',
    global_user_token: "c+O9LCj7q77CfNc7yH3ZEg==", // user login token
  },
  logout: function(){
    this.global_user_token = ""
  }
});