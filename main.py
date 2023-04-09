# load modules
import asyncio
import json
import os

import BSAPI.beatleader as beatleader
import pandas as pd

from version import VERSION

os.environ['USER_AGENT'] = f'{VERSION} (+contact twitter/@aruru_bs discord/あるる#1137)'


async def main():

    # init
    count = 1000

    # 1. ranked playlist
    for star in range(18):

        # 1-1. total rank
        # init
        page = 0
        IDs = []
        songs = []

        while (True):

            # increment
            page += 1
            print(f'star={star:02}, page={page:03}, total')

            # get ranked maplist
            leaderboardInfoResponseResponseWithMetadata = await beatleader.get_leaderboards(page=page, count=count, type='ranked', stars_from=star-0.1, stars_to=star+1.1)

            # set songs
            if leaderboardInfoResponseResponseWithMetadata is not None:
                if (leaderboardInfoResponseResponseWithMetadata.data is not None) and (len(leaderboardInfoResponseResponseWithMetadata.data) > 0):
                    for leaderboardInfoResponse in leaderboardInfoResponseResponseWithMetadata.data:
                        if (leaderboardInfoResponse.song is not None) and (leaderboardInfoResponse.difficulty is not None):
                            if int(leaderboardInfoResponse.difficulty.stars) == star:
                                # get
                                IDs += [leaderboardInfoResponse.song.id]
                                songs += [{
                                    "songName": leaderboardInfoResponse.song.name,
                                    "levelAuthorName": leaderboardInfoResponse.song.mapper,
                                    "hash": leaderboardInfoResponse.song.hash,
                                    "levelid": f"custom_level_{leaderboardInfoResponse.song.hash}",
                                    "difficulties": [
                                        {
                                            "characteristic": leaderboardInfoResponse.difficulty.modeName,
                                            "name": leaderboardInfoResponse.difficulty.difficultyName
                                        }
                                    ]
                                }]
                else:
                    break
            else:
                break

            await asyncio.sleep(1/200)

        # del duplicated element
        slct_index = [not b for b in list(pd.Index(IDs).duplicated())]
        songs = [e for e, i in zip(songs, slct_index) if i]

        # read image
        with open(f'imgs/r{star:02}.txt', 'r') as f:
            img = f.read()

        # gen playlist
        fname = f'bl_ranked_star_{star:02}.bplist'
        playlist = {
            "customData": {
                "syncURL": f"https://github.com/jundoll/bs-bl-ranked-playlist/releases/latest/download/{fname}"
            },
            "playlistTitle": f"bl_ranked_star_{star:02}",
            "playlistAuthor": "",
            "songs": songs,
            "image": img
        }

        # save
        with open(f'out/{fname}', 'w') as f:
            json.dump(playlist, f)

        # 1-2. pass rate
        # init
        page = 0
        IDs = []
        songs = []

        while (True):

            # increment
            page += 1
            print(f'star={star:02}, page={page:03}, pass')

            # get ranked maplist
            leaderboardInfoResponseResponseWithMetadata = await beatleader.get_leaderboards(page=page, count=count, type='ranked', passrating_from=star-0.1, passrating_to=star+1.1)

            # set songs
            if leaderboardInfoResponseResponseWithMetadata is not None:
                if (leaderboardInfoResponseResponseWithMetadata.data is not None) and (len(leaderboardInfoResponseResponseWithMetadata.data) > 0):
                    for leaderboardInfoResponse in leaderboardInfoResponseResponseWithMetadata.data:
                        if (leaderboardInfoResponse.song is not None) and (leaderboardInfoResponse.difficulty is not None):
                            if int(leaderboardInfoResponse.difficulty.passRating) == star:
                                # get
                                IDs += [leaderboardInfoResponse.song.id]
                                songs += [{
                                    "songName": leaderboardInfoResponse.song.name,
                                    "levelAuthorName": leaderboardInfoResponse.song.mapper,
                                    "hash": leaderboardInfoResponse.song.hash,
                                    "levelid": f"custom_level_{leaderboardInfoResponse.song.hash}",
                                    "difficulties": [
                                        {
                                            "characteristic": leaderboardInfoResponse.difficulty.modeName,
                                            "name": leaderboardInfoResponse.difficulty.difficultyName
                                        }
                                    ]
                                }]
                else:
                    break
            else:
                break

            await asyncio.sleep(1/200)

        # del duplicated element
        slct_index = [not b for b in list(pd.Index(IDs).duplicated())]
        songs = [e for e, i in zip(songs, slct_index) if i]

        # read image
        with open(f'imgs/p{star:02}.txt', 'r') as f:
            #  img = f.read()

            # gen playlist
        fname = f'bl_ranked_pass_rate_{star:02}.bplist'
        playlist = {
            "customData": {
                "syncURL": f"https://github.com/jundoll/bs-bl-ranked-playlist/releases/latest/download/{fname}"
            },
            "playlistTitle": f"bl_ranked_pass_rate_{star:02}",
            "playlistAuthor": "",
            "songs": songs,
            "image": img
        }

        # save
        with open(f'out/{fname}', 'w') as f:
            json.dump(playlist, f)

        # 1-3. acc rate
        # init
        page = 0
        IDs = []
        songs = []

        while (True):

            # increment
            page += 1
            print(f'star={star:02}, page={page:03}, acc')

            # get ranked maplist
            leaderboardInfoResponseResponseWithMetadata = await beatleader.get_leaderboards(page=page, count=count, type='ranked', accrating_from=star-0.1, accrating_to=star+1.1)

            # set songs
            if leaderboardInfoResponseResponseWithMetadata is not None:
                if (leaderboardInfoResponseResponseWithMetadata.data is not None) and (len(leaderboardInfoResponseResponseWithMetadata.data) > 0):
                    for leaderboardInfoResponse in leaderboardInfoResponseResponseWithMetadata.data:
                        if (leaderboardInfoResponse.song is not None) and (leaderboardInfoResponse.difficulty is not None):
                            if int(leaderboardInfoResponse.difficulty.accRating) == star:
                                # get
                                IDs += [leaderboardInfoResponse.song.id]
                                songs += [{
                                    "songName": leaderboardInfoResponse.song.name,
                                    "levelAuthorName": leaderboardInfoResponse.song.mapper,
                                    "hash": leaderboardInfoResponse.song.hash,
                                    "levelid": f"custom_level_{leaderboardInfoResponse.song.hash}",
                                    "difficulties": [
                                        {
                                            "characteristic": leaderboardInfoResponse.difficulty.modeName,
                                            "name": leaderboardInfoResponse.difficulty.difficultyName
                                        }
                                    ]
                                }]
                else:
                    break
            else:
                break

            await asyncio.sleep(1/200)

        # del duplicated element
        slct_index = [not b for b in list(pd.Index(IDs).duplicated())]
        songs = [e for e, i in zip(songs, slct_index) if i]

        # read image
        with open(f'imgs/a{star:02}.txt', 'r') as f:
            img = f.read()

        # gen playlist
        fname = f'bl_ranked_acc_rate_{star:02}.bplist'
        playlist = {
            "customData": {
                "syncURL": f"https://github.com/jundoll/bs-bl-ranked-playlist/releases/latest/download/{fname}"
            },
            "playlistTitle": f"bl_ranked_acc_rate_{star:02}",
            "playlistAuthor": "",
            "songs": songs,
            "image": img
        }

        # save
        with open(f'out/{fname}', 'w') as f:
            json.dump(playlist, f)

        # 1-4. tech rate
        # init
        page = 0
        IDs = []
        songs = []

        while (True):

            # increment
            page += 1
            print(f'star={star:02}, page={page:03}, tech')

            # get ranked maplist
            leaderboardInfoResponseResponseWithMetadata = await beatleader.get_leaderboards(page=page, count=count, type='ranked', techrating_from=star-0.1, techrating_to=star+1.1)

            # set songs
            if leaderboardInfoResponseResponseWithMetadata is not None:
                if (leaderboardInfoResponseResponseWithMetadata.data is not None) and (len(leaderboardInfoResponseResponseWithMetadata.data) > 0):
                    for leaderboardInfoResponse in leaderboardInfoResponseResponseWithMetadata.data:
                        if (leaderboardInfoResponse.song is not None) and (leaderboardInfoResponse.difficulty is not None):
                            if int(leaderboardInfoResponse.difficulty.techRating) == star:
                                # get
                                IDs += [leaderboardInfoResponse.song.id]
                                songs += [{
                                    "songName": leaderboardInfoResponse.song.name,
                                    "levelAuthorName": leaderboardInfoResponse.song.mapper,
                                    "hash": leaderboardInfoResponse.song.hash,
                                    "levelid": f"custom_level_{leaderboardInfoResponse.song.hash}",
                                    "difficulties": [
                                        {
                                            "characteristic": leaderboardInfoResponse.difficulty.modeName,
                                            "name": leaderboardInfoResponse.difficulty.difficultyName
                                        }
                                    ]
                                }]
                else:
                    break
            else:
                break

            await asyncio.sleep(1/200)

        # del duplicated element
        slct_index = [not b for b in list(pd.Index(IDs).duplicated())]
        songs = [e for e, i in zip(songs, slct_index) if i]

        # read image
        with open(f'imgs/t{star:02}.txt', 'r') as f:
            img = f.read()

        # gen playlist
        fname = f'bl_ranked_tech_rate_{star:02}.bplist'
        playlist = {
            "customData": {
                "syncURL": f"https://github.com/jundoll/bs-bl-ranked-playlist/releases/latest/download/{fname}"
            },
            "playlistTitle": f"bl_ranked_tech_rate_{star:02}",
            "playlistAuthor": "",
            "songs": songs,
            "image": img
        }

        # save
        with open(f'out/{fname}', 'w') as f:
            json.dump(playlist, f)


if __name__ == '__main__':
    asyncio.run(main())
