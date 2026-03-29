# 📱 轻松记账 - 手机 APP 安装指南

## ✅ 已完成准备

你的记账 APP 已经打包成 **PWA（渐进式 Web 应用）**，可以像原生 APP 一样安装到手机上！

---

## 🚀 部署步骤

### 第一步：上传文件到 GitHub

1. **打开 GitHub 仓库**
   - 访问：https://github.com/weijialaoda/weishi
   
2. **上传所有文件**
   - 点击 **"Add file"** → **"Upload files"**
   - 将 `expense_tracker` 文件夹中的以下文件全部拖入：
     - ✅ index.html（主页面）
     - ✅ manifest.json（APP 配置）
     - ✅ sw.js（离线功能）
     - ✅ icon-192.png（APP 图标）
     - ✅ icon-512.png（APP 图标）
   
3. **提交文件**
   - 填写提交信息："添加 PWA 支持"
   - 点击 **"Commit changes"**

---

### 第二步：在 Vercel 重新部署

1. **打开 Vercel Dashboard**
   - 访问：https://vercel.com/dashboard
   
2. **找到 weishi 项目**
   - 点击进入项目详情页
   
3. **重新部署**
   - 点击 **"Redeploy"**（重新部署）
   - 等待 1-2 分钟完成构建

---

### 第三步：在手机浏览器访问

1. **打开手机浏览器**
   - iPhone：使用 Safari
   - Android：使用 Chrome
   
2. **访问你的域名**
   ```
   https://weishi.vercel.app
   ```
   或使用 Vercel 分配的完整域名（如 `weishi-xxx.vercel.app`）

---

## 📲 安装到手机桌面

### iPhone (iOS) 安装方法

1. **用 Safari 打开** `https://weishi.vercel.app`

2. **点击分享按钮**（底部中间的方框箭头图标）

3. **向下滑动，找到并点击** "添加到主屏幕"

4. **输入名称**（如"轻松记账"），点击右上角"添加"

5. **完成！** 手机桌面会出现记账 APP 图标，点击即可全屏使用

---

### Android (安卓) 安装方法

1. **用 Chrome 打开** `https://weishi.vercel.app`

2. **点击右上角菜单**（三个点）

3. **点击** "添加到主屏幕" 或 "安装应用"

4. **确认安装**

5. **完成！** 手机桌面会出现记账 APP 图标

---

## ✨ PWA APP 特性

✅ **全屏显示** - 没有浏览器地址栏，和原生 APP 一样  
✅ **离线使用** - 即使没网也能打开查看之前的记录  
✅ **自动更新** - 每次打开自动获取最新版本  
✅ **数据本地存储** - 所有记账数据安全存在手机里  
✅ **语音记账** - 点击麦克风说话就能记账  

---

## 🔧 如果遇到问题

### 问题 1：Vercel 访问超时
- **原因**：Vercel 在国内网络不稳定
- **解决**：改用 Netlify 部署（见下方备选方案）

### 问题 2：无法安装到桌面
- **检查**：确保用手机浏览器访问（不是电脑）
- **检查**：确保使用的是 Safari (iOS) 或 Chrome (Android)
- **检查**：页面必须通过 HTTPS 访问（Vercel 默认支持）

### 问题 3：语音功能不可用
- **原因**：部分浏览器需要用户授权
- **解决**：首次使用时允许麦克风权限即可

---

## 🎯 备选方案：使用 Netlify 部署

如果 Vercel 访问困难，可改用 Netlify：

1. **登录 Netlify**
   - 访问：https://app.netlify.com/login
   - 使用 GitHub 账号登录（避免邮箱验证码问题）

2. **导入 GitHub 仓库**
   - 点击 "Add new site" → "Import an existing project"
   - 选择 GitHub，找到 `weijialaoda/weishi` 仓库
   - 点击 "Deploy site"

3. **获得访问链接**
   - 部署成功后会获得类似 `xxx.netlify.app` 的域名
   - Netlify 在国内访问更稳定

4. **按上述"第三步"安装到手机**

---

## 📞 需要帮助？

如有任何问题，请告诉我具体遇到的错误提示或截图！
