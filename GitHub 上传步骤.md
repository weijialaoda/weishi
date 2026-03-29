# 📤 GitHub 文件上传步骤

## 当前状态
✅ 你已经创建了 GitHub 仓库：`weijialaoda/weishi`
✅ 仓库地址：https://github.com/weijialaoda/weishi

---

## 🎯 上传方法（3 种任选其一）

### 方法一：直接拖拽上传（最简单）⭐推荐

1. **打开文件资源管理器**
   - 按 `Win + E` 打开文件资源管理器
   - 进入路径：`C:\Users\Administrator\.real\users\user-d11b7c7ffb5ea17fb529446a5fc99972\workspace\expense_tracker\`

2. **选择要上传的文件**
   - 按住 `Ctrl` 键，依次点击以下 5 个文件：
     - ✅ `index.html`
     - ✅ `mobile.html`
     - ✅ `README_手机使用指南.md`
     - ✅ `快速开始.md`
     - ✅ `部署教程.md`

3. **拖拽到 GitHub**
   - 把选中的 5 个文件**直接拖到**浏览器中 GitHub 页面的虚线框内
   - 或者在页面中找到 "uploading an existing file" 链接点击

4. **提交文件**
   - 等待文件上传完成（绿色进度条）
   - 在底部的 "Commit changes" 输入框中输入：`Add expense tracker app`
   - 点击绿色的 **"Commit changes"** 按钮

---

### 方法二：逐个文件上传

1. 在 GitHub 仓库页面，点击 **"add file"** 按钮
2. 选择 **"Upload files"**
3. 点击 **"choose your files"** 或直接拖拽文件
4. 选择 `index.html` 文件
5. 在底部输入提交信息：`Add index.html`
6. 点击 **"Commit changes"**
7. 重复以上步骤上传其他 4 个文件

---

### 方法三：使用 Git 命令行（适合熟悉 Git 的用户）

```bash
# 1. 克隆仓库到本地
git clone https://github.com/weijialaoda/weishi.git
cd weishi

# 2. 复制文件到仓库目录
copy C:\Users\Administrator\.real\users\user-d11b7c7ffb5ea17fb529446a5fc99972\workspace\expense_tracker\*.html .
copy C:\Users\Administrator\.real\users\user-d11b7c7ffb5ea17fb529446a5fc99972\workspace\expense_tracker\*.md .

# 3. 添加并提交
git add .
git commit -m "Add expense tracker app"

# 4. 推送到 GitHub
git push origin main
```

---

## ✅ 上传完成后

1. **确认文件已上传**
   - 刷新 GitHub 仓库页面
   - 应该能看到 5 个文件：`index.html`, `mobile.html`, `README_手机使用指南.md`, `快速开始.md`, `部署教程.md`

2. **启用 GitHub Pages**
   - 点击仓库顶部的 **"Settings"** 标签
   - 在左侧菜单找到并点击 **"Pages"**
   - 在 "Build and deployment" 部分：
     - Source: 选择 **"Deploy from a branch"**
     - Branch: 选择 **"main"** 分支，文件夹选择 **"/ (root)"**
   - 点击 **"Save"** 按钮
   - 等待 1-2 分钟，页面会显示你的网站地址

3. **获取访问链接**
   - GitHub Pages 会生成一个链接，格式为：
   ```
   https://weijialaoda.github.io/weishi/
   ```
   - 复制这个链接到手机浏览器即可访问记账 APP！

---

## 📱 手机访问

部署成功后，在手机浏览器打开：
```
https://weijialaoda.github.io/weishi/index.html
```

就可以开始使用语音记账功能了！🎉

---

## ❓ 常见问题

### Q: 上传时提示需要登录？
A: 点击右上角的 "Sign in" 登录你的 GitHub 账号

### Q: 找不到拖拽区域？
A: 点击 "add file" → "Upload files" 就会出现拖拽区域

### Q: GitHub Pages 不生效？
A: 等待 1-2 分钟，刷新 Settings → Pages 页面查看状态

### Q: 手机端无法访问？
A: 确保链接正确，格式应为 `https://用户名.github.io/仓库名/index.html`

---

## 📞 需要帮助？

如果在上传过程中遇到任何问题，请截图发给我，我会帮你解决！
