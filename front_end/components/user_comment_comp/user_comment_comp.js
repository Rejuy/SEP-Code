Component({
  properties: {
    user: String, // url link
    user_icon: String, // url link
    title: String,
    text: String, // 评论
    rate: Number, // rating
    likes: Number,
    "imageurls": Array,
    is_self: Boolean, // 评论是自己的?
  },
  data: {
    tag: "",
    show_text: "",
    show_imageurls: [],
    show_all: false,

    brief_max_text_size: 50, //const
    brief_max_img_len: 1, //const

    text_length: 0,
    image_num: 0,
    show_hide_button: false,
  },
  methods: {
    show_hide: function () {
      if (!this.data.show_all) {
        // show all now
        this.setData({
          show_text: this.properties.text,
          show_imageurls: this.properties.imageurls,
        })
      } else {
        this.setData({
          show_text: this.properties.text.substring(0, this.data.brief_max_text_size),
          show_imageurls: this.properties.imageurls.slice(0, this.data.brief_max_img_len),
        })
      }
      this.setData({
        show_all: !this.data.show_all
      })
    }
  },
  lifetimes: {
    ready() {
      if (this.properties.is_self) {
        this.setData({
          tag: "自己",
        })
      }
      this.setData({
        show_text: this.properties.text.substring(0, this.data.brief_max_text_size),
        show_imageurls: this.properties.imageurls.slice(0, this.data.brief_max_img_len),
        text_length: this.properties.text.length,
        image_num: this.properties.imageurls.length,
        show_hide_button: (this.properties.text.length > this.data.brief_max_text_size) || (this.properties.imageurls.length > this.data.brief_max_img_len)
      })
    }
  }
})