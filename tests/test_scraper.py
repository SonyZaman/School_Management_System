from scraper.scrape import scrape_books

def test_scraper_parses_books(monkeypatch):
    class DummyResponse:
        status_code = 200
        text = """
        <html><body>
        <article class="product_pod">
            <h3><a title="Book 1" href="book1.html"></a></h3>
            <p class="price_color">£10.00</p>
        </article>
        </body></html>
        """
    def fake_get(*args, **kwargs):
        return DummyResponse()

    import requests
    monkeypatch.setattr(requests, "get", fake_get)

    results = scrape_books(pages=1)
    assert len(results) == 1
    assert results[0]["title"] == "Book 1"
    assert results[0]["price_or_author"] == "£10.00"
