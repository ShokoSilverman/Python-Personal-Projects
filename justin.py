import re
import json

IMG_REG = '(images_results": )(\[((.*)([\n\t]))*\])'

response = '''{
"search_metadata": {
"id": "6287e5dd87a0ee3012060497",
"status": "Success",
"json_endpoint": "https://serpapi.com/searches/91165a70d24b0cae/6287e5dd87a0ee3012060497.json",
"created_at": "2022-05-20 19:02:53 UTC",
"processed_at": "2022-05-20 19:02:53 UTC",
"google_url": "https://www.google.com/search?q=%22coffee%22&oq=%22coffee%22&hl=en&gl=us&tbm=isch&sourceid=chrome&ie=UTF-8",
"raw_html_file": "https://serpapi.com/searches/91165a70d24b0cae/6287e5dd87a0ee3012060497.html",
"total_time_taken": 4.83
},
"search_parameters": {
"engine": "google",
"q": "\"coffee\"",
"google_domain": "google.com",
"hl": "en",
"gl": "us",
"device": "desktop",
"tbm": "isch"
},
"search_information": {
"image_results_state": "Results for exact spelling",
"query_displayed": "\"coffee\""
},
"images_results": [
{
"position": 1,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa609be60e07a7a0d7e1354186998aa2a517e21eefe921370d.jpeg",
"source": "en.wikipedia.org",
"title": "Coffee - Wikipedia",
"link": "https://en.wikipedia.org/wiki/Coffee",
"original": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_small_cup_of_coffee.JPG/1200px-A_small_cup_of_coffee.JPG",
"is_product": false
},
{
"position": 2,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0dd878275c94f959fbc1bf3bf192ac2f35.jpeg",
"source": "tastingtable.com",
"title": "20 Different Types Of Coffee Explained",
"link": "https://www.tastingtable.com/794355/different-types-of-coffee-explained/",
"original": "https://www.tastingtable.com/img/gallery/20-different-types-of-coffee-explained/intro-1646842160.jpg",
"is_product": false
},
{
"position": 3,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aaeda465a6ece8cfb1928b11ed47f7d5b4b14fd73f05ef5d8f.jpeg",
"source": "nbcnews.com",
"title": "How to tap into the health benefits of coffee",
"link": "https://www.nbcnews.com/better/lifestyle/how-tap-health-benefits-coffee-ncna1096031",
"original": "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1200-630,f_auto,q_auto:best/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p.jpg",
"is_product": false
},
{
"position": 4,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa284a29a32b353c2ec45d6a336ff14204798bec90e08550d9.jpeg",
"source": "bbcgoodfood.com",
"title": "Coffee recipes | BBC Good Food",
"link": "https://www.bbcgoodfood.com/recipes/collection/coffee-recipes",
"original": "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/flat-white-3402c4f.jpg?quality=90&resize=768,574",
"is_product": false
},
{
"position": 5,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa2e494f0551913462ffa7201699640e4ed8da12422012a727.jpeg",
"source": "tastingtable.com",
"title": "31 Coffee Brands, Ranked From Worst To Best",
"link": "https://www.tastingtable.com/718678/coffee-brands-ranked-from-worst-to-best/",
"original": "https://www.tastingtable.com/img/gallery/coffee-brands-ranked-from-worst-to-best/l-intro-1645231221.jpg",
"is_product": false
},
{
"position": 6,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aaabc356e36ddcaa4f3434b1d292e7fc146a6293852fbd780b.jpeg",
"source": "cancer.org",
"title": "Coffee and Cancer: What the Research Really Shows | American Cancer Society",
"link": "https://www.cancer.org/latest-news/coffee-and-cancer-what-the-research-really-shows.html",
"original": "https://wompampsupport.azureedge.net/fetchimage?siteId=7716&url=https%3A%2F%2Fwww.cancer.org%2Fcontent%2Fdam%2Fcancer-org%2Fimages%2Fphotographs%2Fsingle-use%2Fespresso-coffee-cup-with-beans-on-table-restricted.jpg%2Fjcr%3Acontent%2Frenditions%2Fcq5dam.web.1280.1280.jpeg",
"is_product": false
},
{
"position": 7,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa04ee7158975095e917c8bccb3e4bbda288f4bdf0053bffc5.jpeg",
"source": "cnn.com",
"title": "Is coffee healthy? | CNN",
"link": "https://www.cnn.com/2017/09/29/health/coffee-healthy-food-drayer/index.html",
"original": "https://media.cnn.com/api/v1/images/stellar/prod/150929101049-black-coffee-stock.jpg?q=x_3,y_1231,h_1684,w_2993,c_crop/w_800",
"is_product": false
},
{
"position": 8,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aaac8c361a41a917a3de59808f83c5ddd12a7cdae3435f80a6.jpeg",
"source": "inc.com",
"title": "Best News of 2021: Coffee Is Incredibly Good for You | Inc.com",
"link": "https://www.inc.com/geoffrey-james/best-news-of-2021-coffee-is-incredibly-good-for-you.html",
"original": "https://img-cdn.inc.com/image/upload/images/panoramic/getty_1025739950_ddrzvl.jpg",
"is_product": false
},
{
"position": 9,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa41a493e27b4b0045a9f2b32b5b36d44f42abb04d94ef1ba8.jpeg",
"source": "worldatlas.com",
"title": "The Top Coffee-Consuming Countries - WorldAtlas",
"link": "https://www.worldatlas.com/articles/top-10-coffee-consuming-nations.html",
"original": "https://www.worldatlas.com/r/w768/upload/12/f8/83/coffee-cup.jpg",
"is_product": false
},
{
"position": 10,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa09f7373066ee5bf68b5fd2f036825145001c8d9a74ff9214.jpeg",
"source": "eatright.org",
"title": "Benefits of Coffee",
"link": "https://www.eatright.org/health/wellness/preventing-illness/benefits-of-coffee",
"original": "https://www.eatright.org/-/media/eatrightimages/cup-of-coffee_528814833.jpg",
"is_product": false
},
{
"position": 11,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0dee5f37e59e852d2e039cb7fcf7cd0971.jpeg",
"source": "healthline.com",
"title": "Coffee and Antioxidants: Everything You Need to Know",
"link": "https://www.healthline.com/nutrition/coffee-worlds-biggest-source-of-antioxidants",
"original": "https://post.healthline.com/wp-content/uploads/2020/08/coffee-worlds-biggest-source-of-antioxidants-1296x728-feature_0-800x728.jpg",
"is_product": false
},
{
"position": 12,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0d0ca92c881031511ba7d10728a24ed001.jpeg",
"source": "theguardian.com",
"title": "Coffee bean price spike just a taste of what's to come with climate change  | Coffee | The Guardian",
"link": "https://www.theguardian.com/food/2021/sep/30/coffee-bean-price-spike-just-a-taste-of-whats-to-come-with-climate-change",
"original": "https://i.guim.co.uk/img/media/0c0498199aa53a3d7eeb6f4fe5253ec9e2db4791/0_166_4891_2934/master/4891.jpg?width=465&quality=45&auto=format&fit=max&dpr=2&s=7dc271fc95462025fa9cad83c0ce7b4e",
"is_product": false
},
{
"position": 13,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0d0022ccf6af146b401d48baf5a47e175c.jpeg",
"source": "medicalnewstoday.com",
"title": "Coffee health benefits: Diabetes, heart health, liver cancer, and more",
"link": "https://www.medicalnewstoday.com/articles/270202",
"original": "https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/270202_2200-800x1200.jpg",
"is_product": false
},
{
"position": 14,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0dbf8e1e302c3955d44898625fe4205702.jpeg",
"source": "mcdonalds.com",
"title": "Premium Roast Coffee: McCafé® Coffee with 100% Arabica Beans | McDonald's",
"link": "https://www.mcdonalds.com/us/en-us/product/coffee-small.html",
"original": "https://s7d1.scene7.com/is/image/mcdonalds/t-mcdonalds-Coffee-Medium:1-3-product-tile-desktop?wid=765&hei=472&dpr=off",
"is_product": false
},
{
"position": 15,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0dbfc9eeb0ef883bb0582534cf431604b7.jpeg",
"source": "kidney.org",
"title": "Coffee and Kidney Disease: Is it Safe? | National Kidney Foundation",
"link": "https://www.kidney.org/newsletter/coffee-and-kidney-disease",
"original": "https://www.kidney.org/sites/default/files/Coffee_LYK%20fb.jpg",
"is_product": false
},
{
"position": 16,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0df32d5dba6b7c81608d6b7857098202b8.png",
"source": "health.clevelandclinic.org",
"title": "Low-Acid Coffee Options to Try Today – Cleveland Clinic",
"link": "https://health.clevelandclinic.org/coffee-giving-you-tummy-trouble-try-these-low-acid-options/",
"original": "https://health.clevelandclinic.org/wp-content/uploads/sites/3/2017/05/CoffeeStomachPains-533906501-770x533-1.jpg",
"is_product": false
},
{
"position": 17,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0d90f40c9c76ec469ee85eb7982b159a98.jpeg",
"source": "paramountcoffee.com",
"title": "Paramount Coffee - Roasting the Finest Coffee | Paramount Coffee",
"link": "https://www.paramountcoffee.com/",
"original": "https://paramountcoffee.com/pub/media/weltpixel/owlcarouselslider/images/b/a/banner3_1.jpg",
"is_product": false
},
{
"position": 18,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0d292040bb0417bee68ba2f37c6283f35c.jpeg",
"source": "en.wikipedia.org",
"title": "Coffee bean - Wikipedia",
"link": "https://en.wikipedia.org/wiki/Coffee_bean",
"original": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Roasted_coffee_beans.jpg",
"is_product": false
},
{
"position": 19,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0db3585cd4332f6a9343fe53340a21e4ee.jpeg",
"source": "theguardian.com",
"title": "How to make the perfect coffee at home | Coffee | The Guardian",
"link": "https://www.theguardian.com/lifeandstyle/2021/jan/09/how-to-make-the-perfect-coffee-at-home",
"original": "https://i.guim.co.uk/img/media/585df8fa3efe0587e947d346b4067cc06388dac8/0_0_5000_3000/master/5000.jpg?width=465&quality=45&auto=format&fit=max&dpr=2&s=0d278c5fe8bf4b20a34f9ab79d2b031e",
"is_product": false
},
{
"position": 20,
"thumbnail": "https://serpapi.com/searches/6287e5dd87a0ee3012060497/images/994722b5007f53aa8cd12a1a35561a0db9082e984b177a50c085f069da93b702.jpeg",
"source": "dailymail.co.uk",
"title": "What your daily coffee is really doing to your body | Daily Mail Online",
"link": "https://www.dailymail.co.uk/health/article-2987126/It-good-brain-waistline-bad-bones-kidneys-daily-coffee-really-doing-body.html",
"original": "https://i.dailymail.co.uk/i/pix/scaled/2015/03/09/0C07226D00000578-0-image-a-23_1425939890281.jpg",
"is_product": false
},
{
"position": 21,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaO8NQiV61q2GJrHo2dsQ99MRhACvOdvLc2Q&usqp=CAU",
"source": "independent.co.uk",
"title": "Coffee can help you lose weight, according to a nutritionist | The  Independent | The Independent",
"link": "https://www.independent.co.uk/life-style/food-and-drink/coffee-weight-loss-healthy-nutritional-value-fat-burn-diet-metabolism-a8296946.html",
"original": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/04/09/20/istock-157528129.jpg?quality=75&width=1200&auto=webp",
"is_product": false
},
{
"position": 22,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUigYB8X6DvedbWfxerUo-L_SZEVx3JMKBiA&usqp=CAU",
"source": "thespruceeats.com",
"title": "Traditional Swedish Egg Coffee Recipe",
"link": "https://www.thespruceeats.com/egg-coffee-2952648",
"original": "https://www.thespruceeats.com/thmb/IlsUmBXjueZHSkxtmozRHdKb8YI=/5324x3993/smart/filters:no_upscale()/egg-coffee-2952648-hero-01-cee6462de89745109dc1a2bbb5473ca2.jpg",
"is_product": true
},
{
"position": 23,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu_2XF4tgO5eApCYIxiBmH3xjuqs3LhlnO3w&usqp=CAU",
"source": "allrecipes.com",
"title": "Different Types of Coffee, Roasts, and Drinks, Explained | Allrecipes",
"link": "https://www.allrecipes.com/article/types-of-coffee/",
"original": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F43%2F2020%2F08%2F20%2FGettyImages-1165807395-2000.jpg&q=60",
"is_product": false
},
{
"position": 24,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1E-OLqFiNyluW-WUnbTufDmkV9lrsTdKxlw&usqp=CAU",
"source": "lybrate.com",
"title": "Benefits of Coffee And Its Side Effects | Lybrate",
"link": "https://www.lybrate.com/topic/benefits-of-coffee-and-its-side-effects",
"original": "https://assets.lybrate.com/q_auto:eco,f_auto,w_1200,h_720,c_fill,g_auto/imgs/product/health-wiki/bpages/Benefits-Of-Coffee.jpg",
"is_product": false
},
{
"position": 25,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4toEFOPEvnIQo4WW_glVxEFEzJOYSQlA4iw&usqp=CAU",
"source": "vegrecipesofindia.com",
"title": "Hot Coffee",
"link": "https://www.vegrecipesofindia.com/hot-coffee-recipe-cafe-style/",
"original": "https://www.vegrecipesofindia.com/wp-content/uploads/2018/02/cafe-style-hot-coffee-recipe-1.jpg",
"is_product": true
},
{
"position": 26,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpTDToHx9VL8x8cXALhySYSeAFpsWfwGPrfA&usqp=CAU",
"source": "southsoundtalk.com",
"title": "Where to Sip Some Delicious Coffee in Tacoma - SouthSoundTalk",
"link": "http://www.southsoundtalk.com/2019/11/25/where-to-sip-some-delicious-coffee-in-tacoma/",
"original": "http://www.southsoundtalk.com/wp-content/uploads/2019/11/Coffee-ander-Latte-e1573143205948.jpg",
"is_product": false
},
{
"position": 27,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAdTPKl6Fm2xIxZHojm8gHiss6djZ6RISyxg&usqp=CAU",
"source": "inquirer.com",
"title": "Best coffee shops in Philly",
"link": "https://www.inquirer.com/philly-tips/best-coffee-shops-philadelphia-20210928.html",
"original": "https://www.inquirer.com/resizer/56MZH_9OQg_WMp-3vF8J23-Okac=/0x0:3899x2601/760x507/filters:format(webp)/cloudfront-us-east-1.images.arcpublishing.com/pmn/NYH73TOV2BCJRLUHKPTLG6LYHI.jpg",
"is_product": false
},
{
"position": 28,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKQENS7nz2WDZBVJPAaUwzTFQssi2qQivn2Q&usqp=CAU",
"source": "tastingtable.com",
"title": "The Best Coffee Shop In Every State",
"link": "https://www.tastingtable.com/374113/the-best-coffee-shop-in-every-state/",
"original": "https://www.tastingtable.com/img/gallery/the-best-coffee-shop-in-every-state/intro-1639519645.jpg",
"is_product": false
},
{
"position": 29,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ27kSZxFQ_ZVeSz4qN0gPTmTEmCtsHEAIm2Q&usqp=CAU",
"source": "cnn.com",
"title": "Coffee could benefit your heart and help you live longer | CNN",
"link": "https://www.cnn.com/2022/03/25/health/drinking-coffee-heart-benefits-wellness/index.html",
"original": "https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F220324162251-adult-drinking-coffee-stock.jpg",
"is_product": false
},
{
"position": 30,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRii7KU57Iq_lHoQ_Ix5NUntDscT3LMXEhZUg&usqp=CAU",
"source": "foodandwine.com",
"title": "How to Store Coffee So It Stays as Fresh as Possible | Food & Wine",
"link": "https://www.foodandwine.com/coffee/how-to-store-coffee-beans",
"original": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F9%2F2021%2F01%2F21%2Fhow-to-store-coffee-beans-FT-BLOG0121.jpg&q=60",
"is_product": false
},
{
"position": 31,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGqj2r6J1eeXu5NkMzr_zlUk2MNEB2sajEgw&usqp=CAU",
"source": "insider.com",
"title": "Drinking 4 Cups of Coffee a Day Strengthens Your Liver",
"link": "https://www.insider.com/drinking-4-cups-of-coffee-a-day-strengthens-your-liver-2021-6",
"original": "https://i.insider.com/60d223afdb3f80001848d4c4?width=700",
"is_product": false
},
{
"position": 32,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9fRRtw7dduzQDzFopBXweRkhUauURYX-wsw&usqp=CAU",
"source": "healthline.com",
"title": "8 Ways to Make Your Coffee Super Healthy",
"link": "https://www.healthline.com/nutrition/8-ways-to-make-your-coffee-super-healthy",
"original": "https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/AN_images/ways-to-make-coffee-super-healthy-1296x728-feature.jpg?w=1155&h=1528",
"is_product": false
},
{
"position": 33,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0YIIRbA4aTJPjoAaLmQpJpHy-Nu8E2EO6vA&usqp=CAU",
"source": "tasteofhome.com",
"title": "Your Ultimate Guide to Different Types of Coffee and Coffee Makers",
"link": "https://www.tasteofhome.com/article/types-of-coffee/",
"original": "https://www.tasteofhome.com/wp-content/uploads/2020/02/Types-of-Coffee-Drinks_1200X1200.jpg?fit=680,680",
"is_product": false
},
{
"position": 34,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmYqxaYDjNoMblv1cb2vNoICb0n2tjvN2Hdw&usqp=CAU",
"source": "pexels.com",
"title": "40,000+ Best Coffee Photos · 100% Free Download · Pexels Stock Photos",
"link": "https://www.pexels.com/search/coffee/",
"original": "https://images.pexels.com/photos/312418/pexels-photo-312418.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
"is_product": false
},
{
"position": 35,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFealdli0Z-qpV_NGsvoWoISu6XVG2XonGrA&usqp=CAU",
"source": "peets.com",
"title": "The Original Craft Coffee | Peet's Coffee",
"link": "https://www.peets.com/",
"original": "https://peets-shop.imgix.net/products/DSM-M_2.png?v=1645554277&auto=format,compress",
"is_product": false
},
{
"position": 36,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRviyxJI50BRp3FvPx5s8nFVPkvgwyvyN_Z3w&usqp=CAU",
"source": "verywellhealth.com",
"title": "Is Coffee Gluten-Free? (Not Always!)",
"link": "https://www.verywellhealth.com/does-coffee-contain-gluten-562352",
"original": "https://www.verywellhealth.com/thmb/7JrHdW-pjC-lcxk4wTubdF4FIRk=/2000x1500/filters:no_upscale():max_bytes(150000):strip_icc()/Coffee-OleksiyMaksymenko-58c5600c5f9b58af5cc7c009.jpg",
"is_product": false
},
{
"position": 37,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwp3f5wb3gj1A-yXSRUb82ZKfqdcIqZj5mAA&usqp=CAU",
"source": "cooking.nytimes.com",
"title": "Vietnamese Iced Coffee Recipe - NYT Cooking",
"link": "https://cooking.nytimes.com/recipes/1020268-vietnamese-iced-coffee",
"original": "https://static01.nyt.com/images/2019/06/03/dining/kc-vietnamese-iced-coffee/kc-vietnamese-iced-coffee-articleLarge.jpg",
"is_product": true
},
{
"position": 38,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtiQqp9lW4cpCeV8Q06Z6qIx2U8CTB2tJCmw&usqp=CAU",
"source": "austin.eater.com",
"title": "18 Excellent Coffee Shops in Austin",
"link": "https://austin.eater.com/maps/best-coffee-austin-cafes-patio-latte-pour-over",
"original": "https://cdn.vox-cdn.com/thumbor/YRdUE6q6yshn6oaCsp0tC5kHGXs=/0x347:1440x1498/1200x900/filters:focal(607x678:837x908)/cdn.vox-cdn.com/uploads/chorus_image/image/60125101/247812794_6637824999625754_1859052583027870136_n.41.jpg",
"is_product": false
},
{
"position": 39,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIE2P5rxqxqc2t7pSaAYNPNBL-jYc-TpH_CA&usqp=CAU",
"source": "enjoyjava.com",
"title": "How to Make Strong Coffee (Ultimate Guide to Better Coffee) - EnjoyJava",
"link": "https://enjoyjava.com/how-to-make-strong-coffee/",
"original": "https://enjoyjava.com/wp-content/uploads/2018/01/How-to-make-strong-coffee.jpg",
"is_product": false
},
{
"position": 40,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk3RGEF71iMm5kveXSkQKw28nSIIS80sK4YA&usqp=CAU",
"source": "downtownjacksonville.org",
"title": "Best Coffee in Downtown Jacksonville - Downtown Jacksonville",
"link": "https://downtownjacksonville.org/blog/best-coffee-in-downtown-jacksonville/",
"original": "https://downtownjacksonville.org/wp-content/uploads/2021/01/Ground-level-@904coffee.png",
"is_product": false
},
{
"position": 41,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj10VBDUH-RdNXQAev-IjZ9v_jlzWntHH9yQ&usqp=CAU",
"source": "healthifyme.com",
"title": "9 Unique Benefits of Coffee - HealthifyMe",
"link": "https://www.healthifyme.com/blog/web-stories/benefits-of-coffee/",
"original": "https://www.healthifyme.com/blog/wp-content/uploads/2021/12/Benefits-Of-Black-Coffee.jpg",
"is_product": false
},
{
"position": 42,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjsup_dKZBo4UwiV1b-HZDMaG8kLP8pL1yJw&usqp=CAU",
"source": "eatthis.com",
"title": "8 Coffee Shop Chains With the Best Quality Coffee In America — Eat This Not  That",
"link": "https://www.eatthis.com/news-coffee-shops-highest-quality-coffee/",
"original": "https://www.eatthis.com/wp-content/uploads/sites/4/2022/03/disposable-cup.jpg?quality=82&strip=1",
"is_product": false
},
{
"position": 43,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6aE4uARdODLz6JhQty-M2ZI8piSWGs6f8QQ&usqp=CAU",
"source": "mashed.com",
"title": "Coffee Mistakes You're Probably Making At Home",
"link": "https://www.mashed.com/226589/coffee-mistakes-youre-probably-making-at-home/",
"original": "https://www.mashed.com/img/gallery/coffee-mistakes-youre-probably-making-at-home/intro-1594766282.jpg",
"is_product": false
},
{
"position": 44,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN00vuJgJ70vy-BbSMICNqZGV877Y94I0EgQ&usqp=CAU",
"source": "rush.edu",
"title": "Health Benefits of Coffee | Rush System",
"link": "https://www.rush.edu/news/health-benefits-coffee",
"original": "https://www.rush.edu/sites/default/files/media-images/coffee-cup-with-beans-og.jpg",
"is_product": false
},
{
"position": 45,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-qV7pjmgmrpEIpjE7kG38_4Rak1Zs9ngQUQ&usqp=CAU",
"source": "unisa.edu.au",
"title": "Déjà brew? Another shot for lovers of coffee. - News and events -  University of South Australia",
"link": "https://www.unisa.edu.au/Media-Centre/Releases/2021/deja-brew-another-shot-for-lovers-of-coffee/",
"original": "https://unisa.edu.au/siteassets/media-centre/images/heart-coffee---shutterstock_512503885_web.jpg",
"is_product": false
},
{
"position": 46,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_-QIl3MvFXKIj20PhZicilTL2J8YQ0QP3Ug&usqp=CAU",
"source": "craves.everybodyshops.com",
"title": "Coffee 101: The differences among coffeehouse drinks - EverybodyCraves",
"link": "https://craves.everybodyshops.com/coffee-101-the-major-differences-between-macchiatos-cappuccinos-lattes-and-more/",
"original": "https://craves.everybodyshops.com/wp-content/uploads/Coffee-101-The-major-differences-between-macchiatos-cappuccinos-lattes-and-more.jpg",
"is_product": false
},
{
"position": 47,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR54BKkevv5GKhFIQX9hpe6dEWdSyaigwfxtg&usqp=CAU",
"source": "starbucks.com",
"title": "Starbucks Coffee Company",
"link": "https://www.starbucks.com/",
"original": "https://content-prod-live.cert.starbucks.com/binary/v2/asset/137-78062.jpg",
"is_product": false
},
{
"position": 48,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTieTj2JC3mHGpRqM25S2vjfLQ9Ih_nZWAPag&usqp=CAU",
"source": "bbcgoodfood.com",
"title": "Is coffee good for you?",
"link": "https://www.bbcgoodfood.com/howto/guide/health-benefits-coffee",
"original": "https://images.immediate.co.uk/production/volatile/sites/30/2017/07/GettyImages-1204189958-fb4b98b.jpg",
"is_product": false
},
{
"position": 49,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8jNpOdCf4_JNAhPjzwMfOzHznHXH4Ilq4hw&usqp=CAU",
"source": "thewoksoflife.com",
"title": "How to Make Vietnamese Coffee - The Woks of Life",
"link": "https://thewoksoflife.com/how-to-make-vietnamese-coffee/",
"original": "https://thewoksoflife.com/wp-content/uploads/2017/12/vietnamese-coffee-7.jpg",
"is_product": true
},
{
"position": 50,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6xXhCismhwZJ9_leI8SUpv9qbIOo8KQknAg&usqp=CAU",
"source": "hattiesburgamerican.com",
"title": "National Coffee Day: Fives places to get caffeinated in Hattiesburg",
"link": "https://www.hattiesburgamerican.com/story/life/2021/09/28/national-coffee-day-fives-places-get-caffeinated-hattiesburg/5901214001/",
"original": "https://www.gannett-cdn.com/presto/2021/09/28/USAT/56a8b2da-de99-4373-86d2-fa38d0ebc833-National_Coffee_Day_2021_deals.jpg?crop=4779,2689,x0,y0&width=3200&height=1801&format=pjpg&auto=webp",
"is_product": false
},
{
"position": 51,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1yoR525-n2sfD6bio4L3zNa5NSEVw6NDNTg&usqp=CAU",
"source": "morethanmeatandpotatoes.com",
"title": "Dark Chocolate Coffee - More Than Meat And Potatoes",
"link": "https://morethanmeatandpotatoes.com/dark-chocolate-coffee/",
"original": "https://morethanmeatandpotatoes.com/wp-content/uploads/2020/10/Dark-Chocolate-Coffee-Featured-Image-720x720.jpg",
"is_product": true
},
{
"position": 52,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZDIhfX35bbcMvLLv5bIQFMxjTcYMNdwG_SQ&usqp=CAU",
"source": "myfox8.com",
"title": "Drinking coffee could lead to heart disease — depending on how you brew  your beans | FOX8 WGHP",
"link": "https://myfox8.com/news/health/drinking-coffee-could-lead-to-heart-disease-depending-on-how-you-brew-your-beans/",
"original": "https://myfox8.com/wp-content/uploads/sites/17/2022/05/coffee.jpg",
"is_product": false
},
{
"position": 53,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTCdlml7NDOIZOh2kYqWynpernPXLn6-26ag&usqp=CAU",
"source": "food52.com",
"title": "Best Magical Coffee Recipe - How to Make Homemade Cold-Brew Coffee",
"link": "https://food52.com/recipes/2018-magical-coffee",
"original": "https://images.food52.com/ZKDbtmqzR0-DSu7Y_kHZz_lDF7A=/1200x900/bed2a564-d6c0-4c6b-a241-3971228053a0--2021-0413_magical-coffee_3x2_julia-gartland_063.jpg",
"is_product": true
},
{
"position": 54,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt-_ua8uug6IA-MBtArp7Dar0976Ot9ZLtVg&usqp=CAU",
"source": "newfoodmagazine.com",
"title": "Single origin coffee: What is it and why are consumers opting for it?",
"link": "https://www.newfoodmagazine.com/article/161957/single-origin-coffee-what-is-it-and-why-are-consumers-opting-for-it/",
"original": "https://www.newfoodmagazine.com/wp-content/uploads/shutterstock_1424702054-750x500.jpg",
"is_product": false
},
{
"position": 55,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQgKRZ3cgeYbVsDzYoENP4-HFVOghHKN8EMw&usqp=CAU",
"source": "inc.com",
"title": "A Massive New Study of 347,077 People Just Revealed Exactly How Much Coffee  You Should Drink Each Day. (Before the Health Dangers Outweigh the  Benefits) | Inc.com",
"link": "https://www.inc.com/bill-murphy-jr/a-massive-new-study-of-347077-people-just-revealed-exactly-how-much-coffee-you-should-drink-each-day-before-health-dangers-outweigh-benefits.html",
"original": "https://www.incimages.com/uploaded_files/image/1920x1080/getty_938993594_391384.jpg",
"is_product": false
},
{
"position": 56,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDbV7dwYXT2s-j-9pCdRFYth46lYnT_T9E3Q&usqp=CAU",
"source": "scientificamerican.com",
"title": "Brewing a Great Cup of Coffee Depends on Chemistry and Physics - Scientific  American",
"link": "https://www.scientificamerican.com/article/brewing-a-great-cup-of-coffee-depends-on-chemistry-and-physics/",
"original": "https://static.scientificamerican.com/sciam/cache/file/4A9B64B5-4625-4635-848AF1CD534EBC1A.jpg",
"is_product": false
},
{
"position": 57,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP4igjBQLPiZcHzpxzGoMxjiYpQSM363Z_uA&usqp=CAU",
"source": "comunicaffe.com",
"title": "Isic analysis reveals top ten most-searched health topics on coffee",
"link": "https://www.comunicaffe.com/isic-analysis-reveals-the-top-ten-searches-on-coffee-and-health/",
"original": "https://www.comunicaffe.com/wp-content/uploads/2015/12/coffee-cup.jpg",
"is_product": false
},
{
"position": 58,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVcdtWH-by3Op2kO12b-IbVVcgq8h35kE7xg&usqp=CAU",
"source": "southernshorescoffee.com",
"title": "Coffee | Gulf Shores, AL | Southern Shores Coffee",
"link": "https://www.southernshorescoffee.com/",
"original": "https://lirp.cdn-website.com/d6de1443/dms3rep/multi/opt/182717746-307w.png",
"is_product": false
},
{
"position": 59,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJJdvEjTf5tgHr7tMReRlZmsTJWbBarHogBA&usqp=CAU",
"source": "britannica.com",
"title": "How Is Coffee Decaffeinated? | Britannica",
"link": "https://www.britannica.com/story/how-is-coffee-decaffeinated",
"original": "https://cdn.britannica.com/83/138783-050-AB5CDAE4/Coffee-beans-roasting.jpg?q=60",
"is_product": false
},
{
"position": 60,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9hma3DlwFO0Yl-2cuAUil_I0SEyFNqJICvQ&usqp=CAU",
"source": "onemedical.com",
"title": "10 healthy reasons to drink coffee | One Medical",
"link": "https://www.onemedical.com/blog/newsworthy/10-healthy-reasons-to-drink-coffee-2/",
"original": "https://www.onemedical.com/media/images/47579045_ckeSjj1.original.jpg",
"is_product": false
},
{
"position": 61,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAh7tz_i5p2_60zPDSC_Air2ZMrBEZQ3o3RA&usqp=CAU",
"source": "ny.eater.com",
"title": "27 Essential NYC Coffee Shops",
"link": "https://ny.eater.com/maps/best-cafe-coffee-shop-new-york-city-brooklyn-queens",
"original": "https://cdn.vox-cdn.com/thumbor/lsgIEqjDuvYzUnoDheU6FbLrEbE=/0x0:2048x1365/1200x900/filters:focal(861x520:1187x846)/cdn.vox-cdn.com/uploads/chorus_image/image/59779955/Interlude.73.jpeg",
"is_product": false
},
{
"position": 62,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVroAwY5T6FKrwm93ruLlWDI7DpnvprTnhtg&usqp=CAU",
"source": "goodhousekeeping.com",
"title": "How to Make Espresso at Home — With or Without a Machine",
"link": "https://www.goodhousekeeping.com/food-recipes/cooking/a35952377/how-to-make-espresso/",
"original": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/how-to-make-espresso-1617301390.png",
"is_product": true
},
{
"position": 63,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfuw8ndaG5jqItfTeV89iPsaZbmvp315e1kw&usqp=CAU",
"source": "sciencealert.com",
"title": "Drinking 6 Cups of Coffee a Day? Your Brain May Pay For It Later, Says a  Large Study",
"link": "https://www.sciencealert.com/largest-study-of-its-kind-says-too-much-coffee-could-harm-your-brain-in-the-long-run",
"original": "https://www.sciencealert.com/images/2021-07/processed/cup-of-coffee_1024.jpg",
"is_product": false
},
{
"position": 64,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh4NRxwgeC6ndJ7BCjdNhYp-J-6rv4T9hf7A&usqp=CAU",
"source": "osfhealthcare.org",
"title": "Coffee craze: the good and bad of coffee | OSF HealthCare",
"link": "https://www.osfhealthcare.org/blog/coffee-craze-the-good-and-bad-of-coffee/",
"original": "https://www.osfhealthcare.org/blog/wp-content/uploads/2022/04/shutterstock_2147822373-1-1.jpg",
"is_product": false
},
{
"position": 65,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT08hgnENH_CxQSRaDsTIDmUy2wa-Amalky_A&usqp=CAU",
"source": "cariboucoffee.com",
"title": "Caribou Coffee® | Life Is Short. Stay Awake For It®",
"link": "https://www.cariboucoffee.com/",
"original": "https://www.cariboucoffee.com/wp-content/uploads/2022/05/coffee-thumbnail-2.jpg",
"is_product": false
},
{
"position": 66,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUGmCjcRlGcEyyr-QRLWLkEeyP8vSFAe7cDw&usqp=CAU",
"source": "nytimes.com",
"title": "The Health Benefits of Coffee - The New York Times",
"link": "https://www.nytimes.com/2021/06/14/well/eat/coffee-health-benefits.html",
"original": "https://static01.nyt.com/images/2021/06/15/science/14sci-brody-coffee/14sci-brody-coffee-superJumbo.jpg",
"is_product": false
},
{
"position": 67,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0u_eLJRtH05Qxr2mEh2k5Pj6DPBWYndq2qg&usqp=CAU",
"source": "peets.com",
"title": "The Original Craft Coffee | Peet's Coffee",
"link": "https://www.peets.com/",
"original": "https://peets-shop.imgix.net/products/SLW-M_2.png?v=1645824637&auto=format,compress",
"is_product": false
},
{
"position": 68,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7ULSkJnhTWoy4LPF74nCr3lLvGou72YMlDQ&usqp=CAU",
"source": "liquor.com",
"title": "Irish Coffee Cocktail Recipe",
"link": "https://www.liquor.com/recipes/irish-coffee-2/",
"original": "https://www.liquor.com/thmb/G8wGMU8PzJKVZEy0AA5QC-eaFDo=/720x720/filters:fill(auto,1)/__opt__aboutcom__coeus__resources__content_migration__liquor__2017__02__22140200__irish-coffee-720x720-recipe1-b1ddbe38da014bdb9c21cb2b6fcc629f.jpg",
"is_product": true
},
{
"position": 69,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC8LGVfJlTHvGDO6X9qzv9JgHhaWyIDvEVQA&usqp=CAU",
"source": "condesacoffee.com",
"title": "Condesa Coffee",
"link": "http://www.condesacoffee.com/",
"original": "http://static1.squarespace.com/static/564f9de1e4b08f0af88460e4/t/5bbc1b6353450aa93b8eee1b/1539055186795/DSCF3703.jpg?format=1500w",
"is_product": false
},
{
"position": 70,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQintr58qo223N73PjDOAD3k0tcqFAaLwHafg&usqp=CAU",
"source": "bonappetit.com",
"title": "Coffee Crème Caramel Recipe | Bon Appétit",
"link": "https://www.bonappetit.com/recipe/coffee-creme-caramel",
"original": "https://assets.bonappetit.com/photos/5c5de7c033a51d5ba1cac9a5/4:3/w_3331,h_2498,c_limit/Coffee-Cre%CC%80me-Caramel.jpg",
"is_product": true
},
{
"position": 71,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGayCLGUjVplzwHvNRKwgdB2F3diLcerlYBg&usqp=CAU",
"source": "epicurious.com",
"title": "The Best Coffee Makers 2022: Top Drip Coffee Machines, Espresso Machines,  French Press, Pour Over, and Cold Brew Pitchers | Epicurious",
"link": "https://www.epicurious.com/expert-advice/best-coffee-makers-article",
"original": "https://assets.epicurious.com/photos/616d9d2b78e846f58dd4597a/9:4/w_6812,h_3027,c_limit/BestCoffeeMaker_HERO_101321_077.jpg",
"is_product": false
},
{
"position": 72,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ19WNFWuy7t8hrmorO3ueGSSVWTw33J2gZJg&usqp=CAU",
"source": "thespruceeats.com",
"title": "Easy Instant Hot Cocoa Coffee Recipe",
"link": "https://www.thespruceeats.com/instant-hot-cocoa-coffee-recipe-765340",
"original": "https://www.thespruceeats.com/thmb/hOLhvfHPoK10WHdlTxNk54I9CEI=/1000x1000/smart/filters:no_upscale()/instant-hot-cocoa-coffee-recipe-765340-hero-01-049e4bb694844b38acbcab24c2c17358.jpg",
"is_product": true
},
{
"position": 73,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROi8Bl4PkEBuvo6IRcfFDHjp-VMf44NY_RMw&usqp=CAU",
"source": "parade.com",
"title": "31 Different Types of Coffee Drinks, All Explained",
"link": "https://parade.com/1354797/elizabethnarins/types-of-coffee/",
"original": "https://static.parade.com/wp-content/uploads/2022/03/different-types-of-coffee.jpg",
"is_product": false
},
{
"position": 74,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmcPPYQWC7Mm_AmDwBGMtSZcwx55n1SC8J1Q&usqp=CAU",
"source": "today.com",
"title": "How drinking coffee every day benefits heart health",
"link": "https://www.today.com/video/how-drinking-coffee-every-day-benefits-heart-health-136119877659",
"original": "https://media11.s-nbcnews.com/i/mpx/2704722219/2022_03/1648125770988_tdy_health_8a_torres_coffee_220324_1920x1080-2bqviy.jpg",
"is_product": true
},
{
"position": 75,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5kguZzRbRqsoNeN_9cDlV1zI64LfnrzPTdQ&usqp=CAU",
"source": "giolittideli.com",
"title": "Celebrate National Coffee Day At Giolitti Deli | Giolitti Deli",
"link": "https://www.giolittideli.com/giolitti-deli/celebrate-national-coffee-day-at-giolitti-deli/",
"original": "https://www.giolittideli.com/wp-content/uploads/2019/09/aroma-art-beverage-1251175.jpg",
"is_product": false
},
{
"position": 76,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0E1ny93Ps15cfkpfHQVObfVhAomSoxR8tXw&usqp=CAU",
"source": "hsph.harvard.edu",
"title": "Coffee | The Nutrition Source | Harvard T.H. Chan School of Public Health",
"link": "https://www.hsph.harvard.edu/nutritionsource/food-features/coffee/",
"original": "https://cdn1.sph.harvard.edu/wp-content/uploads/sites/30/2019/02/caffeine-close-up-coffee-539432.jpg",
"is_product": false
},
{
"position": 77,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1otc50mQAOdhDhJdBmRJMzn1eqQkC0JiQtQ&usqp=CAU",
"source": "huffingtonpost.co.uk",
"title": "Scientists Have Found A Curious Link Between Coffee And Cholesterol |  HuffPost UK Life",
"link": "https://www.huffingtonpost.co.uk/entry/how-the-type-of-coffee-you-drink-impacts-cholesterol_uk_627a5bdbe4b0b7c8f0899f3d",
"original": "https://img.huffingtonpost.com/asset/627a6670210000f1c3507cbe.jpeg?ops=1778_1000",
"is_product": false
},
{
"position": 78,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDYScAkl8K9YvlMTcQYbItpHjj0AcU9aq2rw&usqp=CAU",
"source": "timeout.com",
"title": "Say Coffee Co. is now open at Time Out Market Boston!",
"link": "https://www.timeout.com/boston/news/say-coffee-co-is-now-open-at-time-out-market-boston-050322",
"original": "https://media.timeout.com/images/105889065/750/422/image.jpg",
"is_product": false
},
{
"position": 79,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvXtDyEp84YxDrYPvJw0-jw2fhFI1XiOdeAw&usqp=CAU",
"source": "illy.com",
"title": "Brewed Coffee: How to Make Drip Coffee in a Coffee Maker",
"link": "https://www.illy.com/en-us/coffee/coffee-preparation/how-to-make-brewed-coffee",
"original": "https://www.illy.com/content/dam/channels/website/consumer/global/coffee/american_coffee_cup.jpg",
"is_product": true
},
{
"position": 80,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoYcV4-lXfvSXbTe35Fnz7wqS2ryi_6V2Hcg&usqp=CAU",
"source": "kickinghorsecoffee.com",
"title": "Kicking Horse Coffee | Wake Up & Kick Ass",
"link": "https://www.kickinghorsecoffee.com/",
"original": "https://cdn.sanity.io/images/0cvyr85o/us/8f11bfbbb8989887525e3cd2b9f2ecdb4d1c060f-3600x2000.jpg",
"is_product": false
},
{
"position": 81,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDZPvgporqobsWtoVGztXIsJooR0S30LcMJg&usqp=CAU",
"source": "thinkingnutrition.com.au",
"title": "Coffee and its surprising health benefits - Thinking Nutrition",
"link": "https://www.thinkingnutrition.com.au/coffee-health-benefits/",
"original": "https://i0.wp.com/www.thinkingnutrition.com.au/wp-content/uploads/2020/08/Coffee-Cup-scaled.jpg?fit=2560%2C1920&ssl=1",
"is_product": false
},
{
"position": 82,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQX6PRyws9mBc91Q5zcRIcH1G3kNmEFcqvejA&usqp=CAU",
"source": "goodhousekeeping.com",
"title": "History of Coffee - Surprising Facts About Coffee and Caffeine",
"link": "https://www.goodhousekeeping.com/health/diet-nutrition/a30303/facts-about-coffee/",
"original": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cup-of-coffee-on-colored-background-royalty-free-image-875681938-1543862983.jpg",
"is_product": false
},
{
"position": 83,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOCY8vlyc7fmULFkqoG7T3LKsvK2mJ0idZWg&usqp=CAU",
"source": "acouplecooks.com",
"title": "Breve Coffee – A Couple Cooks",
"link": "https://www.acouplecooks.com/breve-coffee/",
"original": "https://www.acouplecooks.com/wp-content/uploads/2021/09/Breve-Coffee-003.jpg",
"is_product": true
},
{
"position": 84,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQdmNrXmHOmS2BSXny98ym41z8NEigtojHxQ&usqp=CAU",
"source": "mcdonalds.com",
"title": "Iced Coffee: McCafé Flavored or Black Coffee | McDonald's",
"link": "https://www.mcdonalds.com/us/en-us/product/iced-coffee-small.html",
"original": "https://s7d1.scene7.com/is/image/mcdonalds/t-mcdonalds-Premium-Roast-Iced-Coffee-Medium:1-3-product-tile-desktop?wid=765&hei=472&dpr=off",
"is_product": true
},
{
"position": 85,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe8CMUpZ2fCPOymOYlqq0xp3Bv18GyZphS9w&usqp=CAU",
"source": "healio.com",
"title": "Drinking coffee associated with lower risk for chronic kidney disease",
"link": "https://www.healio.com/news/nephrology/20201014/drinking-coffee-associated-with-lower-risk-for-chronic-kidney-disease",
"original": "https://www.healio.com/~/media/slack-news/stock-images/fm_im/c/coffee_shutterstock.jpg",
"is_product": false
},
{
"position": 86,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsxXktRuvtCi2KxCWBwACPV3MlqrTDxDhWGA&usqp=CAU",
"source": "istockphoto.com",
"title": "iStock",
"link": "https://www.istockphoto.com/photos/coffee",
"original": "https://media.istockphoto.com/photos/cup-of-espresso-with-coffee-beans-picture-id1177900338?k=20&m=1177900338&s=612x612&w=0&h=rwLAoPzPiKdSbcdBFs4-TTt5O1Qpe0EFVY5KRqRPKmI=",
"is_product": true
},
{
"position": 87,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPZem1TJ2vMwebsOlHuW3EmGHUQoRQjhbKqw&usqp=CAU",
"source": "roastycoffee.com",
"title": "What Is An Americano?: Exploring a Coffee Classic",
"link": "https://www.roastycoffee.com/americano/",
"original": "https://www.roastycoffee.com/wp-content/uploads/photo-1514432324607-a09d9b4aefdd-720x720.jpeg",
"is_product": true
},
{
"position": 88,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwjhaGq7ITAs4f3VUgWNyWPf4vBCwgK9O-3w&usqp=CAU",
"source": "health.clevelandclinic.org",
"title": "Is Coffee Good for Your Liver? – Cleveland Clinic",
"link": "https://health.clevelandclinic.org/is-coffee-good-for-your-liver/",
"original": "https://health.clevelandclinic.org/wp-content/uploads/sites/3/2021/05/coffeeLiver-030421-ST_770x533.jpg",
"is_product": false
},
{
"position": 89,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvVGhu7t1pWXfrT6-U_p0d9_9_AA9oa5-gvA&usqp=CAU",
"source": "lacolombe.com",
"title": "La Colombe | Fresh Roasted Coffee, and the First-Ever Draft Latte – La  Colombe Coffee Roasters",
"link": "https://www.lacolombe.com/",
"original": "https://cdn.shopify.com/s/files/1/0056/4562/files/10StarterPack_Bundle_Web_CB_500x500.jpg?v=1651497198",
"is_product": true
},
{
"position": 90,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT00MOI97hlKm22GKZ1Jw7nhmzvs0GxpJPULw&usqp=CAU",
"source": "health.harvard.edu",
"title": "The latest scoop on the health benefits of coffee - Harvard Health",
"link": "https://www.health.harvard.edu/blog/the-latest-scoop-on-the-health-benefits-of-coffee-2017092512429",
"original": "https://domf5oio6qrcr.cloudfront.net/medialibrary/9263/bigstock-Coffee-Cup-Cup-Of-Coffee-1375146.jpg",
"is_product": false
},
{
"position": 91,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYsbSLnTH-a_wfgvjxyemEwhGhs0LoE5XTSA&usqp=CAU",
"source": "phys.org",
"title": "60 percent of coffee varieties face 'extinction risk'",
"link": "https://phys.org/news/2019-01-percent-coffee-varieties-extinction.html",
"original": "https://scx1.b-cdn.net/csz/news/800a/2019/globalcoffee.jpg",
"is_product": false
},
{
"position": 92,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv83VYUIdhegt4_uK70gIByGYDOSGZNaN1sA&usqp=CAU",
"source": "weaverscoffee.com",
"title": "The World's Top Coffee Consuming Nations",
"link": "https://weaverscoffee.com/blogs/blog/the-worlds-top-coffee-consuming-nations-and-how-they-take-their-cup",
"original": "https://cdn.shopify.com/s/files/1/1186/7382/files/coffee-around-the-world.jpg?v=1538683476",
"is_product": false
},
{
"position": 93,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR01_9l6JWx4Sh6cmOr3yDBIEVRnJtgvgMVCA&usqp=CAU",
"source": "perccoffee.com",
"title": "PERC COFFEE",
"link": "https://perccoffee.com/",
"original": "https://images.squarespace-cdn.com/content/v1/54d7bab5e4b06d06b3b19323/1651257178568-GAP46ENXE0ITIGIQW522/image0.jpeg?format=1500w",
"is_product": false
},
{
"position": 94,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmhVW3ZgWriw1z1-CA7jf1hPYJbuQefR1bFw&usqp=CAU",
"source": "time.com",
"title": "Is Coffee Good For You? Is Coffee Bad For You? | TIME",
"link": "https://time.com/4768860/is-coffee-good-for-you/",
"original": "https://api.time.com/wp-content/uploads/2017/05/drinking-coffee.jpg",
"is_product": false
},
{
"position": 95,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl4ghqBpPklWlpdN3a70tm2zsP-a6kmwtimA&usqp=CAU",
"source": "nypost.com",
"title": "35 gift ideas for coffee lovers on your 2021 Christmas list",
"link": "https://nypost.com/article/best-gifts-for-coffee-lovers/",
"original": "https://nypost.com/wp-content/uploads/sites/2/2021/11/best-gifts-for-coffee-lovers2.jpg?quality=75&strip=all&w=744",
"is_product": false
},
{
"position": 96,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTG_EldlXTO61yADuQ-czoRqoxb4tphcZq8pA&usqp=CAU",
"source": "townandcountrymag.com",
"title": "15+ Best Coffee Brands to Try 2022",
"link": "https://www.townandcountrymag.com/leisure/drinks/g38416612/best-coffee-brands/",
"original": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-626920549-1638559348.jpg",
"is_product": false
},
{
"position": 97,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjkaXHCVYym8Iw5DMZQd2rUrZM_NvLBEpEUw&usqp=CAU",
"source": "heb.com",
"title": "Starbucks Mocha Frappuccino Coffee Drink - Shop Coffee at H-E-B",
"link": "https://www.heb.com/product-detail/starbucks-mocha-frappuccino-coffee-drink/836123",
"original": "https://images.heb.com/is/image/HEBGrocery/000836123?fit=constrain,1&wid=800&hei=800&fmt=jpg&qlt=85,0&resMode=sharp2&op_usm=1.75,0.3,2,0",
"is_product": false
},
{
"position": 98,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6b61CNVBi57OFfU9LY6XPY9toX9Em20M-8w&usqp=CAU",
"source": "unsplash.com",
"title": "100+ Coffee Wallpapers [HD] | Download Free Images & Stock Photos On  Unsplash",
"link": "https://unsplash.com/s/photos/coffee-cup",
"original": "https://media.istockphoto.com/photos/cup-glass-of-coffee-with-smoke-and-coffee-beans-on-old-wooden-picture-id1303583671?b=1&k=20&m=1303583671&s=170667a&w=0&h=Nq5aWss-PVbEm5jDIa0nTf35qsxQH8znqtX9MAU5__A=",
"is_product": false
},
{
"position": 99,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWHvd6ipkJchp4aMHRyKujezVV3TJA1rFeTQ&usqp=CAU",
"source": "en.wikipedia.org",
"title": "Raf coffee - Wikipedia",
"link": "https://en.wikipedia.org/wiki/Raf_coffee",
"original": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Rafcoffe.jpg/220px-Rafcoffe.jpg",
"is_product": false
},
{
"position": 100,
"thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf72ZHy9aWbR6J2sXxVsb0Okc361zGs2wcVQ&usqp=CAU",
"source": "agiboo.com",
"title": "16 most interesting facts to know about coffee - Agiboo",
"link": "https://www.agiboo.com/16-interesting-facts-about-coffee/",
"original": "https://www.agiboo.com/wp-content/uploads/2018/03/mike-kenneally-tNALoIZhqVM-unsplash-1024x672.jpg",
"is_product": false
}
]
}'''

global matches
matches = re.search(IMG_REG, response, re.DOTALL).group(2)

item_num = 2

res: list = json.loads(matches)
for i in range(item_num, item_num+5):
    print(res[i]['thumbnail'])
item_num += 5

