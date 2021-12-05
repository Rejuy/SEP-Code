from app import createApp


app = createApp()

#TODO
#研究flask蓝图模块，重新调整目录结构
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

