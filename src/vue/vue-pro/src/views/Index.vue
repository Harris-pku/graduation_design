<template>
    <div id="app">
      <!-- <img src="./assets/logo.png"> -->
      <!-- <router-view/> -->
      <el-container>
        <div class="wrap">
          <div class="ms-login">
            <div class="ms-title">CSDN问答帖分类与检索系统</div>
              <el-button type="primary" icon="el-icon-search" style="width: 100px; float: right; margin-top: 25px; margin-left: 8px" @click="handleSearch()">搜索</el-button>
              <el-col :span="3" style="margin-left: 2px; margin-top: 25px; width: 540px;">
                <el-input v-model="searchInput" placeholder="请输入你要搜索的内容…"></el-input>
              </el-col>
          </div>
  
          <el-aside width="180px">
            <!-- <div class="mySimpleInfo"> </div> -->
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
    margin: 190px 0 0 -331px;
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
  