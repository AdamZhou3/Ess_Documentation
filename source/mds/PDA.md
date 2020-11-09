```python
T = np.arctan2(cars['weight'],cars['mpg'])
https://www.jianshu.com/p/c02291ab4c3b
```



## Dtypes

https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes

* df.convert_dtypes()

### type transfer

```python
dt = dfc.dtypes.to_dict()
dt["行政区"] = pd.StringDtype()
dt["街道"] = pd.StringDtype()
dt["社区"] = pd.StringDtype()
dt["小区/社区"] = pd.StringDtype()
dt["确诊"] = pd.Int64Dtype()
dt["疑似"] = pd.Int64Dtype()
dt["通报日期"] = pd.DatetimeTZDtype(tz=8)

dfc.astype(dt) # 可以传递字典
```



### 数据存储类型与空值

```python
## 数据导入进pandas 进行convert_dtypes后 列中仍然存在空值  因此列的数据类型是str和Natype的混合
pd.notna(dfc["街道"])
pd.notna(dfc["街道"])

pd.notna(dfc["街道"].astype(str)) # 将NA也作为一种值 此时列的值是单一的

pd.notna(dfc["确诊"])  # 对于数值类型同理 也会得到false
dfc["疑似"].fillna(0).astype(np.int32) 
```



### 数值存储error

```python
pd.to_numeric(s, errors='coerce') 
 # If ‘raise’, then invalid parsing will raise an exception.
 # If ‘coerce’, then invalid parsing will be set as NaN.
 # If ‘ignore’, then invalid parsing will return the input.
```

## Styling 

```python
#dfc.style.background_gradient(cmap='viridis', low=.5, high=0).highlight_null('red') #
dfc.query("确诊 > 7")
```

## 常用操作

* df.lookup()
* df.query()
* df.values
* df.apply()
* df.assign()
* df.set_index(["code"], append=True)

### 在整个表中选取

```

```

### 选取拼接的某几段

```
df.iloc[pd.np.r_[10:12, 25:28]]
```



### 根据数据类型选取行

```
dfc_intDate = dfc[dfc["通报日期"].apply(lambda x: isinstance(x, int))]
```

### 删除行

```
dfc.drop(dfc_intDate.index.values).reset_index(drop=True) 
```

### 重复行a

```
### 找到重复的保存  
dfd_cases = dfd.iloc[:,[-8,-7,-6,-1]] # ['确诊', '疑似', '通报日期', 'code'] 重复
dfd_dupli = dfd[dfd_cases.duplicated(keep=False)]# 查看 根据code和日期筛选重复值 




## 根据某些列的重复 进行去重  = drop_duplicates subset 参数
# dfd_R= dfd[dfd_cases.duplicated()!=True].reset_index(drop=True) # 去掉重复的 Remove duplicated  

## 
dfd_R = dfd_R.drop_duplicates(keep="first").reset_index(drop=True) # inplace 在原对象上发生修改

# 这个更好 注意在哪几列查重
dfc_R = dfc.drop_duplicates(subset = ["code","确诊","疑似","通报日期"],keep="first").reset_index() # inplace 在原对象上发生修改  

dfc_dupli = dfc_dupli.sort_values(by="code").reset_index()  # 对结果排序使更好看
dfd_dupli.to_excel("./2_Processed/WuhanData_1104_duplicated.xls",index=False)
```

### links

* https://cloud.tencent.com/developer/article/1550971  



## 填充

```python
dfd_R_YS = dfd_R_YS.fillna(0).astype(np.int32).apply(lambda x : np.cumsum(x),axis=1)

```



## 日期

``` python
dfc['通报日期'] = pd.to_datetime(dfc['通报日期'],format="%Y-%m-%d %H:%M:%S").dt.strftime("%Y/%m/%d") 

dfc['通报日期'] = dfc['通报日期'].apply(lambda a: pd.to_datetime(a).date())  ## date()


dfc['通报日期'].apply(lambda a: pd.to_datetime(a).strftime('%Y-%m-%d')) ## 一定要注意日期的输出格式！！！！
```

## 坐标解析

```python
import requests
from requests.exceptions import ReadTimeout, ConnectTimeout

def transform(geo):
    parameters = { "address" : geo,  "key" : "30577d170f94533d1c546b964c103738","city":"武汉市"}
    base =  "https://restapi.amap.com/v3/geocode/geo"
    loc = 0
    try:
        response = requests.get(base, parameters, timeout=2)
        if response.status_code == 200:
            answer = response.json()
            loc = answer["geocodes"][0]["location"]
        else:
            pass
    except (ReadTimeout, ConnectTimeout,IndexError):
        print(geo)
            # ConnectTimeout指的是建立连接所用的时间，适用于网络状况正常的情况下，两端连接所用的时间。ReadTimeout指的是建立连接后从服务器读取到可用资源所用的时间。
        pass
    return loc
```





## 坐标转换

