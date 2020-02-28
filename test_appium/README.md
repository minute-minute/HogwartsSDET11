#### adb
查看当前界面的元素   
```
adb shell dumpsys activity top
```
获取当前任务列表  
```
adb shell dumpsys activity activities
```
安装apk  
```
adb install -r path/name.apk
```
查看日志  
```
adb logcat |grep -i displayed
```
查看apk内容和配置信息  
```
aapt dump badging mobike.apk | grep launchable-activity
```
启动app  
```
adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S
// com.xueqiu.android/.view.WelcomeActivityAlias app入口
```

#### appium
```
<!-- -g:将控制台打印输出到指定文件 -->
appium -g appium.log --log-timestamp --local-timezone
```

待：hamcrest