#### selenium
1. 安装driver、python库
2. 基本使用
3. 使用过程中遇到问题解决方法记录

tips1: input的name是给后端使用的一般不会改变，定位元素时优先使用
tips2: 若上传文件为input标签,可用send_keys直接传入文件（绝对路径）
       如不是input标签
       1.js hook execute_script
       2.find input
       3.autoit支持windows自动化 appium支持mac自动化（不跨平台，不建议）
