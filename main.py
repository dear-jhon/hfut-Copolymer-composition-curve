import wx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 定义函数 fun，接受两个参数 r1 和 r2，执行绘图操作
def fun(r1, r2, add=0, newplot=0):
    x = np.linspace(0, 1, 300)

    # 如果 add 和 newplot 都为 0，初始化绘图
    if add == 0 and newplot == 0:
        plt.title('Copolymer composition curve (powered by Chunhua Liu)')
        plt.gca().set_aspect('equal')
        plt.xlim(0, 1)  # 限制 x 轴范围
        plt.ylim(0, 1)  # 限制 y 轴范围
          # 固定纵横比

        # 定义 y 函数
        y = (r1 * x ** 2 + x * (1 - x)) / (r1 * x ** 2 + 2 * x * (1 - x) + r2 * (1 - x) ** 2)
        content = "r1:" + str(r1)
        plt.plot(x, y, label=content)
        plt.grid(True)
        plt.xlabel('r1')
        plt.ylabel('F1')

    # 如果 add 为 1，则绘制第二个曲线
    if add == 1:
        y = (r1 * x ** 2 + x * (1 - x)) / (r1 * x ** 2 + 2 * x * (1 - x) + r2 * (1 - x) ** 2)
        content = "r1:" + str(r1)
        plt.plot(x, y, label=content)
        plt.gca().set_aspect('equal',)  # 固定纵横比
        plt.grid(True)

    if newplot == 1:
        plt.clf()
        x = np.linspace(0, 1, 300)
        plt.gca().set_aspect('equal')  # 固定纵横比
        plt.title('Copolymer composition curve (powered by Chunhua Liu)')
        plt.xlim(0, 1)  # 限制 x 轴范围
        plt.ylim(0, 1)  # 限制 y 轴范围


        y = (r1 * x ** 2 + x * (1 - x)) / (r1 * x ** 2 + 2 * x * (1 - x) + r2 * (1 - x) ** 2)
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('r1')
        plt.ylabel('F1')
    plt.legend()  # 添加图例

# 定义主窗口类
class MyApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.SetSize((400, 200))
        self.SetTitle("共聚物组成曲线(v2.0版本)")
        panel = wx.Panel(self)

        r1_label = wx.StaticText(panel, label="r1:", pos=(20, 20))
        r2_label = wx.StaticText(panel, label="r2:", pos=(20, 60))

        self.r1_input = wx.TextCtrl(panel, pos=(60, 20), size=(100, -1))
        self.r2_input = wx.TextCtrl(panel, pos=(60, 60), size=(100, -1))

        plot_button = wx.Button(panel, label="Plot", pos=(250, 20))
        plot_button.Bind(wx.EVT_BUTTON, self.on_plot)

        add_button = wx.Button(panel, label="Add", pos=(200, 60))
        add_button.Bind(wx.EVT_BUTTON, self.on_add)

        newplot_button = wx.Button(panel, label="NewPlot", pos=(300, 60))
        newplot_button.Bind(wx.EVT_BUTTON, self.on_newplot)

        newplot_button = wx.Button(panel, label="交流邮箱：3317115870@qq.com", pos=(60, 100))

    def on_plot(self, event):
        try:
            r1 = float(self.r1_input.GetValue())
            r2 = float(self.r2_input.GetValue())
            fun(r1, r2)
            plt.show()
        except ValueError:
            wx.MessageBox("请输入有效的数字！", "错误", wx.OK | wx.ICON_ERROR)

    def on_add(self, event):
        try:
            r1 = float(self.r1_input.GetValue())
            r2 = float(self.r2_input.GetValue())
            fun(r1, r2, add=1)
            plt.show()
        except ValueError:
            wx.MessageBox("请输入有效的数字！", "错误", wx.OK | wx.ICON_ERROR)
        wx.MessageBox("添加曲线成功！", "添加曲线", wx.OK | wx.ICON_INFORMATION)

    def on_newplot(self, event):
        plt.clf()
        try:
            r1 = float(self.r1_input.GetValue())
            r2 = float(self.r2_input.GetValue())
            fun(r1, r2, newplot=1)
            plt.show()
        except ValueError:
            wx.MessageBox("请输入有效的数字！", "错误", wx.OK | wx.ICON_ERROR)
        wx.MessageBox("新绘制图像成功", "新绘制", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyApp(None)
    frame.Show()
    app.MainLoop()
