from app.models import db, Pin, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, timedelta
import random


def seed_pins():
    pins = [{  # 1 board7
        "owner_id": 1,
        "image_url": 'https://i.pinimg.com/564x/e8/03/5d/e8035dc96a35982877b0827e3e9e9a2d.jpg',
        "title": 'What\'s your interior design style?',
        "description": 'What\'s your interior design style? Take my interior design quiz to find out! Do you love modern, mid century, farmhouse, traditional, rustic, glam, eclectic, or industrial? Or maybe you like a few styles...I can help you put a name to your unique decorating style!',
        "link": 'https://nadinestay.com/blog/whats-your-style-quiz',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    }, {  # 2 board7
        "owner_id": 1,
        "image_url": 'https://cdn.shopify.com/s/files/1/1033/8103/files/Istome-blog-playroom-essentials-18_2048x2048.jpg',
        "title": 'Playroom essemtials',
        "description": 'When choosing a decorating scheme for your child\'s playroom idea, the more imaginative and colourful the better. It\'s a dedicated and fun space for your children to spark and develop their little imaginations.',
        "link": 'https://istome.co.uk/blogs/news/playroom-essentials',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 3 board7
        "owner_id": 1,
        "image_url": 'https://i.pinimg.com/564x/43/35/3a/43353a88ecd2afb61d25876bcd574899.jpg',
        "title": 'Spring Tour: Part II-- Family Room — Design Loves Detail',
        "description": 'Finding your design style can be hard, but it doesn\'t have to be. Start by taking this design style quiz',
        "link": 'https://www.designlovesdetail.com/recentposts/spring-tour-part-ii-family-room/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 4 board7
        "owner_id": 1,
        "image_url": 'https://i.pinimg.com/564x/ae/77/50/ae7750f4aea424284170c9f4cd02fe28.jpg',
        "title": 'How To Create a Montessori Room-The Prepared Environment From 1 -3 Years',
        "description": 'How to Create a Montessori Children\'s Room. 4 Key Principles to keep in mind when creating a montessori room.',
        "link": 'https://fredtedandcompany.wordpress.com/2017/07/12/how-to-create-a-montessori-room-the-prepared-environment-from-1-3-years/',
        "allow_comment": False,
        "show_shopping_recommendations": True,
    },
        {  # 5 board7
        "owner_id": 1,
        "image_url": 'https://flavoreatsbucket.s3.us-west-2.amazonaws.com/pinthis_bedroom.jpeg',
        "title": '54 Simple Dining Room Wall Decor Ideas | Displate Blog',
        "description": 'Here are some great ideas to make your snack room or dining room look stunning with some simple wall decor ideas.',
        "link": 'https://blog.displate.com/dining-room-wall-decor/?epik=dj0yJnU9c04yOU42RWNqWTdPeHZtczJxUlk4NTRYUFFLSHZVRE4mcD0wJm49dTIzd1l2cDNpaS0zeF9vc1VzSzcwUSZ0PUFBQUFBR1RCN3Z3',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 6 board7
        "owner_id": 1,
        "image_url": 'https://i.pinimg.com/564x/90/0b/69/900b6958edba7d19c9b7e409080b0fb7.jpg',
        "title": 'Pumpkin Center piece',
        "description": 'Fall decor. Farmhouse wooden pumpkin centerpiece.',
        "link": 'https://blog.displate.com/dining-room-wall-decor/?epik=dj0yJnU9c04yOU42RWNqWTdPeHZtczJxUlk4NTRYUFFLSHZVRE4mcD0wJm49dTIzd1l2cDNpaS0zeF9vc1VzSzcwUSZ0PUFBQUFBR1RCN3Z3',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 7 board7
        "owner_id": 1,
        "title": 'This South London Home Has a Colorful Eclectic Pop Vibe',
        "description": 'Sophie Lopez\'s maximalist home is full of personality, personal touches, and lots of colour.',
        "image_url": 'https://i.pinimg.com/564x/47/b9/90/47b9904640217a559bec8b478a6cd55a.jpg',
        "link": 'https://www.apartmenttherapy.com/south-london-home-with-colorful-eclectic-pop-vibe-36977739?utm_source=pinterest&utm_medium=tracking&utm_campaign=inline-img-share&epik=dj0yJnU9Zk1aVmZBcHNJQVlEZE5mdExwZUFPYi1IWnRiOWg3Q1ImcD0wJm49aFNjdDR6RndDMXp4T2Jsc1FTY2pmQSZ0PUFBQUFBR1RLenFR',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 8 board7
        "owner_id": 1,
        "title": 'Watermelon Doormat - Spring Doormat - Summer Doormat - Pattern Doormat - Doormat - Home Decor - Custom Doormat - Farmhouse Decor',
        "description": '',
        "image_url": 'https://i.pinimg.com/736x/81/c1/b5/81c1b518427076865e0910719c0e1c57.jpg',
        "link": 'https://www.etsy.com/listing/776788299/watermelon-doormat-spring-doormat-summer?epik=dj0yJnU9ZFQzQTdiM3hRR2xwVEJDMENYUkV3bmktMHVCTXkwcUgmcD0wJm49NHprOENFZ2NZbExzVDdHSGs5X3Z6ZyZ0PUFBQUFBR1RLendr',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 9 board7
        "owner_id": 1,
        "title": 'Trish Bygott, Nathan Crotty and family - The Design Files | Australia\'s most popular design blog.',
        "description": 'The eclectic home of Trish Bygott, Nathan Crotty and their family in Fremantle, WA, which incorporate a 1950\'s bus and a 1970\'s caravan which function as additional rooms, expanding an otherwise modest one bedroom home to accommodate a family of 6!',
        "image_url": 'https://i.pinimg.com/564x/60/53/18/6053189f8efd0b52ce8ab7a9e441102d.jpg',
        "link": 'https://thedesignfiles.net/2013/09/fremantle-home-trish-bygott-nathan-crotty-and-family',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 10 board7
        "owner_id": 1,
        "title": '18 Amazing Small Living Room Ideas (On a Budget!)',
        "description": 'If you\'re moving into a small apartment or living in one, you need to check out these amazing small living room ideas! 18 creative and inexpensive ideas to copy immediately.',
        "image_url": 'https://i.pinimg.com/564x/c2/9b/03/c29b03b65f6955327d0da4a696f1f2f4.jpg',
        "link": 'https://malenapermentier.com/best-small-living-room-ideas-on-a-budget/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 11 board7
        "owner_id": 1,
        "title": 'OBSESSES WITH THESE AMAZON MUST HAVE IDEAS IF YOU LOVE A EARTHY & BOHO BEDROOM',
        "description": 'This post is all about boho bedrooms that are also earthy bedrooms. If you need some earthy bedroom ideas or boho bedroom decor ideas, this post has some really good ideas. Amazon must haves that are affordable for your bedroom. see it here: https://byannabellerose.com/earthy-bedroom-ideas/',
        "image_url": 'https://i.pinimg.com/564x/44/10/2b/44102beca82f10c3c6c58a8388c0f865.jpg',
        "link": 'https://byannabellerose.com/earthy-bedroom-ideas/',
        "allow_comment": False,
        "show_shopping_recommendations": True,
    },
        {  # 12 board7
        "owner_id": 1,
        "title": '19 Modern Farmhouse Master Bedrooms + 10 helpful decorating tips.',
        "description": 'Are you trying to create your perfect master bedroom on a budget? Look no further these helpful tips will help you save tons of money while decorating. Whether you want a cozy or glam bedroom you\'ll get ideas here. ',
        "image_url": 'https://i.pinimg.com/564x/e2/d8/04/e2d8042f0e07811e8d28e5857f8c2164.jpg',
        "link": 'http://www.rusticpassionbyallieblog.com/farmhousemasterbedrooms/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 13 board7
        "owner_id": 1,
        "title": 'Stores like Pottery Barn but without the price tag',
        "description": 'Stores Like Pottery Barn And Where To Shop For Affordable Home Decor',
        "image_url": 'https://i.pinimg.com/564x/d2/02/b5/d202b534c426db4421e7a1948367197f.jpg',
        "link": 'https://www.lanternlanedesigns.com/stores-like-pottery-barn/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 14 board7
        "owner_id": 1,
        "title": 'Hello from NJ and Some Spring Decor',
        "description": 'Farmhouse style kitchen with spring decor',
        "image_url": 'https://i.pinimg.com/564x/eb/9d/27/eb9d2762f1916b862daefcf45a44e1a5.jpg',
        "link": 'http://www.goldenboysandme.com/2020/04/hello-from-nj-and-some-spring-decor.html?spref=pi&m=1',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 15 board8
        "owner_id": 1,
        "title": 'Small Entryway Makeover with IKEA Shoe Storage Hack',
        "description": 'Come see how I gave our small entry a makeover with DIY trim, IKEA shoe storage ideas, and tons of hidden hallway storage.',
        "image_url": 'https://i.pinimg.com/564x/bb/0b/d8/bb0bd8ead4e68c6065fac2df52a97ff7.jpg',
        "link": 'https://thediymommy.com/small-entry-makeover-with-tons-of-hallway-storage/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 16 board8
        "owner_id": 1,
        "title": 'The Best of Ikea: Black White & Natural Pieces That Look Expensive',
        "description": 'Designer IKEA Favourites | The best black, white, natural and neutral IKEA pieces that look expensive but aren\'t. Up your home style on budget with these top IKEA picks like Stockholm, Vittsjo, Sinnerlig, Lisabo and More! Boho Chic Home on a budget!',
        "image_url": 'https://i.pinimg.com/564x/39/da/79/39da795b106e3028454676a3e096e515.jpg',
        "link": 'https://bynicolerobin.com/2020/05/15/the-best-of-ikea-black-white-natural-pieces-that-look-more-expensive-than-they-actually-are/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 17 board9
        "owner_id": 1,
        "title": '9 Best Christmas Vacation Destinations in the United States',
        "description": '9 Best Christmas Vacation Destinations in the United States',
        "image_url": 'https://i.pinimg.com/564x/73/bc/4c/73bc4c1f94e0b7ef43d6f05878e7b614.jpg',
        "link": 'https://www.tripstodiscover.com/best-christmas-vacation-destinations-in-the-united-states/?epik=dj0yJnU9a280czVuZzl5dExSa2tSVnJUa1JNN3JrSnFpQUl3MF8mcD0wJm49dE53a1VxLXlGY3BnTUlyUHlWcWltdyZ0PUFBQUFBR1RLMHhj',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 18 board9
        "owner_id": 1,
        "title": 'Best Places To Spend Christmas In The USA',
        "description": 'Planning your Christmas vacation? These are the best places in the USA to visit this Christmas! united states travel | winter travel destinations | christmas towns | christmas travel ideas | christmas getaways | travel tips | winter vacation | holiday travel',
        "image_url": 'https://i.pinimg.com/564x/8c/99/6e/8c996ef0de1ef302a1e711505f1a040b.jpg',
        "link": 'https://bellawilde.com/best-christmas-vacations-in-usa/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 19 board11
        "owner_id": 2,
        "title": 'Mind-Blowing Organization Ideas for Every Room in your Home',
        "description": 'Yep, it\'s organization time! Today I am sharing Organization Ideas for Every Room in your Home. Okay, it\'s the beginning of the year and Kon Marie has a hit show on Netflix. If you...',
        "image_url": 'https://i.pinimg.com/564x/63/d6/6f/63d66fa5f9a3fa842f143e01328b58c1.jpg',
        "link": 'https://www.atlaneandhigh.com/organization-ideas-for-every-room-in-your-home/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 20 board12
        "owner_id": 3,
        "title": 'How To Use Wallpaper In A Bathroom',
        "description": 'Read on for our top tips on getting #wallpaper in a #bathroom right, plus a little-known trade secret that will revolutionise your decorating, and allows you to use wallpaper pretty much anywhere you want!',
        "image_url": 'https://i.pinimg.com/564x/ed/05/97/ed05979b68b176e7fc0f7e5e4a543716.jpg',
        "link": 'https://www.atlaneandhigh.com/organization-ideas-for-every-room-in-your-home/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 21 board12
        "owner_id": 3,
        "title": 'Pantone Color of The Year 2021 Yellow Sage Green Pastel Hue Window Architecture Building Photography',
        "description": 'Discover more beautiful color palettes in my page',
        "image_url": 'https://i.pinimg.com/564x/a7/59/2b/a7592bfb9129e36cc8542419435cb277.jpg',
        "link": 'https://designs.ai/colors?utm_source=pinterest&utm_medium=imagepost&utm_campaign=dsasm',
        "allow_comment": False,
        "show_shopping_recommendations": True,
    },
        {  # 22 board12
        "owner_id": 3,
        "title": 'Wall paper you might like',
        "description": '',
        "image_url": 'https://i.pinimg.com/564x/17/ed/46/17ed469f1611e032c7731e668967e396.jpg',
        "link": '',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 23 board12
        "owner_id": 3,
        "title": 'Wall paper you might like',
        "description": '',
        "image_url": 'https://i.pinimg.com/564x/89/7b/e7/897be720c53fad5c1231bf3beda0f95d.jpg',
        "link": '',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 24 board14
        "owner_id": 5,
        "title": 'Strawberry Pound Cake',
        "description": 'This Strawberry Pound Cake is a one bowl treat that has a fruity and sweet glaze and satisfies that sweet tooth! It’s a great spring and summer dessert! Perfectly moist and packed with flavor..it will be a hit!',
        "image_url": 'https://i.pinimg.com/564x/31/cb/58/31cb589a6c564901bff50ab790a10673.jpg',
        "link": 'https://www.yellowblissroad.com/strawberry-pound-cake/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 25 board14
        "owner_id": 5,
        "title": 'Strawberry Oatmeal Bars',
        "description": 'The easiest, best strawberry oatmeal bars with butter crumb topping. One bowl, simple ingredients, and 100% whole grainperfect for a snack or dessert!',
        "image_url": 'https://i.pinimg.com/564x/dc/ea/41/dcea41b1eff00bd64f34762ed674cdec.jpg',
        "link": 'https://www.wellplated.com/strawberry-oatmeal-bars/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 26 board14
        "owner_id": 5,
        "title": 'What To Make With Fresh Strawberries',
        "description": 'Looking for something to make with fresh strawberries? Here are 10 easy and delicious strawberry recipes that you need to try! Lots of amazing options to choose from including breakfast, drinks, snacks and desserts. Some of these recipes are healthy, some super easy to make and all of them are incredibly delicious. The hardest part is deciding what to make first!',
        "image_url": 'https://i.pinimg.com/564x/06/8a/55/068a55e0910fbde239263d954690fcee.jpg',
        "link": 'https://www.mapleandmango.com/strawberry-recipes/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 27 board15
        "owner_id": 5,
        "title": '40 Kid-Friendly Dinner Recipes to Make This Summer',
        "description": 'Looking for quick and easy dinner recipes to make for your family this summer that won’t keep you in the hot kitchen for hours? This list has all of our family’s favorites. You’re gonna love these summer dinner ideas for kids!',
        "image_url": 'https://i.pinimg.com/564x/96/ce/7a/96ce7a69941fd3ae7db0e62f9148b2cf.jpg',
        "link": 'https://simply-well-balanced.com/summer-dinner-ideas-kids/',
        "allow_comment": False,
        "show_shopping_recommendations": True,
    },
        {  # 28 board15
        "owner_id": 5,
        "title": 'Easy Sticky Chicken Wings',
        "description": '',
        "image_url": 'https://i.pinimg.com/750x/47/92/84/479284d05b1b4c5e04d7c61ba5bd8b72.jpg',
        "link": 'https://40aprons.com/marry-me-chicken/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 29 board15
        "owner_id": 5,
        "title": 'Fresh Peach Margaritas',
        "description": 'Fresh Peach Margaritas make an incredible Summer drink!',
        "image_url": 'https://i.pinimg.com/564x/ce/54/3f/ce543fe837b4f6d47107a4740d941c5e.jpg',
        "link": 'https://bakerbynature.com/fresh-peach-margaritas/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 30 board16
        "owner_id": 6,
        "title": '9 Top Kitchen Trends In 2023',
        "description": 'This is your list of 9 kitchen trends for 2023 you want to consider. Does a new year equal new kitchen trends? “Trends” sounds like cheap, fast fashion fads, whereas your kitchen is full of permanent, expensive materials. But this list has a lot of classic elements to it that will take you through this decade.',
        "image_url": 'https://i.pinimg.com/564x/9e/75/4b/9e754bd26c0313358a445bd31cd06e13.jpg',
        "link": 'https://chrissymarieblog.com/kitchen-trends-2023',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
        {  # 31 board16
        "owner_id": 6,
        "title": '22 Dollar Tree Farmhouse DIYs For Decor with Serious Style',
        "description": 'Dollar Tree Farmhouse DIYs with Serious Style. ',
        "image_url": 'https://i.pinimg.com/564x/cb/e4/7e/cbe47eaafd6cfec5dc6183d31188f56b.jpg',
        "link": 'https://bogoten.com/dollar-store-farmhouse-diy/',
        "allow_comment": True,
        "show_shopping_recommendations": True,
    },
    ]

    today = datetime.now()
    # define the range of 2 years ago from today
    two_years_ago = today - timedelta(days=365*2)
    # generate 31 elements for 31 pins with random datetimes within the 2-year range
    randomCreatedAtDates = []
    for _ in range(31):
        created_at = datetime.fromtimestamp(random.randint(
            int(two_years_ago.timestamp()), int(today.timestamp())))
        randomCreatedAtDates.append(created_at)

    randomCreatedAtDates.sort(reverse=True)

    for i, pin in enumerate(pins):
        pin["created_at"] = randomCreatedAtDates[i]
        pin["updated_at"] = pin["created_at"]

    seed_pins = [db.session.add(Pin(**pin)) for pin in pins]
    db.session.commit()


def undo_pins():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.pins RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM pins"))

    db.session.commit()
