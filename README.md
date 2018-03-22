采用RedisSpider爬取梨视频接口分析：
1.列表页接口：
http://www.pearvideo.com/category_loading.jsp?reqType=14&categoryId=&start=24&mrd=0.07115130200551278
http://www.pearvideo.com/category_loading.jsp?reqType=14&categoryId=&start=36&mrd=0.11231103369207251
精简后：
http://www.pearvideo.com/category_loading.jsp?reqType=14&start=36
reqType=为5得时候是资讯，为14得时候是拍客
start=36是页数为12的倍数

每条的详情：
<li class="categoryem">
            <div class="vervideo-bd">
                <a href="video_1301572" class="vervideo-lilink actplay">
                    <div class="vervideo-img" >
                        <div class="verimg-view"><div  class="img" style="background-image: url(http://image2.pearvideo.com/cont/20180318/cont-1301572-11080403.jpg);"></div></div>
                        <div class="cm-duration">01:03</div>
                        </div>
                    <div class="vervideo-title">2牌友抢手机过年,销赃留实名露马脚</div>
                </a>
                <div class="actcont-auto">
                    <span class='source yc'>推荐</span><a href="author_10571419" class="author">百姓百事</a>
                                <span class="fav" data-id="1301572">22</span>
                </div>
            </div>
        </li>
2.详情页接口：video_1301572
http://www.pearvideo.com/video_1301572
响应当中提取视频地址：
<script type="text/javascript">var contId="1301572",liveStatusUrl="liveStatus.jsp",liveSta="",playSta="1",autoPlay=!1,isLiving=!1,isVrVideo=!1,hdflvUrl="",sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",srcUrl="http://video.pearvideo.com/mp4/short/20180318/cont-1301572-11709793-hd.mp4",vdoUrl=srcUrl,skinRes="//www.pearvideo.com/domain/skin",videoCDN="//video.pearvideo.com";</script>
视频地址：
http://video.pearvideo.com/mp4/short/20180318/cont-1301572-11709793-hd.mp4

3.类别：
社会热点资讯短视频_社会热点新闻-梨视频官网-Pear Video -----视频----社会
http://www.pearvideo.com/category_1
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=1&start=12&mrd=0.6455149630534462&hotContIds=1301462,1301326,1301525

财富热点资讯短视频_财富热点新闻-梨视频官网-Pear Video-----视频----生活
http://www.pearvideo.com/category_3
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=3&start=12&mrd=0.4338639270462359&hotContIds=1301713,1301517,1301529

娱乐热点资讯短视频_娱乐热点新闻-梨视频官网-Pear Video-----视频----娱乐
http://www.pearvideo.com/category_4
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=4&start=12&mrd=0.8258490388956994&hotContIds=1293531,1301486,1301459

生活热点资讯短视频_生活热点新闻-梨视频官网-Pear Video-----视频----生活
http://www.pearvideo.com/category_5
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=5&start=12&mrd=0.5582392946716315&hotContIds=1301426,1301500,1301374

美食热点资讯短视频_美食热点新闻-梨视频官网-Pear Video-----视频----生活
http://www.pearvideo.com/category_6
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=6&start=12&mrd=0.592223716747232&hotContIds=1300505,1301503,1301359

搞笑热点资讯短视频_搞笑热点新闻-梨视频官网-Pear Video-----视频----搞笑
http://www.pearvideo.com/category_7
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=7&start=12&mrd=0.7527963348955429&hotContIds=1298789,1301575,1299620

科技热点资讯短视频_科技热点新闻-梨视频官网-Pear Video-----视频----科技
http://www.pearvideo.com/category_8
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=12&mrd=0.9805378306167583&hotContIds=1299289,1300092,1298797

体育热点资讯短视频_体育热点新闻-梨视频官网-Pear Video-----视频----体育
http://www.pearvideo.com/category_9
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=12&mrd=0.5273584103396416&hotContIds=1301540,1301388,1299944

二次元热点资讯短视频_二次元热点新闻-梨视频官网-Pear Video-----视频----动漫
http://www.pearvideo.com/category_17
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=17&start=12&mrd=0.9268184815103735&hotContIds=1299931,1301458,1301512

汽车热点资讯短视频_汽车热点新闻-梨视频官网-Pear Video-----视频----生活
http://www.pearvideo.com/category_31
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=31&start=12&mrd=0.3779312996330164&hotContIds=1300661,1296506,1300306

音乐热点资讯短视频_音乐热点新闻-梨视频官网-Pear Video-----视频----音乐
http://www.pearvideo.com/category_59
http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=59&start=12&mrd=0.7271411765108191&hotContIds=1297783,1301345,1301769

最新拍客短视频-梨视频官网-Pear Video -----视频----生活
http://www.pearvideo.com/shooters
http://www.pearvideo.com/category_loading.jsp?reqType=14&categoryId=&start=36&mrd=0.11231103369207251
