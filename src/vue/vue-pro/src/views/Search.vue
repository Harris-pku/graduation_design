<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- <router-view/> -->
    <el-container>
      <div class="wrap">
        <div class="ms-login">
          <!-- <div class="ms-title">CSDN问答帖分类与检索系统</div> -->
            <el-button type="primary" icon="el-icon-search" style="width: 100px; float: right; margin-top: 10px; margin-left: 8px" @click="handleSearch()">搜索</el-button>
            <el-col :span="3" style="margin-left: 20px; margin-top: 10px; width: 515px;">
              <el-input v-model="searchInput" placeholder="请输入你要搜索的内容…"></el-input>
            </el-col>

            <!-- <el-main>
              <div class="comment_left" style="background-color: #EBEEF5;">
                  <el-container direction="vertical">
                      <el-container width=100%>
                          <p class="text" style="font-size: 20px; margin-top: 20px; margin-left: 25px;">
                            <b>标题：系统界面的代码及运行界面</b>
                          </p>
                      </el-container>
                  </el-container>
              </div>
              <div class="comment_left" style="background-color: #EBEEF5;">
                <el-container direction="vertical">
                    <el-container width=100%>
                        <p class="text" style="font-size: 15px; margin-left: 25px;">
                          <b>正文：</b>设计程序围绕餐厅点餐系统的功能完成以下内容:程序运行后输出显示预约点餐的相关信息，包括点餐系统名称、店地址等，要求用结构体实现。系统名称:XXXX。饭店名:XXXx。饭店地址:XXX。用餐人数: XXXX。预约人姓名: XXXX 预定包厢名首字母:XXX。
                        </p>
                    </el-container>
                    <el-button type="success" plain style="width: 130px; float: right; margin-bottom: 10px; margin-left: 15px">类别：Review</el-button>
                </el-container>
              </div>
            </el-main>

            <el-main>
              <div class="comment_left" style="background-color: #EBEEF5;">
                  <el-container direction="vertical">
                      <el-container width=100%>
                          <p class="text" style="font-size: 20px; margin-top: 20px; margin-left: 25px;">
                            <b>标题：Excel pandas，无法进行 merge</b>
                          </p>
                      </el-container>
                  </el-container>
              </div>
              <div class="comment_left" style="background-color: #EBEEF5;">
                <el-container direction="vertical">
                    <el-container width=100%>
                        <p class="text" style="font-size: 15px; margin-left: 25px;">
                          <b>正文：</b>Excel pandas导入 分列每一列数据后，截取两列数据，为啥有一列数据是为浮点数据，无法进行merge
                        </p>
                    </el-container>
                    <el-button type="success" plain style="width: 130px; float: right; margin-bottom: 10px; margin-left: 15px">类别：API use</el-button>
                </el-container>
              </div>
            </el-main>

            <el-main>
              <div class="comment_left" style="background-color: #EBEEF5;">
                  <el-container direction="vertical">
                      <el-container width=100%>
                          <p class="text" style="font-size: 20px; margin-top: 20px; margin-left: 25px;">
                            <b>标题：java下载文件时，没有文件路径怎么下载？</b>
                          </p>
                      </el-container>
                  </el-container>
              </div>
              <div class="comment_left" style="background-color: #EBEEF5;">
                <el-container direction="vertical">
                    <el-container width=100%>
                        <p class="text" style="font-size: 15px; margin-left: 25px;">
                          <b>正文：</b>常用的下载都是如下方式，先读到输入流，然后再输出到本地。InputStream fis = new BufferedInputStream(new FileInputStream(path)); 现在我是通过将html格式转换，直接生成了一个File file，这样就没有文件路径，要怎么把这个file下载下来或者保存到服务器？
                        </p>
                    </el-container>
                    <el-button type="success" plain style="width: 130px; float: right; margin-bottom: 10px; margin-left: 15px">类别：Review</el-button>
                </el-container>
              </div>
            </el-main> -->
            <el-main>
              
            </el-main>

            <el-main>
              <div class="comment_left" style="background-color: #EBEEF5;">
                  <el-container direction="vertical">
                      <el-container width=100%>
                          <p class="text" style="font-size: 20px; margin-top: 20px; margin-left: 25px;">
                            <b>标题：C/C++ 库函数strcpy的使用问题</b>
                          </p>
                      </el-container>
                  </el-container>
              </div>
              <div class="comment_left" style="background-color: #EBEEF5;">
                <el-container direction="vertical">
                    <el-container width=100%>
                        <p class="text" style="font-size: 15px; margin-left: 25px;">
                          <b>正文：</b>近来，在strcpy的使用中发现了一个很难想清楚的问题。鄙人水平不足，还请大佬们指点。问题：我想问一下为什么下面这串代码q[0]与q[1]的交换不能使用strcpy（下面注释掉的代码），q[0]和q[1]指向的不就是那两个字符串吗？难道是字符串的地址？可字符串的内容不就是字符串的地址吗？
                        </p>
                    </el-container>
                    <el-button type="success" plain style="width: 130px; float: right; margin-bottom: 10px; margin-left: 15px">类别：Review</el-button>
                </el-container>
              </div>
            </el-main>

            <el-main>
              <div class="comment_left" style="background-color: #EBEEF5;">
                  <el-container direction="vertical">
                      <el-container width=100%>
                          <p class="text" style="font-size: 20px; margin-top: 20px; margin-left: 25px;">
                            <b>标题：c语言strncpy函数的使用</b>
                          </p>
                      </el-container>
                  </el-container>
              </div>
              <div class="comment_left" style="background-color: #EBEEF5;">
                <el-container direction="vertical">
                    <el-container width=100%>
                        <p class="text" style="font-size: 15px; margin-left: 25px;">
                          <b>正文：</b>在visual stdio2013中不能使用strncpy函数，说是应该用strcpy_s。 strncpy_s(&q_StrGameBack[q_arrSanke[i][0]][q_arrSanke[i][1]],&m, 2);可是我调用的时候总是提示调用参数太少，查了下函数原型，我应该是缺少了_In_ rsize_t _SizeInBytes这个参数，可是这个参数该怎么填啊，求哪位大神给我解答下，谢谢了
                        </p>
                    </el-container>
                    <el-button type="success" plain style="width: 130px; float: right; margin-bottom: 10px; margin-left: 15px">类别：API use</el-button>
                </el-container>
              </div>
            </el-main>

            <el-main>
              <div class="comment_left" style="background-color: #EBEEF5;">
                  <el-container direction="vertical">
                      <el-container width=100%>
                          <p class="text" style="font-size: 20px; margin-top: 20px; margin-left: 25px;">
                            <b>标题：关于C语言strcpy函数问题</b>
                          </p>
                      </el-container>
                  </el-container>
              </div>
              <div class="comment_left" style="background-color: #EBEEF5;">
                <el-container direction="vertical">
                    <el-container width=100%>
                        <p class="text" style="font-size: 15px; margin-left: 25px;">
                          <b>正文：</b>这个代码是直接照着c primer plus第五版 上面的程序写的了，但是运行起来还是有错误，主要问题是strcpy这个函数，下面是报错信息
                        </p>
                    </el-container>
                    <el-button type="success" plain style="width: 130px; float: right; margin-bottom: 10px; margin-left: 15px">类别：Error</el-button>
                </el-container>
              </div>
            </el-main>

        </div>

        <el-aside width="180px">
          <div class="mySimpleInfo"> </div>
          <template scope="scope">
            <el-button class="button_outside" type="primary" icon="el-icon-s-home" @click="handleHome">首页</el-button><br>
            <el-button class="button_outside" type="primary" icon="el-icon-search" @click="handleSelect">搜索</el-button><br>
            <el-button class="button_outside" type="primary" icon="el-icon-info" @click="handleAbout">关于</el-button>
            <el-button class="button_outside" type="primary" icon="el-icon-question" @click="handleHelp">帮助</el-button><br>
          </template>
        </el-aside>
        
        

      </div>
    </el-container>
  </div>
