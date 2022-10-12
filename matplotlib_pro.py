import matplotlib
import matplotlib.pyplot as plt

# 解决无法显示中文字体的解决方案
matplotlib.rc('font', family='Microsoft Yahei')

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 设置内置样式
plt.style.use('seaborn')
# 在一张图片中绘制一个或多个图表,变量ax表示图片中的各个图表，变量fig表示整张图片
fig, ax = plt.subplots()
# 传递一对x坐标和y坐标，将在指定位置绘制一个点,s表示使用点的尺寸，如果需要绘制一系列的点，需要向x,y参数传递一系列的列表
ax.scatter(2,4,s = 200)
# 尝试根据给定的数据以有意义的方式绘制图表。linewidth决定绘制图表的线条粗细
ax.plot(input_values, squares, linewidth=3)
# 给图表指定标题，可用fontsize指定文字的大小
ax.set_title('平方数', fontsize=24)
# 给x轴设置标题，可用fontsize指定文字的大小
ax.set_xlabel('值', fontsize=14)
# 给y轴设置标题，可用fontsize指定文字的大小
ax.set_ylabel('值的平方', fontsize=14)
# 设置图标刻度的样式。 其中axis表示轴线样式，labelsize表示刻度字号大小
ax.tick_params(axis='both', which = 'major', labelsize=14)
# 打开Matplotlib查看器并显示绘制的图表
plt.show()
