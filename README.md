# MyScripts

记录一些脚本

## setup_pyver.py

用于在安装多版本python时快速切换，必须确保当前**环境变量**的**Path**中已包含各个Python版本的路径

以从Python2切换到Python36为例（指定36是因为有可能同时装了多版本的Python3，如3.6、3.7、3.8等）

```cmd
python setup_pyver.py 36
```

理论上脚本是同时支持py2和py3的运行的，所以不需要指定版本，直接用`python`命令执行即可

> 其实也可以生成exe，通过带参数执行exe就不需要关心python版本了
