# from unittest import TestCase, main
# from stg import STG
# from utils_db.insert_or_update_row import insert_or_update_row
# from db.model import VideoChannel
#
#
# class TestInsertOrUpdateRow(TestCase):
#     def test_(self):
#         insert_or_update_row(table=VideoChannel,
#                              filter_=(VideoChannel.video_id == "hi video",),
#                              data_2_save={"video_id": "hi video",
#                                           "channel_id": "hi first channel"},
#                              crud=STG.CRUD)
#
#         insert_or_update_row(table=VideoChannel,
#                              filter_=(VideoChannel.video_id == "hi video",),
#                              data_2_save={"video_id": "hi video",
#                                           "channel_id": "hi second channel"},
#                              crud=STG.CRUD)
#
#         objs = STG.CRUD.session.query(VideoChannel) \
#                        .filter(VideoChannel.channel_id == "hi first channel").all()
#
#         self.assertEqual(len(objs), 0)
#
#         objs = STG.CRUD.session.query(VideoChannel) \
#                        .filter(VideoChannel.channel_id == "hi second channel").all()
#
#         self.assertEqual(len(objs), 1)
#
#
# if __name__ == "__main__":
#     main()
