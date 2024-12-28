#encoding: utf-8
import os
import base64

def gen_gfw_file(str):
    # 打开文件,不存在则创建
    GFW_RULE_NAME = RUN_DIR + '/' + 'rule-mini.conf'
    f = open(GFW_RULE_NAME, 'w')
    f.write(str)
    f.close()

    GFW_RULE_NAME = RUN_DIR + '/' + 'rule-mini.txt'
    f = open(GFW_RULE_NAME, 'wb')
    str64 = str.encode('utf-8')
    tmp_str = base64.encodebytes(str64)
    f.write( tmp_str )
    # f.write( str(tmp_str, encoding = "utf-8") )
    f.close()


def gen_qx_file(str):
    # 打开文件,不存在则创建
    QX_RULE_NAME = RUN_DIR + '/' + 'rule-qx.list'
    f = open(QX_RULE_NAME, 'w')
    f.write(str)
    f.close()

def gen_file(str, file_name=''):
    # 打开文件,不存在则创建
    f = open(file_name, 'w')
    f.write(str)
    f.close()

def conv_gfw_str(str):
    if str[0:1] == '#':
        str = '!'+str[1:]
    elif str[0:1]  not in ['\t','\n', ''] :
        str = "||"+str
    return str

def conv_qx_str(str):
    if str[0:1] == '#':
        pass
        # str = '!'+str[1:]
    elif str[0:1]  not in ['\t','\n', ''] :
        str = "DOMAIN-SUFFIX," + str.replace('\n', '') + ",PROXY\n"
    return str

def conv_loon_str(str):
    if str[0:1] == '#':
        return ''
    elif str[0:1]  not in ['\t','\n', ''] :
        str = "DOMAIN-SUFFIX," + str.replace('\n', '') + "\n"
    return str

def conv_shadowrocket_str(str):
    if str[0:1] == '#':
        return ''
    elif str[0:1]  not in ['\t','\n', ''] :
        str = "DOMAIN-SUFFIX," + str.replace('\n', '') + ",Proxy\n"
    return str


def conv_ss_str(str):
    if str[0:1] == '#':
        return ''
        # str = '!'+str[1:]
    elif str[0:1]  not in ['\t','\n', ''] :
        str = "server=/." + str.replace('\n', '') + "/127.0.0.1#7913\nipset=/." + str.replace('\n', '') + "/gfwlist\n"
    return str

def str_sw_start():
    return '''
# update source: https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist.conf
# usage link: https://down.2151512.com/https://raw.githubusercontent.com/cnnas/conf/refs/heads/master/proxy/bxrules/rule-sw.confrule-gen.py
[General]
ipv6 = true
bypass-system = true
skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.apple.com, *.ls.apple.com
bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,233.252.0.0/24,224.0.0.0/4,255.255.255.255/32,::1/128,::ffff:0:0/96,::ffff:0:0:0/96,64:ff9b::/96,64:ff9b:1::/48,100::/64,2001::/32,2001:20::/28,2001:db8::/32,2002::/16,3fff::/20,5f00::/16,fc00::/7,fe80::/10,ff00::/8
dns-server = https://dns.alidns.com/dns-query, https://doh.pub/dns-query
[Rule]

#tg ip
IP-CIDR,91.108.56.0/22,Proxy
IP-CIDR,91.108.4.0/22,Proxy
IP-CIDR,91.108.8.0/22,Proxy
IP-CIDR,91.108.16.0/22,Proxy
IP-CIDR,91.108.12.0/22,Proxy
IP-CIDR,149.154.160.0/20,Proxy
IP-CIDR,91.105.192.0/23,Proxy
IP-CIDR,91.108.20.0/22,Proxy
IP-CIDR,185.76.151.0/24,Proxy
IP-CIDR,2001:b28:f23d::/48,Proxy
IP-CIDR,2001:b28:f23f::/48,Proxy
IP-CIDR,2001:67c:4e8::/48,Proxy
IP-CIDR,2001:b28:f23c::/48,Proxy
IP-CIDR,2a0a:f280::/32,Proxy

#50 whatsapp
IP-CIDR,18.194.0.0/15,Proxy
IP-CIDR,34.224.0.0/12,Proxy

# other
IP-CIDR,67.220.91.23/32,Proxy
IP-CIDR,14.102.250.18/32,Proxy
IP-CIDR,72.52.81.22/32,Proxy
IP-CIDR,85.17.73.31/32,Proxy
IP-CIDR,14.102.250.19/32,Proxy
IP-CIDR,174.142.105.153/32,Proxy
IP-CIDR,67.220.91.18/32,Proxy
IP-CIDR,69.65.19.160/32,Proxy
IP-CIDR,67.220.91.15/32,Proxy
IP-CIDR,50.7.31.230/32,Proxy


#72 #112 Google Voice
IP-CIDR,74.125.0.0/16,Proxy

# 修复 Telegram #105
IP-CIDR,67.198.55.0/24,Proxy
IP-CIDR,91.108.4.0/22,Proxy
IP-CIDR,91.108.8.0/22,Proxy
IP-CIDR,91.108.12.0/22,Proxy
IP-CIDR,91.108.16.0/22,Proxy
IP-CIDR,91.108.56.0/22,Proxy
IP-CIDR,109.239.140.0/24,Proxy
IP-CIDR,149.154.160.0/20,Proxy
IP-CIDR,149.154.164.0/22,Proxy
IP-CIDR,149.154.168.0/22,Proxy
IP-CIDR,149.154.172.0/22,Proxy
# 修复 google voice #112
IP-CIDR,74.125.23.127/32,Proxy

'''


