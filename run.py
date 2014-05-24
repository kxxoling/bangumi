#! -*- coding: utf8 -*-
from website import app
from website.models.models import Anime, ActorQuote, AnimeReview, Torrent, User


if __name__ == '__main__':
    User('kxxoling', 'https://www.google.com/accounts/o8/id?id=AItOawnbfJtiF3G0UihMZZ06LyoJjKM2L3bp4LQ',
         'kxxoling@gmail.com').create()
    Anime(u'化物语', u'化物语', finished=1, name=u'化物语').create()
    Anime(u'囮物语', u'物语系列', finished=1, name=u'物语系列').create()
    Anime(u'物语系列（二）', u'物语系列（二）', finished=1, name=u'物语系列（二）').create()
    Anime(u'虫师 续章', u'虫师 续章', finished=1, name=u'虫师 续章').create()
    assert Anime.query.count >= 4
    ActorQuote(u'好奇心就像蟑螂——随意的打听不想被人触及的秘密。让人郁闷到不行。伤脑筋的恶心虫子。', 1, actor=u'战场原黑仪').create()
    ActorQuote(u'不过，心神荡漾的荡字，是个很不错的词。你知道吗？草字头下一个汤。我觉得，这要比草字头下一个明的萌字更上一层楼。'
               u'作为次世代的敏感单词，它很受期待哟。比如、女仆荡漾、猫耳荡漾之类。', 1, actor=u'战场原黑仪').create()
    ActorQuote(u'喜欢的东西变得厌倦了，喜欢的东西变得讨厌了——这很难受吧，这很无趣吧？一般来说，十份现在的讨厌，加上过去十份的喜欢，'
               u'就会变成二十份的讨厌了吧？这种事——会让人屈服呢', 1, actor=u'战场原黑仪').create()
    ActorQuote(u'好、好厉害。没想到竟然是这么变态的……果然不愧为历哥哥……真不是盖的……不、不对，可是。这个也……', 2,
               actor=u'千石抚子').create()
    ActorQuote(u'如、如果抚子不可爱的话……月火你在那时候就不跟抚子做朋友……了吗？', 2, actor=u'千石抚子').create()
    ActorQuote(u'呀啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！', 2,
               actor=u'千石抚子').create()
    ActorQuote(u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。', 2, actor=u'千石抚子').create()
    ActorQuote(u'常有人说胖虎在剧场版中成长了，性格变好了。不过，那其实应该是用来形容大雄才对吧？', 2, actor=u'千石抚子').create()
    ActorQuote(u'嗯。这样沿着正中线用链锯之类刚好切成两半的话，阿良良木先生是否会变成两个人呢？', 3, actor=u'羽川翼').create()
    AnimeReview(u'嗯。这样沿着正中线用链锯之类刚好切成两半的话，阿良良木先生是否会变', 'http://windrunner.info/173567', 1,
                u'嗯。这样沿着正中线用链锯之类刚好切成两半的话，阿良良木先生是否会变成两个人呢？').create()
    AnimeReview(u'嗯。这样沿着正中线用链锯之类刚好切成两半的话，阿良良木先生', 'http://windrunner.info/172567', 1,
                u'嗯。这样沿着正中线用链锯之类刚好切成两半的话，阿良良木先生是否会变成两个人呢？').create()
    AnimeReview(u'这样沿着正中线用链锯之类刚好切成两半的话', 'http://windrunner.info/157567', 1,
                u'嗯。这样沿着正中线用链锯之类刚好切成两半的话，阿良良木先生是否会变成两个人呢？').create()
    AnimeReview(u'沿着正中线用链锯之类刚好切成两半的话，阿良良木先生是否会变成两个人呢？', 'http://windrunner.info/175767', 2,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'阿良良木先生是否会变成？', 'http://windrunner.info/1785676', 2,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'嗯。这样沿着正中线用链锯之类刚好切成两半的话', 'http://windrunner.info/178567', 3,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'阿良良木先生是否会变成两个人呢？', 'http://windrunner.info/175967', 3,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'http://windrunner.info/1', 'http://windrunner.info/175067', 3,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'其实应该是用来形容大雄才对吧', 'http://windrunner.info/1756567', 3,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'其实应该是用来形容大雄才对吧5', 'http://windrunner.info/1575', 3,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'其实应该是用来形容大雄才对吧', 'http://windrunner.info/567', 3,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'常有人说胖虎在剧场版中成长了，性格变好了。不过，那其实应该是用来形容大雄才对吧？'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。', 'http://windrunner.info/177', 3,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    AnimeReview(u'常有人说胖虎在剧场版中成长了', 'http://windrunner.info/1567', 3,
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。'
                u'常有人说胖虎在剧场版中成长了，性格变好了。不过，那其实应该是用来形容大雄才对吧？'
                u'对于‘我’来说，抚子的事都是与己无关的——所以，抚子不会把抚子称作‘我’。').create()
    Torrent(u'化物语', 'http://windrunner.info/13425567', 'http://windrunner.info/15hh6g7').create()
    Torrent(u'化物语', 'http://windrunner.info/15346745', 'http://windrunner.info/156f7').create()
    Torrent(u'化物语', 'http://windrunner.info/15er67', 'http://windrunner.info/15dfg67').create()
    Torrent(u'化物语', 'http://windrunner.info/1df567', 'http://windrunner.info/15g67').create()
    Torrent(u'化物语', 'http://windrunner.info/15g67', 'http://windrunner.info/15cv67').create()
    Torrent(u'化物语', 'http://windrunner.info/15s67', 'http://windrunner.info/15vrt67').create()
    Torrent(u'化物语', 'http://windrunner.info/15c67', 'http://windrunner.info/1eb567').create()
    Torrent(u'化物语', 'http://windrunner.info/156gh7', 'http://windrunner.info/1tbr567').create()
    Torrent(u'囮物语', 'http://windrunner.info/15cs67', 'http://windrunner.info/1yc567').create()
    Torrent(u'囮物语', 'http://windrunner.info/15b67', 'http://windrunner.info/15bj67').create()
    Torrent(u'囮物语', 'http://windrunner.info/15fd67', 'http://windrunner.info/1v5h67').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/15e67', 'http://windrunner.info/15vb67').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/15c67', 'http://windrunner.info/15h67b').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/15s67', 'http://windrunner.info/15bj67').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/1d5v67', 'http://windrunner.info/15xh67').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/15bc67', 'http://windrunner.info/1gb567').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/1567', 'http://windrunner.info/1mc67').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/15n67', 'http://windrunner.info/15bn6h7').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/15h67', 'http://windrunner.info/1t5x67').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/15b67', 'http://windrunner.info/1t5w67').create()
    Torrent(u'物语系列（二）', 'http://windrunner.info/1n567', 'http://windrunner.info/15g467').create()
    app.run(debug=True)