#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
ps_arr={}
ps_arr['78']='959,159,1612,2uettottanta,1368,4C,719,8C,1615,Disco Volante,1334,Giulietta,1915,Gloria,681,MiTo,1614,TZ3'
ps_arr['56']='2061,CC100,1304,Cygnet,2071,DB5,343,DB9,342,DBS,1616,Lagonda,720,ONE''77,968,Rapide,938,V12 Vantage,517,V8 Vantage,1617,Vanquish ,1303,Virage,1394,Zagato'
ps_arr['148']='1978,ABT A1,1977,ABT A3,1979,ABT A4,1980,ABT A5,1981,ABT A6,1985,ABT A7,1982,ABT A8,1986,ABT Q3,1987,ABT Q5,1983,ABT Q7,1988,ABT R8,2321,ABT RS 4,1984,ABT TT'
ps_arr['1']='10005,'' 一汽''大众奥迪 '',2365,奥迪A3,553,奥迪A4L,8,奥迪A6L,1784,奥迪Q3,2458,奥迪Q4,758,奥迪Q5,10063,'' 进口奥迪 '',1653,Allroad,1821,Crosslane Coupe ,2404,Nanuk,575,奥迪A1,1026,奥迪A2,2450,奥迪A3 e''tron,2394,奥迪A3敞篷,694,奥迪A3两厢,1885,奥迪A3三厢,2,奥迪A4旅行车 ,1437,奥迪A5敞篷,1436,奥迪A5双门,4,奥迪A5掀背,827,奥迪A6(进口),1645,奥迪A6混合动力,957,奥迪A7,7,奥迪A8L,1543,奥迪A8L混合动力,1621,奥迪Cross ,2371,奥迪Q2,1287,奥迪Q3(进口),439,奥迪Q5(进口),1597,奥迪Q5混合动力,1,奥迪Q7,1961,奥迪Q8,1916,奥迪R18,5,奥迪R8,2480,奥迪S1,2491,奥迪S3敞篷,1027,奥迪S3两厢,1887,奥迪S3三厢,1917,奥迪S4,1439,奥迪S5敞篷,1438,奥迪S5双门,627,奥迪S5掀背,452,奥迪S6,1522,奥迪S7,6,奥迪S8,1785,奥迪SQ5,1442,奥迪TTS敞篷,1441,奥迪TTS双门,1440,奥迪TT敞篷,3,奥迪TT双门,1620,奥迪Urban ,1622,奥迪e''tron ,1618,奥迪quattro,10276,'' 进口奥迪RS '',1536,奥迪RS Q3,1624,奥迪RS3,691,奥迪RS4,1521,奥迪RS5,1625,奥迪RS6,1825,奥迪RS7,1626,奥迪TT RS ' 
ps_arr['118']='2332,巴博斯 A级,2333,巴博斯 B级,2065,巴博斯 CLS级,2334,巴博斯 CL级,1428,巴博斯 E级,1430,巴博斯 GL级,2335,巴博斯 G级,1429,巴博斯 M级,2336,巴博斯 SLK级,2337,巴博斯 SLS级,2338,巴博斯 SL级,1427,巴博斯 S级,1935,巴博斯 smart fortwo' 
ps_arr['52']='331,Boxster,330,Cayman,2063,Macan,745,Panamera,333,保时捷911,2449,保时捷917,1306,保时捷918,2508,保时捷919,332,卡宴' 
ps_arr['162']='1999,La Joya' 
ps_arr['109']='2466,宝骏610,1251,宝骏630,2522,宝骏730,143,乐驰' 
ps_arr['2']='10025,'' 华晨宝马 '',21,宝马3系,22,宝马5系,1391,宝马X1,10059,'' 进口宝马 '',1911,Active Tourer,1629,ConnectedDrive ,1630,EfficientDynamics ,2073,Gran Lusso,1631,Zagato Coupe ,1444,宝马1系敞篷,17,宝马1系两厢,1443,宝马1系双门,2399,宝马2系,2489,宝马2系Active Tourer,1568,宝马3系GT,1446,宝马3系敞篷,1790,宝马3系混合动力,1972,宝马3系旅行车,1445,宝马3系双门,13,宝马3系四门,2407,宝马4系敞篷,1327,宝马4系双门,1447,宝马5系GT,1639,宝马5系混合动力,1448,宝马5系旅行车,11,宝马5系四门,1449,宝马6系敞篷,15,宝马6系双门,1566,宝马6系四门,14,宝马7系,1450,宝马7系混合动力,2075,宝马GINA,656,宝马X1(进口),2372,宝马X2,16,宝马X3,1177,宝马X4,10,宝马X5,19,宝马X6,1459,宝马X6混合动力,12,宝马Z4,1371,宝马i3,1372,宝马i8,10218,'' 进口宝马M '',1451,宝马1系M,2415,宝马M2,1454,宝马M3敞篷,1453,宝马M3双门,1452,宝马M3四门,2377,宝马M4,1455,宝马M5,1456,宝马M6双门,1943,宝马M6四门,1457,宝马X5 M,1458,宝马X6 M' 
ps_arr['88']='2077,concept500,2078,concept900,2317,北京汽车B60,1206,北京汽车B61,1634,北京汽车B70,2318,北京汽车B90,1635,北京汽车BC302Z ,652,北京汽车BJ40,1224,北京汽车C30,2319,北京汽车C50E,1636,北京汽车C51X,1196,北京汽车C60,1637,北京汽车C60F ,1197,北京汽车C70,1198,北京汽车C71,1559,北京汽车C90L,2507,北京汽车E系列电动,1412,北京汽车E系列两厢,1907,北京汽车E系列三厢,1638,北京汽车T60 ' 
ps_arr['179']='2481,幻速S2,2482,幻速S3' 
ps_arr['129']='1772,威旺205,1333,威旺306,2413,威旺307,2379,威旺M20' 
ps_arr['123']='1871,BJ212,1152,角斗士,1060,陆霸,1809,陆铃,990,骑士,1810,锐铃,661,勇士,1165,域胜007,1811,越铃,1039,战旗' 
ps_arr['3']='10140,'' 北京奔驰 '',39,奔驰C级,40,奔驰E级,2452,奔驰E级混合动力,1338,奔驰GLK级,10186,'' 福建奔驰 '',1388,凌特,1182,威霆,1180,唯雅诺,10085,'' 进口奔驰 '',2079,Biome,1641,BlueZero ,2080,Ener''G''Force,2081,Silver Arrow,1541,Style Coupe,23,奔驰A级,450,奔驰B级,1760,奔驰CLA级,29,奔驰CLS级,2457,奔驰CLS级猎装车,1642,奔驰Citan ,1783,奔驰C级(进口),24,奔驰C级旅行车,35,奔驰E级(进口),1469,奔驰E级敞篷,1834,奔驰E级混合动力(进口),1833,奔驰E级旅行车,1468,奔驰E级双门,1796,奔驰F125,1643,奔驰F800 ,1808,奔驰GLA级,26,奔驰GL级,27,奔驰G级,33,奔驰M级,31,奔驰R级,28,奔驰SLK级,25,奔驰SL级,37,奔驰S级,1607,奔驰S级混合动力,2484,奔驰S级双门,2478,奔驰V级,1243,斯宾特Sprinter,32,唯雅诺(进口),10219,'' 进口奔驰AMG '',1845,奔驰A级AMG ,1886,奔驰CLA级AMG ,1461,奔驰CLS级AMG,2082,奔驰CL级AMG,1460,奔驰C级AMG,1644,奔驰E级AMG ,2456,奔驰GLA级AMG,1930,奔驰GL级AMG,1462,奔驰G级AMG,1463,奔驰M级AMG,1466,奔驰SLK级AMG,1120,奔驰SLS级AMG,1465,奔驰SL级AMG,1464,奔驰S级AMG,2467,奔驰Vision AMG' 
ps_arr['105']='2529,奔腾B30,969,奔腾B50,1944,奔腾B50 EV,323,奔腾B70,1398,奔腾B90,1786,奔腾X80' 
ps_arr['17']='10163,'' 东风本田 '',1558,艾力绅,151,本田CR''V,1798,杰德,936,思铂睿,150,思域,10022,'' 广汽本田 '',148,奥德赛,967,本田pilot,152,飞度,561,锋范,1109,歌诗图,1799,凌派,149,雅阁,10112,'' 进口本田 '',1883,奥德赛(海外),2109,本田AC''X,2368,本田Brio,2105,本田CONCEPT M,1174,本田CR''Z,2106,本田EV''Ster,2110,本田FCX,1842,本田Gear,2111,本田HSV''010 GT,964,本田Insight,582,本田Legend,2112,本田N BOX,2113,本田N ONE,2414,本田N''WGN,2018,本田NSX,2114,本田P''NUT,2107,本田Ridgeline,722,本田S2000,2412,本田S660,2117,本田SUT,2108,本田Step Bus,1822,本田Urban ,2439,本田VEZEL,2115,飞度(海外),1791,飞度混合动力,2116,歌诗图(海外),1851,思域(海外) ,845,思域混合动力,667,雅阁(海外)' 
ps_arr['152']='1998,BAC Mono' 
ps_arr['27']='258,比亚迪F0,257,比亚迪F3,1470,比亚迪F3DM,259,比亚迪F3R,260,比亚迪F6,794,比亚迪G3,1288,比亚迪G3R,2477,比亚迪G5,1113,比亚迪G6,1144,比亚迪L3,689,比亚迪M6,1087,比亚迪S6,1905,比亚迪S7,951,比亚迪e6,1514,秦,1770,思锐,1570,速锐' 
ps_arr['5']='10129,'' 东风标致 '',1789,CROSS 207,1519,CROSS 307,2431,标致2008,549,标致207两厢,1347,标致207三厢,1396,标致3008,1937,标致301,71,标致307两厢,1346,标致307三厢,1339,标致308,1106,标致408,1262,标致508,10074,'' 进口标致 '',2119,Urban Crossover,685,标致107,2486,标致108,1818,标致2008(进口),416,标致207CC,1423,标致208,567,标致3008(进口),1908,标致301(海外),1976,标致308(进口),1471,标致308CC,659,标致308SW,748,标致4007,1418,标致4008,2120,标致5008,1205,标致508(进口),2121,标致BB1,2122,标致EX1,2123,标致HR1,2124,标致HX1,2126,标致Onyx,1107,标致RCZ,2127,标致SR1,2128,标致SXC,2125,标致iOn' 
ps_arr['13']='10003,'' 上海通用别克 '',1733,昂科拉,1472,别克GL8豪华商务,123,别克GL8商务,1925,别克Riviera,122,君威,1384,君威GS,1089,君越,1473,君越eAssist,121,凯越,120,林荫大道,1110,英朗GT,1348,英朗XT,10092,'' 进口别克 '',451,昂科雷,2129,别克Business,1399,别克Encore,2131,别克Verano,1328,君威(进口),1881,君越(进口),1298,愿景Envision' 
ps_arr['57']='2146,Brooklands,1416,宾利Falcon,1847,飞驰 ,1147,慕尚,345,欧陆,2148,雅骏' 
ps_arr['58']='2147,Galibier,347,威航' 
ps_arr['154']='2000,Knight XV' 
ps_arr['28']='263,爱迪尔,906,福瑞达,1344,福运' 
ps_arr['29']='2447,奔奔,1253,奔奔LOVE,267,奔奔MINI,2068,长安CINTURX,1550,长安CS35,2390,长安CS75,2149,长安CS95,1242,长安CX20,1184,长安CX30三厢,2320,长安E30,1322,长安SENSE,2150,长安VOSS,709,长安v802,1367,逸动,2476,逸动混合动力,1513,悦翔V3,1736,悦翔V5,628,悦翔三厢,1888,致尚XT,1549,睿骋' 
ps_arr['130']='1250,长安金牛星,1406,长安欧诺,1759,长安神骐,1167,长安小卡,910,长安星光,1166,长安星卡,984,长安之星,1580,长安之星S460,1782,欧力威,2411,尊行,2410,睿行' 
ps_arr['30']='1178,长城C20R,1172,长城C30,1171,长城C50,1176,长城C70,803,长城M2,1291,长城M4,276,长城V80,273,风骏3,1596,风骏5,1951,风骏6,524,金迪尔,570,欧拉,1494,炫丽CROSS' 
ps_arr['124']='10214,'' 长安标致雪铁龙 '',2461,DS 5LS,2383,DS5,10224,'' 进口DS '',1929,DS Wild Rubis,646,DS3,1231,DS4,1285,DS5(进口),2347,DS9' 
ps_arr['136']='1863,Dokker,1866,Duster,1865,Lodgy ,1867,Logan,1868,Sandero' 
ps_arr['32']='2156,Copen,2419,Kopen,2157,MATERIA,2158,Mira,2159,PICO' 
ps_arr['4']='10001,'' 上海大众 '',1431,Cross Polo,1651,Polo GTI,56,Polo两厢,1350,Polo三厢,2384,朗境,1928,朗行,52,朗逸,601,帕萨特,54,桑塔纳,50,桑塔纳志俊,51,途安,658,途观,10002,'' 一汽''大众 '',58,宝来,1154,大众CC,1093,高尔夫,1476,高尔夫GTI,60,捷达,63,迈腾,62,速腾,1864,速腾GLI,10062,'' 进口大众 '',1375,Amarok 皮卡,721,BlueSport,2182,Buggy Up,2183,Bulli,1419,Cross Coupe,1474,Cross Golf,1823,CrossBlue ,1535,E''Bugster,2185,Jetta,2186,Milano,2187,New Compact,2188,Nils,1693,Passat,679,Polo(进口),2189,Routan,2190,Space Up,2504,T''ROC,2191,Taigun,1078,Tiguan,2184,e''Co''Motion,586,大众CC(进口),751,大众E''UP,49,大众EOS,2194,大众Fox,2193,大众Up!Lite,1838,大众XL1,2192,大众up!,2322,高尔(海外),2397,高尔夫(进口),1692,高尔夫GTI(进口),1574,高尔夫GTI敞篷,43,高尔夫R,2445,高尔夫R敞篷,1567,高尔夫敞篷,1475,高尔夫旅行车,42,辉腾,48,甲壳虫,2323,开迪(海外),2525,凯路威,41,迈特威Multivan,1478,迈腾旅行车,587,尚酷,1477,尚酷R,2324,途安(海外),47,途锐,1479,途锐混合动力,521,夏朗' 
ps_arr['11']='1001,Charger,2343,Charger SRT,2170,Circuit EV,1812,Dart,1004,Durango ,2171,Rampage,2172,道奇M80,111,锋哲,913,公羊,664,酷威,729,挑战者,2344,挑战者 SRT,2173,翼龙,725,蝰蛇' 
ps_arr['33']='1839,东风HUV,1595,御风' 
ps_arr['163']='191,奥丁,2455,俊风,187,锐骐皮卡,197,锐骐厢式车,1103,帅客,196,御轩' 
ps_arr['90']='1390,风神A60,2217,风神E30L,1480,风神H30 CROSS,647,风神S30' 
ps_arr['127']='2174,东风小康C35,1742,东风小康C37,1696,东风小康K01,1699,东风小康K07,1700,东风小康K07Ⅱ,1753,东风小康K17,1750,东风小康V07S,1751,东风小康V21,2325,东风小康V22,1752,东风小康V27,1792,东风小康V29 ,1964,风光' 
ps_arr['34']='409,V3菱悦,946,V5菱致,1599,V6菱仕,412,得利卡,945,东南V4,2175,东南V7,1256,希旺' 
ps_arr['155']='2001,Atlantic,2002,Karma,2004,Latigo,2003,Surf,2005,Tramonto' 
ps_arr['59']='589,California,1417,F12berlinetta,1749,LaFerrari ,2198,Sergio,1088,法拉利458,351,法拉利599,349,法拉利612,1273,法拉利FF' 
ps_arr['6']='10213,'' 广汽菲亚特 '',1407,菲翔,2060,致悦,10069,'' 进口菲亚特 '',2479,Avventura,79,博悦,966,多宝,2181,菲亚特126P,568,菲亚特500,1434,菲亚特500C,2067,菲亚特500L,732,菲亚特Fiorino Qubo,2176,菲亚特Idea,2177,菲亚特Panda,2178,菲亚特Strada,2179,菲亚特Uno,692,菲亚特熊猫,1387,菲跃,2180,派力奥(海外)' 
ps_arr['18']='10166,'' 广汽丰田 '',2380,YARiS L 致炫,677,汉兰达,166,凯美瑞,1802,凯美瑞 尊瑞,168,雅力士,1261,逸致,1562,逸致跨界车,10008,'' 一汽丰田 '',642,丰田RAV4,169,花冠,163,皇冠,162,卡罗拉,165,柯斯达,164,兰德酷路泽,160,普拉多,161,普锐斯,159,锐志,167,威驰,10109,'' 进口丰田 '',157,FJ酷路泽,552,HIACE,2454,JPN Taxi,737,Venza威飒,1236,埃尔法,2206,丰田1X,1255,丰田4Runner,1544,丰田86,2441,丰田AQUA,1183,丰田Auris,891,丰田Avalon,712,丰田Avensis,680,丰田Aygo,2434,丰田FCV,2207,丰田FCV''R,2471,丰田FT''1,1855,丰田FT''86,2208,丰田FT''Bh,2209,丰田FT''CH,2210,丰田FT''EV,743,丰田FT''HS,2199,丰田Fun''Vii,2211,丰田Hi''CT,2200,丰田Hilux,571,丰田IQ,2212,丰田ME.WE,742,丰田MR2,2202,丰田Matrix,2213,丰田NS4,155,丰田RAV4(进口),2214,丰田RiN,2203,丰田Tacoma,2204,丰田Urban Cruiser,733,丰田Verso,2201,丰田i''Road,156,汉兰达(进口),1126,红杉,761,皇冠(进口),1265,杰路驰,2132,卡罗拉(海外),1376,考斯特,900,兰德酷路泽(进口),564,普拉多(进口),158,普瑞维亚,2215,锐志(海外),1125,塞纳,1128,坦途,1882,威驰(海外),1381,小霸王WISH,2205,雅力士(海外),2216,悦佳' 
ps_arr['131']='1909,风行CM7,284,景逸,2490,景逸S3,1408,景逸SUV,2521,景逸X3,2218,景逸X5,283,菱智' 
ps_arr['116']='1378,探索者6,1379,探索者II,1380,探索者III,1577,小超人,1756,雄狮,1819,雄狮F16' 
ps_arr['178']='2468,启腾M70' 
ps_arr['10']='10017,'' 长安福特 '',109,嘉年华两厢,1352,嘉年华三厢,105,经典福克斯两厢,1351,经典福克斯三厢,107,麦柯斯S''MAX,1590,新福克斯两厢,1591,新福克斯三厢,2348,新蒙迪欧,1405,翼搏,1611,翼虎,104,致胜,10277,'' 江铃福特 '',1761,经典全顺,540,新世代全顺,10098,'' 进口福特 '',2250,Airstream,1828,Atlas ,1947,Escort,2421,Everest,2251,Falcon,2326,Formula,2252,Galaxy,2253,Ranger,2259,S''MAX(海外),2327,Super Duty,2254,Territory,2255,Tourneo Courier,2256,Tourneo Custom,2257,Vertrek,1527,福克斯ST,2492,福克斯（海外）,1852,福特B''MAX ,1859,福特C''MAX ,1269,福特E,2258,福特Evos,1267,福特F''150,2403,福特F''250,2401,福特F''350,1803,福特F''650 ,650,福特Flex,714,福特Fusion ,576,福特Ka,713,福特Taurus,1830,福特Transit ,687,福特iosis max,2260,嘉年华(海外),1424,嘉年华ST,2261,金牛座,2262,蒙迪欧(海外),1159,锐界EDGE,1820,探险者,731,野马,1400,翼搏(海外),103,翼虎(进口),2263,征服者' 
ps_arr['76']='923,MP''X蒙派克,2353,奥铃CTX,2358,奥铃TX,2357,奥铃捷运,1075,风景,545,风景快运,2069,蒙派克S,533,迷迪,1555,萨普,1554,拓陆者 ' 
ps_arr['168']='2009,弗那萨利 99' 
ps_arr['104']='2315,Acadia,2470,GMC CANYON,1274,GMC3500,1241,Savana,2314,Sierra,2313,Terrain,2312,Yukon' 
ps_arr['157']='2012,Apollo,2520,Explosion,2013,Tornante' 
ps_arr['119']='1432,观致3轿车,2488,观致3五门' 
ps_arr['111']='1277,Galue嘉路,1278,Himiko女王,1279,大蛇' 
ps_arr['103']='2331,Cabrio''Coupe,2329,E''jet,2330,e''linker,1920,传祺GA3,1233,传祺GA5,1389,传祺GS5' 
ps_arr['92']='1247,奥轩G3,1324,奥轩G5,1592,奥轩GX5,1569,财运100,1571,财运300,1572,财运500,2464,吉奥GA,1959,星朗,1589,星旺,1730,星旺CL,1967,星旺L,1965,星旺M1,1966,星旺M2' 
ps_arr['37']='1586,骏意,286,路宝,782,路尊大霸王,1140,路尊小霸王,1058,民意,287,赛豹,285,赛马,1869,中意V5' 
ps_arr['139']='2219,哈弗E,1932,哈弗H2,783,哈弗H5,1168,哈弗H6,1949,哈弗H7,1175,哈弗H8,2197,哈弗H9,1393,哈弗IF,269,哈弗·派' 
ps_arr['164']='2015,海格H5C,2459,海格H5V,2418,海格H7V,2311,龙威,2016,御骏' 
ps_arr['38']='289,福美来,2475,福美来M5,1504,福美来VS,291,海福星,1794,海马M3,1922,海马M6,1517,海马M8,2426,海马S5,1934,海马S7,791,海马骑士,293,普力马,789,丘比特' 
ps_arr['132']='2220,白马王子,1151,福仕达,1320,海马C2,1321,海马C3,793,海马Me,1769,海马V30,1318,海马爱尚,952,海马王子,2221,青蛙王子' 
ps_arr['158']='2072,VelociRaptor,2014,Venom GT' 
ps_arr['68']='376,悍马H2,375,悍马H3' 
ps_arr['125']='1605,途腾T1,1606,途腾T2,2310,途腾T3' 
ps_arr['106']='1506,红旗H7,2527,红旗L5,1542,红旗L7,643,红旗L9,947,红旗SUV' 
ps_arr['80']='1156,宝利格,1155,华泰B11,1207,路盛E70,229,圣达菲,236,特拉卡' 
ps_arr['141']='1956,HORKI''1' 
ps_arr['91']='1135,翱龙,1138,傲骏,1134,大柴神,1201,法萨特NCV,1133,旗胜F1,1481,旗胜V3,1137,挑战者,1136,小柴神' 
ps_arr['138']='1889,伊思坦纳' 
ps_arr['77']='2222,Jeep J12,2345,大切诺基 SRT,307,大切诺基(进口),306,牧马人,308,指南者,1884,自由光,735,自由客,304,自由人,2500,自由侠' 
ps_arr['95']='1296,吉利帝豪EC6''RV,770,吉利帝豪EC7,771,吉利帝豪EC7''RV,772,吉利帝豪EC8,2223,吉利帝豪EV7,773,吉利帝豪EV8,1258,吉利帝豪EX7,774,吉利帝豪EX8,775,吉利帝豪EX9,777,吉利帝豪GT,2224,吉利帝豪KC' 
ps_arr['96']='976,吉利GX7,971,吉利全球鹰EK''2,2225,吉利全球鹰GC3,972,吉利全球鹰GC5,2226,吉利全球鹰GC6,1382,吉利全球鹰GC7,2227,吉利全球鹰GS,974,吉利全球鹰GV5,1257,吉利全球鹰GX2,1551,吉利全球鹰GX5 ,2228,吉利全球鹰GX6,977,吉利全球鹰IG,970,吉利全球鹰熊猫,978,吉利全球鹰熊猫CROSS,1222,吉利全球鹰远景,1223,吉利全球鹰自由舰' 
ps_arr['94']='780,吉利英伦GE,1609,吉利英伦SC3,2229,吉利英伦SC5,1249,吉利英伦SC5''RV,778,吉利英伦SC6,2230,吉利英伦SC6''RV,1141,吉利英伦SC7,1537,吉利英伦SC7''RV,2231,吉利英伦SV5,1538,吉利英伦SX5 ,2232,吉利英伦SX6,1826,吉利英伦SX7,779,吉利英伦TX4,1220,吉利英伦金刚,1219,吉利英伦金鹰CROSS' 
ps_arr['159']='2017,Vulcano' 
ps_arr['44']='2328,宝斯通,310,宾悦,796,和悦,2512,和悦A13,2514,和悦A13 CROSS,2513,和悦A13 RS,1924,和悦A20,1800,和悦A30,795,和悦RS,1918,和悦S30,1601,和悦SC,2495,和悦iEV,2451,和悦iREV,1508,江淮S''11,309,瑞风,1286,瑞风M5,2233,瑞风M6,1553,瑞风S5,1579,瑞铃,311,瑞鹰,548,同悦,1499,同悦CROSS,1363,同悦RS,1740,星锐,584,愿景III,2309,愿景IV,939,悦悦,1652,悦悦CROSS' 
ps_arr['79']='542,宝典,541,宝威,1762,凯锐,1763,凯威,1764,凯运,1765,顺达,2387,新驭胜S350,1604,域虎,1200,驭胜S350' 
ps_arr['60']='2234,捷豹C''TYPE,2395,捷豹C''X17,1319,捷豹C''X75,2235,捷豹E''TYPE,1766,捷豹F''TYPE,2526,捷豹XE,440,捷豹XF,353,捷豹XJ,352,捷豹XK,2059,捷豹XQ' 
ps_arr['39']='408,大海狮,1575,大力神,294,阁瑞斯,1648,海狮,1195,海星,1345,金杯S50,1576,金典,1573,雷龙,2349,小海狮X30,2528,新海狮,1305,智尚S30' 
ps_arr['169']='2008,金威,2019,凯歌' 
ps_arr['170']='2020,金旅海狮,2021,金旅考斯特' 
ps_arr['171']='2460,艾菲,2375,大MPV,2022,九龙A5,2023,九龙A6' 
ps_arr['165']='2024,X''BOW' 
ps_arr['133']='1773,卡尔森C,1774,卡尔森CGL,2025,卡尔森CK,2373,卡尔森CML,1775,卡尔森CS' 
ps_arr['99']='2509,开瑞Q26,1335,优劲,1112,优派,1150,优胜,1114,优雅,1226,优优' 
ps_arr['172']='2026,战盾' 
ps_arr['69']='10136,'' 上海通用凯迪拉克 '',1771,凯迪拉克XTS,10093,'' 进口凯迪拉克 '',2376,Elmiraj,1401,凯迪拉克ATS,705,凯迪拉克BLS,381,凯迪拉克CTS(进口),1482,凯迪拉克CTS双门,2236,凯迪拉克Ciel,1815,凯迪拉克ELR,380,凯迪拉克SRX,1130,凯迪拉克XTS(进口),378,凯雷德' 
ps_arr['121']='2502,One:1,1512,柯尼塞格Agera,1511,柯尼塞格CCR,1510,柯尼塞格CCXR' 
ps_arr['12']='10201,'' 东南克莱斯勒 '',115,大捷龙,10101,'' 进口克莱斯勒 '',1385,城乡,1654,大捷龙(进口),1837,克莱斯勒200,715,克莱斯勒200C,2342,克莱斯勒300C SRT,993,克莱斯勒300C(进口),2239,克莱斯勒700C,2237,克莱斯勒Delta,716,克莱斯勒Sebring,2238,克莱斯勒Ypsilon,1230,猎兽PROWLER' 
ps_arr['173']='2032,蓝旗亚Delta,2027,蓝旗亚Flavia,2028,蓝旗亚Stratos,2029,蓝旗亚Thema,2030,蓝旗亚Voyager,2031,蓝旗亚Ypsilon' 
ps_arr['61']='1299,Aventador ,2006,Egoista,961,Estoque,356,Gallardo,2462,Huracan,744,Insecta,727,Reventon,1534,Urus,1857,Veneno' 
ps_arr['150']='1975,朗世' 
ps_arr['174']='2036,劳伦士C级,2033,劳伦士E级,2037,劳伦士G级,2034,劳伦士M级,2035,劳伦士S级' 
ps_arr['62']='1139,古思特,358,幻影,1858,魅影' 
ps_arr['71']='1145,雷克萨斯CT,389,雷克萨斯ES,1602,雷克萨斯ES混合动力,390,雷克萨斯GS,1501,雷克萨斯GS混合动力,832,雷克萨斯GX,1122,雷克萨斯HS,387,雷克萨斯IS,1503,雷克萨斯IS敞篷,723,雷克萨斯LF''A,2240,雷克萨斯LF''CC,2241,雷克萨斯LF''Gh,1530,雷克萨斯LF''LC,2405,雷克萨斯LF''NX,739,雷克萨斯LF''Xh,391,雷克萨斯LS,1502,雷克萨斯LS混合动力,385,雷克萨斯LX,2424,雷克萨斯RC,384,雷克萨斯RX,991,雷克萨斯RX混合动力' 
ps_arr['63']='1483,大风景,360,风景,1235,风朗,740,科雷傲,666,克力奥,359,拉古那,1484,拉古那古贝,2246,雷诺Alpine,1827,雷诺Captur,862,雷诺Espace,1797,雷诺Frendzy,2483,雷诺Kwid,1914,雷诺R''Space,1913,雷诺Symbol,2247,雷诺Twin''Run,2248,雷诺Twin''Z,1025,雷诺Twingo,1912,雷诺Twizy,1148,雷诺Wind,1850,雷诺ZOE ,362,梅甘娜 ,1545,塔利斯曼,1227,纬度' 
ps_arr['112']='1280,理念S1' 
ps_arr['40']='1582,丰顺,1556,福顺,629,力帆320,1927,力帆330,295,力帆520,1509,力帆520i,1594,力帆530,417,力帆620,1942,力帆630,1308,力帆720,2518,力帆820,2430,力帆X50,1282,力帆X60,1587,兴顺' 
ps_arr['108']='1364,莲花L3两厢,1083,莲花L3三厢,1173,莲花L5,1600,莲花L6,1515,莲花T5,928,莲花savvy' 
ps_arr['31']='1099,飞铃皮卡,905,飞腾,2242,飞腾C5,1098,飞扬皮卡,1033,黑金刚,277,猎豹CS6,1816,猎豹CT5,1082,猎豹欧酷曼,526,猎豹奇兵' 
ps_arr['70']='383,城市,1824,林肯MKC,1216,林肯MKS,1215,林肯MKT ,738,林肯MKX,1214,林肯MKZ ,382,领航员' 
ps_arr['19']='10180,'' 昌河铃木 '',264,北斗星,261,浪迪,2433,利亚纳A6两厢,1954,利亚纳A6三厢,265,利亚纳两厢,1353,利亚纳三厢,572,派喜,10016,'' 长安铃木 '',172,奥拓,2389,锋驭,444,羚羊,174,天语SX4两厢,1266,天语尚悦,176,雨燕,10114,'' 进口铃木 '',2245,Authentics,2498,Celerio,2442,Crosshiker,2440,HUSTLER,2244,Regina,1787,S''CROSS(海外),1021,SX4 S''CROSS,2443,X''Lander,171,超级维特拉,170,吉姆尼,1090,凯泽西,2392,铃木iV''4,2243,派喜(海外),1179,速翼特' 
ps_arr['65']='365,发现,366,揽胜,653,揽胜极光,1163,揽胜运动版,1906,路虎DC100 ,955,神行者,820,卫士' 
ps_arr['24']='2276,Elan,364,Elise,2277,Elite,2278,Eterne,585,Evora,950,Exige' 
ps_arr['45']='314,风尚,1619,陆风X5,313,陆风X6,760,陆风X8,475,陆风X9' 
ps_arr['54']='10274,'' JOHN COOPER WORKS '',2354,MINI JCW,2356,MINI JCW CLUBMAN,2359,MINI JCW COUNTRYMAN,2355,MINI JCW COUPE,2360,MINI JCW PACEMAN,10060,'' MINI '',336,MINI ,2280,MINI BEACHCOMBER,686,MINI CABRIO,337,MINI CLUBMAN,2279,MINI CLUBVAN,693,MINI COUNTRYMAN,1337,MINI COUPE,1776,MINI PACEMAN,1343,MINI ROADSTER,2370,MINI VISION' 
ps_arr['156']='2007,Evantra' 
ps_arr['66']='2505,Alfieri,1904,Ghibli,1162,GranCabrio ,2064,Levante,370,玛莎拉蒂GT,369,总裁' 
ps_arr['14']='10162,'' 长安马自达 '',2524,昂科塞拉三厢,2493,昂克赛拉两厢,136,马自达2,1355,马自达2三厢,131,马自达3,1386,马自达3星骋两厢,1377,马自达3星骋三厢,1923,马自达CX''5,10053,'' 一汽马自达 '',2523,阿特兹,132,马自达6,1160,马自达8,1891,马自达CX''7,538,睿翼,1485,睿翼轿跑,10106,'' 进口马自达 '',1841,ATENZA,2501,Hazumi,2281,Shinari,1532,Takeri,2282,马自达2(海外),129,马自达3(进口),130,马自达5,1921,马自达6 Wagon,1807,马自达CX''3,1294,马自达CX''5(进口),654,马自达CX''7(进口),1628,马自达CX''9,724,马自达MX''5 ,128,马自达RX''8' 
ps_arr['53']='335,迈巴赫' 
ps_arr['126']='1640,迈凯伦12C ,2487,迈凯伦650S,1840,迈凯伦P1 ,1897,迈凯伦X''1' 
ps_arr['153']='2038,MELKUS RS2000' 
ps_arr['15']='1552,Icon,1950,MG CS,1263,MG3,1435,MG3 Xross,706,MG5,1365,MG6三厢,698,MG6掀背,138,MG7' 
ps_arr['175']='2367,摩根4''4,2039,摩根Aero,2040,摩根Plus 8,2366,摩根Roadster' 
ps_arr['113']='1297,MASTER CEO,1893,大7 MPV,1289,大7 SUV,1781,纳智捷 5 Sedan,2423,优6' 
ps_arr['166']='2042,Noble M12,2043,Noble M14,2044,Noble M15,2041,Noble M600' 
ps_arr['55']='407,安德拉,865,麦瑞纳,707,欧宝AMPERA,1861,欧宝Adam ,708,欧宝CORSA,1862,欧宝Cascada,2284,欧宝Combo,2285,欧宝Mokka,2381,欧宝Monza,341,赛飞利,1498,雅特敞篷,339,雅特两厢,1497,雅特三厢,592,英速亚' 
ps_arr['117']='2420,欧朗两厢,1395,欧朗三厢' 
ps_arr['72']='2386,讴歌ILX,1523,讴歌ILX混合动力,518,讴歌MDX ,1564,讴歌NSX,1518,讴歌RDX,1793,讴歌RLX,2283,讴歌SUV''X,392,讴歌TL,2465,讴歌TLX,718,讴歌TSX,810,讴歌ZDX' 
ps_arr['84']='2286,Huayra,632,Zonda' 
ps_arr['160']='2045,CEVENNES,2046,HEMERA' 
ps_arr['25']='2350,艾瑞泽3,2516,艾瑞泽5,1946,艾瑞泽7,246,东方之子,1357,风云2两厢,948,风云2三厢,2287,奇瑞@ANT,244,奇瑞A1,2196,奇瑞A2,1356,奇瑞A3两厢,239,奇瑞A3三厢,1284,奇瑞E3,1302,奇瑞E5,726,奇瑞M14,1836,奇瑞QQ,245,奇瑞QQ3,1801,奇瑞QQ3 EV,2288,奇瑞TX,1102,奇瑞X1,1757,奇瑞爱卡,1185,旗云1,1186,旗云2,1187,旗云3,1311,旗云5,241,瑞虎,2515,瑞虎3,1948,瑞虎5' 
ps_arr['22']='10015,'' 东风悦达起亚 '',757,福瑞迪,1392,起亚K2两厢,1293,起亚K2三厢,1403,起亚K3,2497,起亚K3S,1260,起亚K5,219,锐欧,218,赛拉图,1358,赛拉图欧风,217,狮跑,577,秀尔,1225,智跑,10117,'' 进口起亚 '',2472,GT4 Stinger,210,霸锐,1116,凯尊,1894,起亚CUB,1404,起亚Cee’d,2291,起亚Cross GT,1844,起亚Forte ,1341,起亚GT,1779,起亚K5混合动力,1777,起亚K9,2393,起亚Niro,2195,起亚Optima,1373,起亚Picanto,1854,起亚Provo,2292,起亚Ray EV,1561,起亚Trackster,215,起亚VQ,1516,起亚VQ''R,1123,起亚venga,2293,锐欧(海外),1052,狮跑(进口),1085,速迈,212,索兰托,211,新佳乐,2294,秀尔(海外)' 
ps_arr['114']='2289,晨风,1309,启辰D50,1613,启辰R50,2408,启辰R50X,2062,启辰R60,2290,启辰ViWa' 
ps_arr['20']='10013,'' 东风日产 '',1340,楼兰,1100,玛驰,404,奇骏,189,天籁,1608,新一代轩逸,194,轩逸经典,193,阳光,190,逍客,199,骊威,186,骐达,10164,'' 郑州日产 '',195,帕拉丁,192,日产D22皮卡,185,日产D22厢式车,1169,日产NV200,10111,'' 进口日产 '',441,Altima,2274,Armada,2427,BladeGlider,2265,DeltaWing,2264,Extrem,1953,Friend''ME,2266,Frontier,2267,Hi''Cross,2438,IDX,2268,Invitation,1738,Pathfinder,1831,Resonance,2391,Rogue,2269,Sentra,2473,Sports Sedan,2270,Terra,2271,Titan,1829,Versa,872,碧莲,178,贵士,180,楼兰(海外),869,玛驰(海外),181,奇骏(进口),588,日产370Z,700,日产Cube,641,日产GT''R,1143,日产Juke,798,日产NUVU,2272,日产NV200(海外),2273,日产NV3500,184,途乐,2275,逍客(海外),1091,聆风' 
ps_arr['46']='1086,荣威350,315,荣威550,2446,荣威550混合动力,316,荣威750,1486,荣威750混合动力,1080,荣威950,933,荣威E50,1194,荣威W5' 
ps_arr['149']='1973,如虎 CTR 3,2047,如虎 RT 12,2048,如虎 XL' 
ps_arr['97']='1528,瑞麒G2,1170,瑞麒G3,953,瑞麒G5,578,瑞麒G6,786,瑞麒M1,1193,瑞麒M3,1192,瑞麒M5,1301,瑞麒Z5' 
ps_arr['140']='1900,Scion FR''S,1901,Scion iQ,1899,Scion tC,2049,Scion xA,1902,Scion xB,2050,Scion xD' 
ps_arr['83']='1539,smart for''us,2517,smart forfour,1931,smart forjeremy,1936,smart forstars,566,smart fortwo,1940,smart fortwo 电动车' 
ps_arr['67']='728,萨博9X' 
ps_arr['110']='1268,斯派朗' 
ps_arr['21']='10144,'' 东南三菱 '',2083,三菱风迪思,205,三菱戈蓝,563,三菱君阁,1149,三菱蓝瑟,209,三菱翼神,10160,'' 广汽三菱 '',1768,劲炫ASX,207,帕杰罗,1952,帕杰罗劲畅,10107,'' 进口三菱 '',2295,Endeavor,1316,Global Small ,1806,Mirage,2444,eK Space,204,格蓝迪,415,蓝瑟翼豪陆神 ,202,欧蓝德(进口),200,帕杰罗(进口),1317,帕杰罗劲畅(进口),2296,三菱CA''MiEV,702,三菱Colt,1945,三菱G4,2436,三菱GC''PHEV,2297,三菱GR''HEV,2298,三菱PX''MiEV,2435,三菱XR''PHEV,579,三菱i' 
ps_arr['151']='2051,Tuatara,2052,Ultimate' 
ps_arr['147']='1974,福家' 
ps_arr['134']='2053,上汽大通G10,1804,上汽大通V80' 
ps_arr['135']='1546,绅宝' 
ps_arr['87']='1870,世爵B6,927,世爵C12,1050,世爵C8,663,世爵D12' 
ps_arr['146']='1971,首望' 
ps_arr['47']='318,双环SCEO,317,小贵族' 
ps_arr['75']='400,爱腾,1336,柯兰多,402,雷斯特,2011,雷斯特W,399,路帝,2306,双龙SIV''1,2307,双龙XIV''1,1565,双龙XIV''2,2506,双龙XLV,2305,双龙e''XIV,401,享御,403,主席' 
ps_arr['73']='2453,CROSS SPORT,2437,LEVORG,2299,Trezia,2300,Viziv,395,傲虎,397,驰鹏,396,力狮,394,森林人,1526,斯巴鲁BRZ,930,斯巴鲁G4e,2428,斯巴鲁WRX,1369,斯巴鲁XV,1359,翼豹三厢' 
ps_arr['7']='10148,'' 上海大众斯柯达 '',536,晶锐,1488,晶锐Scout,86,明锐,1489,明锐RS,2369,速派,2084,野帝,638,昊锐,2448,昕动,1578,昕锐,10065,'' 进口斯柯达 '',1421,Citigo,1533,Mission L,2352,Polar,1017,Roomster,2301,Vision D,2503,VisionC,672,Yeti(进口),2302,晶锐(海外),1853,明锐(海外),2118,明锐RS(海外),1955,速尊,1719,昊锐(海外),2066,昕锐(海外)' 
ps_arr['120']='1505,思铭' 
ps_arr['167']='2054,Tramontana' 
ps_arr['161']='2055,Sagaris,2056,Tuscan' 
ps_arr['122']='1548,腾势概念车' 
ps_arr['142']='1962,MODEL S,1960,MODEL X,1963,TESLA Roadster' 
ps_arr['128']='1724,威兹曼GT,2058,威兹曼Roadster,2057,威兹曼Spyder' 
ps_arr['98']='1248,威麟H3,1096,威麟H5,1095,威麟V5,986,威麟V8,590,威麟X5' 
ps_arr['9']='10143,'' 长安沃尔沃 '',634,沃尔沃S80L,10278,'' 沃尔沃亚太 '',2425,沃尔沃S60L,10084,'' 进口沃尔沃 '',2316,Air Motion,2499,ESTATE,2303,Universe,97,沃尔沃C30,2396,沃尔沃Coupe,520,沃尔沃S60,100,沃尔沃S80,1414,沃尔沃V40,1795,沃尔沃V40越界车,669,沃尔沃V50,1307,沃尔沃V60,671,沃尔沃V70,2469,沃尔沃XC Coupe,98,沃尔沃XC60,101,沃尔沃XC70,99,沃尔沃XC90,2304,沃尔沃You' 
ps_arr['137']='1874,沃克斯豪尔Adam,1872,沃克斯豪尔Antara,1873,沃克斯豪尔Astra,1875,沃克斯豪尔Cascada,1876,沃克斯豪尔Corsa,1877,沃克斯豪尔Insignia,1878,沃克斯豪尔Meriva,1879,沃克斯豪尔Mokka,1880,沃克斯豪尔VXR8' 
ps_arr['82']='1217,五菱宏光,547,五菱荣光,2096,五菱荣光小卡,554,五菱之光' 
ps_arr['145']='1970,五十铃皮卡 ' 
ps_arr['86']='995,欧悦搏,674,西雅特ALTEA,711,西雅特EXEO,1409,西雅特IBE,1410,西雅特IBL,1411,西雅特IBX,753,西雅特LEON,1425,西雅特Mii,580,伊比飒,2363,伊比飒旅行车' 
ps_arr['23']='10012,'' 北京现代 '',645,i30,2511,ix25,1094,ix35,1531,朗动,1939,名图,235,名驭,1778,全新胜达,1491,瑞纳,1164,瑞奕,1270,索纳塔八,233,新途胜,234,雅绅特,231,伊兰特,232,悦动,10116,'' 进口现代 '',2160,Blue2,2161,Curb,2162,Hexa Space,2494,Intrado,2163,Nuvis,2167,Sonata(海外),1290,Veloster飞思,1633,i10,668,i20,1422,i30(海外),2164,ix20,2165,ix35(海外),2351,格锐,1202,辉翼,2374,朗动(海外),413,劳恩斯,631,劳恩斯酷派,511,全新胜达(进口),2432,瑞纳(海外）,223,圣达菲(进口),527,途胜(进口),224,维拉克斯,1860,现代HB20 ,1896,现代HND''9 ,2166,现代RB,1420,现代i''oniq,1329,现代i40,227,雅科仕,2168,雅绅特(海外),226,雅尊,2169,伊兰特(海外)' 
ps_arr['176']='2364,凯胜1代,2361,凯胜2代' 
ps_arr['16']='10135,'' 上海通用雪佛兰 '',1331,爱唯欧两厢,1361,爱唯欧三厢,2474,创酷,142,景程,630,科鲁兹三厢,1933,科鲁兹掀背,1374,科帕奇,1402,迈锐宝,1958,赛欧SPRINGO,1360,赛欧两厢,141,赛欧三厢,10094,'' 进口雪佛兰 '',2133,Agile,2134,Caprice,2485,City Express,2139,Cobalt,2135,Colorado,2136,Equinox,2145,Express,2137,Impala,1832,Silverado,1161,Sonic,2406,Suburban,2138,TrailBlazer,710,VOLT沃蓝达,920,科尔维特,1415,科鲁兹(海外),730,科迈罗,445,科帕奇(进口),717,迈锐宝(海外),1079,斯帕可,670,雪佛兰Beat,2140,雪佛兰Code,2141,雪佛兰Miray,2142,雪佛兰Onix,734,雪佛兰Orlando,1846,雪佛兰SS,2143,雪佛兰Tahoe,662,雪佛兰Traverse,1632,雪佛兰Trax,2144,雪佛兰Tru' 
ps_arr['8']='10014,'' 东风雪铁龙 '',1755,C2 Cross,88,经典爱丽舍三厢,2388,全新爱丽舍,1754,新世嘉Cross,1362,新世嘉两厢,87,新世嘉三厢,94,雪铁龙C2,1735,雪铁龙C4L,937,雪铁龙C5,10075,'' 进口雪铁龙 '',1563,C''Zero,752,C3毕加索,1426,C4 Aircross,2402,Cactus,2097,Lacoste,2098,Metropolis,2099,REVOLTe,2100,Survolt,1919,Technospace,2101,Tubik,562,大C4毕加索,2102,雪铁龙C''Crosser,1910,雪铁龙C''Elysee,619,雪铁龙C1,581,雪铁龙C3,509,雪铁龙C4,1598,雪铁龙C4L(海外),515,雪铁龙C5(进口),2103,雪铁龙GQ,2104,雪铁龙GT' 
ps_arr['144']='1969,亚琛施纳泽 1系,1989,亚琛施纳泽 3系,1990,亚琛施纳泽 5系,1991,亚琛施纳泽 6系,1992,亚琛施纳泽 7系,1993,亚琛施纳泽 MINI,1994,亚琛施纳泽 X1,1995,亚琛施纳泽 X3,1996,亚琛施纳泽 X5,1997,亚琛施纳泽 X6' 
ps_arr['115']='1676,野马A''MPV,2151,野马B60X,2152,野马E,1342,野马F10,1520,野马F12,2153,野马F16,2385,野马F18,1817,野马F19,2400,野马M302,2154,野马M31D,2155,野马T系' 
ps_arr['50']='10007,'' 天津一汽 '',320,威乐,321,威志,1254,威志V2,1547,威志V2 CROSS,1540,威志V5,322,威姿,941,夏利N5,1627,夏利N7,1490,夏利两厢,319,夏利三厢,2092,一汽NH2,2093,一汽NS2,2094,一汽TFC,2095,一汽X121,10182,'' 一汽吉林 '',1647,佳宝T50,1650,佳宝T51,1649,佳宝T57,1583,佳宝V52,1584,佳宝V55,1585,佳宝V70,1903,佳宝V80,1101,森雅M80,1259,森雅S80,10273,'' 一汽通用 '',2341,坤程' 
ps_arr['81']='10024,'' 南京依维柯 '',1413,宝迪,83,得意,82,都灵,10272,'' 进口依维柯 '',2339,Campagnola,2340,Massif' 
ps_arr['74']='2086,Emerg''E,962,Essence,2087,Etherea,2416,QX60混合动力,497,英菲尼迪G系,1525,英菲尼迪JX,2088,英菲尼迪LE,2382,英菲尼迪Q30,2422,英菲尼迪Q50,2519,英菲尼迪Q50混合动力,1492,英菲尼迪Q60,1493,英菲尼迪Q60S,516,英菲尼迪Q70L,431,英菲尼迪QX50,496,英菲尼迪QX70,655,英菲尼迪QX80' 
ps_arr['35']='1938,猎鹰,759,永源A380,1758,永源五星' 
ps_arr['143']='1968,Zenvo ST1' 
ps_arr['177']='2429,之诺1E' 
ps_arr['41']='2085,中华C3,2417,中华H120,2070,中华H220,1507,中华H230,1646,中华H320,1814,中华H320 CROSS,1767,中华H330,1295,中华H530,1283,中华V5,296,中华骏捷,684,中华骏捷CROSS,298,中华骏捷FRV,1084,中华骏捷FSV,428,中华骏捷Wagon,297,中华酷宝,299,中华尊驰' 
ps_arr['93']='1209,昌铃,1926,陆地方舟,1208,旗舰A9,1203,威虎G3,1957,威虎SUV,2378,威虎TUV,1495,威虎海外版,1204,无限,2010,中兴C3,1941,中兴CP2' 
ps_arr['51']='1332,江南TT,327,众泰2008,328,众泰5008,594,众泰M300,1312,众泰T200,1313,众泰T300,1314,众泰T600,1397,众泰V10,1892,众泰Z100,1276,众泰Z200,1199,众泰Z200HB,1315,众泰Z300'
def getModel(id):
    #print id
    return (ps_arr[id]).encode('utf-8')