def str_sw_end():
    return r'''
RULE-SET,https://down.2151512.com/https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/AppleNews/AppleNews.list,PROXY
GEOIP,CN,DIRECT
FINAL,proxy

[URL Rewrite]
^https?://(www.)?(g|google)\.cn https://www.google.com 302

[MITM]
hostname = *.google.cn,*.googlevideo.com
'''

def str_sw_diy_end():
    return r'''
RULE-SET,https://down.2151512.com/https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/AppleNews/AppleNews.list,PROXY
FINAL,DIRECT

[URL Rewrite]
^https?://(www.)?(g|google)\.cn https://www.google.com 302

[MITM]
hostname = *.google.cn,*.googlevideo.com
'''

def get_conf():
    CONF_RULE_SITE = RUN_DIR + "/rule-sites.conf"
    if os.path.exists(CONF_RULE_SITE):
        rule_str_gfw = ''
        rule_str_qx = ''
        rule_str_ss = ''
        rule_str_loon = ''
        rule_str_shadowrocket = str_sw_start()

        with open(CONF_RULE_SITE, 'r', errors='ignore') as f:
            lines = f.readlines()
        
        # f = open(CONF_RULE_SITE, 'r')               # 返回一个文件对象 
        # lines = f.readlines()
        for line in lines:
            # line = conv_qx_str(line)
            # print(line, end = '')
            rule_str_gfw = rule_str_gfw + conv_gfw_str(line)
            rule_str_qx = rule_str_qx + conv_qx_str(line)
            rule_str_ss = rule_str_ss + conv_ss_str(line)
            rule_str_loon = rule_str_loon + conv_loon_str(line)
            rule_str_shadowrocket = rule_str_shadowrocket + conv_shadowrocket_str(line)


        f.close()
        
        gen_gfw_file(rule_str_gfw)
        gen_qx_file(rule_str_qx)
        gen_file(rule_str_ss, RUN_DIR + '/' + 'rule-ss.conf')
        gen_file(rule_str_loon, RUN_DIR + '/' + 'rule-loon.conf')

        rule_str_shadowrocket_diy = rule_str_shadowrocket + str_sw_diy_end()
        gen_file(rule_str_shadowrocket_diy, RUN_DIR + '/' + 'rule-sw-diy.conf')

        rule_str_shadowrocket = rule_str_shadowrocket + str_sw_end()
        gen_file(rule_str_shadowrocket, RUN_DIR + '/' + 'rule-sw.conf')
        # line = f.readline()               # 调用文件的 readline()方法 
        # while line: 
        #     # print line,                   # 后面跟 ',' 将忽略换行符 
        #     print(line, end = '')      # 在 Python 3 中使用 
        #     line = f.readline() 
        
        # f.close()  
    else:
        print('not such file:')

if __name__ == '__main__':
    RUN_DIR = os.path.split(os.path.realpath(__file__))[0]
    get_conf()
