from ssd1306 import SSD1306

_ssd1306 = SSD1306(128, 64)
while True:
    # 绘制一个黑色填充框以清除图像。
    _ssd1306.clear_image()
    # 第一行
    # 显示IP地址
    # _ssd1306.print_line_cmd("IP地址: ", "hostname -I | cut -d' ' -f1", 0)
    _ssd1306.print_line_normal_string(" 蒲 公 英 的 约 定", 2)
    # 第二行
    # 显示CPU使用率
    # _ssd1306.print_line_cmd("CPU load: ", 'cut -f 1 -d " " /proc/loadavg', 8)
    _ssd1306.print_line_normal_string(" 高 温 红 色 预 警", 18)
    # 第三行
    # 显示内存使用情况
    # _ssd1306.print_line_cmd("", "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'", 16)
    _ssd1306.print_line_normal_string(" 室 外 路 边 火 锅", 34)
    # 第四行
    # 显示磁盘使用情况
    # _ssd1306.print_line_cmd("", 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\'', 25)
    _ssd1306.print_line_normal_string(" 做 大 做 强 朗 起", 50)
    # 显示图像，0.1s刷新周期
    # _ssd1306.show(0.1)
    # 显示图像，10s刷新周期
    _ssd1306.show(10)
