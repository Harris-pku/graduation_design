<!-- <template>
    <div>
        <h1>主页</h1>
    </div>
    <el-container>
        <div class="title">这个是主页</div>
    </el-container>
</template>

<script>
    export default {
        name: "Index"
    }
</script>

<style scoped>
.title {
    width: 100%;
    font-family: '楷体';
    line-height: 60px;
    text-align: center;
    font-size: 50px;
    color: #ffffff;
    /* border-bottom: 1px solid #ddd; */
}
</style> -->

<template>
    <div id="app">
      <!-- <img src="./assets/logo.png"> -->
      <!-- <router-view/> -->
      
      <el-container>
        <div class="wrap">
          <div class="ms-login">
            <div class="ms-title">CSDN问答帖分类与检索系统</div>
          </div>
  
          <el-aside width="180px">
            <!-- <div class="mySimpleInfo"> </div> -->
            <template scope="scope">
              <el-button class="button_outside" type="primary" icon="el-icon-s-home" onclick="handleHome">首页</el-button><br>
              <el-button class="button_outside" type="primary" icon="el-icon-search" onclick="handleSelect">搜索</el-button><br>
              <el-button class="button_outside" type="primary" icon="el-icon-info" onclick="window.location.href='https://www.baidu.com'">关于</el-button>
              <el-button class="button_outside" type="primary" icon="el-icon-question" onclick="window.location.href=''">帮助</el-button><br>
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
            this.$router.push({path:'./components/Index.vue', params:{id : 10}});
        },
        handleSelect() {
            // console.log(key, keyPath);
            window.location.href = 'https://www.baidu.com';
            // this.$router.push(key);
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
  