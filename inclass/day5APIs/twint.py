import twint

c = twint.Config()
c.Username = "Jacob_Montg" #user name to search under
c.Links = "include" #return tweets sent by user containing links
twint.run.Search(c)

c = twint.Config()
c.Search = "medicare for all"
c.Min_likes = 5 #only return tweets that have at least 5 likes
twint.run.Search(c)

#search for up to 100 tweets by ZiyaOnis and save to a csv
c = twint.Config()
c.Username = "ZiyaOnis"
c.Limit = 100
c.Store_csv = True
c.Output = "KocPython2021/inclass/day5APIs/ziya.csv"
twint.run.Search(c)
