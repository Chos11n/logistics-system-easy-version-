# 📦 Logistics System (Simple Version)

一个使用 Python + Flask + SQLite + JavaScript 构建的简单物流信息管理系统。

---

## 🧱 功能说明

- 添加货物记录（姓名、厂家、件数、立方、吨数、备注、日期）
- 支持通过前端表单录入数据
- 数据存储于本地 SQLite 数据库
- 简单 REST API 提供数据接口（POST/GET）

---

## 📁 项目结构

logistics-system/
├── backend/
│ ├── main.py # Flask 后端逻辑
│ └── requirements.txt # 后端依赖
├── config/
│ └── .env # 数据库配置
├── database/
│ └── schema.sql # 数据库建表语句
├── frontend/
│ ├── index.html # 主页面
│ └── js/
│ └── main.js # JS 提交表单
├── .gitignore
└── README.md

python依赖安装：
pip install -r backend/requirements.txt