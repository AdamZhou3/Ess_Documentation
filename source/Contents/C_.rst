.. role:: raw-html-m2r(raw)
   :format: html


markdown
========

如何目录跳转
^^^^^^^^^^^^

``[内容](地址 "标题")``

锚点与锚点目标（标题）

`markdown 跳转测试 <./C_.html###Dtypes>`_

demo
----

Google Earth Engine
===================

Documents
---------

ImageCollection
^^^^^^^^^^^^^^^

ImageCollection Visualization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collection preparation
""""""""""""""""""""""

Filtering
#########

GAIA 处理
---------

下载GAIA
^^^^^^^^

.. code-block:: python

   import requests
   import re
   url = 'http://data.ess.tsinghua.edu.cn/data/GAIA/GAIA_1985_2018_00_008.tif'
   r = requests.get(url, allow_redirects=True)
   ##if r.headers.get( 'Content-Type')== 'Content-Type':
   r.content

   f = open("demo.txt\")
   line = f.read()
   f.close()

   pattern = re.compile("GAIA_1985_2018(_\\-?\\d{2})(_\\-?\\d{3}).tif\")  
   result = pattern.findall(line)

   for i in result:
   url = "http://data.ess.tsinghua.edu.cn/data/GAIA/GAIA_1985_2018\"+i[0]+i[1]+\".tif\"
   r = requests.get(url, allow_redirects=True)
   name = "GAIA_1985_2018\"+i[0]+i[1]+\".tif\"
   open(\"../GAIA_Data/\"+name, 'wb').write(r.content)"

如何上传到gee
^^^^^^^^^^^^^

``` {.python linenos=""}
!pip install --upgrade google-cloud-storage
!gsutil ls gs://gaia-zzz/

project_id = 'groovy-bay-266911'
import uuid
bucket_name = 'colab-sample-bucket-' + str(uuid.uuid1())
from google.colab import auth
auth.authenticate_user()

!gcloud config set project {project_id}

test
^^^^

with open('/tmp/to\ *upload*\ -01.txt', 'w') as f:
f.write('my sample file')
print('/tmp/to_upload.txt contains:')
!cat /tmp/to\ *upload*\ -01.txt
!gsutil cp /tmp/to\ *upload*\ -01.txt gs://gaia-zzz/

lats = []
lats.append("%02d"% 0 )
for i in range(1,80):
    lats.append("%02d" % i)
    lats.append("%03d" % -i)
for lat in lats:
    AssetID = 'users/zhouzz400/GAIA_2018_lat/GAIA_1985\ *2018*\ '+lat
    ImageFile = 'gs://gaia-zzz/GAIA_1985\ *2018*\ ' + lat + '.tif'

.. code-block::

   ##print(ImageFile,AssetID)
   line = "earthengine --no-use_cloud_api upload image --asset_id={AssetID} --nodata_value=255 {ImageFile}".format(AssetID=AssetID,ImageFile=ImageFile)
   print(line)
   !eval {line}

.. code-block::


   ### gee 投影

   gee 使用geotools 库 不支持Interrupted_Goode_Homolosine 可以使用mollwide
   <https://gis.stackexchange.com/questions/272818/google-earth-engine-reprojection-to-non-epsg-defined-crs>

   <https://spatialreference.org/ref/sr-org/7619>

   python接口会支持吗？

   ``` {.javascript linenos=""}
   var region = "SPA"
   var boun = ee.FeatureCollection("users/zhouzz400/Boundries/worldRegion")
   .filter(ee.Filter.eq("Abbrv",region)).geometry()

   var GAIA = ee.ImageCollection("users/zhouzz400/GAIA")
   .filterBounds(boun).mosaic().clip(boun)
   var GAIA_year = GAIA.gte(4)

   var GAIA_viz = {min:0,max:34,palette:["000000","ff0000"]}
   //Map.addLayer(GAIA,GAIA_viz)

   function getArea(image,boun){
   var area_imag = image.multiply(ee.Image.pixelArea())
   var sumarea = ee.Number(area_imag.reduceRegion(
                   {"reducer": ee.Reducer.sum(),
                   "scale": 30,
                   "geometry":boun
                   })
                   .get("b1") )
   return sumarea}
   var area = getArea(GAIA_year,boun)

   //Lambert cylindrical projection epsg:9843
   // WKT string
   var wkt = ' \
   PROJCS["World_Mollweide", \
       GEOGCS["GCS_WGS_1984", \
       DATUM["WGS_1984", \
           SPHEROID["WGS_1984",6378137,298.257223563]], \
       PRIMEM["Greenwich",0], \
       UNIT["Degree",0.017453292519943295]], \
       PROJECTION["Mollweide"], \
       PARAMETER["False_Easting",0], \
       PARAMETER["False_Northing",0], \
       PARAMETER["Central_Meridian",0], \
       UNIT["Meter",1], \
       AUTHORITY["EPSG","54009"]]';

   var proj_mollweide = ee.Projection(wkt);
   var boun_moll = boun.transform(proj_mollweide,
   ee.ErrorMargin(10))
   print(boun_moll.area(ee.ErrorMargin(1000)))//5010868555175.95
   print(boun.area(ee.ErrorMargin(1000)))//5010868555175.796
   print(boun.area(ee.ErrorMargin(10),proj_mollweide))//5022090468716.392

矢量与栅格总面积是不是相等的？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``` {.javascript linenos=""}
var boun2 = ee.FeatureCollection("users/zhouzz400/Boundries/China_Provinces")
.filter(ee.Filter.eq("Name","湖北省")).geometry()

var GAIA = ee.ImageCollection("users/zhouzz400/GAIA")
.filterBounds(boun2)

Map.addLayer(GAIA.mosaic().clip(boun2))
Map.addLayer(boun2)
print("mosaic area:",getArea(GAIA.mosaic())) //185940066188.5224

function getArea(image){
var a = ee.Image(image).gte(0).clip(boun2)
var area_imag = a.multiply(ee.Image.pixelArea())
var sumarea = ee.Number(area_imag.reduceRegion(
                {"reducer": ee.Reducer.sum(),
                "scale": 300,
                "geometry":boun2
                })
                .get("b1") )
return sumarea
}
var area = GAIA.toList(10).map(getArea).reduce(ee.Reducer.sum())
print("map imgcol area:",area)//185905517767.81976
print("boun area:",boun2.area(ee.ErrorMargin(1)))//186114667454.5676

// peojection area
var wkt = ' \
PROJCS["World_Mollweide", ["GCS_WGS_1984", ["WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Mollweide"],PARAMETER["False_Easting",0],PARAMETER["False_Northing",0],PARAMETER["Central_Meridian",0],UNIT["Meter",1],AUTHORITY["EPSG","54009"]]';

var proj_mollweide = ee.Projection(wkt);
print("boun transform area:",boun2.transform(proj_mollweide,ee.ErrorMargin(1)).area(ee.ErrorMargin(1))) //186114667454.5346
print("boun areapro area:",boun2.area(ee.ErrorMargin(10),proj_mollweide))//186531461977.6914

function getAreaProject(image){
var a = ee.Image(image).gte(0).reproject(proj_mollweide).clip(boun2)
var area_imag = a.multiply(ee.Image.pixelArea())
var sumarea = ee.Number(area_imag.reduceRegion(
                {"reducer": ee.Reducer.sum(),
                "scale": 30,
                "geometry":boun2
                })
                .get("b1") )
return sumarea
}
var area = GAIA.toList(70).map(getArea).reduce(ee.Reducer.sum())
print("img reproject area:",area)//185905517767.81976

mosaic area:
185940066188.5224
map imgcol area:
185905517767.81976
boun area:
186114667454.5676
boun transform area:
186114667454.5346
boun areapro area:
186531461977.6914
img reproject area:
185905517767.81976

.. code-block::


   ### 栅格区域太大时切片计算

   ``` {.javascript linenos=""}
   var b = ee.Array(lslat).reshape([60,1])
   var region = "SPA"
   var boun = ee.FeatureCollection("users/zhouzz400/Boundries/worldRegion")
   .filter(ee.Filter.eq("Abbrv",region)).geometry()
   var bound = ee.List(boun.bounds().coordinates().get(0))
   var pro = boun.bounds().projection()
   print(boun.bounds().coordinates())
   Map.addLayer(boun.bounds())
   var left = ee.Number(ee.List(bound.get(0)).get(0)).floor()
   var right = ee.Number(ee.List(bound.get(1)).get(0)).ceil()
   var down = ee.Number(ee.List(bound.get(0)).get(1)).floor()
   var up = ee.Number(ee.List(bound.get(2)).get(1)).ceil()

   //92,236,-30,29
   var rec = ee.Geometry.Rectangle([left, down,right, up],null,false)

   // var ls = ee.List([])
   // for(var i = left; i < right; i++) {
   //   for (var j = down; i< up; i++){
   //     var rec = ee.Geometry.Rectangle([i, j,i.add(1), j.add(1)],null,false)
   //     ls.evaluate(function(rec){  //行不通，push不进去
   //       ls.add(rec)
   //       return ls})
   //   }
   // }

   // var lslat = ee.List.sequence(down,up)
   // var lslng = ee.List.sequence(left,right)
   var down = ee.Number(0)
   var left = ee.Number(90)
   var lslat = ee.List.sequence(down,down.add(10))
   var lslng = ee.List.sequence(left,left.add(10))
   var ls = lslat.map(function(lat){
   var y = lslng.map(function(lng){
   return ee.List([lat,lng])
   })
   return y
   })

   //var array = ee.Array(ls).reshape([8700,2])
   var array = ee.Array(ls).reshape([121,2])
   var rect = array.toList().map(function(point){
   var x = ee.Number(ee.List(point).get(0))
   var y = ee.Number(ee.List(point).get(1))
   var rec = ee.Geometry.Rectangle([y,x.subtract(1) ,y.add(1), x],null,false)
   return rec
   })
   //var rectg = ee.List(ee.Geometry.MultiPolygon(rect))
   Map.addLayer(ee.Geometry.MultiPolygon(rect))
   var area = rect.map(function(fets){
   var fet = ee.Geometry(fets)
   var GAIA = ee.ImageCollection("users/zhouzz400/GAIA")
   .filterBounds(fet).mosaic().clip(fet).gte(0)
   var a = ee.Image(GAIA)
   var area_imag = a.multiply(ee.Image.pixelArea())
   var sumarea = ee.Number(area_imag.reduceRegion(
               {"reducer": ee.Reducer.sum(),
               "scale": 300,
               "geometry":fet
               })
               .get("b1") )
   return sumarea
   })
   var area = area.reduce(ee.Reducer.sum())
   print(area)
   //3151140115.2027273
   //6305539433.349972
   //1482707901266.5425

造掩膜填空
^^^^^^^^^^

``` {.javascript linenos=""}
var region = "SPA"
var boun = ee.FeatureCollection("users/zhouzz400/Boundries/worldRegion")
.filter(ee.Filter.eq("Abbrv",region)).geometry()

var GAIA = ee.ImageCollection("users/zhouzz400/GAIA")
.filterBounds(boun).mosaic().clip(boun)
var GAIA_viz = {min:0,max:34,palette:["000000","ff0000"]}
//Map.addLayer(GAIA,GAIA_viz)

var GAIA_masked = GAIA.updateMask(GAIA.gte(1))
var emp = ee.Image.constant(0).select(["constant"],["b1"])
//print(emp.get("system:band_names"))
//print(emp.propertyNames())
print(emp)
var x = ee.ImageCollection([GAIA_masked,emp]).mosaic()
Map.addLayer(x,{min:0,max:1,palette:["000000","ff0000"]})
print(x)

.. code-block::


   ``` {.javascript linenos=""}
   var region = "SPA"
   var boun = ee.FeatureCollection("users/zhouzz400/Boundries/worldRegion")
   .filter(ee.Filter.eq("Abbrv",region)).geometry()

   var GAIA = ee.ImageCollection("users/zhouzz400/GAIA")
   .filterBounds(boun).mosaic()

   var emp = ee.Image(1).select(["constant"],["b1"])

   var GAIA_mask = GAIA.mask().toUint8()
   var mask= ee.ImageCollection([GAIA_mask,GAIA]).mosaic().reduce(ee.Reducer.min())
   var g = GAIA.updateMask(mask)
   Map.addLayer(g,{min:0,max:34,palette:["000000","ff0000"]})

   var bound = ee.List(boun.bounds().coordinates().get(0))
   var pro = boun.bounds().projection()
   Map.addLayer(boun.bounds())
   var left = ee.Number(ee.List(bound.get(0)).get(0)).floor()
   var right = ee.Number(ee.List(bound.get(1)).get(0)).ceil()
   var down = ee.Number(ee.List(bound.get(0)).get(1)).floor()
   var up = ee.Number(ee.List(bound.get(2)).get(1)).ceil()

   //92,236,-30,29

   var rec = ee.Geometry.Rectangle([left, down,right, up],null,false)

   var lslat = ee.List.sequence(down,up)
   var lslng = ee.List.sequence(left,right)
   var ls = lslat.map(function(lat){
   var y = lslng.map(function(lng){
       return ee.List([lat,lng])
   })
   return y
   })

   var array = ee.Array(ls).reshape([8700,2])
   var rect = array.toList().map(function(point){
   var x = ee.Number(ee.List(point).get(0))
   var y = ee.Number(ee.List(point).get(1))
   var rec = ee.Geometry.Rectangle([y,x.subtract(1) ,y.add(1), x],null,false)
   return rec
   })
   //var rectg = ee.List(ee.Geometry.MultiPolygon(rect))
   Map.addLayer(ee.Geometry.MultiPolygon(rect))
   var area = rect.map(function(fets){
   var fet = ee.Geometry(fets)
   var a = ee.Image(g.clip(boun).gte(3))
   var area_imag = a.multiply(ee.Image.pixelArea())
   var sumarea = ee.Number(area_imag.reduceRegion(
                   {"reducer": ee.Reducer.sum(),
                   "scale": 300,
                   "geometry":fet
                   })
                   .get("b1") )
   return sumarea
   })
   var area = area.reduce(ee.Reducer.sum())
   print(area)

``` {.javascript linenos=""}
var bound = ee.List(boun.bounds().coordinates().get(0))
var pro = boun.bounds().projection()
Map.addLayer(boun.bounds())
var left = ee.Number(ee.List(bound.get(0)).get(0)).floor()
var right = ee.Number(ee.List(bound.get(1)).get(0)).ceil()
var down = ee.Number(ee.List(bound.get(0)).get(1)).floor()
var up = ee.Number(ee.List(bound.get(2)).get(1)).ceil()

//92,236,-30,29

var rec = ee.Geometry.Rectangle([left, down,right, up],null,false)
var down = ee.Number(0)
var lslat = ee.List.sequence(down,down.add(14),6)
var lslng = ee.List.sequence(left,left.add(24),6)
// var lslat = ee.List.sequence(down,up)
// var lslng = ee.List.sequence(left,right)
var ls = lslat.map(function(lat){
var y = lslng.map(function(lng){
    return ee.List([lat,lng])
})
return y
})
var array = ee.Array(ls).reshape([15,2])

var rect = array.toList().map(function(point){
var x = ee.Number(ee.List(point).get(0))
var y = ee.Number(ee.List(point).get(1))
var rec = ee.Geometry.Rectangle([y,x.subtract(6) ,y.add(6), x],null,false)
return rec
})
//var rectg = ee.List(ee.Geometry.MultiPolygon(rect))
Map.addLayer(ee.Geometry.MultiPolygon(rect))
var area = rect.map(function(fets){
var fet = ee.Geometry(fets)
var a = ee.Image(g.clip(boun).gte(3))
var area_imag = a.multiply(ee.Image.pixelArea())
var sumarea = ee.Number(area_imag.reduceRegion(
                {"reducer": ee.Reducer.sum(),
                "scale": 300,
                "geometry":fet
                })
                .get("b1") )
return sumarea
})
var area = area.reduce(ee.Reducer.sum())
print(area)

.. code-block::


   ### GAIA 数据提取

   ``` {.javascript linenos=""}
   var year_dic = ee.Dictionary({34:1985,33:1986,32:1987,31:1988,
       30:1989,29:1990,28:1991,27:1992,26:1993,25:1994,24:1995,23:1996,22:1997,21:1998,
       20:1999,19:2000,18:2001,17:2002,16:2003,15:2004,14:2005,13:2006,12:2007,11:2008,
       10:2009, 9:2010, 8:2011, 7:2012, 6:2013, 5:2014, 4:2015, 3:2016, 2:2017, 1:2018,})
   var yDic = ee.List([34,29,24,19,14,9,4,1])

   var gaia = ee.ImageCollection("users/zhouzz400/GAIA")
       .filterBounds(geometry).mosaic().clip(geometry)
   //Map.addLayer(gaia,{min:1,max:34,palette:["white","blue","red"]})
   Map.addLayer(gaia.gte(33)) //  1986年

焦点统计 密度计算 转矢量
^^^^^^^^^^^^^^^^^^^^^^^^

``` {.javascript linenos=""}
// 34年渐变
var sh = ee.Image("users/zhouzz400/shanghai_GAIA");
print(sh);

var Viz_Color =  {palette:['blue', 'purple', 'cyan', 'green', 'yellow', 'red']}
var Viz_GAIA = {min: 1, max: 34, palette: ['FFFFFF', 'FF0000']};
Map.addLayer(sh,Viz)

// 某一年不透水面
var sh_10 = sh.gte(9)

var Viz2 = {min: 0, max: 1, palette: ['FFFFFF', 'FF0000']};
Map.addLayer(sh_10,Viz2)

// 焦点统计
var ker_sq = ee.Kernel.square({
radius: 3, units: 'pixels', normalize: false
});

// ee.Kernel.circle(7)
var ker_st = sh_10.reduceNeighborhood({
reducer: ee.Reducer.mean(),
kernel: ker_sq,
});

var des_25 = ker_st.gte(0.25).selfMask().rename('Dens_25');
//Map.addLayer(des_25,Viz4)
//print(des_25)

// 识别斑块
var objectId = des_25.connectedComponents({
connectedness: ee.Kernel.plus(1),
maxSize: 256
});
Map.addLayer(objectId.randomVisualizer(), null, 'Objects');

// 栅格转矢量
var des_25_v = des_25.reduceToVectors({
scale: 80,
geometryType: 'polygon',
eightConnected: false,
labelProperty: 'zone',}
);
Map.addLayer(des_25_v);

.. code-block::


   ### 层级焦点统计

   焦点统计与focal的区别？ kernel种类对focal的影响。

   ``` {.javascript linenos="
   var Viz_GAIA = {min: 1, max: 34, palette: ['FFFFFF', 'FF0000']};
   Map.addLayer(sh,Viz_GAIA)

   var sh_10 = sh.gte(9)

   var ker_sq = ee.Kernel.circle({
   radius: 10, units: 'pixels', normalize: false
   });

   // ee.Kernel.circle(7)
   var ker_st1 = sh_10.reduceNeighborhood({
   reducer: ee.Reducer.mean(),
   kernel: ker_sq,
   });

   var Viz_Dens = {min: 0, max: 1, palette: ['FFFFFF', 'FF0000']};
   var des_50_1 = ker_st1.gte(0.7);
   Map.addLayer(des_50_1,Viz_Dens)
   print(des_50_1)

   var ker_st2 = des_50_1.reduceNeighborhood({
   reducer: ee.Reducer.mean(),
   kernel: ker_sq,
   });

   var des_50_2 = ker_st2.gte(0.7);
   Map.addLayer(des_50_2,Viz_Dens)
   print(des_50_2)


   var ker_st3 = des_50_2.reduceNeighborhood({
   reducer: ee.Reducer.mean(),
   kernel: ker_sq,
   });

   var des_50_3 = ker_st3.gte(0.7);
   Map.addLayer(des_50_3,Viz_Dens)
   print(des_50_3)

   var objectId = des_50_3.connectedComponents({
   connectedness: ee.Kernel.plus(1),
   maxSize: 256
   });
   Map.addLayer(objectId.randomVisualizer(), null, 'Objects');"}

城市中心与Buffer
^^^^^^^^^^^^^^^^

``` {.javascript linenos=""}
var fid = ee.Number(857683023); //墨西哥城
var center = ee.FeatureCollection("users/zhouzz400/Boundries/city_center")
    .filter(ee.Filter.eq("wof_id",fid)).geometry();
var region = center.buffer(31000)
var GAIA = ee.ImageCollection("users/zhouzz400/GAIA")
    .filterBounds(region).mosaic().clip(region)
var gaia_viz = {min:0,max:34,palette:["FFFFFF","FF0000"]}
Map.addLayer(GAIA,gaia_viz)

.. code-block::


   ### function

   ``` {.javascript linenos=""}
   function func1(yIndex){
       yIndex = ee.Number(yIndex)
       var year = ee.Number(year_dic.get(yIndex))
       var GAIA_year = GAIA.gte(yIndex)
       var water = ee.ImageCollection("JRC/GSW1_1/YearlyHistory")
           .filter(ee.Filter.eq("year",year)).first().neq(1)
       var dis_list = ee.List.sequence(1000,30000,1000)
       function getUrban(dis){
           var buffer = center.buffer(dis)
           var buffer_urban = GAIA_year.eq(1).clip(buffer)
           var area_imag = buffer_urban.multiply(ee.Image.pixelArea());
           var sumarea = ee.Number(area_imag.reduceRegion({"reducer": ee.Reducer.sum(),"scale": 30,"maxPixels": 1e9}).get("b1") )
           return sumarea
       }
       var areaA_urban = dis_list.map(getUrban)
       return areaA_urban
   }
   print(func1(34))
   var res = yDic.map(func1)
   print(res)

获取中心
^^^^^^^^

``` {.javascript linenos=""}
var imageCollection = ee.ImageCollection("NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG"),
    imageCollection2 = ee.ImageCollection("NOAA/DMSP-OLS/NIGHTTIME_LIGHTS"),
    table = ee.FeatureCollection("users/zhouzz400/Boundries/China_Provinces");
// // var imgc = imageCollection.filterDate("2014-01-01","2016-01-01").select("avg_rad");
// var imgc = imageCollection2.filterDate("2011-01-01","2012-01-01").select("stable_lights");
// var img = imgc.reduce(ee.Reducer.max()).clip(table)
// //var img = imgc.first()
// var viz = {min:0,max:60,palette:["000000","0000FF","FF0000"]}
// //Map.addLayer(img,viz);
// print(img)

// var ker_sq = ee.Kernel.square({
//   radius: 10, units: 'pixels', normalize: false
// });

//     // ee.Kernel.circle(7)
// var ker_st = img.reduceNeighborhood({
//   reducer: ee.Reducer.mean(),
//   kernel: ker_sq,
// }).gte(63).eq(1);

// //var viz2 = {min:0,max:1,palette:["cccccc","FF0000"],opacity:0.5}
// var viz3 = {min:0,max:1,palette:["cccccc","0000FF"]}
// //Map.addLayer(img.gte(63).eq(1),viz2);
// Map.addLayer(ker_st,viz3);
// print(ker_st);

// // // Define a boxcar or low-pass kernel.
// // var boxcar = ee.Kernel.square({
// //   radius: 100, units: 'pixels', normalize: true
// // });

// // // Smooth the image by convolving with the boxcar kernel.
// // var smooth = ker_st.convolve(boxcar);
// // Map.addLayer(smooth);

// var center_area = ker_st.eq(1).selfMask();
// Map.addLayer(center_area, {palette: 'FF00FF'});

// var objectId = center_area.connectedComponents({
//   connectedness: ee.Kernel.plus(1),
//   maxSize: 256
// }).select("stable_lights_max_mean");
// //Map.addLayer(objectId.randomVisualizer(), null, 'Objects');
// print(objectId)
// // Compute the number of pixels in each object defined by the "labels" band.

// var des_25_v = objectId.reduceToVectors({
//   geometry: table,
//   scale:3000,
//   geometryType: 'polygon',
//   eightConnected: false,
//   }
//   );
// // Display object pixel count to the Map.
// Map.addLayer(des_25_v);
// print(des_25_v)

var modis = ee.Image(ee.ImageCollection('OREGONSTATE/PRISM/AN81d').first())
    .select('ppt');
var proj = modis.projection();
// Load a Japan boundary from the Large Scale International Boundary dataset.
var japan = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')
.filter(ee.Filter.eq('country_na', 'France'));

// Load a 2012 nightlights image, clipped to the Japan border.
// var nl2012 = ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F182013')
//   .select('stable_lights')
//   .clipToCollection(japan)
// //  .reproject({crs:"SR-ORG:6974"});
// Map.addLayer(nl2012)
var nl = ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F182013')
var projnl = nl.projection() 

var nl2012 = ee.ImageCollection('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS')
    .filterDate("1993-01-01","2014-01-01")
    .select('stable_lights')
    .reduce(ee.Reducer.mean())
    .reproject({crs:projnl})
    .clipToCollection(japan)
print(nl2012.projection())
// 
// .reduce(ee.Reducer.mean()) )
// .clipToCollection(japan)
//  .reproject({crs:"SR-ORG:6974"});
Map.addLayer(nl2012)

var zones2 = nl2012.reduceResolution({
reducer:ee.Reducer.mean(),
maxPixels:1024,}).reproject({
    crs:proj
});

var zones3 = zones2.gte(60).selfMask()
// Define arbitrary thresholds on the 6-bit nightlights image.
print(zones3);
//Map.addLayer(zones3,{min:0,max:1,palette:["000000","FF00FF"]});

//SR-ORG:6974

var objectId = zones3.connectedComponents({
    connectedness: ee.Kernel.plus(1),
    maxSize: 256
    }).select("stable_lights_mean");
Map.addLayer(objectId.randomVisualizer(), null, 'Objects');
print(objectId);
// Compute the number of pixels in each object defined by the "labels" band.

var des_25_v = objectId.reduceToVectors({
    geometry: japan,
    scale:3000,
    tileScale :4,
    geometryType: 'polygon',
    eightConnected: false,
})
// Display object pixel count to the Map.
Map.addLayer(des_25_v,{palette:"ffffff"});
print(des_25_v)

var getCentroid = function(feature){
    //var keepProperties = ['name', 'huc6', 'tnmid', 'areasqkm'];
    // Get the centroid of the feature's geometry.
    var centroid = feature.centroid(ee.ErrorMargin(10000));
    // Return a new Feature, copying properties from the old Feature.
    return ee.Feature(centroid)//.copyProperties(feature, keepProperties);
};

// Map the centroid getting function over the features.
var centroids = des_25_v.map(getCentroid);

// Display the results.
Map.addLayer(centroids, {color: 'FF0000'}, 'centroids');

print(centroids)

.. code-block::


   ### 下载数据

   ``` {.javascript linenos=""}
   var water1 = ee.Image("JRC/GSW1_1/YearlyHistory/1995")
   var water2 = ee.Image("JRC/GSW1_1/YearlyHistory/1996")
   var image = ee.ImageCollection([water1,water2])
       .reduce(ee.Reducer.mean()).rename("FVC").toFloat()
   print(image)
   var geometry = ee.Geometry.Rectangle([179, 90, 180, 89.9]);
   Export.image.toDrive({
       image: image,
       description: 'YearlyHistory/1995',
       scale: 30,
       region: geometry,
       fileFormat: 'GeoTIFF',
   });

Gallery
-------

区域均值
^^^^^^^^

``` {.javascript linenos=""}
var point = /\ * color: ##98ff00 *\ /ee.Geometry.Point([114.3362584771894, 30.54952805541824]),
    l8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_TOA"),
    bare = /\ * color: ##c24823 *\ /ee.Geometry.Polygon(
        [[[114.30517811719619, 30.554663336996253],
        [114.30161614362441, 30.552224189574872],
        [114.30958338525011, 30.55368954007891],
        [114.30803843285753, 30.5546134528199]]]),
    veget = /\ * color: ##ff0000 *\ /ee.Geometry.Polygon(
        [[[114.48716604174274, 30.507213819178254],
        [114.4845928059624, 30.5054401948097],
        [114.48682294356126, 30.505144587441116],
        [114.4883667488358, 30.505144633458844],
        [114.49162631694242, 30.504848979348527],
        [114.49368490531106, 30.506622614826078]]]),
    water = /\ * color: ##00ff00 *\ /ee.Geometry.Polygon(
        [[[114.28774101355862, 30.565245523015815],
        [114.28482277015041, 30.561845853255953],
        [114.28516609290432, 30.5602198821312],
        [114.28774101355862, 30.559480795340228],
        [114.29237587073635, 30.563619608862606]]]);

var bands = ["B2","B3","B4","B5","B6","B7"];
var image = ee.Image(l8
.filterBounds(point)
.sort("CLOUD_COVER")
.first())
.select(bands);

Map.addLayer(image,{bands:["B4","B3","B2"],max:0.3},"image");

var bareMean = image.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:bare,
scale:30,
}).values();

var vegetMean = image.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:veget,
scale:30,
}).values();

var waterMean = image.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:water,
scale:30,
}).values();

var chart = ui.Chart.image.regions(image,ee.FeatureCollection([
ee.Feature(bare, {label:"bare"}),
ee.Feature(veget,{label:"vaget"}),
ee.Feature(water,{label:"water"})]),
ee.Reducer.mean(),30,"label",[0.48,0.56,0.65,0.86,1.61,2.2]
);
print(chart);

var endmembers = ee.Array.cat([bareMean,vegetMean,waterMean],1);
var arrayImage = image.toArray().toArray(1);
var unmixed = ee.Image(endmembers).matrixSolve(arrayImage);
var unmixedImage = unmixed.arrayProject([0])
                        .arrayFlatten([["bare","veget","water"]]);
Map.addLayer(unmixedImage,{},"fractions")

.. code-block::


   ### landsat可视化

   ``` {.javascript linenos=""}
   //loading the image using the image ID
   var Souht_Texas = ee.Image("LANDSAT/LC8_L1T/LC80260412016037LGN00")

   //zoom to the image
   Map.centerObject(Souht_Texas,10);

   var Color = {bands:["B5","B4","B3"],min: 5000,max: 15000,gamma: [0.95,1.1,1]};

   //add the image to the map at 
   Map.addLayer(Souht_Texas,Color,"True Color");

``` {.javascript linenos=""}
//Location for bounds, in this case the city of El Paso,Use the inspector tool
var city= ee.Geometry.Point(114.3,30.6);

// Create a variable using the Geometry function Point,lat and lon
//Add the point to the map
Map.addLayer(city);

//Datas of intrest
var start = ee.Date("2013-5-30");
var finish = ee.Date("2015-12-1");

//create image collection
var Wuhan = ee.ImageCollection("LANDSAT/LC08/C01/T1")
.filterBounds(city)
.filterDate(start,finish)
.sort("CLOUD_COVER",false);

// Get the number of image 
var count = Wuhan.size();
print("size of collection Wuhan",count);

//Sort by a cloud cover property,get the least cloud image
var Best = ee.Image(Wuhan.sort("CLOUD_COVER").first());
print("size of collection Wuhan",Best);

//get metadata
var data = Best.get("DATE_ACQUIRED")
print("date taken",data)

Map.centerObject(Wuhan,10);

var Color = {bands:["B4","B3","B2"],min: 5000,max: 15000,gamma: [0.95,1.1,1]};

//add the image to the map at 
Map.addLayer(Best,Color,"True Color");

.. code-block::


   ### NDVI

   ``` {.javascript linenos="
   //Location for bounds, in this case the city of El Paso,Use the inspector tool
   var city= ee.Geometry.Point(114.3,30.6);

   // Create a variable using the Geometry function Point,lat and lon
   //Add the point to the map
   Map.addLayer(city);

   //Datas of intrest
   var start = ee.Date(\"2013-5-30\");
   var finish = ee.Date(\"2015-12-1\");

   //create image collection
   var Wuhan = ee.ImageCollection(\"LANDSAT/LC08/C01/T1\")
   .filterBounds(city)
   .filterDate(start,finish)
   .sort(\"CLOUD_COVER\",false);

   // Get the number of image 
   var count = Wuhan.size();
   print(\"size of collection Wuhan\",count);

   //Sort by a cloud cover property,get the least cloud image
   var Best = ee.Image(Wuhan.sort(\"CLOUD_COVER\").first());
   print(\"size of collection Wuhan\",Best);

   //get metadata
   var data = Best.get(\"DATE_ACQUIRED\")
   print(\"date taken\",data)

   Map.centerObject(Wuhan,10);

   var Color = {bands:[\"B4\",\"B3\",\"B2\"],min: 5000,max: 15000,gamma: [0.95,1.1,1]};

   //add the image to the map at 
   Map.addLayer(Best,Color,\"True Color\");

   //----------------------------------------------------------------
   var B4_Red = Best.select(\"B4\");
   var B5_NIR = Best.select(\"B5\");

   var ndvi1 = B5_NIR.subtract(B4_Red).divide(B5_NIR.add(B4_Red));

   var ndvi2 = Best.expression(
   \"(B5-B4)/(B5+B4\",{
       \"B5\": B5_NIR,
       \"B4\": B4_Red
   });
   var ndvi_palette =
   'FFFFFF, CE7E45, DF923D, F1B555, FCD163, 99B718, 74A901, 66A000, 529400,'+
   '3E8601, 207401, 056201, 004C00, 023B01, 012E01, 011D01, 011301';

   Map.addLayer(ndvi1,{min:-0.1,max:0.1,palette:ndvi_palette},\"NDVI 1\")"}

火灾
^^^^

``` {.javascript linenos=""}
var dataset = ee.ImageCollection('MODIS/006/MCD64A1')
                .filter(ee.Filter.date('2019-01-01', '2020-01-01'));
var burnedArea = dataset.select('BurnDate');
var burnedAreaVis = {
min: 30.0,
max: 365.0,
palette: ['4e0400', '951003', 'c61503', 'ff1901'],
};
Map.setCenter(6.746, 46.529, 2);
Map.addLayer(burnedArea, burnedAreaVis, 'Burned Area');

.. code-block::


   ### function compute area

   ``` {.javascript linenos=""}
   var Cities = ee.FeatureCollection("users/zhouzz400/Boundries/China_Cities")
   print(Cities);

   function Add_Area(feature){
   var the_Area = ee.Number(feature.area())
   return feature.set("Area_km2",the_Area.divide(1000*1000))
   }

   var City_with_Area = Cities.map(Add_Area);

   print(Cities.first(),City_with_Area.first());

function compute NDVI
^^^^^^^^^^^^^^^^^^^^^

``` {.javascript linenos=""}
var L8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_TOA")
.filterBounds(ee.Geometry.Point(107.193,29.1373))
.filterDate("2019-01-01","2020-01-01")
.select("B[4,5]")
.limit(3);

function add_NDVI(image){
var NDVI = image.normalizedDifference(["B5","B4"]);
return image.addBands(NDVI);
}

var L8_NDVI = L8.map(add_NDVI);

print(L8.first(),L8_NDVI.first());
Map.addLayer(L8_NDVI.select("nd"));
Map.addLayer(L8.limit(1).select("B[4,5]").mean());

.. code-block::


   ### focal 斑块

   ``` {.javascript linenos=""}
   var table2 = ee.FeatureCollection("users/zhouzz400/Boundries/UrbanDensity50_2015"),
       table = ee.FeatureCollection("users/zhouzz400/Boundries/UrbanDensity100_2015"),
       geometry = ee.Geometry.Polygon(
           [[[100.99709998976684, 33.5381776358804],
           [100.99709998976684, 22.143132836963183],
           [126.17776405226684, 22.143132836963183],
           [126.17776405226684, 33.5381776358804]]], null, false);
   var demo = table2.filterBounds(geometry).map(function (feature){ 
       return feature.set({demo:1}).centroid();
   })
   Map.addLayer(table2)
   Map.addLayer(demo)
   var demo2 = table2.filterBounds(geometry).map(function (feature){ 
       return feature.set({demo:1});
   })
   // print(demo.limit(3))
   var image = demo2.reduceToImage(ee.List(["demo"]),ee.Reducer.anyNonZero())

   var focal_2 = image.focal_min(1,"plus","pixels",15)
   Map.addLayer(image)
   Map.addLayer(focal_2)

双变量循环
^^^^^^^^^^

``` {.javascript linenos=""}
var X = ee.List([1,2,3])
var Y = ee.List([1,2,3])
var Z = X.map(function (x){
return Y.map(function(y){
    return x+y
})
})

.. code-block::


   ### iterate

   ``` {.javascript linenos=""}
   var table = ee.FeatureCollection("users/rawailnaeem/CA");
   var S1 = ee.ImageCollection("COPERNICUS/S1_GRD");
   Map.addLayer(table);

   var t = table.limit(1000);
   print(t);
   var Sentinel1 = S1.filterMetadata('instrumentMode', 'equals', 'IW')
                   .filterDate('2016-04-01','2016-08-30' )
                   .filterMetadata('resolution_meters', 'equals' , 10)
                   .filterBounds(t);

   var S1dates = Sentinel1.toList(Sentinel1.size()).map(function(img){
   var idate = ee.Image(img).date();
   return ee.Date.fromYMD(
       idate.get('year'),
       idate.get('month'),
       idate.get('day')
   ).millis()
   });

   // print images dates
   print(S1dates.map(function(millis) {
   return ee.Date(millis).format();
   }));

   var newfc = ee.List(t.iterate(function(feat, ini){
   // cast
   var ini = ee.List(ini);
   var feat = ee.Feature(feat);

   // get src date
   var srcd = ee.String(feat.get('SrcImgDate'));
   var year = ee.Number.parse(srcd.slice(0, 4));
   var month = ee.Number.parse(srcd.slice(4, 6));
   var day = ee.Number.parse(srcd.slice(6, 8));

   var date = ee.Date.fromYMD(year, month, day).millis();

   var condition = S1dates.contains(date);

   return ee.Algorithms.If(condition, ini.add(feat), ini);
   }, ee.List([])));

   var newfc = ee.FeatureCollection(newfc);

   print(newfc);

Courses
-------

string
^^^^^^

``` {.javascript linenos=""}
// create
var string = ee.String("helloworld");
// display
print(string);

// change
var cat_string = string.cat("demo");
print(cat_string);
var rep_string = cat_string.replace("d","zz","g");//global match
print(rep_string);

// split
var spl_string = string.split("o");
print(spl_string);

// match
var mat_string = string.match("o");
print(mat_string);

// slice
var sli_string = string.slice(1,5);
print(sli_string);

// length
var len_string = string.length()
print(string, len_string)

// ### number
var numb1 = ee.Number(1237834050);
var numb2 = ee.Number(-3.1435963);

// transfer
var int_numb2 = numb2.int8()
// int = toInt double = toDouble float = toFloat
print(int_numb2)

// compare
// eq neq gt gte lt lte
// and or not

// calculate
//floor round ceil  abs sqrt exp log log10

// bitwise
var numb3 = ee.Number(1);
var numb4 = ee.Number(2);
var numb_And = numb3.bitwiseAnd(numb4);
var num_Or = numb3.bitwiseOr(numb4);
print(numb_And,num_Or);
// leftshift

// a great examp
    // var meal= rice(50).wash(100, fliter).zheng(100).cheng(12,A>B)

.. code-block::


   ### dictionary

   ``` {.javascript linenos=""}
   // create ee.Dictionary()
   var Dic_1 = ee.Dictionary({
   Name:"demo",
   Age:"20"
   })
   var Dic_2 = ee.Dictionary({
   Weight:"30",
   Hight:"30"
   })

   // change dic.combine() dic.set()
   var Dic_combine = Dic_1.combine(Dic_2,true);//use second first when conflict
   print(Dic_combine);

   var Dic_3 = Dic_1.set("Age","30"); // add or change
   print(Dic_3);

   // iquiry dic.keys dic.get dic.values
   print(Dic_1.keys());
   print(Dic_1.values().slice(1,2));
   print(Dic_1.get("Name"));

   // compare dic.contains
   print(Dic_1.contains("Height")); // if exsist?

   // size dic.size()
   print(Dic_1.size());

reducer
^^^^^^^

``` {.javascript linenos=""}
// .count/.countEvery/.first()
var Reducer_Count = ee.Reducer.count();
var Reducer_CountEvery = ee.Reducer.countEvery();
var Reducer_First = ee.Reducer.first();

var Provinces_Number_1 = China_Provinces.reduceColumns(
Reducer_Count,["Name"]);
var Provinces_Number_2 = China_Provinces.reduceColumns(
Reducer_CountEvery,[]); // count every columns
var Provinces_First = China_Provinces.reduceColumns(
Reducer_First,["Name"]);

Map.addLayer(China_Provinces);
print(China_Provinces);
print("Reducer_Count",Provinces_Number_1);
print("Reducer_CountEvery",Provinces_Number_2);
print("Refucer_First",Provinces_First);

// .frequencyHistogram()
print(China_Cities.limit(10));
var FrequencyHiso_Reducer = ee.Reducer.frequencyHistogram();
var City_Frequency = China_Cities.reduceColumns(FrequencyHiso_Reducer,["省份"]);

var Fig_Histo = ui.Chart.feature.histogram(China_Cities,"省份");
print(City_Frequency,Fig_Histo);
Map.addLayer(China_Cities);

// .allNonZero/.anyNonZero()
var No_Zero_Reducer = ee.Reducer.allNonZero();
var Any_Non_Zero_Reducer = ee.Reducer.anyNonZero();
var List_Test_1 = ee.List([1,2,3,5,9]);
var List_Test_2 = ee.List([1,4,5,6,0]);

var Result_1 = List_Test_1.reduce(No_Zero_Reducer);
var Result_2 = List_Test_1.reduce(Any_Non_Zero_Reducer);
var Result_3 = List_Test_2.reduce(No_Zero_Reducer);
var Result_4 = List_Test_2.reduce(Any_Non_Zero_Reducer);

print("Result_1",Result_1);
print("Result_2",Result_2);
print("Result_3",Result_3);
print("Result_4",Result_4);

// .toList()
print(China_Cities.first());
var Tolist_Reducer = ee.Reducer.toList();
var City_List = China_Cities.reduceColumns(Tolist_Reducer, ["Prefecture"]);
print(City_List);

// .toCollection()
var Reducer_to_Collection = ee.Reducer.toCollection(["provinces","cities"]);//rename
print(Reducer_to_Collection);
var City_Collection = China_Cities.reduceColumns(Reducer_to_Collection,["省份","Prefecture"]);
print(City_Collection);

// .product/ sum/ mean/variance/sampleVariance/stdDev/sampleStdDev
function Add_Area(feature){
var The_Area = ee.Number(feature.area());
return feature.set("Area_km2", The_Area.divide(1000*1000));
}
var City_WithArea = China_Cities.map(Add_Area);
print(City_WithArea)
var Reducer_Product = ee.Reducer.product();
//var Reducer_Product = ee.Reducer.product();sum,mean,variance,sampleVariance,stdDev
var Area_Product = City_WithArea.reduceColumns(Reducer_Product,["Area_km2"]);
print("Area_Product", Area_Product)

// .max/min/minMax/median/mode
var Reducer_Max = ee.Reducer.max()
var Area_Max = City_WithArea.reduceColumns(Reducer_Max,["Area_km2"])
print("Area_Max",Area_Max)

// image max
var image = image.select(["B4","B3","B2"]);
var maxValue = image.reduce(ee.Reducer.max());
Map.centerObject(image,8);//zoom
Map.addLayer(maxValue,{max:13000},"Maximum value image");

// intervalMean/percentile
// 0, 50 mean

// linearFit()
var Data_X = ee.List([12,13,14,5]);
var Data_Y = ee.List([14,12,41,14]);

var Linear_Reducer = ee.Reducer.linearFit();
var Fited = ee.List([Data_X,Data_Y]).reduce(Linear_Reducer);
print(Fited);

// linearFit use to pridict weather
var createTimeBand = function(image){
return image.addBands(image.metadata("system:time_start").divide(1e18));
}
var collection = ee.ImageCollection("NASA/NEX-DCP30_ENSEMBLE_STATS")
.filter(ee.Filter.eq("scenario","rcp85"))
.filterDate(ee.Date("2006-01-01"),ee.Date("2050-01-01"))
.map(createTimeBand);
var linearFit = collection.select(["system:time_start","pr_mean"])
.reduce(ee.Reducer.linearFit());
print(linearFit);
Map.addLayer(linearFit,
{min:0,
max:[-0.9,8e-5,1],
bands:["scale","offset","scale"]},
"fit");
// setOutputs/getOutputs
var Reducer_Original = ee.Reducer.minMax();
var Reducer_Modified = Reducer_Original.setOutputs(["Range_Low","Range_High"]);
print("Original",Reducer_Original.getOutputs());
print("Modified",Reducer_Modified.getOutputs());

// combine
var Reducer_Max = ee.Reducer.max();
var Reducer_Min = ee.Reducer.min();
var Reducer_Combine = Reducer_Max.combine(Reducer_Min);

var Array_Example = ee.Array([[1,2],
                            [3,4]]); // axis = 0 updown

var Combine_Reduced_1 = Array_Example.reduce(
Reducer_Combine, [0], 1);// direction 0 field axis
var Combine_Reduced_2 = Array_Example.reduce(
Reducer_Combine, [1], 0);

print("Max of [1,3] and min of [2,4]",Combine_Reduced_1);
print("Max of [1,2] and min of [3,4]",Combine_Reduced_2);

// repeat
var China_Cities = ee.FeatureCollection("users/zhouzz400/Boundries/China_Cities");
var Reducer_Repeat = ee.Reducer.frequencyHistogram().repeat(2);
var Province_City_Frequency = China_Cities.reduceColumns(Reducer_Repeat,["Prefecture","省份"]);
print(Province_City_Frequency);

// group
var countries = ee.FeatureCollection("ft:1S4EB6319wWW2sWQDPhDvmSBIVrD3iEmCLYB7nMM");
var sums = countries
.filter(
    ee.Filter.and(
    ee.Filter.neq("Census 2000 Population",null),
    ee.Filter.neq("Census 2000 Housing Units", null))
)
.reduceColumns({
    selectors:["Census 2000 Population",
    "Census 2000 Housing Units","StateName"],
    reducer:ee.Reducer.sum().repeat(2).group({
    groupField:2,
    groupName:"state",})
});
print(sums);

.. code-block::


   ### kernel

   ``` {.javascript linenos=""}
   // DEM_Roberts
   var Provinces = ee.FeatureCollection("users/zhouzz400/Boundries/China_Provinces")
   var CQ_table = Provinces.reduceColumns(ee.Reducer.frequencyHistogram(),["Name"])
   var CQ = Provinces.filterMetadata("Name","equals","上海市").geometry()

   var DEM = ee.Image("CGIAR/SRTM90_V4").clip(CQ);

   var DEM_Roberts = DEM.convolve(ee.Kernel.roberts());//卷积
   var DEM_prewitt = DEM.convolve(ee.Kernel.prewitt());
   var DEM_sobel = DEM.convolve(ee.Kernel.sobel());
   var DEM_compass = DEM.convolve(ee.Kernel.compass());
   var DEM_kirsch = DEM.convolve(ee.Kernel.kirsch());

   Map.addLayer(DEM,{min:0,max:2000},"DEM");
   Map.centerObject(CQ,7)
   Map.addLayer(DEM_Roberts,{min:-60,max:60},"DEM_Roberts")
   Map.addLayer(DEM_prewitt,{min:-270,max:270},"DEM_prewitt")
   Map.addLayer(DEM_sobel,{min:-370,max:370},"DEM_sobel")
   Map.addLayer(DEM_compass,{min:-300,max:300},"DEM_compass")
   Map.addLayer(DEM_kirsch,{min:-1100,max:1100},"DEM_kirsch")

   // laplacian4 laplacian8

   // based on distance
   // euclidean/gaussian/manhattan/chebyshev

   // shape kernel
   // circle octagon square diamond cross plus fied

   // operation
   // rotate 90*   add

   // print kernel
   print(ee.Kernel.euclidean(1))
   print(ee.Kernel.gaussian(1))

   // function name(parameters){operation}

APPs
----

获取landsat 数据列表与统计
^^^^^^^^^^^^^^^^^^^^^^^^^^

``` {.javascript linenos=""}
// Load Feature Collections #############################

// Country Fusion Table
var countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw');

// Footprint of Landsat WRS2
var wrs2_descending = ee.FeatureCollection('ft:1_RZgjlcqixp-L9hyS6NYGqLaKOlnhSC35AB5M5Ll');

// Load Landsat Image Collections #######################
var l4_coll = ee.ImageCollection('LANDSAT/LT4_L1T_TOA');  //Aug 22, 1982 - Dec 14, 1993
var l5_coll = ee.ImageCollection('LANDSAT/LT5_L1T_TOA');  //Jan 1, 1984 - May 5, 2012
var l7_coll = ee.ImageCollection('LANDSAT/LE7_L1T_TOA');  //Jan 1, 1999 - Apr 30, 2017
var l8_coll = ee.ImageCollection('LANDSAT/LC8_L1T_TOA');  //Apr 11, 2013 - Apr 30, 2017

// Add Functions #########################################
function redraw(key){
    var selectedCountry = ee.Feature(countries.filter(ee.Filter.eq('Country', key)).first());
    Map.centerObject(selectedCountry);
    var selectedCountry_Strg = ee.String(selectedCountry.get('Country'))

.. code-block::

   // Show country
   var layer0 = ui.Map.Layer(selectedCountry, {color:'purple'}, 'Selected country');
   Map.layers().set(0, layer0);

   // show WRS2 footprint
   var wrs2_filtered = wrs2_descending.filterBounds(selectedCountry.geometry());
   var layer1 = ui.Map.Layer(wrs2_filtered, vizParams, 'WRS2 filtered');
   Map.layers().set(1, layer1);

   // filter the ImageCollection with the boundary of the selected country
   var iC = merged_collection.filterBounds(selectedCountry.geometry());

   iC = iC.map(function(img){
       var year  = img.date().format("Y");            // get the acquisition year
       var CC = img.get('CLOUD_COVER')
       return img.set('year', ee.Number.parse(year)).set('clouds', ee.Number.parse(CC)); // 

});

var iC_FC = ee.FeatureCollection(iC);\ :raw-html-m2r:`<br>`
var iC_FC_size = iC_FC.size();

var options1 = {
    title: 'Landsat Mission 4-8 - GEE image availability',
    hAxis: {title: 'Year'},
    vAxis: {title: 'Image count'},
    colors: ['red']
};

var options2 = {
    title: 'Landsat cloud cover',
    hAxis: {title: '% Cloud Cover'},
    vAxis: {title: 'Image count'},
    colors: ['orange']
};

// Make the histogram, set the options.
var histogram = ui.Chart.feature.histogram({
    features: iC_FC,
    property: 'year',
    minBucketWidth: 1
}).setOptions(options1);

var histogram_CC = ui.Chart.feature.histogram({
    features: iC_FC,
    property: 'clouds',
    minBucketWidth: 5
}).setOptions(options2);
// add text to the panel

var iscoveredby = " is covered by ";
var wrs2_filtered_size = wrs2_filtered.size();
var LandsatWRSgridsIntotalwere = " Landsat WRS-2 grids. During the lifetime of Landsat Mission 4-8 were ";
var text = " images collected. Their spatial distribution is shown in the map (red circles), the temporal distribution is shown in the first chart.";
var text2 = " The relative average cloud cover for each WRS-2 is shown in the map (orange circles), while the 2nd chart shows a histogram of the overall percentage cloud cover."
var info_text = ee.String(selectedCountry_Strg).cat(iscoveredby).cat(wrs2_filtered_size)
    .cat(LandsatWRSgridsIntotalwere).cat(iC_FC_size).cat(text).cat(text2);

panel.widgets().set(0, histogram);
panel.widgets().set(1, histogram_CC);

// create centroids
var centroids = wrs2_filtered.map(getCentroid);
var fC        = centroids.map(addField);

// buffer centroid according to image counts
var buffered_points = fC.map(buffer_count).flatten();

// buffer centroid according to cloud percentage
var buffered_points_cloud = fC.map(buffer_cloud).flatten();

var outlines = empty.paint({featureCollection: buffered_points, color: 1, width: 2});

// show image count circles
var filledOutlines = empty.paint(buffered_points).paint(buffered_points, 0, 2).clip(wrs2_filtered);
var layer2         = ui.Map.Layer(filledOutlines, {palette: ['red'].concat(palette)}, 'Landsat image count');
Map.layers().set(2, layer2);

var innerCircles = empty.paint(buffered_points_cloud).paint(buffered_points_cloud, 0, 2).clip(wrs2_filtered);
var layer3       = ui.Map.Layer(innerCircles, {palette: ['orange'].concat(palette)}, 'Cloud percentage (avg.)');
Map.layers().set(3, layer3);

info_text.evaluate(function(result) { 
    panel.widgets().set(2, ui.Label(result));
});

}  // end - redraw

// ###################################################
// This function creates a new feature from the centroid of the geometry.
var getCentroid = function(feature) {
    // Keep this list of properties.
    var keepProperties = ['PATH', 'ROW'];
    // Get the centroid of the feature's geometry.
    var centroid = feature.geometry().centroid();
    // Return a new Feature, copying properties from the old Feature.
    return ee.Feature(centroid).copyProperties(feature, keepProperties);
}; // end - getCentroid

// ###################################################\ :raw-html-m2r:`<br>`
var addField = function(feature) {

.. code-block::

   var path       = feature.get('PATH');
   var row        = feature.get('ROW');
   var collection = merged_collection.filter(ee.Filter.eq('WRS_PATH', path)).filter(ee.Filter.eq('WRS_ROW', row));
   var cloud_mean = collection.aggregate_mean('CLOUD_COVER');
   cloud_mean     = ee.Number(cloud_mean);
   var count      = collection.size();
   var f          = count.multiply(100).round();
   var cloud_pct  = cloud_mean.multiply(f).divide(100).round();
   var keepProperties = ['PATH', 'ROW', 'CLOUD_COVER'];

   return feature.set({'count': f}).set({'cloud_mean': cloud_mean}).set({'cloud_pct': cloud_pct})
       .copyProperties(feature, keepProperties);

}; // end - addField

// ###################################################\ :raw-html-m2r:`<br>`
var buffer_count = function(feature) {
    return ee.FeatureCollection(feature.buffer(feature.get('count')));
}; // end - buffer_count

// ###################################################\ :raw-html-m2r:`<br>`
var buffer_cloud = function(feature) {
    return ee.FeatureCollection(feature.buffer(feature.get('cloud_pct')));
}; // end - buffer_cloud

// ###################################################\ :raw-html-m2r:`<br>`
ui.root.setLayout(ui.Panel.Layout.absolute());

// Create a panel with vertical flow layout.
var panel = ui.Panel({
layout: ui.Panel.Layout.flow('vertical'),
style: {position: 'bottom-right', height: '500px', width:'350px'}
});

// Create drop down selection

var vizParams = { color: 'grey', opacity: 0.1 };
var palette   = ['FF0000', '00FF00', '0000FF'];

// get country names
var names = countries.aggregate_array('Country');
var merged_collection = ee.ImageCollection(l4_coll.merge(l5_coll).merge(l7_coll).merge(l8_coll));
// Create an empty image into which to paint the features, cast to byte.
var empty   = ee.Image().byte();
// initialize combobox and fire up the redraw function
var select = ui.Select({items: names.getInfo(), onChange: redraw });
select.setPlaceholder('Choose a country ...'); 

Map.setCenter(10.5, 51.3, 4);
Map.add(select);
ui.root.add(panel);

.. code-block::


   ### Landsat NDVI

   ``` {.javascript linenos=""}
   var GJ = GJ_P.filterBounds(point).geometry();
   var NDVI_00 = L7_NDVI.filterDate('2000-01-01','2000-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_00 = NDVI_00.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_00,
   'NDVIsoil':0.22278,//(49)14 0.13089,07 -0.17542,00 -0.05848,19 0.22268
   'NDVIveg':0.78478//(30)14 1,07 0.61322,00 0.43351 ,19 0.96473
   }).rename('FVC');
   // print(fvc_00);
   var NDVI_01 = L7_NDVI.filterDate('2001-01-01','2001-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_01 = NDVI_01.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_01,
   'NDVIsoil':0.26945,//14 0.13089,07 -0.17542,00 -0.05848,19 0.22268
   'NDVIveg':0.75373//14 1,07 0.61322,00 0.43351 ,19 0.96473
   }).rename('FVC');
   // print(fvc_01);
   var NDVI_02 = L7_NDVI.filterDate('2002-01-01','2002-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_02 = NDVI_02.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_02,
   'NDVIsoil':0.20628,
   'NDVIveg':0.76145
   }).rename('FVC');
   // print(fvc_02);
   var NDVI_03 = L5_NDVI.filterDate('2003-01-01','2003-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_03 = NDVI_03.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_03,
   'NDVIsoil':0.14459,//0.17587
   'NDVIveg':0.74578//0.73809
   }).rename('FVC');
   // print(fvc_03);
   var NDVI_04 = L5_NDVI.filterDate('2004-01-01','2004-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_04 = NDVI_04.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_04,
   'NDVIsoil':0.16053,
   'NDVIveg':0.76210
   }).rename('FVC');
   // print(fvc_04);
   var NDVI_05 = L5_NDVI.filterDate('2005-01-01','2005-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_05 = NDVI_05.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_05,
   'NDVIsoil':0.13683,
   'NDVIveg':0.75358
   }).rename('FVC');
   // print(fvc_05);
   var NDVI_06 = L5_NDVI.filterDate('2006-06-01','2006-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_06 = NDVI_06.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_06,
   'NDVIsoil':0.13679,
   'NDVIveg':0.76178
   }).rename('FVC');
   // print(fvc_06);
   var NDVI_07 = L5_NDVI.filterDate('2007-01-01','2007-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_07 = NDVI_07.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_07,
   'NDVIsoil':0.15240,//0.22274
   'NDVIveg':0.755361//0.76144
   }).rename('FVC');
   // print(fvc_07);
   var NDVI_08 = L5_NDVI.filterDate('2008-01-01','2008-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_08 = NDVI_08.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_08,
   'NDVIsoil':0.14452,
   'NDVIveg':0.72232
   }).rename('FVC');
   // print(fvc_08);
   var NDVI_09 = L5_NDVI.filterDate('2009-01-01','2009-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_09 = NDVI_09.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_09,
   'NDVIsoil':0.14457,
   'NDVIveg':0.76880
   }).rename('FVC');
   // print(fvc_09);
   var NDVI_10 = L5_NDVI.filterDate('2010-01-01','2010-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_10 = NDVI_10.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_10,
   'NDVIsoil':0.12892,
   'NDVIveg':0.75360
   }).rename('FVC');
   // print(fvc_10);
   var NDVI_11 = L5_NDVI.filterDate('2011-01-01','2011-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_11 = NDVI_11.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_11,
   'NDVIsoil':0.14458,
   'NDVIveg':0.75363
   }).rename('FVC');
   // print(fvc_11);
   var NDVI_12 = L7_NDVI.filterDate('2012-01-01','2012-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_12 = NDVI_12.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_12,
   'NDVIsoil':0.18363,
   'NDVIveg':0.78475
   }).rename('FVC');
   // print(fvc_12);
   var NDVI_13 = L7_NDVI.filterDate('2013-01-01','2013-12-31')
           .filterBounds(GJ)
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_13 = NDVI_13.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_13,
   'NDVIsoil':0.20681,
   'NDVIveg':0.80047
   }).rename('FVC');
   // print(fvc_13);
   var NDVI_14 = L8.filterDate('2014-01-01','2014-12-31')
           .filterBounds(GJ)
           .map(function(image) {
           return image.addBands(image.normalizedDifference(['B5','B4']).rename('NDVI'))})
           .select('NDVI')
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_14 = NDVI_14.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_14,
   'NDVIsoil':0.27930,//14 0.13089,07 -0.17542,00 -0.05848,19 0.22268
   'NDVIveg':1//14 1,07 0.61322,00 0.43351 ,19 0.96473
   }).rename('FVC');
   // print(fvc_14);
   var NDVI_15 = L8.filterDate('2015-01-01','2015-12-31')
           .filterBounds(GJ)
           .map(function(image) {
           return image.addBands(image.normalizedDifference(['B5','B4']).rename('NDVI'))})
           .select('NDVI')
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_15 = NDVI_15.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_15,
   'NDVIsoil':0.25393,
   'NDVIveg':1
   }).rename('FVC');
   // print(fvc_15);
   var NDVI_16 = L8.filterDate('2016-01-01','2016-12-31')
           .filterBounds(GJ)
           .map(function(image) {
           return image.addBands(image.normalizedDifference(['B5','B4']).rename('NDVI'))})
           .select('NDVI')
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_16 = NDVI_16.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_16,
   'NDVIsoil':0.24803,
   'NDVIveg':1
   }).rename('FVC');
   // print(fvc_16);
   var NDVI_17 = L8.filterDate('2017-01-01','2017-12-31')
           .filterBounds(GJ)
           .map(function(image) {
           return image.addBands(image.normalizedDifference(['B5','B4']).rename('NDVI'))})
           .select('NDVI')
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_17 = NDVI_17.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_17,
   'NDVIsoil':0.26367,
   'NDVIveg':1
   }).rename('FVC');
   // print(fvc_17);
   var NDVI_18 = L8.filterDate('2018-01-01','2018-12-31')
           .filterBounds(GJ)
           .map(function(image) {
           return image.addBands(image.normalizedDifference(['B5','B4']).rename('NDVI'))})
           .select('NDVI')
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_18 = NDVI_18.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_18,
   'NDVIsoil':0.24803,
   'NDVIveg':1
   }).rename('FVC');
   // print(fvc_18);
   var NDVI_19 = L8.filterDate('2019-01-01','2019-12-31')
           .filterBounds(GJ)
           .map(function(image) {
           return image.addBands(image.normalizedDifference(['B5','B4']).rename('NDVI'))})
           .select('NDVI')
           .qualityMosaic('NDVI').select('NDVI').clip(GJ);
   var fvc_19 = NDVI_19.expression(
   '(NDVI-NDVIsoil)/(NDVIveg-NDVIsoil)',{
   'NDVI':NDVI_19,
   'NDVIsoil':0.22268,//14 0.13089,07 -0.17542,00 -0.05848,19 0.22268
   'NDVIveg':0.96473//14 1,07 0.61322,00 0.43351 ,19 0.96473
   }).rename('FVC');
   // print(fvc_19);
   var collection = ee.ImageCollection([fvc_00,fvc_01,fvc_02,fvc_03,fvc_04,fvc_05,fvc_06,fvc_07,fvc_08,
   fvc_09,fvc_10,fvc_11,fvc_12,fvc_13,fvc_14,fvc_15,fvc_16,fvc_17,fvc_18,fvc_19]);
   print(collection);
   var collection_mean = collection.reduce(ee.Reducer.mean()).rename('FVC').toFloat();
   print(collection_mean);
   Export.image.toDrive({
   image:collection_mean,
   description:'fvc_mean',
   fileNamePrefix:'GJ_fvc_mean',
   scale:30,
   region:GJ,
   maxPixels:1e13
   })

Global Urban Extent from Landsat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``` {.javascript linenos=""}
// Global Urban Extent from Landsat
// by Dr. Paolo Gamba
// https://groups.google.com/d/msg/google-earth-engine-developers/guLCR1NvNnI/wQfARABvBgAJ

// Global script multi years 2.0
// ====================================== //
//          Parameters to be set          //
// ====================================== //

// General options 
var area = "Center Asia";             // the name of the region in "Global Shape Table":
                                    //   North America, Center South America, 
                                    //   North South America, South South America,
                                    //   Europe, North Africa, Center South Africa, 
                                    //   Center Africa, Souht Africa Oceania
                                    //   Russia Japan, Center Asia, India, South Est Asia
                                    //   Indonesia, Indochina
                                    //
var convex_hull = false;              // apply the convex hull to the polygon of the chosen area\ :raw-html-m2r:`<br>`
                                    // NB: it must be true for Russia Japan and Oceania
                                    //

var country_name =  "Turkey";     // the name of selected country in Google "Countries of the World" table 
                                    // (set "" if you want to use the entire area instead of this country alone)

var province_name = "";               // selected province of Indonesia
                                    // (set "" if you want to use the entire Indonesia or China, not use for other countries!)

var center_on = "Istanbul";            // Name of city on which center the zoom
                                    // (set "" if you want to zoom on entire area)

var year = 2015;                      // starting year of the collection
var number_of_years =30;             // total number of years to analyze (MAX 30)
var step = 10;                         // step progress (e.g. 1 year in 1 year, 2 years in 2 years, ecc.)
var collection_type = "greenest";     // greenest or standard or simplecomposite
var sensor = "L8";                    // L5, L7, L8 or L45 (only before 1995!)
var cloud_cover = 1;                  // % of cloud cover
var waterfilter = true;               // enable/disable water filter in classification\ :raw-html-m2r:`<br>`
var zoom = 7;                         // level of zoom (center_on automatically set zoom+

// NDVI options
var mask_ndvi = false;                // enable/disable the ndvi mask
var th_ndvi_high = 0.5;               // 1st threshold for ndvi, put at zero all points in classification over this value
var th_ndvi_low = -0.5;               // 2st threshold for ndvi, put at zero all points in classification under this value

// Elevation options
var mask_slope = false;               // enable/disable the slope mask
var th_slope = 10;                    // threshold for slope in degrees, put at zero all points in classification over this value
var mask_dem = false;                 // enable/disable the slope mask
var th_dem = 2000;                    // threshold for slope in degrees, put at zero all points in classification over this value
var use_geometry = false;             // if false apply dem mask to all image, if true only inside the rectangle
var dem_geometry = ee.Geometry.Rectangle(106.67450,-6.79826,  107.08649,-7.11452);

// Morphology options
var morphology_on = false;             // enable/disable morphology
var operator = 'Window.min';          // 'Window.min' -> erode; 'Window.max' -> dilate
var radius1 = 400;                    // radius of the kernel closing/opening
var radius2 = 50;                     // radius of final closing;
var kernelType = 'circle';            // 'circle', 'square', 'cross', 'plus', 'octagon' or 'diamond'
var units = 'meters';                 // units of measure: 'meters' or 'pixels'
var iterations = 1;

var class_or_flag = true;             // enable/disable the new and method correction
var class_morph_radius = 7;

// Ground Truth
var GT_enable = false;                // enable/disable ground truth
var GT_region = 'Southeast Asia';     // the name of the region in Universe of cities Table:
                                    //   Eastern Asia & Pacific
                                    //   Southeast Asia
                                    //   Western Asia
                                    //   South & Central Asia
                                    //   Europe & Japan
                                    //   Northern Africa
                                    //   Sub-Saharan Africa
                                    //   Land Rich Developed Count (north america)
                                    //   Latin America & the Carib

// Classifier parameters
var ts_type = 0;                      // set the type of training set to use: 
                                    //    0 -> fusion table(s) IMPORTANT! GO TO LINE 1081 TO SET WHICH FUSION TABLES TO USE
                                    //    1 -> globcover random points
                                    //    2 -> universe of cities random points

var multiclassifier = false;          // false for single classification true for three classifiers
var multi_random = false;              // if true generate 3 random sets instead of one using the seeds of the next line
                                    // (WORKS ONLY FOR ts_type = 2)
var seeds = new Array(0,1,2);    

var classifiers = new Array(5,9,6);   // CHOOSE CLASSIFIER(S): (IMPORTANT! if multiclassifier is false only the first one is used)
                                    //    0 = "FastNaiveBayes"
                                    //    1 = "GmoMaxEnt" 
                                    //    2 = "Winnow"
                                    //    3 = "MultiClassPerceptron"
                                    //    4 = "Pegasos"
                                    //    5 = "Cart"
                                    //    6 = "RifleSerialClassifier" (aka Random Forest)
                                    //    7 = "IKPamir"
                                    //    8 = "VotingSvm"
                                    //    9 = "MarginSvm"

var compute_area = false;              // compute area of classified data
var area_scale = 300;                 // scale factor for area computation

// RANDOM POINTS TRAINING SET PARAMETERS
var num_points = 500;                 // num points to generate

// Globcover random points parameters
var lng = -48.90564;                  // coordinates of the quad
var lat = -0.890311;
var radius1 = 500;                    // radius of the kernel
var kernelType1 = 'square';           //'circle', 'square', 'cross', 'plus', 'octagon' or 'diamond'

// Universe of cities paramters:
// load universe of cities polygons (NOT CHANGE THIS LINE!)
var cities_table = ee.FeatureCollection('ft:1pQ-PrIEGrYa2Y3v9tsN1xwfYuqRIqOoDPARgpwzS');

// Choose the city or the cities to use
var selectedCities = cities_table.filter(ee.Filter.eq('MAIN_CITY', 'Istanbul')); // use this line only if there is one city!
/\ *var selectedCities = cities_table.filter(ee.Filter.or(ee.Filter.eq('MAIN_CITY', 'Kunming'), // use this command lines if there are more then one city
                                                    ee.Filter.eq('MAIN_CITY', 'Yuxi'),
                                                    ee.Filter.eq('MAIN_CITY', 'Qujing')));*\ /
var use_all_cities = true;              // set true to use all the cities of the current provice 
                                        // instead of the selected ones

// ====================================== //
//          Loading basic data            //
// ====================================== //

// LOAD POLYGONS
// find area in the world
var shapes = ee.FeatureCollection("ft:1rYMVQMw3hTr8IC2d3Ad8nHzHmQy8iBJCqAN20l_O");
var filter = shapes.filter(ee.Filter.eq('Area', area));

// Find Countries in the world
var countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw');
var country = countries.filter(ee.Filter.eq('Country', country_name));

// Find provinces in the selected country
var province = "";
var provinces_table = "";
if(country_name === "Indonesia")
{
// find province of Indonesia
provinces_table = ee.FeatureCollection('ft:1ep1h4bOMUOEg0jwjmmn78T-L32zLbILZotS2lwUC');
province = provinces_table.filter(ee.Filter.eq('name', province_name));
}
else if(country_name === "China")
{
// Find Province of China
provinces_table = ee.FeatureCollection('ft:1h7DGU8yXMYqULLM3F4AsvLPOXiR5WTRswSgWLeHH');
province = provinces_table.filter(ee.Filter.eq('NAME_1', province_name));
}

// load main polygon
var choosen_zone = (province==="") ? ((country_name === "") ? filter : country) : province ;
var polygon1 = choosen_zone.geometry();

if(convex_hull===true && (choosen_zone === filter))
polygon1 = polygon1.convexHull();

// classifier types
var classifier_array = [ee.Classifier.naiveBayes(), ee.Classifier.gmoMaxEnt(), ee.Classifier.winnow(), 
                        ee.Classifier.perceptron(), ee.Classifier.pegasosLinear(),
                        ee.Classifier.cart(), ee.Classifier.randomForest(),
                        ee.Classifier.ikpamir(), ee.Classifier.svm(), ee.Classifier.svm("Margin")];

// classifier names
var classifier_names = ["NaiveBayes", "GmoMaxEnt", "Winnow", "MultiClassPerceptron", "PegasosLinear",
                        "Cart", "RandomForest", "IKPamir", "Svm", "MarginSvm"];

// load elevation data
if(mask_slope===true || mask_dem===true)
    var dem = ee.Image("CGIAR/SRTM90_V4");

// Load ground truth data
if(GT_enable===true)
{
var GT_regions = ee.FeatureCollection('ft:1pQ-PrIEGrYa2Y3v9tsN1xwfYuqRIqOoDPARgpwzS');
var GT_selectedRegions = GT_regions.filter(ee.Filter.eq('REGION', GT_region));
}

if(use_all_cities === true)
{
/\ *
// Universe of cities paramters:
// Join the two collection on their geometries if they're within 2km.
var joinFilter = ee.Filter.intersects('geometry', null, 'geometry', null);
var selectedCities = ee.Join.simple().apply(cities_table, province, joinFilter);*\ /

// Choose the city or the cities to use
var allCities = cities_table.filter(ee.Filter.eq('COUNTRY', country_name)); 
var allProvinceCities = allCities.map(function(f) {
    return f.set("Inside",
        ee.Algorithms.If((f.geometry()).containedIn(polygon1), true, false));
});
selectedCities = allProvinceCities.filterMetadata('Inside', 'equals', true);

}

// check for incorrect parameters
if(ts_type!==2)
multi_random = false;

if(sensor==="L45")
collection_type = "standard";

// color palette for classification
var palette_list = new Array( {palette: '000000, ff0000'},
                            {palette: '000000, ffff00'},
                            {palette: '000000, 00ff00'},
                            {palette: '000000, ff00ff'},
                            {palette: '000000, 00ffff'},
                            {palette: '000000, FFA500'},
                            {palette: '000000, 0000ff'},
                            {palette: '000000, 800000'},
                            {palette: '000000, 8A2BE2'},
                            {palette: '000000, FA8072'},
                            {palette: '000000, 32CD32'},
                            {palette: '000000, F4A460'},
                            {palette: '000000, 1E90FF'},
                            {palette: '000000, F0E68C'},
                            {palette: '000000, 228B22'},
                            {palette: '000000, FFD700'},
                            {palette: '000000, E6E6FA'},
                            {palette: '000000, A0522D'},
                            {palette: '000000, FFC0CB'},
                            {palette: '000000, 66CDAA'},
                            {palette: '000000, FF8C00'},
                            {palette: '000000, 9932CC'},
                            {palette: '000000, 7FFF00'},
                            {palette: '000000, 7FFF00'},
                            {palette: '000000, CD853F'},
                            {palette: '000000, FAEBD7'},
                            {palette: '000000, DDA0DD'},
                            {palette: '000000, 808000'},
                            {palette: '000000, FFDAB9'},
                            {palette: '000000, 4169E1'});

// task name 
var task_name = ((country_name === "") ? area : country_name) + "\ *from*\ " + year + "\ *to*\ " + (year-number_of\ *years) + "*\ " + 
                (collection_type==="greenest" ? "_L7_Annual_Greenest\ *TOA" : ("*\ " + sensor + "_TOA_cloud\ *cover*\ " + cloud_cover + "%")) +
                (multiclassifier===true ? "_3\ *Classifiers" : "*\ "+classifier_names[classifiers[0]]) + 
                (morphology_on===true ? "_with_morphology":"");

// ====================================== //
//              Fusion Tables             //
// ====================================== //

// Jakarta
var ft1 = ee.FeatureCollection("ft:1JYib5GQkiNTMnt2rpVteos0jQeYE9jVXIhCE8_M");
ft1 = ft1.remap([100,101,102,103,104,105,106,107,108,109,200,201,202,203,204,205,206,207,208,209,210,211,212,213],
                [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Kota Bandung
var ft2 = ee.FeatureCollection("ft:1Z0VTqrovwUR0iujsgw6Y44_tLpjkFUeyivn2f2A");
ft2 = ft2.remap([100,101,102,103,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220],
                [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Kota Manado
var ft3 = ee.FeatureCollection("ft:1Dd68TvI-rYwNe9BHhDkdcUnUg17PKeLUdtwqTR4");
ft3 = ft3.remap([100,101,102,103,104,200,201,202,300,301,302,400,401,402],[1,1,1,1,1,0,0,0,0,0,0,0,0,0],"Number");

// Kuala Lumpur
var ft4 = ee.FeatureCollection("ft:1d_HFpj2iM3S8KBHubF5WEERwXaGSChraPbONdC0");
ft4 = ft4.remap([100,101,102,103,104,105,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216],
            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Kalimatan
var ft5 = ee.FeatureCollection("ft:1m3KKK0ApX90x1bLOy-WU_XNitj8fVtw19lXLWZU");
ft5 = ft5.remap([100,101,102,200,201,202,203,204,205,206,207,208,209,210,211],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Surabaya
var ft6 = ee.FeatureCollection("ft:10IZ12uFHlmGZMuzgOkk3HuvAuHdM2Iu10O7MPxk");
ft6 = ft6.remap([100,101,102,103,104,105,106,107,200,201,202,203,204,205,206,207,208,209,210,211,212,213],
            [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// San Paolo
var ft7 = ee.FeatureCollection("ft:1W-iBNcXotAJt06PO0EdANfOveMX8P9Sd_zxUK-w"); 
ft7 = ft7.remap([100,101,200,300,400,500,600,700,701,800,900,901,1000,1001,1100],[1,1,0,0,1,0,0,0,0,1,0,0,0,0,1],"Number");

// Rio 
var ft8 = ee.FeatureCollection("ft:1TvLP4Xe3bJ-dwDyvxudiDxn1BUZieNmDlKelpDU");
ft8 = ft8.remap([100,101,200,201,202],[1,1,0,0,0],"Number");

// Recife
var ft9 = ee.FeatureCollection("ft:199COLkTjEFiYW09eF7kS6bCj6Ju-iWUk4pXwOhk");
ft9 = ft9.remap([100,101,200,201,202,203,204,205,206,207,208,209,210,211,212,213],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

//Curitiba 
var ft10 = ee.FeatureCollection("ft:1lE5JidkBcWPtOf7jDurRezkTv72Ak4ECcCFw6I8");
ft10 = ft10.remap([100,101,200,201,202,203,204,205,206,207,208,209,210,211,212,213],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Buonos Aires
var ft11 = ee.FeatureCollection("ft:1-z1IpdYWOQe-d3xMTkxViQmWJCNfiX7stOWSf9s"); 
ft11 = ft11.remap([100,101,102,103,200,201,202,203,204,205], [1,1,1,1,0,0,0,0,0,0],"Number");

// Mexico City
var ft12 = ee.FeatureCollection("ft:1zgrzKKI2IUU_NcCIGzfSF9-GmTepsQTknlYNHok"); 
ft12 = ft12.remap([100,101,102,200,201,202,203,204,205,206,207], [1,1,1,0,0,0,0,0,0,0,0],"Number");

// Shanghai
var ft13 = ee.FeatureCollection("ft:1DUtGpGJzKiEf63LkUjJj7imQAiK0cxvawP2YQno");
ft13 = ft13.remap([100,101,102,200,201,202,203,204,300,301,400,401],[1,1,1,0,0,0,0,0,0,0,0,0],"Number");

// Jiangsu
var ft14 = ee.FeatureCollection("ft:1h4dMswHa9OPy4pFsHva8fSOi7ZtfhbkDQgbB3UE");
ft14 = ft14.remap([100,101,200,201,300,301,302,303,400,401],[1,1,0,0,0,0,0,0,0,0],"Number");

// Cairo
var ft15 = ee.FeatureCollection("ft:1S5DPVKswvcIczNqZLZXi3-YipExJ7Ez3ySFd3FE"); 
ft15 = ft15.remap([100,101,102,200,201,202,203,204], [1,1,1,0,0,0,0,0],"Number");

// Kinshasa-Brazzaville
var ft16 = ee.FeatureCollection("ft:1VmkJ_EKhOdcNjsyeJuH7Wt7AGzjZK0Il3NKJVFE");
ft16 = ft16.remap([100,101,102,200,201,202,203,204], [1,1,1,0,0,0,0,0],"Number");

// Istambul
var ft17 = ee.FeatureCollection("ft:1SI9e9QIEg2T7ZuBpVmz06VsSbK-Zx4Y-uNnTymo"); 
ft17 = ft17.remap([100,101,102,103,104,105,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216], 
                [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Karachi
var ft18 = ee.FeatureCollection("ft:1MXNLNoQji75DduserB14ca88O1E2u_ZqrRDAcAI"); 
ft18 = ft18.remap([100,101,102,103,200,201,202,203,204], [1,1,1,1,0,0,0,0,0],"Number");

// Londra
var ft19 = ee.FeatureCollection("ft:1-ILTTjz3lvURZ7VC8q-zA0MvSln6bDz2dyj9KTc"); 
ft19 = ft19.remap([100,101,102,103,200,201,202,203,204,205,206,207,208,209,210,211,212,213], 
                [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Manila
var ft20 = ee.FeatureCollection("ft:1VfVvegIbUX-Goi0tqjrLV2AJMxjFR9x5zXlW51c"); 
ft20 = ft20.remap([100,101,102,200,201,202,203,204,205], [1,1,1,0,0,0,0,0,0],"Number");

// Mumbai
var ft21 = ee.FeatureCollection("ft:13IcqxzMwTjePC2cCeVcKZy6d6_sM1CqrbPWEGkY"); 
ft21 = ft21.remap([100,101,102,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216], 
                [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// New York
var ft22 = ee.FeatureCollection("ft:1zzRtyA3nIlwQJJl6en4cm6gjrjuOI3iB_N5B9qg"); 
ft22 = ft22.remap([100,101,102,200,201,202,203,204,205,206,207,208,209,210], [1,1,1,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Osaka
var ft23 = ee.FeatureCollection("ft:1gmLE5_GpE5aeamLRPaWgAcTmbzPNROXsLvexNvM");
ft23 = ft23.remap([100,101,102,103,200,201,202,203,204,205,206,207,208], [1,1,1,1,0,0,0,0,0,0,0,0,0],"Number");

// Seul
var ft24 = ee.FeatureCollection("ft:1hjcTW0AD0qApNiT9LDieZua94UbofkK6Dfd5IRg"); 
ft24 = ft24.remap([100,101,102,103,104,105,200,202,203,204,205,206,207], [1,1,1,1,1,1,0,0,0,0,0,0,0],"Number");

// Vietnam Dong Hoi
var ft25 = ee.FeatureCollection("ft:1btvyTxRJjrigjoYWt3rB8DakxRkhQPPIbRZp_xo");
ft25 = ft25.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Ca Mau
var ft26 = ee.FeatureCollection("ft:1PM7cL_rCRf3cOTzVcWijydFXgWLsnuivyX5PYHw");
ft26 = ft26.remap([100,101,102,103,104,105,106,107,108,109],[1,1,1,0,0,0,0,0,0,0],"Number");

// Vietnam sud Ca Mau
var ft27 = ee.FeatureCollection("ft:1ELY75GK8n-6qYQkh87lKrrElQAvJOKhY3s8OM84");
ft27 = ft27.remap([100,101,102,103,104,105,106,107,108,109,110],[1,1,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam confine cina
var ft28 = ee.FeatureCollection("ft:1-mKabryrKX81T86HEkOQeK9ywbnDwuUKxoPrCJY");
ft28 = ft28.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116],[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Ho Chi Minh
var ft29 = ee.FeatureCollection("ft:1B-wKLMVl1gJPvB-LG3et4F9ydAKI5A2gghk2eU4");
ft29 = ft29.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117],[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Da Nang
var ft30 = ee.FeatureCollection("ft:1jQKQJgEoYOKqihLXBEgkiFZ3JoA0jl238Uu4sc8");
ft30 = ft30.remap([100,101,102,103,104,105,106,107,108,109,110,111,112],[1,1,1,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Quang Tri
var ft31 = ee.FeatureCollection("ft:11INXL4EThmczTQuNvH28i33fyKNnEujsKvTxKZQ");
ft31 = ft31.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Phuroc Hoi
var ft32 = ee.FeatureCollection("ft:19tpEczaE170ez6x5ViPNDqeB7-rfoDFSv9mYVKM");
ft32 = ft32.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Est Ho Chi Minh
var ft33 = ee.FeatureCollection("ft:1Un2B568D-aG_T30POwgWnIW6NGXFlq6wNs0XhOY");
ft33 = ft33.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113],[1,1,1,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Phan Rang
var ft34 = ee.FeatureCollection("ft:16sOtBxUs6lFjIj2426190MO79dObrr51Ksyh0WI");
ft34 = ft34.remap([100,101,102,103,104,105,106,107,108,109],[1,1,1,0,0,0,0,0,0,0],"Number");

// Vietnam Sud Hanoi
var ft35 = ee.FeatureCollection("ft:14TVtC6AD5SVoZF0PlHFS0eV-21BvfBgRbzEx1jQ");
ft35= ft35.remap([100,101,102,103,104,105,106,107,108,109,110,111,112],[1,1,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Ho Chi Minh 2
var ft36 = ee.FeatureCollection("ft:1amd1UCF4ZYYFv7wipfM7P8c1jtcnC3CKlus23a0");
ft36 = ft36.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Vietnam Hanoi
var ft37 = ee.FeatureCollection("ft:1lnHpA_ZlFoJ1ADqvLRno1PJV31PlTlsUXU9zwVQ");
ft37 = ft37.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Africa
var ft38 = ee.FeatureCollection("ft:1Kh31mKZjrcJWXzG1MEQA00mW0-GJ8qyW4jGhlmw");
ft38 = ft38.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,
                118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,
                136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153],
                [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Dallas
var ft39 = ee.FeatureCollection("ft:10VY57FR5fcevkinyMiYvhv-bfzu-1w7bAWuV59XS");
ft39 = ft39.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,
                122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142],
                [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Los Angeles
var ft40 = ee.FeatureCollection("ft:1xTuZ0Cja5BvyEysVGU36rTQolhk_Ad31-UWrD8a5");
ft40 = ft40.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,
                122,123,124,125,126,127,128,129,130,131,132],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Toronto 1998
var ft41 = ee.FeatureCollection("ft:15h2EZU85KFxcnGCgAQq0S39g7Z-ea8iO0h5GJegi");
ft41 = ft41.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,
                122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137],
                [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Toronto 1999
var ft42 = ee.FeatureCollection("ft:1lxJbARYUw5AV_ULv_Qd9aYswHdWGJQ8fJ4j31Nor");
ft42 = ft42.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,
                122,123,124,125,126,127,128,129,130,131,132,133,134,135],
                [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Vancouver 1999
var ft43 = ee.FeatureCollection("ft:1ln312_c7nvpPMoA648yqqzNJDR0HCKLr9gj7PKUx");
ft43 = ft43.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,
                123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,
                146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163],
                [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Vancouver 2009
var ft44 = ee.FeatureCollection("ft:1ln312_c7nvpPMoA648yqqzNJDR0HCKLr9gj7PKUx");
ft44 = ft44.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,
                123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139],
                [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Dakar - Senegal 2009
var ft45 = ee.FeatureCollection("ft:1KgybS5ROczVfioCUnxNVXZL1wUHVTuejCmQDeXTs");
ft45 = ft45.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113],[1,1,1,0,0,0,0,0,0,0,0,0,0,0],"Number");

// Lagos - Nigeria 2009
var ft46 = ee.FeatureCollection("ft:1PVyuUjUMpaYIBQqhHSAl9\ *KG32hStLv*\ -8g0Z8wE");
ft46 = ft46.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,
                121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,
                142,143,144,145,146,147,148,149,150,151,152],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Bangui - Repubblica Centro Africana 2009
var ft47 = ee.FeatureCollection("ft:1vNMbsMDdhdmLuy39PFMnzicD11PFCyfScF6UeTTw");
ft47 = ft47.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,
                122,123,124,125,126,127],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Addis Abeba - Etiopia 2009
var ft48 = ee.FeatureCollection("ft:1AujUNqTt7yZBzlkHZmk0JCZyRxShE6HnO_4pJdDu");
ft48 = ft48.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117],
                [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Nairobi - Kenya 2009
var ft49 = ee.FeatureCollection("ft:1VTTiG4F3uiKhbMKbdjCe41So2Hgk5c7OKls9P4hZ");
ft49 = ft49.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,
                121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141],
                [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Luanda - Angola 2009
var ft50 = ee.FeatureCollection("ft:1wAFG1OyRRugDsBcIiGl6e3m1k60Syggf9PbQjvwC");
ft50 = ft50.remap([100,101,102,103,104,105,106,107,108,109,110,111], [1,1,0,0,0,0,0,0,0,0,0,0], "Number");

// Antanananarivo - Madagascar 2009
var ft51 = ee.FeatureCollection("ft:1BUB0WKrrgj8oEa4Ct6PXynxlV86JemV55f1-2Mgm");
ft51 = ft51.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,], 
                [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Casablanca - Marocco 2009
var ft52 = ee.FeatureCollection("ft:1w1xp3taWI5lXmrN96PkVvNgU8p8nPSx_MnJS26ey");
ft52 = ft52.remap([100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,
                121,122,123,124,125,126,127,128,129,130,131,132,133,134],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Tamanrasset - Algeria 2009
var ft53 = ee.FeatureCollection("ft:1F5i8QzejxFjH3o4xmiKD1b5CF9EhtYLzgEYFL5-R");
ft53 = ft53.remap([101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Hurgada - Egypt  2009\ :raw-html-m2r:`<br>`
var ft54 = ee.FeatureCollection("ft:1RwW2jFBdUEtxlFWQRIM0R1jneXHlXYRlS_k0dCSu");
ft54 = ft54.remap([101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116],
                [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Sirte - Lybia  2009\ :raw-html-m2r:`<br>`
var ft55= ee.FeatureCollection("ft:1H8wOhLPCIWYXayXjcwcQu8PDv3m-_tQd-ZN4L6M1");
ft55 = ft55.remap([101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Cercle de Dire - Mali  2009\ :raw-html-m2r:`<br>`
var ft56= ee.FeatureCollection("ft:1bkRPcvqxJoEQupltGhx1XSH0sKsivXIH_152-EFF");
ft56 = ft56.remap([101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Maputo - Mozambico  2009\ :raw-html-m2r:`<br>`
var ft57 = ee.FeatureCollection("ft:1U6j_VE9vGNk6C4tg1wrEV2Hh7KNIB4EjBUIjmJti");
ft57 = ft57.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,
                121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Harare - Zimbawe  2009\ :raw-html-m2r:`<br>`
var ft58 = ee.FeatureCollection("ft:1x4nBwW3-Hn-PVexdWk3nPN49aH8Usd8l0ljJRsa0");
ft58 = ft58.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,
                123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144],
                [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Johannesburg - South Africa  2009\ :raw-html-m2r:`<br>`
var ft59 = ee.FeatureCollection("ft:1Ye-K6RsCf4ixpUgwQ4r1OSuPFQ0xjB6CVniZ0NIA");
ft59 = ft59.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,
                123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141],
                [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Durban - South Africa  2009\ :raw-html-m2r:`<br>`
var ft60 = ee.FeatureCollection("ft:1fSLrnYRnBmMkZxdrSnIeQr9_TdbKifI-7HPrDk9u");
ft60 = ft60.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,
                123,124,125,126,127,128,129],
                [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Cape Town - South Africa  2009\ :raw-html-m2r:`<br>`
var ft61 = ee.FeatureCollection("ft:1om0_icjG1Wz90_ACpOUU4E50IHZgU9-57HH_dNAS");
ft61 = ft61.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,
                123,124,125,126,127,128,129,130,131,132,133,134],
                [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "Number");

// Tranining set Andres
var ftA4 = ee.FeatureCollection("ft:1YZfa286rC-MiQLdGGanFfvoOFcaACq79D_guqeB2");
ftA4 = ftA4.remap([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,
            121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            "Number");

var ftA6 = ee.FeatureCollection("ft:1E_sQ9l7-uQbuEfGgCcuHlp-fWB6MQJqgFFb0KQqo");
ftA6 = ftA6.remap([100,101,102,103,104,200,201,202,300,301,302,400,401,402],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0],"Number");

// India FT66 Test punti
var ft66 = ee.FeatureCollection("ft:1w65fJ11u4BeJuX0xQDsWCloB5Y1_ZF-h2Cc0qciz");
ft66 = ft66.remap([100,200,300,400,500,600,700,800,900,1000,1100,1200],
                [1,0,0,0,0,0,0,0,0,0,0,0], "Number");

// ====================================== //
//             General Functions          //
// ====================================== //

// autocenter map
function autoCenterMap(polygon, zoom)
{\ :raw-html-m2r:`<br>`
var centroid = polygon.centroid().getInfo().coordinates;

Map.setCenter(centroid[0],centroid[1],zoom);
}

// create a quad polygon from lat and lon
function getPoly(lng, lat)
{
var poly = ee.Geometry.Polygon([[lng-1, lat-1],
                                [lng-1, lat+1],
                                [lng+1, lat+1],
                                [lng+1, lat-1] ]);
return poly;\ :raw-html-m2r:`<br>`
}

// Return an image in flag is 0 or the median of a collection if flag is 1
function img_or_collection(input, flag)
{
if(flag===0)
    return input;
else if(flag===1)
    return input.median();
}

// Return an image in flag is 0 or the median of a collection if flag is 1
function input_selector(year, collection_type, sensor, cloud_cover, polygon)
{

var collection, collection1, collection2, collection3;
var coll;

if(collection_type === "greenest")
{
    coll = (sensor==='L5') ? 'LT5_L1T_ANNUAL_GREENEST_TOA/' : 
        ((sensor==='L7') ? 'LE7_L1T_ANNUAL_GREENEST_TOA/' : 'LC8_L1T_ANNUAL_GREENEST_TOA/');

.. code-block::

   return ee.Image(coll + year).clip(polygon);

}
else if(collection_type === "standard")
{
    coll = (sensor==='L5' || sensor==='L45') ? 'LT5_L1T_TOA' : ((sensor==='L7') ? 'LE7_L1T_TOA' : 'LC8_L1T_TOA');

.. code-block::

       // check for combo L4-L5
   if(sensor==='L45')
   {
       collection1 = ee.ImageCollection("LT5_L1T_TOA").filterDate(new Date(year+"-01-01"), new Date(year+"-12-31"))
                                                   .filterMetadata('catalog_cloud_cover', 'less_than', cloud_cover)
                                                   .filterBounds(polygon);

       collection2 = ee.ImageCollection("LT4_L1T_TOA").filterDate(new Date(year+"-01-01"), new Date(year+"-12-31"))
                                                   .filterMetadata('catalog_cloud_cover', 'less_than', cloud_cover)
                                                   .filterBounds(polygon);

       collection = ee.ImageCollection(collection1.merge(collection2));
       return collection.median().clip(polygon);

   }
   else
   {
       collection = ee.ImageCollection(coll).filterDate(new Date(year+"-01-01"), new Date(year+"-12-31"))
                                           .filterMetadata('catalog_cloud_cover', 'less_than', cloud_cover)
                                           .filterBounds(polygon);
       return collection.median().clip(polygon);
   }


} 
else if(collection_type === "simplecomposite")
{
    coll = (sensor==='L5') ? 'LT5_L1T' : ((sensor==='L7') ? 'LE7_L1T' : 'LC8_L1T');

.. code-block::

   collection = ee.ImageCollection(coll).filterDate(new Date(year+"-01-01"), new Date(year+"-12-31"))
               //.filterMetadata('catalog_cloud_cover', 'less_than', cloud_cover)
               .filterBounds(polygon);
   var simpleComp = ee.Algorithms.Landsat.simpleComposite(collection, 50, 10);
   return simpleComp.clip(polygon);


}
}

// ====================================== //
//           Morphology Functions         //
// ====================================== //

// launch matematical morphology
function morphology(image, operator, radius, kernelType, units, iterations)
{
var morph;

if(image.getInfo().bands[0].data_type.precision == 'int')
{
    morph = ee.call(operator, image, radius, kernelType, units, iterations);
}
else if(image.getInfo().bands[0].data_type.precision == 'float' || image.getInfo().bands[0].data_type.precision == 'double')
{
    morph = ee.call(operator, image.multiply(255).toInt(), radius, kernelType, units, iterations);
}

return morph;

}

// opening function
function opening(image, radius, kernelType, units)
{
var erode = morphology(image, 'Window.min', radius, kernelType, units, 1);
var open = morphology(erode, 'Window.max', radius, kernelType, units, 1);
return open;
}

// closing function
function closing(image, radius, kernelType, units)
{
var dilate = morphology(image, 'Window.max', radius, kernelType, units, 1);
var closure = morphology(dilate, 'Window.min', radius, kernelType, units, 1);
return closure;
}

// Morphology adjustment
function morph_adjustment(img1, radius1, radius2, kernelType)
{
// Opening
var morph = closing(img1, radius1, kernelType, "meters");
morph = opening(morph, radius1, kernelType, "meters");
//Map.addLayer(ee.Image(0).mask(morph), {palette: '000000, 77ff00'}, 'Classified + clos-op', false);

// And
var result = img1.and(morph);
result = closing(result, radius2, kernelType, "meters");

return result;
}

// ====================================== //
//               NDVI Functions           //
// ====================================== //

// NDVI computing
function NDVI(image)
{
return image.expression('((b("B4") - b("B3")) / (b("B4") + b("B3")))');
}

// ====================================== //
//               NDSV Functions           //
// ====================================== //

// NDSV computing
function NDSV(image, b1, b2)
{
//print('((b(\"' + b2 + '\") - b(\"' + b1 + '\")) / (b(\"' + b2 + '\") + b(\"'+ b1 + '\"))) ');
return image.expression(
    '((b(\"' + b2 + '\") - b(\"' + b1 + '\")) / (b(\"' + b2 + '\") + b(\"'+ b1 + '\"))) ');
}

// Compute all the 15 bands of NDSV
function create_ndsv_img_15(image)
{
image = image.float();

//print("NDSV for L5 or L7");

var band_1_2_image = NDSV(image,'B1','B2');
var band_1_3_image = NDSV(image,'B1','B3');
var band_1_4_image = NDSV(image,'B1','B4');
var band_1_5_image = NDSV(image,'B1','B5');
var band_1_7_image = NDSV(image,'B1','B7');

var band_2_3_image = NDSV(image,'B2','B3');
var band_2_4_image = NDSV(image,'B2','B4');
var band_2_5_image = NDSV(image,'B2','B5');
var band_2_7_image = NDSV(image,'B2','B7');

var band_3_4_image = NDSV(image,'B3','B4');
var band_3_5_image = NDSV(image,'B3','B5');
var band_3_7_image = NDSV(image,'B3','B7');

var band_4_5_image = NDSV(image,'B4','B5');
var band_4_7_image = NDSV(image,'B4','B7');
var band_5_7_image = NDSV(image,'B5','B7');

band_1_2_image = band_1_2_image.addBands(band_1_3_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_1_4_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_1_5_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_1_7_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_3_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_4_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_5_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_7_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_3_4_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_3_5_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_3_7_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_4_5_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_4_7_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_5_7_image,null,false);

var bandnames = ["ndsv_1_2", "ndsv_1_3", "ndsv_1_4", "ndsv_1_5", "ndsv_1_7", "ndsv_2_3", "ndsv_2_4", "ndsv_2_5", "ndsv_2_7", "ndsv_3_4", "ndsv_3_5", "ndsv_3_7", "ndsv_4_5", "ndsv_4_7", "ndsv_5_7"];
var ndsv = band_1_2_image.select(['.*'], bandnames);

return ndsv;

}

// Compute all the 15 bands of NDSV for Landsat8
function create_ndsv_img_15_L8(image)
{
image = image.float();
//print("NDSV for L8");
var band_1_2_image = NDSV(image,'B2','B3');
var band_1_3_image = NDSV(image,'B2','B4');
var band_1_4_image = NDSV(image,'B2','B5');
var band_1_5_image = NDSV(image,'B2','B6');
var band_1_7_image = NDSV(image,'B2','B7');

var band_2_3_image = NDSV(image,'B3','B4');
var band_2_4_image = NDSV(image,'B3','B5');
var band_2_5_image = NDSV(image,'B3','B6');
var band_2_7_image = NDSV(image,'B3','B7');

var band_3_4_image = NDSV(image,'B4','B5');
var band_3_5_image = NDSV(image,'B4','B6');
var band_3_7_image = NDSV(image,'B4','B7');

var band_4_5_image = NDSV(image,'B5','B6');
var band_4_7_image = NDSV(image,'B5','B7');

var band_5_7_image = NDSV(image,'B6','B7');

band_1_2_image = band_1_2_image.addBands(band_1_3_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_1_4_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_1_5_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_1_7_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_3_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_4_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_5_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_7_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_3_4_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_3_5_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_3_7_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_4_5_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_4_7_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_5_7_image,null,false);

var bandnames = ["ndsv_1_2", "ndsv_1_3", "ndsv_1_4", "ndsv_1_5", "ndsv_1_7", "ndsv_2_3", "ndsv_2_4", "ndsv_2_5", "ndsv_2_7", "ndsv_3_4", "ndsv_3_5", "ndsv_3_7", "ndsv_4_5", "ndsv_4_7", "ndsv_5_7"];
var ndsv = band_1_2_image.select(['.*'], bandnames);

return ndsv;

}

// Compute all the 6 bands of NDSV
function create_ndsv_img_6(image)
{
image = image.float();
var band_1_2_image = 0;
var band_1_3_image = 0;
var band_1_4_image = 0;

var band_2_3_image = 0;
var band_2_4_image = 0;

var band_3_4_image = 0;

if(image.getInfo().bands[0].id == 1)
{
    band_1_2_image = NDSV(image,'1','2');
    band_1_3_image = NDSV(image,'1','3');
    band_1_4_image = NDSV(image,'1','4');

.. code-block::

   band_2_3_image = NDSV(image,'2','3');
   band_2_4_image = NDSV(image,'2','4');

   band_3_4_image = NDSV(image,'3','4');

}
else if(image.getInfo().bands[0].id == 4){

.. code-block::

   band_1_2_image = NDSV(image,'4','5');
   band_1_3_image = NDSV(image,'4','6');
   band_1_4_image = NDSV(image,'4','7');

   band_2_3_image = NDSV(image,'5','6');
   band_2_4_image = NDSV(image,'5','7');

   band_3_4_image = NDSV(image,'6','7');


}

band_1_2_image = band_1_2_image.addBands(band_1_3_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_1_4_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_3_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_2_4_image,null,false);
band_1_2_image = band_1_2_image.addBands(band_3_4_image,null,false);

var bandnames = ["ndsv_1_2", "ndsv_1_3", "ndsv_1_4", "ndsv_2_3", "ndsv_2_4", "ndsv_3_4"];
var ndsv = band_1_2_image.select(['.*'], bandnames);

return ndsv;

}

// Compute all the bands of NDSV depending on the image
function create_ndsv_img(image)
{
if(sensor==='L8')
    return create_ndsv_img_15_L8(image);
else if(sensor==='L7' || sensor==='L5' || sensor === 'L45')
    return create_ndsv_img_15(image);
else
    return create_ndsv_img_6(image);

}

// ====================================== //
//               Classifier               //
// ====================================== //

// generate training set of random points (Universe of cities)
function ts_generator(poly, numPoints, selectedCities,seed)
{
seed = (seed === undefined) ? 0 : seed;
var random_points = ee.FeatureCollection.randomPoints(poly, numPoints, seed);

var geom = ee.Feature(selectedCities.geometry());

var training_set = random_points.map(function (feature) {
    return feature.set("Number",
        ee.Algorithms.If(feature.containedIn(geom), 1, 0));
});

var numPoints_NotUrban = training_set.filter(ee.Filter.eq("Number", 0)).getInfo().features.length;
//print("not urban: " + numPoints_NotUrban);
var numPoints_Urban = training_set.filter(ee.Filter.eq("Number", 1)).getInfo().features.length;
//print("urban: " + numPoints_Urban);
var numPoits_toAdd = (numPoints_NotUrban-numPoints_Urban)/2;
random_points = ee.FeatureCollection.randomPoints(selectedCities, numPoits_toAdd);
var urban_points = random_points.map(function (feature) {
        return feature.set("Number",1);
});

training_set = training_set.merge(urban_points);

return training_set;

}

// return random point inside a polygon
function getPoints(polygon, num)
{

var random_points = ee.FeatureCollection.randomPoints(polygon, num);

var input_train_img = ee.Image('ESA/GLOBCOVER_L4_200901_200912_V2_3').select("1");

var blank = ee.Image(0); 
var output = blank.where(input_train_img, 1);
var mask_img = output.where(input_train_img.lt(190).or(input_train_img.gt(190)),0);

var x = mask_img.clip(polygon);

var x_erode  = morphology(x, 'Window.min', radius1, kernelType1, 'meters', 1);
var x_dilate = morphology(x, 'Window.max', radius1, kernelType1, 'meters', 1);

var morph = x_erode.add(x_dilate);
//Map.addLayer(morph, null, 'Input data morph');

var trainingImage_ =  ee.Image.cat(ee.Image(0), morph);

var trainingPoints = ee.apply("ReduceToVectors",{
    image: trainingImage_,
    reducer: ee.Reducer.mean(),  // The particular reducer doesn't matter, since it is a point geometry.
    geometry: random_points,
    scale: 30,                   // Scale at which the image is sampled.
    geometryType: 'centroid'     // The output will be a point. 
});

trainingPoints = trainingPoints.filter(ee.Filter.neq("mean", 1));
trainingPoints = trainingPoints.remap([0,2],[0,1],"mean");

var renamed_points = trainingPoints.map(function (feature) {
    return feature.set("Number", feature.get("mean"));
});

return renamed_points;

}

// select and create the fusion tables
function training_selector(ft_array)
{ 
var index;
var merge_ft = ft_array[0];
for (index = 1; index < ft_array.length; index++) 
{
    merge_ft = merge_ft.merge(ft_array[index]);
}

return merge_ft;
}

// classificiation
function classifier(img, ft, c, crs)
{
crs = (crs === undefined) ? "EPSG:4326" : crs;
var training = img.sampleRegions( ft, ["Number"], null, 
                                    ee.Projection(crs, [8.9831528411952135e-05, 0, -180, 0, -8.9831528411952135e-05, 90]));
var trained = c.train(training, "Number", img.bandNames());

/\ * OLD INSTRUCTION
var y = ee.apply("ClassifyImage",{
                "image": img,
                "classifierImage": training
});*\ /

// NEW INSTRUCTION
var classified = img.classify(trained);

return classified;
}

// Choose classification type: single classifier (multi = false) or three and median (multi = true)
function multi_classifier(img, ft, multiseed, multiclass, watermask, type)
{

var name = multiclass===true ? classifier_array[type[0]] : ee.Classifier.cart();\ :raw-html-m2r:`<br>`
var water = ee.Image("MOD44W/MOD44W_005_2000_02_24").select(["water_mask"]);
var classified, classified1, classified2, classified3;

if(multiseed===true)
{
    classified1 = classifier(img, ft[0], name);
    //Map.addLayer(classified1, {palette: '000000, ff0000'}, 'Classified1', false);
    classified2 = classifier(img, ft[1], name);
    //Map.addLayer(classified2, {palette: '000000, ff00ff'}, 'Classified2', false);
    classified3 = classifier(img, ft[2], name);
    //Map.addLayer(classified3, {palette: '000000, 00ff00'}, 'Classified3', false);
    classified = ee.ImageCollection([classified1, classified2, classified3]).median();
}
else
    classified = classifier(img, ft, name);

if(multiclass===true) // multi classifiers
{\ :raw-html-m2r:`<br>`
    var tmp1, tmp2, tmp3;

.. code-block::

   tmp1 = classified;
   Map.addLayer(ee.Image(0).mask(tmp1), {palette: '000000, ff0000'}, classifier_names[type[0]],false);
   tmp2 = classifier(img, ft, classifier_array[type[1]]);
   Map.addLayer(ee.Image(0).mask(tmp2), {palette: '000000, 00ff00'}, classifier_names[type[1]],false);
   tmp3 = classifier(img, ft, classifier_array[type[2]]);
   Map.addLayer(ee.Image(0).mask(tmp3), {palette: '000000, ff00ff'}, classifier_names[type[2]],false);
   classified =  ee.ImageCollection([tmp1, tmp2, tmp3]).median();


}

if(watermask===true)
{
    classified = classified.where(water,0);
}

return classified;
}

// Mask the image with slope
function slope_mask(imgIn, th)
{
var slope = ee.Algorithms.Terrain(dem);
return imgIn.where(slope.select("slope").gt(th),0);

}

// Mask the image with dem
function dem_mask(imgIn, th)
{
if(use_geometry === true)
    return imgIn.where(dem.clip(dem_geometry).select("elevation").gt(th), 0);
else
    return imgIn.where(dem.select("elevation").gt(th), 0);
}

/\ **\ **\ **\ **\ **\ **\ **\ **\ **\ **\ *******\ **\ **\ **\ **\ **\ **\ **\ **\ **\ **\ /
/\ *      MAIN IMAGE CLASSIFICATION FUNCTION     *\ /
/\ **\ **\ **\ **\ **\ **\ **\ **\ **\ **\ *******\ **\ **\ **\ **\ **\ **\ **\ **\ **\ **\ /
function image_classification(image_base, ft, year)
{
/\ **\ * NDSV *\ **\ /
var ndsv_img = create_ndsv_img(image_base);

//launch single or multi classification
var classified1 = multi_classifier(ndsv_img, ft, multi_random, multiclassifier, waterfilter, classifiers);
//Map.addLayer(classified1, {palette: '000000, ff8800'}, 'Classified ' + year, false);

if(mask_ndvi === true)
{
    var ndvi = 0;

.. code-block::

   if(collection_type === "greenest")
   ndvi = image_base.select("greenness");
   else
   ndvi = NDVI(image_base);

   classified1 = classified1.where(ndvi.gt(th_ndvi_high), 0);
   classified1 = classified1.where(ndvi.lte(th_ndvi_low), 0);

   //Map.addLayer(ee.Image(0).mask(classified1), {palette: '000000, efef00'}, 'NDVI Masked');


}

// Slope filtering
if(mask_slope === true)
{
    classified1 = slope_mask(classified1, th_slope);
    //Map.addLayer(ee.Image(0).mask(classified1), {palette: '000000, 00ef00'}, 'Slope Masked');
}

// Dem filtering
if(mask_dem === true)
{
    classified1 = dem_mask(classified1, th_dem);
    //Map.addLayer(ee.Image(0).mask(classified1), {palette: '000000, ef00ef'}, 'Dem Masked');
}

// launch morphology
if(morphology_on === true)
{
    var tmp = classified1.where(classified1.eq(0.5), classified1.add(0.5)).toInt().clamp(0,1);
    classified1 = morph_adjustment(tmp, radius1, radius2, kernelType);
}

return classified1;

}

// compute the area of the classification
function computeArea(input_img, polygon, year)
{
// Calculate area
var areaImage = input_img.multiply(ee.Image.pixelArea());
var stats = areaImage.reduceRegion(
    {
    'reducer': ee.Reducer.sum(),
    'geometry': polygon,
    'maxPixels': 5e9,
    'scale': area_scale,
    'bestEffort': true
    });
print('Area ' + year + ': ' + (stats.getInfo().classification/10e5) + ' KM^2');
}

// ===================================== //
//             Main function             //
// ===================================== //

var img_min = (collection_type==='simplecomposite') ? '3': '0.038';
var img_max = (collection_type==='simplecomposite') ? '63': '0.23';
var red = sensor==="L8" ? 'B4' : 'B3';
var green = sensor==="L8" ? 'B3' : 'B2';
var blue = sensor==="L8" ? 'B2' : 'B1';

// load the basic image
var image_base = input_selector(year, collection_type, sensor, cloud_cover, polygon1);
Map.addLayer(image_base.select(red,green,blue),{min: img_min, max: img_max},'Year '+ year);

/\ **\ * Ground Truth *\ **\ /
if(GT_enable===true)
Map.addLayer(GT_selectedRegions, {color: '900000'}, 'Ground Truth');

/\ **\ * Training set initilization *\ **\ /
var ft = 0;

if(ts_type===0) // Fusion table ts
{
var tables_array = new Array(ft17); // INSERT THE CODE(S) OF THE FUSION TABLE(S) TO USE
ft = training_selector(tables_array);

}
else if(ts_type===1) // Globcover ts
{
// random training set
var trainingPoints = getPoints(getPoly(lng,lat), num_points);
Map.addLayer(trainingPoints, {color: '00ffff'}, 'Random Points');
ft = ft.merge(trainingPoints);
}
else if(ts_type===2) // Universe of cities TS
{
// visualize cities
Map.addLayer(selectedCities, {color: '900000'}, 'Cities',false);
// generate training set
    // generate training set
if(multi_random===true)
{
    var ft_1 = ts_generator(polygon1, num_points, selectedCities, seeds[0]);
    var ft_2 = ts_generator(polygon1, num_points, selectedCities, seeds[1]);
    var ft_3 = ts_generator(polygon1, num_points, selectedCities, seeds[2]);
    ft = new Array(ft_1, ft_2, ft_3);
}else\ :raw-html-m2r:`<br>`
    ft = ts_generator(polygon1, num_points, selectedCities);
}
if(multi_random===true)
{
Map.addLayer(ft[0], {color:"00ffff"}, 'Features Points seed1', false);
Map.addLayer(ft[1], {color:"00ff00"}, 'Features Points seed2', false);
Map.addLayer(ft[2], {color:"ff00ff"}, 'Features Points seed3', false);
}
else
Map.addLayer(ft, {color:"00ffff"}, 'Features Points', false);

/\ **\ * array of classifications *\ **\ /
var class_array = [];

/\ **\ * first classification *\ **\ /
var classified = image_classification(image_base, ft, year);
Map.addLayer(ee.Image(0).mask(classified), palette_list[0], 'Classified Mask '+ year);
class_array.push(classified);
if(compute_area===true)
computeArea(classified, polygon1, year);

/\ **\ * Loop on all the years *\ **\ /
var classified_tmp;
var classified_collection_tmp;
var palette_index = 1;
var global_mask = classified;
var classified_collection;

for(var i=step; i<number_of_years; i+=step)
{
var x = 0;
while(x<=step)
{
    if(year-i>=2013)
    {
    sensor = 'L8';
    }
    if(year-i<2013 && year-i>2000)
    {
    sensor = 'L7';
    }
    else if (year-i<=2000 && year-i>1995)
    {
    sensor = 'L5';
    }
    else
    {
    sensor = 'L45';
    collection_type = 'standard';
    }

.. code-block::

   image_base = input_selector((year-i), collection_type, sensor, cloud_cover, polygon1);

   if(image_base.getInfo().bands.length !== 0)
   {

   classified_tmp = image_classification(image_base, ft, (year-i));

   if(class_or_flag===true)
   {
       class_array.push(classified_tmp);
       global_mask = global_mask.or(classified_tmp);

   }else
   {
       // logical AND with the previous year classification
       classified = classified_tmp.and(classified);
       if(compute_area===true)
       computeArea(classified, polygon1, year-i);
       Map.addLayer(ee.Image(0).mask(classified), palette_list[palette_index], 'Classified AND Mask '+ (year-i));
   }
   x = step+1;
   palette_index++;
   }
   else
   {
   x++;
   i++;
   }


}
}

if(class_or_flag===true)
{
// update global mask
global_mask = global_mask.and(closing(class_array[0], class_morph_radius, kernelType, units));
// visualize the corrected classified images
var dim = class_array.length;
for(var j=1; j<dim; j++)
{
    classified = class_array[j].and(global_mask);
    Map.addLayer(ee.Image(0).mask(classified), palette_list[j], 'Classified AND Mask '+ (year-(step\ *j)));
    if(compute_area===true)
    computeArea(classified, polygon1, year-(step*\ j));
}

}

// autocenter map
if(center_on === "")
autoCenterMap(polygon1, zoom);
else
autoCenterMap(cities_table.filter(ee.Filter.eq('MAIN_CITY', center_on)).geometry(), zoom+4);

//多行注释
/\ *
// download
exportImage(result_morph, task_name, 
{
'crs':'EPSG:4326', 
'scale':30, 
'region':JSON.stringify(polygon1.getInfo().coordinates),
'maxPixels':13000000000, 
'driveFolder':'prova'
});*\ /

.. code-block::


   # Python 
   ```python
   T = np.arctan2(cars['weight'],cars['mpg'])
   https://www.jianshu.com/p/c02291ab4c3b

Dtypes
^^^^^^

https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html##basics-dtypes


* df.convert_dtypes()

type transfer
~~~~~~~~~~~~~

.. code-block:: python

   dt = dfc.dtypes.to_dict()
   dt["行政区"] = pd.StringDtype()
   dt["街道"] = pd.StringDtype()
   dt["社区"] = pd.StringDtype()
   dt["小区/社区"] = pd.StringDtype()
   dt["确诊"] = pd.Int64Dtype()
   dt["疑似"] = pd.Int64Dtype()
   dt["通报日期"] = pd.DatetimeTZDtype(tz=8)

   dfc.astype(dt) ## 可以传递字典

数据存储类型与空值
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   ### 数据导入进pandas 进行convert_dtypes后 列中仍然存在空值  因此列的数据类型是str和Natype的混合
   pd.notna(dfc["街道"])
   pd.notna(dfc["街道"])

   pd.notna(dfc["街道"].astype(str)) ## 将NA也作为一种值 此时列的值是单一的

   pd.notna(dfc["确诊"])  ## 对于数值类型同理 也会得到false
   dfc["疑似"].fillna(0).astype(np.int32)

数值存储error
~~~~~~~~~~~~~

.. code-block:: python

   pd.to_numeric(s, errors='coerce') 
    ## If ‘raise’, then invalid parsing will raise an exception.
    ## If ‘coerce’, then invalid parsing will be set as NaN.
    ## If ‘ignore’, then invalid parsing will return the input.

Styling
^^^^^^^

.. code-block:: python

   ##dfc.style.background_gradient(cmap='viridis', low=.5, high=0).highlight_null('red') ##
   dfc.query("确诊 > 7")

常用操作
^^^^^^^^


* df.lookup()
* df.query()
* df.values
* df.apply()
* df.assign()
* df.set_index(["code"], append=True)

在整个表中选取
~~~~~~~~~~~~~~

.. code-block::



选取拼接的某几段
~~~~~~~~~~~~~~~~

.. code-block::

   df.iloc[pd.np.r_[10:12, 25:28]]

根据数据类型选取行
~~~~~~~~~~~~~~~~~~

.. code-block::

   dfc_intDate = dfc[dfc["通报日期"].apply(lambda x: isinstance(x, int))]

删除行
~~~~~~

.. code-block::

   dfc.drop(dfc_intDate.index.values).reset_index(drop=True)

重复行a
~~~~~~~

.. code-block::

   #### 找到重复的保存  
   dfd_cases = dfd.iloc[:,[-8,-7,-6,-1]] ## ['确诊', '疑似', '通报日期', 'code'] 重复
   dfd_dupli = dfd[dfd_cases.duplicated(keep=False)]## 查看 根据code和日期筛选重复值 




   ### 根据某些列的重复 进行去重  = drop_duplicates subset 参数
   ## dfd_R= dfd[dfd_cases.duplicated()!=True].reset_index(drop=True) ## 去掉重复的 Remove duplicated  

   ### 
   dfd_R = dfd_R.drop_duplicates(keep="first").reset_index(drop=True) ## inplace 在原对象上发生修改

   ## 这个更好 注意在哪几列查重
   dfc_R = dfc.drop_duplicates(subset = ["code","确诊","疑似","通报日期"],keep="first").reset_index() ## inplace 在原对象上发生修改  

   dfc_dupli = dfc_dupli.sort_values(by="code").reset_index()  ## 对结果排序使更好看
   dfd_dupli.to_excel("./2_Processed/WuhanData_1104_duplicated.xls",index=False)

links
~~~~~


* https://cloud.tencent.com/developer/article/1550971  

填充
^^^^

.. code-block:: python

   dfd_R_YS = dfd_R_YS.fillna(0).astype(np.int32).apply(lambda x : np.cumsum(x),axis=1)

日期
^^^^

.. code-block:: python

   dfc['通报日期'] = pd.to_datetime(dfc['通报日期'],format="%Y-%m-%d %H:%M:%S").dt.strftime("%Y/%m/%d") 

   dfc['通报日期'] = dfc['通报日期'].apply(lambda a: pd.to_datetime(a).date())  ### date()


   dfc['通报日期'].apply(lambda a: pd.to_datetime(a).strftime('%Y-%m-%d')) ### 一定要注意日期的输出格式！！！！

坐标解析
^^^^^^^^

.. code-block:: python

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
               ## ConnectTimeout指的是建立连接所用的时间，适用于网络状况正常的情况下，两端连接所用的时间。ReadTimeout指的是建立连接后从服务器读取到可用资源所用的时间。
           pass
       return loc

坐标转换
^^^^^^^^

.. code-block:: python

   import math

   class LngLatTransfer():

       def __init__(self):
           self.x_pi = 3.14159265358979324 * 3000.0 / 180.0
           self.pi = math.pi  ## π
           self.a = 6378245.0  ## 长半轴
           self.es = 0.00669342162296594323  ## 偏心率平方
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

pandoc
^^^^^^

pandoc -f markdown -t markdown -o X05_QM.md --shift-heading-level-by=-1 --atx-headers X05_QM.md

Pandas
======

https://github.com/firmai/pandasvault##table-processing

Genertate DF
------------

Create Data Frame
^^^^^^^^^^^^^^^^^

.. code-block:: python

   np.random.seed(1)
   """quick way to create a data frame for testing""" 
   df_test = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd']).assign(target=lambda x: (x['b']+x['a']/x['d'])*x['c'])

Data Frames For Testing
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import pandas.util.testing
   df1 = pd.util.testing.makeDataFrame()
   df2 = pd.util.testing.makeMissingDataframe() ## contains missing values
   df3 = pd.util.testing.makeTimeDataFrame() ## contains datetime values
   df4 = pd.util.testing.makeMixedDataFrame()

Table Processing
----------------

Configure Pandas
^^^^^^^^^^^^^^^^

.. code-block:: python

   ###
   def pd_config():
       options={
           "display":{
               'max_colwidth': 7, ### 每一格行宽度
               "max_columns":30,
               'expand_frame_repr': False,  ## wrap to multiple pages
               'max_rows': 30,
               'max_seq_items': 30,         ## Max length of printed sequence
               'precision': 3,               ## 小数精度
               'show_dimensions': True,    ##显示行列
               "large_repr":"truncate",##"info" show as summary of df 
               "unicode.east_asian_width":False, ## true to show east word in same length but in a longer time 
               "date_dayfirst":True ## 20/01/2005 false:2005/01/20
           },
           "mode":{
               'chained_assignment': None,
               "use_inf_as_na":False ##True means treat None, NaN, -INF, INF as NA (old way), False means None and NaN are null, but INF, -INF are not NA (new way).
           }
       }
       for category, option in options.items():
           for op, value in option.items():
               pd.set_option(f'{category}.{op}', value)  ## Python 3.6+
   ### pd.reset_option("^display")### 复原

Data Frame Formatting
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["number"] = [3,10,1]
   df_out = (
   df.style.format({"a":"${:.2f}", "target":"${:.5f}"})
   .hide_index()
   .highlight_min("a", color ="red")
   .highlight_max("a", color ="green")
   .background_gradient(subset = "target", cmap ="Blues")
   .bar("number", color = "lightblue", align = "zero")
   .set_caption("DF with different stylings")
   ) 
   df_out


.. image:: ./00_img/df_formatting.jpg
   :target: ./00_img/df_formatting.jpg
   :alt: image


Lower Case Columns
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df.columns = ["A","BGs","c","dag","Target"]##df.columns.to_list() 
   df.columns = map(str.lower, df.columns)

Fast Data Frame Split
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   test =  df.sample(frac=0.4) ### sample
   train = df[~df.isin(test)].dropna(); train

Create Features and Labels List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   ### 选择除A之外的列名
   X = [name for name in df.columns if name not in ["target", 'd']]

Gallery
^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["category"] = np.where( df["target"]>1, "1",  "0") 
   df["k"] = df["category"].astype(str) +": " + df["d"].round(1).astype(str) 
   df = df.append(df, ignore_index=True)

   """set display width, col_width etc for interactive pandas session""" 
   pd.set_option('display.width', 200)
   pd.set_option('display.max_colwidth', 20)
   pd.set_option('display.max_rows', 100)

   """when you have an excel sheet with spaces in column names"""
   df.columns = [c.lower().replace(' ', '_') for c in df.columns]

   """Add prefix to all columns"""
   df.add_prefix("1_")

   """Add suffix to all columns"""
   df.add_suffix("_Z")

   """Droping column where missing values are above a threshold"""
   df.dropna(thresh = len(df)*0.95, axis = "columns") 

   """Given a dataframe df to filter by a series ["a","b"]:""" 
   df[df['category'].isin(["1","0"])]

   """filter by multiple conditions in a dataframe df"""
   df[(df['a'] >1) & (df['b'] <1)]

   """filter by conditions and the condition on row labels(index)"""
   df[(df.a > 0) & (df.index.isin([0, 1]))]

   """regexp filters on strings (vectorized), use .* instead of *"""
   df[df.category.str.contains(r'.*[0-9].*')]

   """logical NOT is like this"""
   df[~df.category.str.contains(r'.*[0-9].*')]

   """creating complex filters using functions on rows"""
   df[df.apply(lambda x: x['b'] > x['c'], axis=1)]

   """Pandas replace operation"""
   df["a"].round(2).replace(0.87, 17, inplace=True)
   df["a"][df["a"] < 4] = 19

   """Conditionals and selectors"""
   df.loc[df["a"] > 1, ["a","b","target"]]

   """Selecting multiple column slices"""
   df.iloc[:, np.r_[0:2, 4:5]] 

   """apply and map examples"""
   df[["a","b","c"]].applymap(lambda x: x+1)

   """add 2 to row 3 and return the series"""
   df[["a","b","c"]].apply(lambda x: x[0]+2,axis=0)

   """add 3 to col A and return the series"""
   df.apply(lambda x: x['a']+1,axis=1)

   """ Split delimited values in a DataFrame column into two new columns """
   df['new1'], df['new2'] = zip(*df['k'].apply(lambda x: x.split(': ', 1)))

   """ Doing calculations with DataFrame columns that have missing values
   In example below, swap in 0 for df['col1'] cells that contain null """ 
   df['new3'] = np.where(pd.isnull(df['b']),0,df['a']) + df['c']

   """ Exclude certain data type or include certain data types """
   df.select_dtypes(exclude=['O','float'])
   df.select_dtypes(include=['int'])

   """one liner to normalize a data frame""" 
   (df[["a","b"]] - df[["a","b"]].mean()) / (df[["a","b"]].max() - df[["a","b"]].min())

   """groupby used like a histogram to obtain counts on sub-ranges of a variable, pretty handy""" 
   df.groupby(pd.cut(df.a, range(0, 1, 2))).size()

   """use a local variable use inside a query of pandas using @"""
   mean = df["a"].mean()
   df.query("a > @mean")

   """Calculate the % of missing values in each column"""
   df.isna().mean() 

   """Calculate the % of missing values in each row"""
   rows = df.isna().mean(axis=1) ; df.head()

Read Commands
^^^^^^^^^^^^^

.. code-block:: python

   """To avoid Unnamed: 0 when loading a previously saved csv with index"""
   """To parse dates"""
   """To set data types"""

   df_out = pd.read_csv("data.csv", index_col=0,
                   parse_dates=['D'],
                   dtype={"c":"category", "B":"int64"}).set_index("D")

   """Copy data to clipboard; like an excel copy and paste
   df = pd.read_clipboard()
   """

   """Read table from website
   df = pd.read_html(url, match="table_name")
   """

   """ Read pdf into dataframe ()
   !pip install tabula
   from tabula import read_pdf
   df = read_pdf('test.pdf', pages='all')
   """
   df_out.head()

Create Ordered Categories
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df["cats"] = ["bad","good","excellent"]
   from pandas.api.types import CategoricalDtype

   ### Let's create our own categorical order.
   cat_type = CategoricalDtype(["bad", "good", "excellent"], ordered = True)
   df["cats"] = df["cats"].astype(cat_type)

   ### Now we can use logical sorting.
   df = df.sort_values("cats", ascending = True)

   ### We can also filter this as if they are numbers.
   df[df["cats"] > "bad"]

Select Columns Based on Regex
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   ## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html
   df_out = df.filter(regex="_l",axis=1) 
   ## items : Keep labels from axis which are in items.
   ## like ：Keep labels from axis for which “like in label == True”.
   ## regex : 
   ## axis : 0 rows 1 columns

Accessing Group of Groupby Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df = df.append(df, ignore_index=True)
   df["groupie"] = ["falcon","hawk","hawk","eagle","falcon","hawk"]
   gbdf = df.groupby("groupie")
   hawk = gbdf.get_group("hawk").mean();

Multiple External Selection Criteria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   cr1 = df["a"] > 0
   cr2 = df["b"] < 0
   cr3 = df["c"] > 0
   cr4 = df["d"] >-1
   df[cr1 & cr2 & cr3 & cr4]

Memory Reduction Script (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import gc
   def reduce_mem_usage(df):
       """ iterate through all the columns of a dataframe and modify the data type
           to reduce memory usage.        
       """
       start_mem = df.memory_usage().sum() / 1024**2
       print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

       for col in df.columns:
           col_type = df[col].dtype
           gc.collect()
           if col_type != object:
               c_min = df[col].min()
               c_max = df[col].max()
               if str(col_type)[:3] == 'int':
                   if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                       df[col] = df[col].astype(np.int8)
                   elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                       df[col] = df[col].astype(np.int16)
                   elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                       df[col] = df[col].astype(np.int32)
                   elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                       df[col] = df[col].astype(np.int64)  
               else:
                   if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                       df[col] = df[col].astype(np.float16)
                   elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                       df[col] = df[col].astype(np.float32)
                   else:
                       df[col] = df[col].astype(np.float64)
           else:
               df[col] = df[col].astype('category')

       end_mem = df.memory_usage().sum() / 1024**2
       print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
       print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

       return df
   df_out = reduce_mem_usage(df); df_out

Verify Primary Key (func)
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["first_d"] = [0,1,2]
   df["second_d"] = [4,1,9]
   def verify_primary_key(df, column_list):
       return df.shape[0] == df.groupby(column_list).size().reset_index().shape[0]

   verify_primary_key(df, ["first_d","second_d"])

Shift Columns to Front (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   def list_shuff(items, df):
       "Bring a list of columns to the front"
       cols = list(df)
       for i in range(len(items)):
           cols.insert(i, cols.pop(cols.index(items[i])))
       df = df.loc[:, cols]
       df.reset_index(drop=True, inplace=True)
       return df

   df_out = list_shuff(["target","c","d"],df); df_out

Multiple Column Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df_out = (df.assign(stringed = df["a"].astype(str),
           ounces = df["b"]*12,##    this will allow yo set a title
           galons = lambda df: df["a"]/128)
          .query("b > -1")
          .style.set_caption("Average consumption"))

Method Chaining Technique
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df[df>df.mean()]  = None

   ## with line continuation character
   df_out = df.dropna(subset=["b","c"],how="all").loc[df["a"]>0].round(2).groupby(
   ["target","b"]).max() \
   .unstack() \
   .fillna(0) \
   .rolling(1).sum() \
   .reset_index() \
   .stack() \
   .ffill().bfill() 
   df_out

Load Multiple Files
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import os
   os.makedirs("folder",exist_ok=True,); df_test.to_csv("folder/first.csv",index=False) ; df_test.to_csv("folder/last.csv",index=False)

   import glob
   files = glob.glob('folder/*.csv')
   dfs = [pd.read_csv(fp) for fp in files]
   df_out = pd.concat(dfs)

Drop Rows with Column Substring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["string_feature"] = ["1xZoo", "Safe7x", "bat4"]
   substring = ["xZ","7z", "tab4"]
   df_out = df[~df.string_feature.str.contains('|'.join(substring))]
   df_out

Unnest (Explode) a Column
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.head()
   df["g"] = [[str(a)+lista for a in range(4)] for lista in ["a","b","c"]]
   df_out = df.explode("g"); df_out.iloc[:5,:]

Nest List Back into Column
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   #### Run above example first 
   df = df_out.copy()
   df_out['g'] = df_out.groupby(df_out.index)['g'].agg(list)
   df_out.head()

Split Cells With Lists
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.head()
   df["g"] = [",".join([str(a)+lista for a in range(4)]) for lista in ["a","b","c"]]
   df_out = df.assign(g = df["g"].str.split(",")).explode("g")

Table Exploration
-----------------

Groupby Functionality
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df["gr"] = [1, 1 , 0]
   df_out = df.groupby('gr').agg([np.sum, np.mean, np.std])
   df_out.iloc[:,:]

Cross Correlation Series Without Duplicates (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   def corr_list(df):

       return  (df.corr()
               .unstack()
               .sort_values(kind="quicksort",ascending=False)
               .drop_duplicates().iloc[1:]); df_out

   corr_list(df)

Missing Data Report
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df[df>df.mean()]  = None

   def missing_data(data):
       "Create a dataframe with a percentage and count of missing values"
       total = data.isnull().sum().sort_values(ascending = False)
       percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
       return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

   df_out = missing_data(df)

Duplicated Rows Report
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["a"].iloc[2] = df["a"].iloc[1]
   df["b"].iloc[2] = df["b"].iloc[1] 
   ## Get a report of all duplicate records in a dataframe, based on specific columns
   df_out = df[df.duplicated(['a'], keep=False)]

Skewness (func)
^^^^^^^^^^^^^^^

.. code-block:: python

   from scipy.stats import skew

   def display_skewness(data):
       '''show skewness information

           Parameters
           ----------
           data: pandas dataframe

           Return
           ------
           df: pandas dataframe
       '''
       numeric_cols = data.columns[data.dtypes != 'object'].tolist()
       skew_value = []

       for i in numeric_cols:
           skew_value += [skew(data[i])]
       df = pd.concat(
           [pd.Series(numeric_cols), pd.Series(data.dtypes[data.dtypes != 'object'].apply(lambda x: str(x)).values)
               , pd.Series(skew_value)], axis=1)
       df.columns = ['var_name', 'col_type', 'skew_value']

       return df

   display_skewness(df)

Feature Processing
------------------

Remove Correlated Pairs (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df= df_test.copy(); df
   def drop_corr(df, thresh=0.99,keep_cols=[]):
       df_corr = df.corr().abs()
       upper = df_corr.where(np.triu(np.ones(df_corr.shape), k=1).astype(np.bool))
       to_remove = [column for column in upper.columns if any(upper[column] > thresh)] ### Change to 99% for selection
       to_remove = [x for x in to_remove if x not in keep_cols]
       df_corr = df_corr.drop(columns = to_remove)
       return df.drop(to_remove,axis=1)

   df_out = drop_corr(df, thresh=0.1,keep_cols=["target"]); df_out

Replace Infrequently Occuring Categories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

替换频率比较小的类别

.. code-block:: python

   df = df_test.copy()
   df = df.append([df]*2)
   df["cat"] = ["bat","bat","rat","mat","mat","mat","mat","mat","mat"]; df
   def replace_small_cat(df, columns, thresh=0.2, term="other"):
       for col in columns:
           ## Step 1: count the frequencies
           frequencies = df[col].value_counts(normalize = True)
           ## Step 2: establish your threshold and filter the smaller categories
           small_categories = frequencies[frequencies < thresh].index
           df[col] = df[col].replace(small_categories, "Other")
       return df
   df_out = replace_small_cat(df,["cat"])

Quasi-Constant Features Detection (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["a"] = 3 
   def constant_feature_detect(data,threshold=0.98):
       data_copy = data.copy(deep=True)    ##if False Any changes to the data of the original will be reflected in the shallow copy
       quasi_constant_feature = []
       for feature in data_copy.columns:
           predominant = (data_copy[feature].value_counts() / np.float(
                       len(data_copy))).sort_values(ascending=False).values[0]
           if predominant >= threshold:
               quasi_constant_feature.append(feature)   
       return quasi_constant_feature

   ## the original dataset has no constant variable
   qconstant_col = constant_feature_detect(data=df,threshold=0.9)
   df_out = df.drop(qconstant_col, axis=1) ; df_out

Filling Missing Values Separately
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df[df>df.mean()]  = None 
   ## Clean up missing values in multiple DataFrame columns
   dict_fill = {'a': 4,'b': 3,'c': 5, 'd': 9999,'target': "False"}
   df = df.fillna(dict_fill) ;df

.. code-block:: python

   df = df_test.copy() ## Set DataFrame column values based on other column values
   df.loc[(df['a'] >1 ) & (df['c'] <0),['target']] = np.nan

Remove Non-numeric Values in Data Frame
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy().assign(target=lambda row: row["a"].round(4).astype(str)+"SC"+row["b"].round(4).astype(str))
   df["a"] = "TI4560L" + df["a"].round(4).astype(str)
   df_out = df.replace('[^0-9]+', '', regex=True)

Feature Scaling, Normalisation, Standardisation (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from sklearn.preprocessing import StandardScaler
   from sklearn.preprocessing import MinMaxScaler

   def scaler(df,scaler=None,train=True, target=None, cols_ignore=None, type="Standard"):

       if cols_ignore:
           hold = df[cols_ignore].copy()
           df = df.drop(cols_ignore,axis=1)
       if target:
           x = df.drop([target],axis=1).values ##returns a numpy array
       else:
           x = df.values
       if train:
           if type=="Standard":
           scal = StandardScaler()
           elif type=="MinMax":
           scal = MinMaxScaler()
           scal.fit(x)
           x_scaled = scal.transform(x)
       else:
           x_scaled = scaler.transform(x)

       if target:
           df_out = pd.DataFrame(x_scaled, index=df.index, columns=df.drop([target],axis=1).columns)
           df_out[target]= df[target]
       else:
           df_out = pd.DataFrame(x_scaled, index=df.index, columns=df.columns)

       df_out = pd.concat((hold,df_out),axis=1)
       if train:
           return df_out, scal
       else:
           return df_out

   df_out_train, scl = scaler(df,target="target",cols_ignore=["a"],type="MinMax")
   df_out_test = scaler(df_test,scaler=scl,train=False, target="target",cols_ignore=["a"])

Impute Null with Tail Distribution (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df[df>df.mean()]  = None
   def impute_null_with_tail(df,cols=[]):
       """
       replacing the NA by values that are at the far end of the distribution of that variable
       calculated by mean + 3*std
       """

       df = df.copy(deep=True)
       for i in cols:
           if df[i].isnull().sum()>0:
               df[i] = df[i].fillna(df[i].mean()+3*df[i].std())
           else:
               warn("Column %s has no missing" % i)
       return df    

   df_out = impute_null_with_tail(df,cols=df.columns); df_out

Detect Outliers (func)
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   def outlier_detect(data,col,threshold=3,method="IQR"):

       if method == "IQR":
           IQR = data[col].quantile(0.75) - data[col].quantile(0.25)
           Lower_fence = data[col].quantile(0.25) - (IQR * threshold)
           Upper_fence = data[col].quantile(0.75) + (IQR * threshold)
       if method == "STD":
           Upper_fence = data[col].mean() + threshold * data[col].std()
           Lower_fence = data[col].mean() - threshold * data[col].std()   
       if method == "OWN":
           Upper_fence = data[col].mean() + threshold * data[col].std()
           Lower_fence = data[col].mean() - threshold * data[col].std() 
       if method =="MAD":
           median = data[col].median()
           median_absolute_deviation = np.median([np.abs(y - median) for y in data[col]])
           modified_z_scores = pd.Series([0.6745 * (y - median) / median_absolute_deviation for y in data[col]])
           outlier_index = np.abs(modified_z_scores) > threshold
           print('Num of outlier detected:',outlier_index.value_counts()[1])
           print('Proportion of outlier detected',outlier_index.value_counts()[1]/len(outlier_index))
           return outlier_index, (median_absolute_deviation, median_absolute_deviation)


       para = (Upper_fence, Lower_fence)
       tmp = pd.concat([data[col]>Upper_fence,data[col]<Lower_fence],axis=1)
       outlier_index = tmp.any(axis=1)
       print('Num of outlier detected:',outlier_index.value_counts()[1])
       print('Proportion of outlier detected',outlier_index.value_counts()[1]/len(outlier_index))

       return outlier_index, para

   index,para = outlier_detect(df,"a",threshold=0.5,method="IQR")
   print('Upper bound:',para[0],'\nLower bound:',para[1])

Windsorize Outliers (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   def windsorization(data,col,para,strategy='both'):
       """
       top-coding & bottom coding (capping the maximum of a distribution at an arbitrarily set value,vice versa)
       """

       data_copy = data.copy(deep=True)  
       if strategy == 'both':
           data_copy.loc[data_copy[col]>para[0],col] = para[0]
           data_copy.loc[data_copy[col]<para[1],col] = para[1]
       elif strategy == 'top':
           data_copy.loc[data_copy[col]>para[0],col] = para[0]
       elif strategy == 'bottom':
           data_copy.loc[data_copy[col]<para[1],col] = para[1]  
       return data_copy


   df_out = windsorization(data=df,col='a',para=para,strategy='both')

Drop Outliers
^^^^^^^^^^^^^

.. code-block:: python

   ### run the top two examples
   df = df_test.copy()
   df_out = df[~index]

Impute Outliers
^^^^^^^^^^^^^^^

.. code-block:: python

   def impute_outlier(data,col,outlier_index,strategy='mean'):
       """
       impute outlier with mean/median/most frequent values of that variable.
       """

       data_copy = data.copy(deep=True)
       if strategy=='mean':
           data_copy.loc[outlier_index,col] = data_copy[col].mean()
       elif strategy=='median':
           data_copy.loc[outlier_index,col] = data_copy[col].median()
       elif strategy=='mode':
           data_copy.loc[outlier_index,col] = data_copy[col].mode()[0]   

       return data_copy

   df_out = impute_outlier(data=df,col='a', outlier_index=index,strategy='mean')

Feature Engineering
-------------------

Automated Dummy (one-hot) Encoding(func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["e"] = np.where(df["c"]> df["a"], 1,  2)
   def auto_dummy(df, unique=15):
       ## Creating dummies for small object uniques
       if len(df)<unique:
           raise ValueError('unique is set higher than data lenght')
       list_dummies =[]
       for col in df.columns:
           if (len(df[col].unique()) < unique):
               list_dummies.append(col)
               print(col)
       df_edit = pd.get_dummies(df, columns = list_dummies) ## Saves original dataframe
       ##df_edit = pd.concat([df[["year","qtr"]],df_edit],axis=1)
       return df_edit

   df_out = auto_dummy(df, unique=3)

Binarise Empty Columns (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df[df>df.mean()]  = None
   def binarise_empty(df, frac=80):
   ## Binarise slightly empty columns
       this =[]
       for col in df.columns:
           if df[col].dtype != "object":
               is_null = df[col].isnull().astype(int).sum()
               if (is_null/df.shape[0]) >frac: ## if more than 70% is null binarise
                   print(col)
                   this.append(col)
                   df[col] = df[col].astype(float)
                   df[col] = df[col].apply(lambda x: 0 if (np.isnan(x)) else 1)
       df = pd.get_dummies(df, columns = this) 
       return df

   df_out = binarise_empty(df, frac=0.6); df_out

Polynomials (func)
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   def polynomials(df, feature_list):
       for feat in feature_list:
           for feat_two in feature_list:
               if feat==feat_two:
                   continue
               else:
                   df[feat+"/"+feat_two] = df[feat]/(df[feat_two]-df[feat_two].min()) ##zero division guard
                   df[feat+"X"+feat_two] = df[feat]*(df[feat_two])
       return df

   df_out = polynomials(df, ["a","b"]) ; df_out

Transformations (func)
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   def transformations(df,features):
       df_new = df[features]
       df_new = df_new - df_new.min()

       sqr_name = [str(fa)+"_POWER_2" for fa in df_new.columns]
       log_p_name = [str(fa)+"_LOG_p_one_abs" for fa in df_new.columns]
       rec_p_name = [str(fa)+"_RECIP_p_one" for fa in df_new.columns]
       sqrt_name = [str(fa)+"_SQRT_p_one" for fa in df_new.columns]

       df_sqr = pd.DataFrame(np.power(df_new.values, 2),columns=sqr_name, index=df.index)
       df_log = pd.DataFrame(np.log(df_new.add(1).abs().values),columns=log_p_name, index=df.index)
       df_rec = pd.DataFrame(np.reciprocal(df_new.add(1).values),columns=rec_p_name, index=df.index)
       df_sqrt = pd.DataFrame(np.sqrt(df_new.abs().add(1).values),columns=sqrt_name, index=df.index)

       dfs = [df, df_sqr, df_log, df_rec, df_sqrt]
       df=  pd.concat(dfs, axis=1)
       return df

   df_out = transformations(df,["a","b"]); df_out

Genetic Programming
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   from gplearn.genetic import SymbolicTransformer
   function_set = ['add', 'sub', 'mul', 'div',
                   'sqrt', 'log', 'abs', 'neg', 'inv','tan']

   gp = SymbolicTransformer(generations=800, population_size=200,
                           hall_of_fame=100, n_components=10,
                           function_set=function_set,
                           parsimony_coefficient=0.0005,
                           max_samples=0.9, verbose=1,
                           random_state=0, n_jobs=6)

   gen_feats = gp.fit_transform(df.drop("target", axis=1), df["target"]); df.iloc[:,:8]
   df_out = pd.concat((df,pd.DataFrame(gen_feats, columns=["gen_"+str(a) for a in range(gen_feats.shape[1])])),axis=1); df_out.iloc[:,:8]

Prinicipal Component Features (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df =df_test.copy()
   from sklearn.decomposition import PCA, IncrementalPCA

   def pca_feature(df, memory_issues=False,mem_iss_component=False,variance_or_components=0.80,drop_cols=None):

       if memory_issues:
           if not mem_iss_component:
               raise ValueError("If you have memory issues, you have to preselect mem_iss_component")
       pca = IncrementalPCA(mem_iss_component)
       else:
           if variance_or_components>1:
               pca = PCA(n_components=variance_or_components) 
           else: ## automted selection based on variance
               pca = PCA(n_components=variance_or_components,svd_solver="full") 
       X_pca = pca.fit_transform(df.drop(drop_cols,axis=1))
       df = pd.concat((df[drop_cols],pd.DataFrame(X_pca, columns=["PCA_"+str(i+1) for i in range(X_pca.shape[1])])),axis=1)
       return df

   df_out =pca_feature(df,variance_or_components=0.80,drop_cols=["target","a"]); df_out

Multiple Lags (func)
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   def multiple_lags(df, start=1, end=3,columns=None):
       if not columns:
           columns = df.columns.to_list()
       lags = range(start, end+1)  ## Just two lags for demonstration.

       df = df.assign(**{
       '{}_t_{}'.format(col, t): df[col].shift(t)
       for t in lags
       for col in columns
       })
       return df

   df_out = multiple_lags(df, start=1, end=2,columns=["a","target"]); df_out

Multiple Rolling (func)
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   def multiple_rolling(df, windows = [1,2], functions=["mean","std"], columns=None):
       windows = [1+a for a in windows]
       if not columns:
           columns = df.columns.to_list()
       rolling_dfs = (df[columns].rolling(i)                                    ## 1. Create window
                       .agg(functions)                                ## 1. Aggregate
                       .rename({col: '{0}_{1:d}'.format(col, i)
                                   for col in columns}, axis=1)  ## 2. Rename columns
                   for i in windows)                                ## For each window
       df_out = pd.concat((df, *rolling_dfs), axis=1)
       da = df_out.iloc[:,len(df.columns):]
       da = [col[0] + "_" + col[1] for col in  da.columns.to_list()]
       df_out.columns = df.columns.to_list() + da 

       return  df_out                      ## 3. Concatenate dataframes

   df_out = multiple_rolling(df, columns=["a"])
   df_out

Date Features
^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["date_fake"] = pd.date_range(start="2019-01-03", end="2019-01-06", periods=len(df))
   def date_features(df, date="date"):
       df[date] = pd.to_datetime(df[date])
       df[date+"_month"] = df[date].dt.month.astype(int)
       df[date+"_year"]  = df[date].dt.year.astype(int)
       df[date+"_week"]  = df[date].dt.week.astype(int)
       df[date+"_day"]   = df[date].dt.day.astype(int)
       df[date+"_dayofweek"]= df[date].dt.dayofweek.astype(int)
       df[date+"_dayofyear"]= df[date].dt.dayofyear.astype(int)
       df[date+"_hour"] = df[date].dt.hour.astype(int)
       df[date+"_int"] = pd.to_datetime(df[date]).astype(int)
       return df

   df_out = date_features(df, date="date_fake"); df_out.iloc[:,:8]

Haversine Distance (Location Feature) (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["latitude"] = [39, 35 , 20]
   df["longitude"]=  [-77, -40 , -10 ]
   from math import sin, cos, sqrt, atan2, radians
   def haversine_distance(row, lon="latitude", lat="longitude"):
       c_lat,c_long = radians(52.5200), radians(13.4050)
       R = 6373.0
       long = radians(row['longitude'])
       lat = radians(row['latitude'])

       dlon = long - c_long
       dlat = lat - c_lat
       a = sin(dlat / 2)**2 + cos(lat) * cos(c_lat) * sin(dlon / 2)**2
       c = 2 * atan2(sqrt(a), sqrt(1 - a))

       return R * c

   df['distance_central'] = df.apply(haversine_distance,axis=1); df.iloc[:,4:]

Parse Address
^^^^^^^^^^^^^

.. code-block:: python

   df = df_test.copy()
   df["addr"] = pd.Series([
               'Washington, D.C. 20003',
               'Brooklyn, NY 11211-1755',
               'Omaha, NE 68154' ])
   regex = (r'(?P<city>[A-Za-z ]+), (?P<state>[A-Z]{2}) (?P<zip>\d{5}(?:-\d{4})?)')  

   df.addr.str.replace('.', '').str.extract(regex)

Processing Strings in Pandas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = pd.util.testing.makeMixedDataFrame()
   df["C"] = df["C"] + " " + df["C"]


   """convert column to UPPERCASE"""

   col_name = "C"
   df[col_name].str.upper()

   """count string occurence in each row"""
   df[col_name].str.count(r'\d') ## counts number of digits

   """count ## o chars in each row"""
   df[col_name].str.count('o') ## counts number of digits

   """split rows"""
   s = pd.Series(["this is a regular sentence", "https://docs.p.org", np.nan])
   s.str.split()

   """this creates new columns with the different split values (instead of lists)"""
   s.str.split(expand=True)  

   """limit the number of splits to 1, and start spliting from the rights side"""
   s.str.rsplit("/", n=1, expand=True)

