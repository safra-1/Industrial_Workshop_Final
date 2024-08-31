import datetime
from requests_html import HTMLSession
from .database import SessionLocal
from .crud import create_news
from .schemas import NewsCreate, News

def single_news_scraper(url: str):
    session = HTMLSession()
    try:
        response = session.get(url)
        response.html.render()  # This will download Chromium if not found

        publisher_website = url.split('/')[2] if len(url.split('/')) > 2 else None
        publisher = publisher_website.split('.')[-3] if publisher_website else None

        title = response.html.find('h3', first=True).text if response.html.find('h3') else None
        reporter = response.html.find('h4.font-bold.text-xl', first=True).text if response.html.find('h4.font-bold.text-xl') else None

        category_element = response.html.find('div.mb-2.flex.items-center.mb-4', first=True)
        category = category_element.find('a', first=True).text if category_element else None
        
        news_body = '\n'.join([p.text for p in response.html.find('p')])

        img_tags = response.html.find('img')
        images = [img.attrs['src'] for img in img_tags if 'src' in img.attrs]
        # response.html.render()  # This will download Chromium if not found

        
        news_datetime = datetime.datetime.now()

        print(f"Scraped news from {url}")
        print(f"Title: {title}")
        print(f"Reporter: {reporter}")
        print(f"Date: {news_datetime}")
        print(f"Category: {category}")
        print(f"Images: {images}")


        return NewsCreate(
            publisher_website=publisher_website,
            news_publisher=publisher,
            title=title,
            news_reporter=reporter,
            datetime=news_datetime,
            link=url,
            news_category=category,
            body=news_body,
            images=images,
        )
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def scrape_and_store_news(url: str, db:SessionLocal):#typing error
    #db = SessionLocal()
    news_data = single_news_scraper(url)
    #print(news_data)
    inserted_news = ""
    if news_data:
        #print(news_data)
        inserted_news = create_news(db=db, news=news_data)
    db.close()

    return inserted_news