```python
import math

class LngLatTransfer():

    def __init__(self):
        self.x_pi = 3.14159265358979324 * 3000.0 / 180.0
        self.pi = math.pi  # π
        self.a = 6378245.0  # 长半轴
        self.es = 0.00669342162296594323  # 偏心率平方
        pass

    def GCJ02_to_BD09(self, gcj_lng, gcj_lat):
        """
        实现GCJ02向BD09坐标系的转换
        :param lng: GCJ02坐标系下的经度
        :param lat: GCJ02坐标系下的纬度
        :return: 转换后的BD09下经纬度
        """
        z = math.sqrt(gcj_lng * gcj_lng + gcj_lat * gcj_lat) + 0.00002 * math.sin(gcj_lat * self.x_pi)
        theta = math.atan2(gcj_lat, gcj_lng) + 0.000003 * math.cos(gcj_lng * self.x_pi)
        bd_lng = z * math.cos(theta) + 0.0065
        bd_lat = z * math.sin(theta) + 0.006
        return bd_lng, bd_lat


    def BD09_to_GCJ02(self, bd_lng, bd_lat):
        '''
        实现BD09坐标系向GCJ02坐标系的转换
        :param bd_lng: BD09坐标系下的经度
        :param bd_lat: BD09坐标系下的纬度
        :return: 转换后的GCJ02下经纬度
        '''
        x = bd_lng - 0.0065
        y = bd_lat - 0.006
        z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * self.x_pi)
        theta = math.atan2(y, x) - 0.000003 * math.cos(x * self.x_pi)
        gcj_lng = z * math.cos(theta)
        gcj_lat = z * math.sin(theta)
        return gcj_lng, gcj_lat


    def WGS84_to_GCJ02(self, lng, lat):
        '''
        实现WGS84坐标系向GCJ02坐标系的转换
        :param lng: WGS84坐标系下的经度
        :param lat: WGS84坐标系下的纬度
        :return: 转换后的GCJ02下经纬度
        '''
        dlat = self._transformlat(lng - 105.0, lat - 35.0)
        dlng = self._transformlng(lng - 105.0, lat - 35.0)
        radlat = lat / 180.0 * self.pi
        magic = math.sin(radlat)
        magic = 1 - self.es * magic * magic
        sqrtmagic = math.sqrt(magic)
        dlat = (dlat * 180.0) / ((self.a * (1 - self.es)) / (magic * sqrtmagic) * self.pi)
        dlng = (dlng * 180.0) / (self.a / sqrtmagic * math.cos(radlat) * self.pi)
        gcj_lng = lat + dlat
        gcj_lat = lng + dlng
        return gcj_lng, gcj_lat


    def GCJ02_to_WGS84(self, gcj_lng, gcj_lat):
        '''
        实现GCJ02坐标系向WGS84坐标系的转换
        :param gcj_lng: GCJ02坐标系下的经度
        :param gcj_lat: GCJ02坐标系下的纬度
        :return: 转换后的WGS84下经纬度
        '''
        dlat = self._transformlat(gcj_lng - 105.0, gcj_lat - 35.0)
        dlng = self._transformlng(gcj_lng - 105.0, gcj_lat - 35.0)
        radlat = gcj_lat / 180.0 * self.pi
        magic = math.sin(radlat)
        magic = 1 - self.es * magic * magic
        sqrtmagic = math.sqrt(magic)
        dlat = (dlat * 180.0) / ((self.a * (1 - self.es)) / (magic * sqrtmagic) * self.pi)
        dlng = (dlng * 180.0) / (self.a / sqrtmagic * math.cos(radlat) * self.pi)
        mglat = gcj_lat + dlat
        mglng = gcj_lng + dlng
        lng = gcj_lng * 2 - mglng
        lat = gcj_lat * 2 - mglat
        return lng, lat


    def BD09_to_WGS84(self, bd_lng, bd_lat):
        '''
        实现BD09坐标系向WGS84坐标系的转换
        :param bd_lng: BD09坐标系下的经度
        :param bd_lat: BD09坐标系下的纬度
        :return: 转换后的WGS84下经纬度
        '''
        lng, lat = self.BD09_to_GCJ02(bd_lng, bd_lat)
        return self.GCJ02_to_WGS84(lng, lat)


    def WGS84_to_BD09(self, lng, lat):
        '''
        实现WGS84坐标系向BD09坐标系的转换
        :param lng: WGS84坐标系下的经度
        :param lat: WGS84坐标系下的纬度
        :return: 转换后的BD09下经纬度
        '''
        lng, lat = self.WGS84_to_GCJ02(lng, lat)
        return self.GCJ02_to_BD09(lng, lat)


    def _transformlat(self, lng, lat):
        ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
              0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
        ret += (20.0 * math.sin(6.0 * lng * self.pi) + 20.0 *
                math.sin(2.0 * lng * self.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(lat * self.pi) + 40.0 *
                math.sin(lat / 3.0 * self.pi)) * 2.0 / 3.0
        ret += (160.0 * math.sin(lat / 12.0 * self.pi) + 320 *
                math.sin(lat * self.pi / 30.0)) * 2.0 / 3.0
        return ret


    def _transformlng(self, lng, lat):
        ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
              0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
        ret += (20.0 * math.sin(6.0 * lng * self.pi) + 20.0 *
                math.sin(2.0 * lng * self.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(lng * self.pi) + 40.0 *
                math.sin(lng / 3.0 * self.pi)) * 2.0 / 3.0
        ret += (150.0 * math.sin(lng / 12.0 * self.pi) + 300.0 *
                math.sin(lng / 30.0 * self.pi)) * 2.0 / 3.0
        return ret

    def WGS84_to_WebMercator(self, lng, lat):
        '''
        实现WGS84向web墨卡托的转换
        :param lng: WGS84经度
        :param lat: WGS84纬度
        :return: 转换后的web墨卡托坐标
        '''
        x = lng * 20037508.342789 / 180
        y = math.log(math.tan((90 + lat) * self.pi / 360)) / (self.pi / 180)
        y = y * 20037508.34789 / 180
        return x, y

    def WebMercator_to_WGS84(self, x, y):
        '''
        实现web墨卡托向WGS84的转换
        :param x: web墨卡托x坐标
        :param y: web墨卡托y坐标
        :return: 转换后的WGS84经纬度
        '''
        lng = x / 20037508.34 * 180
        lat = y / 20037508.34 * 180
        lat = 180 / self.pi * (2 * math.atan(math.exp(lat * self.pi / 180)) - self.pi / 2)
        return lng, lat
```

