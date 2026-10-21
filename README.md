# star-radio 星海电台

随机收听全球电台,three.js 可视化,纯前端单文件。

## 功能
- **三种视图**:地球(大陆轮廓 + 光点定位 + 点击播放)、流派星云(粒子分簇 + 流派标签)、唱片(💿 按钮 / Enter 进入,黑胶盘 / 频谱山脉 / 星球环三种形态,盘内上台/下台;闲置 30s 也会自动进入)
- **数据**:Radio Browser 直连(de1→de2→all 镜像容错),浏览器直连电台流,服务器零带宽
- **三层容错**:localStorage 目录缓存(SWR,7 天)→ 仓库快照 `fallback.json` → 报错
- **中文台省份归位**:坐标缺失的台按 state 邮政拼音/台名省名安放到省会附近;国家 bbox 校验过滤错标数据
- 筛选(流派/语言/国家/码率)、搜索(`/`)、收藏/历史/只听收藏、睡眠定时、换台杂音、当地时间、快捷键(空格 N F V D Esc)、PWA、手机适配
- 死链自动跳台、`?s=<uuid>` 分享链接、记住上次收听、saveData 省流量

## 使用
静态站,无构建。任一静态托管(Vercel / GitHub Pages / 本地)直接放 `index.html` + `manifest.webmanifest` 即可:

```bash
python3 -m http.server 8000
```

## 备用目录快照

Radio Browser 全部镜像不可用时,自动回退到同目录的 `fallback.json`(~3.3 万台,已滤 HLS)。
生成/更新:

```bash
python3 make_fallback.py   # 产出 fallback.json
git add fallback.json && git commit -m 'update fallback snapshot' && git push
```

快照数据派生自 Radio Browser 目录(经 roamdial 公开接口的服务端探测与地理编码加工),再分发请遵守其署名要求。

## 说明
- 电台目录:[Radio Browser](https://www.radio-browser.info)(API 条款要求署名)
- 只播 https 流(混合内容限制);部分目录数据不准(错标/死链)由自动跳台兜底
- 大陆轮廓:world-atlas 110m(TopoJSON)
