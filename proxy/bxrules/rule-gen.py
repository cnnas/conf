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
    str = str.encode('utf-8')
    tmp_str = base64.b64encode(str)
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

def conv_ss_str(str):
    if str[0:1] == '#':
        return ''
        # str = '!'+str[1:]
    elif str[0:1]  not in ['\t','\n', ''] :
        str = "server=/." + str.replace('\n', '') + "/127.0.0.1#7913\nipset=/." + str.replace('\n', '') + "/gfwlist\n"
    return str


def get_conf():
    CONF_RULE_SITE = RUN_DIR + "/rule-sites.conf"
    if os.path.exists(CONF_RULE_SITE):
        rule_str_gfw = ''
        rule_str_qx = ''
        rule_str_ss = ''

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


        f.close()
        
        gen_gfw_file(rule_str_gfw)
        gen_qx_file(rule_str_qx)
        gen_file(rule_str_ss, RUN_DIR + '/' + 'rule-ss.conf')
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