</template>

<script> 
export default {
  // name: 'App',
  // data() {
  //   return {
  //       activeIndex: '/index',
  //   };
  // },
  methods: {
      handleHome() {
          // window.location.href = 'www.baidu.com';
          console.log(222);
          this.$router.push('/home');
          console.log(this.$router);
      },
      handleSelect() {
          console.log(333);
          // window.location.href = 'https://www.baidu.com';
          this.$router.push('/search');
      },
      handleAbout() {
          // console.log(key, keyPath);
          // window.location.href = 'https://www.baidu.com';
          this.$router.push('/about');
      },
      handleHelp() {
          // console.log(key, keyPath);
          // window.location.href = 'https://www.baidu.com';
          this.$router.push('/help');
      }
  }
}
</script>

<style>
#app,
/* {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
.text {
    font-family: Times;
}
.comment_left {
    background-color: #DCDFE6;
        /* border-radius: 6px; */
        /* margin: 8px; */
    /* margin-left: 20px; */
    direction: vertical;
        /* padding: 10px; */
}
.mySimpleInfo {
    margin: 10px;
}
.button {
  background-color: #409eff;
  border-color: #409eff;
  font-family: 'Pingang SC';
}
.button_outside {
  background-color: #409eff;
  border-color: #409eff;
  font-family: 'Pingang SC';
  width: 108px;
  margin-top: 4px;
  margin-bottom: 4px;
  margin-left: 10px;
  margin-right: 6px;
}
.ms-title {
  width: 100%;
  font-family: '楷体';
  line-height: 60px;
  text-align: center;
  font-size: 50px;
  color: #303133;
  /* border-bottom: 1px solid #ddd; */
}
.ms-login {
  position: absolute;
  left: 50%;
  top: 0%;
  width: 650px;
  margin: 30px 0 0 -400px;
  /* border-radius: 5px; */
  /* background: rgba(255, 255, 255, 0.3); */
  overflow: hidden;
}
.wrap {
  position: fixed;
  width:100%;
  height: 100%;
  background-size: 100%;
  background-repeat:no-repeat;
  background-attachment: fixed;
  background-image: url(../assets/img/pic2.jpg);
  background-size: cover;
}
</style>