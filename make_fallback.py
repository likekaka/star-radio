#!/usr/bin/env python3
"""生成 fallback.json:电台快照,供星海电台在 Radio Browser 不可用时兜底。

数据来源 roamdial.com 公开接口的快照(其本身派生自 Radio Browser 目录,
经服务端探测与地理编码)。重新生成:直接运行本脚本。

输出行结构(紧凑数组):
[id, name, url, countryZh, cc, state, bitrate, tags, lat, lng, langZh, prec]
"""
import json, sys, urllib.request

CORE = 'https://roamdial.com/api/globe?part=core'
REST = 'https://roamdial.com/api/globe?part=rest'

def get(url):
    req = urllib.request.Request(url, headers={ 'User-Agent': 'star-radio-fallback-generator/1.0' })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def main(out='fallback.json'):
    core, rest = get(CORE), get(REST)
    rows = []
    for i in range(core['n']):
        url = rest['url'][i]
        if not url.startswith('https') or '.m3u8' in url:   # 原生 audio 播不了 HLS
            continue
        co = core['countries'][core['c'][i]] if core['c'][i] < len(core['countries']) else []
        rows.append([
            rest['id'][i], rest['name'][i], url,
            co[1] if co else '', co[0] if co else '',
            rest['state'][i] or '', core['br'][i] or 0, rest['tags'][i] or '',
            core['lat'][i] / 100, core['lng'][i] / 100,
            core['langs'][core['l'][i]] if core['l'][i] < len(core['langs']) else '',
            core['prec'][i],
        ])
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, separators=(',', ':'))
    print(f'{len(rows)} stations -> {out}')

if __name__ == '__main__':
    main(*sys.argv[1:])
