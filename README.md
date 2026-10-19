# star-radio 星海电台

随机收听全球电台,three.js 可视化,纯前端单文件。

## 功能
- **三种视图**:地球(大陆轮廓 + 光点定位 + 点击播放)、流派星云(粒子分簇)、唱片(闲置 30s 自动进入,螺旋/山脉/星球轮换)
- **数据**:Radio Browser 直连(de1→de2→all 镜像容错),浏览器直连电台流,服务器零带宽
- **中文台省份归位**:坐标缺失的台按 state 邮政拼音/台名省名安放到省会附近
- 筛选(流派/语言/国家/码率)、搜索(`/`)、收藏/历史/只听收藏、睡眠定时、换台杂音、当地时间、快捷键(空格 N F V D Esc)、PWA、手机适配
- 死链自动跳台、`?s=<uuid>` 分享链接、记住上次收听

## 使用
静态站,无构建。任一静态托管(Vercel / GitHub Pages / 本地)直接放 `index.html` + `manifest.webmanifest` 即可:

```bash
python3 -m http.server 8000
```

## 说明
- 电台目录:[Radio Browser](https://www.radio-browser.info)(API 条款要求署名)
- 只播 https 流(混合内容限制);部分目录数据不准(错标/死链)由自动跳台兜底
- 大陆轮廓:world-atlas 110m(TopoJSON)
