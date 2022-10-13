// pipeline声明
pipeline{
//  在哪个节点上构建，此处可以在Jenkins的工作目录下的流水线语法中Declarative Directive Generator（指令生成器）中点击生成即可
//  包括stages、stage、steps都可以通过指令生成器生成
    agent any
//  阶段，所有的任务步骤都放入其中
    stages {
//    每一个阶段
      stage('autotest_api') {
//      步骤，具体的任务步骤
        steps {
//        此处需要在流水线语法的片段生成器中输入常用代码，点击生成pipeline语法
          bat 'python selenium练习.py'
        }
      }
    }
}