# CNnas Conf

## Proxy Conf
### 1. Shadowrocket
- sr_banlist_ad
    - [Shadowrocket BanList AD(by jsdelivr)](https://cdn.jsdelivr.net/gh/cnnas/conf/proxy/sr_banlist_ad.conf)
    - [Shadowrocket BanList AD](https://raw.githubusercontent.com/cnnas/conf/master/proxy/sr_banlist_ad.conf)
- sr_my(TODO：需解决youtube去广告后无法播放视频问题)
    - [My Shadowrocket Conf(by jsdelivr)](https://cdn.jsdelivr.net/gh/cnnas/conf/proxy/sr_my.conf)
    - [My Shadowrocket Conf](https://raw.githubusercontent.com/cnnas/conf/master/proxy/sr_my.conf)
> 说明： sr的配置参考： <https://github.com/h2y/Shadowrocket-ADBlock-Rules>

### 2. loon

### 3. AdGuard

#### 3.1 AdGuard Home设置过滤youtube广告

在AdGuard Home的过滤器——自定义过滤规则下面添加以下规则：
```conf
/googleads.$~script,domain=~googleads.github.io
/pagead/lvz?
||google.com/pagead/
||static.doubleclick.net^$domain=youtube.com
||youtube.com/get_midroll_
```

## CA证书设置
### iOS & iPadOS CA证书设置
1. 【通用】-【描述文件】 中添加证书文件
2. 【通用】-【关于本机】-【证书信任设置】中开启对应的根证书。


