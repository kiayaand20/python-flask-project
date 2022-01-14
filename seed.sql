TRUNCATE TABLE MEMES;

ALTER SEQUENCE memes_id_seq RESTART WITH 1;

INSERT INTO memes(name, url, width, height, box_count) VALUES ('Drake Hotline Bling', 'https://i.imgflip.com/30b1gx.jpg', 1200, 1200, 2);
-- meme2 = Meme(name='Two Buttons', url='https://i.imgflip.com/1g8my4.jpg',
--              width=600, height=908, box_count=3)
-- meme3 = Meme(name='Distracted Boyfriend', url='https://i.imgflip.com/1ur9b0.jpg',
--              width=1200, height=800, box_count=3)
-- meme4 = Meme(name='Running Away Balloon', url='https://i.imgflip.com/261o3j.jpg',
--              width=761, height=1024, box_count=2)
-- meme5 = Meme(name='UNO Draw 25 Cards', url='https://i.imgflip.com/3lmzyx.jpg',
--              width=500, height=494, box_count=2)
-- meme6 = Meme(name='Left Exit 12 Off Ramp', url='https://i.imgflip.com/22bdq6.jpg',
--              width=804, height=767, box_count=3)
-- meme7 = Meme(name='Change My Mind', url='https://i.imgflip.com/24y43o.jpg',
--              width=482, height=361, box_count=2)
-- meme8 = Meme(name='Batman Slapping Robin', url='https://i.imgflip.com/9ehk.jpg',
--              width=400, height=387, box_count=2)
-- meme9 = Meme(name='Woman Yelling At Cat', url='https://i.imgflip.com/345v97.jpg',
--              width=680, height=438, box_count=2)
-- meme10 = Meme(name='Waiting Skeleton', url='https://i.imgflip.com/2fm6x.jpg',
--               width=298, height=403, box_count=2)