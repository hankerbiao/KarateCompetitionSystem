

# 空手道竞赛系统

## 简介

这是一个基于FastAPI和VUE3开发的空手道竞赛系统，旨在提供运动员的录入、赛程录入、比赛过程信息管理等功能。该系统能够帮助组织者高效地管理比赛，并为参与者提供便捷的比赛信息查询服务。

## 功能特性

- 运动员信息管理
- 赛程安排与管理
- 比赛过程信息记录
- 实时比赛结果查询
- 用户权限管理

## 技术栈

- 后端：FastAPI
- 前端：VUE3
- 数据库：待定（如：PostgreSQL, MySQL）
- 其他：Docker（可选）

[vue-manage-system]([GitHub - lin-xin/vue-manage-system: Vue3、Element Plus、typescript后台管理系统](https://github.com/lin-xin/vue-manage-system)) for the web parts

## 安装与使用

### 环境要求

- Python 3.8+
- Node.js 14+

### 克隆项目

```bash
git clone https://github.com/yourusername/karate-competition-system.git
cd karate-competition-system
```

### 后端

1. 进入`backend`目录：
   
   ```bash
   cd backend
   ```

2. 创建并激活虚拟环境：
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. 安装依赖：
   
   ```bash
   pip install -r requirements.txt
   ```

4. 运行应用：
   
   ```bash
   uvicorn app.main:app --reload
   ```

### 前端

1. 进入`web`目录：
   
   ```bash
   cd web
   ```

2. 安装依赖：
   
   ```bash
   npm install
   ```

3. 运行开发服务器：
   
   ```bash
   // 运行
   npm run dev
   
   // 执行构建命令，生成的dist文件夹放在服务器下即可访问
   npm run build
   ```

## ## 项目截图



## API文档

API文档使用Swagger生成，启动后可访问`http://localhost:8000/docs`查看详细API接口说明。

## 贡献

欢迎任何形式的贡献！请阅读[贡献指南](CONTRIBUTING.md)了解更多。

## 许可证

该项目采用**Apache**许可证，详情请参阅[LICENSE](LICENSE)文件。