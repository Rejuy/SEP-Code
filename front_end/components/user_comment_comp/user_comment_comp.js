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
          tag:"自己",
          text: "Description dksfjlaksdjflk sajdfklsaj dlfasjdflkdsajflkasjflkasjd sakd fa skjf alks jflksaj dflkdsjf lsakd ksdjf salkjdfkls jdlkasjdlkfjsd lkfsjl sjkdflksaj flksajdflksjdflkasjldkfjslkdfdk jsak fksjlaksdjskjdf al lk dfjla jsljlk. ksadjflksadjlfk jaklds jflksaj dflksdajf lksadjfklsajdflksjdflksjdflksjdflksjdflksjdflkj lfksjdlkf jlskdjf lksa jf lkdjf lkj lkj fslkdfsajlkdfsajsdf lkj fsalsf l."
        })
      }
    }
  }
})