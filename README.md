# RTK电子围栏模拟测试系统

基于RTK定位的平地机电子围栏系统模拟测试平台，用于硕士论文研究。

## 功能特性

- ✅ RTK定位数据模拟（精度、状态、误差）
- ✅ 平地机运动轨迹生成
- ✅ 电子围栏算法实现
- ✅ 多场景测试（静态、动态、极端场景）
- ✅ 自动化数据分析
- ✅ 论文级可视化输出

## 安装依赖

```bash
pip install -r requirements.txt
```

## 快速开始

```bash
# 运行完整测试
python main.py

# 运行详细测试
python tests/run_all_tests.py
```

## 测试场景

1. **静态精度测试**：固定点长时间定位精度
2. **动态精度测试**：不同速度下的定位性能
3. **边界穿越测试**：不同角度/速度穿越围栏

## 输出结果

- `outputs/data/`: CSV格式原始数据
- `outputs/figures/`: 高分辨率图表（PNG/PDF）
- `outputs/reports/`: Markdown/JSON测试报告

## 项目结构

```
rtk-geofence-simulator/
├── README.md
├── requirements.txt
├── main.py
├── config/
│   └── test_config.yaml
├── src/
│   ├── rtk_simulator.py
│   ├── geofence_engine.py
│   ├── trajectory_generator.py
│   └── utils.py
├── analysis/
│   └── visualizer.py
└── tests/
    └── run_all_tests.py
```
