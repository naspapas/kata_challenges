wikipediacost = 0.10
youtubecost = 0.05


def usage(wikiamount, youtubeamount):
    totalwikicost = wikiamount * wikipediacost
    totalyoutubecost = youtubeamount * youtubecost
    if totalwikicost + totalyoutubecost > 100:
        print("Too much Consumption")
    if totalyoutubecost > totalwikicost:
        print("Too much wasted time")
    else:
        print("All good")


usage(5555, 1000000)