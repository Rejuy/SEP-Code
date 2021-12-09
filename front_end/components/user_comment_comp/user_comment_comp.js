Component({
  properties:{
    user: String, // url link
    user_icon: String, // url link
    text: String, // 评论
    "imageurls": Array, 
    is_self: Boolean, // 评论是自己的?
  },
  data:{
    tag: ""
  },
  lifetimes: {
    ready(){
      if (this.properties.is_self){
        this.setData({
          tag:"自己"
        })
      }
    }
  }
})