Filtering Strings in Pandas
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   df = pd.util.testing.makeMixedDataFrame()
   df["C"] = df["C"] + " " + df["C"]
   col_name = "C"

   """check if a certain word/pattern occurs in each row"""
   df[col_name].str.contains('oo')  ## returns True/False for each row

   """find occurences"""
   df[col_name].str.findall(r'[ABC]\d') ## returns a list of the found occurences of the specified pattern for each row

   """replace Weekdays by abbrevations (e.g. Monday --> Mon)"""
   df[col_name].str.replace(r'(\w+day\b)', lambda x: x.groups[0][:3]) ## () in r'' creates a group with one element, which we acces with x.groups[0]

   """create dataframe from regex groups (str.extract() uses first match of the pattern only)"""
   df[col_name].str.extract(r'(\d?\d):(\d\d)')
   df[col_name].str.extract(r'(?P<hours>\d?\d):(?P<minutes>\d\d)')
   df[col_name].str.extract(r'(?P<time>(?P<hours>\d?\d):(?P<minutes>\d\d))')

   """if you want to take into account ALL matches in a row (not only first one):"""
   df[col_name].str.extractall(r'(\d?\d):(\d\d)') ## this generates a multiindex with level 1 = 'match', indicating the order of the match

   df[col_name].replace('\n', '', regex=True, inplace=True)

   """remove all the characters after &## (including &##) for column - col_1"""
   df[col_name].replace(' &##.*', '', regex=True, inplace=True)

   """remove white space at the beginning of string"""
   df[col_name] = df[col_name].str.lstrip()

