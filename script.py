from datetime import datetime

from alibabacloud_swas_open20200601.client import Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_swas_open20200601 import models as swas_models
from alibabacloud_tea_util import models as util_models


# 1.创建client
print(datetime.now().replace(microsecond=0))
client = Client(open_api_models.Config(
    # 获取Access Key：https://ram.console.aliyun.com/manage/ak
    access_key_id = '',
    access_key_secret = '',
    endpoint = 'swas.cn-hongkong.aliyuncs.com'  # https://api.aliyun.com/product/SWAS-OPEN
))

# 2.配置订单
# 参数参考 https://next.api.aliyun.com/api/SWAS-OPEN/2020-06-01/CreateInstances?tab=DEMO&lang=PYTHON&sdkStyle=dara&RegionId=cn-hongkong
order_request = swas_models.CreateInstancesRequest(
    region_id = 'cn-hongkong',  # 地域：中国香港
    image_id = 'e9363571cf2444aba422b17470285465',  # 系统镜像：Ubuntu 22.04 LTS
    plan_id = 'swas.s2.c2m1s40b30t1.un',  # 套餐：24元/月, 2核vCPU, 1GB内存, ESSD 40GB, 1TB流量, 30Mbps带宽
    period = 1,  # 购买时长：1个月
    data_disk_size = 0,  # 额外挂载数据盘大小：0 GB
    amount = 1,  # 购买数量：1台
    auto_renew = False,  # 自动续费：否
)

# 3.发送请求
try:
    response = client.create_instances_with_options(order_request, util_models.RuntimeOptions())
    print(response)
except Exception as e:
    print(e)
