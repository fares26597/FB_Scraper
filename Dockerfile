FROM python
WORKDIR ./Scraper
COPY ./ ./Scraper
RUN pip install -r ./Scraper/Requirements.txt
CMD uvicorn main:app --reload