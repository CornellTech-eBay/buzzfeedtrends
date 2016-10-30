## BuzzFeed Trends

This project will use BuzzFeed API to get the trending stories on BuzzFeed

### Feeds API
BuzzFeed supports access to its various sections by API
For example:
- https://www.buzzfeed.com/api/v2/feeds/trending
- https://www.buzzfeed.com/api/v2/feeds/life

The sections include:

News, Videos, Quizzes, Tasty, DIY, Animals, Audio, Big, Stories, Books, Business, Buzz, Celebrity, Entertainment, Food, Geeky, Health, LGBT, Life, Music, Parents, Podcasts, Politics, Puzzles, Reader, Rewind, Science, Sports, Style, Tech, Travel, Weddings, Weekend, World

Usage:

- (Make sure Python 3.0+ is installed)
- Clone this repo
- python BFRequest.py [sectionNum=trending, maxN=20]

Example:

- **python BFRequest.py trending** will get top 20 stories in the /trending section
- **python BFRequest.py diy 10** will get top 10 stories in the /diy section