Model Validation
----------------

Classification Metrics (func)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   y_test = [0, 1, 1, 1, 0]
   y_predict = [0, 0, 1, 1, 1]
   y_prob = [0.2,0.6,0.7,0.7,0.9]
   from sklearn.metrics import roc_auc_score, average_precision_score, confusion_matrix
   from sklearn.metrics import log_loss, brier_score_loss, accuracy_score

   def classification_scores(y_test, y_predict, y_prob):

       confusion_mat = confusion_matrix(y_test,y_predict)

       TN = confusion_mat[0][0]
       FP = confusion_mat[0][1]
       TP = confusion_mat[1][1]
       FN = confusion_mat[1][0]

       TPR = TP/(TP+FN)
       ## Specificity or true negative rate
       TNR = TN/(TN+FP) 
       ## Precision or positive predictive value
       PPV = TP/(TP+FP)
       ## Negative predictive value
       NPV = TN/(TN+FN)
       ## Fall out or false positive rate
       FPR = FP/(FP+TN)
       ## False negative rate
       FNR = FN/(TP+FN)
       ## False discovery rate
       FDR = FP/(TP+FP)

       ll = log_loss(y_test, y_prob) ## Its low but means nothing to me. 
       br = brier_score_loss(y_test, y_prob) ## Its low but means nothing to me. 
       acc = accuracy_score(y_test, y_predict)
       print(acc)
       auc = roc_auc_score(y_test, y_prob)
       print(auc)
       prc = average_precision_score(y_test, y_prob) 

       data = np.array([np.arange(1)]*1).T

       df_exec = pd.DataFrame(data)

       df_exec["Average Log Likelihood"] = ll
       df_exec["Brier Score Loss"] = br
       df_exec["Accuracy Score"] = acc
       df_exec["ROC AUC Sore"] = auc
       df_exec["Average Precision Score"] = prc
       df_exec["Precision - Bankrupt Firms"] = PPV
       df_exec["False Positive Rate (p-value)"] = FPR
       df_exec["Precision - Healthy Firms"] = NPV
       df_exec["False Negative Rate (recall error)"] = FNR
       df_exec["False Discovery Rate "] = FDR
       df_exec["All Observations"] = TN + TP + FN + FP
       df_exec["Bankruptcy Sample"] = TP + FN
       df_exec["Healthy Sample"] = TN + FP
       df_exec["Recalled Bankruptcy"] = TP + FP
       df_exec["Correct (True Positives)"] = TP
       df_exec["Incorrect (False Positives)"] = FP
       df_exec["Recalled Healthy"] = TN + FN
       df_exec["Correct (True Negatives)"] = TN
       df_exec["Incorrect (False Negatives)"] = FN

       df_exec = df_exec.T[1:]
       df_exec.columns = ["Metrics"]
       return df_exec


   met = classification_scores(y_test, y_predict, y_prob); met

Git
===
