-- Random users being added to show the intialize DB
-- Quick ID checks: Blackpink = 2, Infinite = 5, IU = 7, Carat = 10
INSERT INTO users(username, password, firstName, lastName, email) 
VALUES
        ('Blackpink', '2016', 'Jennie', 'Kim', 'solo@yg.com'),
        ('IKON','2o02','Hannie','Kim','loveScenario@yg.com'), 
        ('EXO','2012','Park','Chanyeol','power@sm.com'),
        ('Infinite', '2010', 'Sungyeol', 'Lee', 'typhoon@woollim.com'), 
        ('Inspirit', '2014', 'Myungsoo', 'Kim', 'forever@gmail.com'),
        ('IU', '2008', 'Jieun', 'Lee', 'lovePoem@edam.com'),
        ('Ueana', '2013Always1!', 'Manwol', 'Jang', 'friday@gmail.com'),
        ('Seventeen', '2013<3', 'Mingyu', 'Kim', 'goingSVT@pledis.com'), 
        ('Carat', '2017!DWC', 'Wonwoo', 'Jeon', 'bittersweet@minwon.com'), 
        ('WannaOne', '2018~!', 'Seongwoo', 'Ong', 'energetic@produce101.com');

-- Random post being added
-- Users with posts are: IU, EXO, Infinite, Blackpink, Carat, IKON, EXO, WannaOne, Seventeen, Inspirit
-- Uaer with NO posts: Ueana, and any other account created that hasn't post
-- EXO and Seventeen has >=2 posts
INSERT INTO post(id, subject, description, dateCreatedOn, createdBy, author)
VALUES
        (2, 'Lilac', 'Could this last goodbye be any more perfect? ', '2022-03-01', 'IU', '7'),
        (3, 'Stay with Me', 'The truth hidden in me.', '2022-03-06', 'EXO', '4'),
        (4, 'Walk to Remember', 'When I look back on my past self, the more I look, I have lost my way.', '2022-03-10', 'Infinite', '5'),
        (5, 'Solo', 'From now on, I am going solo.', '2022-03-14', 'Blackpink', '2'),
        (6, 'Beautiful', 'When I think about you. Whenever paradise. Paradise beautiful', '2022-03-26', 'Carat', '10'),
        (7, 'Love Scenario', 'We were in love. We met and became a memory that cannot be erased. It was a commendable melodrama.', '2022-03-31', 'IKON', '3'),
        (8, 'With You', 'If this is a dream, please let me wake up.', '2022-04-02', 'EXO', '4'), 
        (9, 'Beautiful', 'I was young, I did not know I would be like this. I thought it was a given back then.', '2022-04-26', 'WannaOne', '11'),
        (10, "Don't Wanna Cry", 'The path that used to be familiar, it is now unfamiliar. Is this the path I know? I ask myself.', '2022-05-01', 'Seventeen', '9'),
        (11, 'Voice of My Heart', 'I call out without sound. I call out remembering you.', '2022-05-01', 'Inspirit', '6'),
        (12, 'To You', 'You have placed all of the smiles in the world in my hands.', '2022-05-03', 'Seventeen', '9');

-- Random tags being added to different posts
-- Dupe Tags: 
--    'ballad' on post_id 4
--    'OST' on post_id 3, 8
--    'healing' on post_id 4, 8, 9
--    'heartbreak' and 'calming' on post_id 7, 10 (from IKON, EXO, and Seventeen)
--     Query #1 only returns EXO and Seventeen for tags: 'heartbreak' and 'calming'
INSERT INTO tag(text, author, post_id)
VALUES
        ('29', '7', '2'),
        ('calming', '4', '3'),
        ('heartbreak', '4', '3'),
        ('OST', '4', '3'),
        ('ballad', '5', '4'),
        ('healing', '5', '4'),
        ('single', '2', '5'),
        ('snowdrop', '2', '5'),
        ('new_era', '10', '6'),
        ('concert', '10', '6'),
        ('heartbreak', '3', '7'),
        ('calming', '3', '7'),
        ('OST', '4', '8'),
        ('healing', '4', '8'),
        ('healing', '11', '9'),
        ('youth', '11', '9'),
        ('farewell', '11', '9'),
        ('heartbreak', '9', '10'),
        ('calming', '9', '10'),
        ('memories', '6', '11'),
        ('pretty', '9', '12');

-- Random comments being added to different posts
-- Post_id with comments: 3, 4, 5, 7, 9, 10, 11
-- Post with only negative commemts: 3, 5, 10
-- Never commented: Blackpink, EXO, Seventeen, Carat
-- Users that only posted negative comments: 3, 6 (IKON and Inspirit)
-- Posts with NO negative comments: 2, 4, 6, 7, 9, 11 (author: IU, Infinite, Carat, IKON, WannaOne, Inspirit)
INSERT INTO comment(sentiment, text, dateCreatedOn, post_id, author)
VALUES
        ('negative', 'Is this from that drama?! What is all the hype about?', '2022-03-06', '3', '5'),
        ('negative', 'It is actually better than a lot of recent fantasy dramas.', '2022-03-26', '3', '7'),
        ('positive', 'Nice lyrics.','2022-03-12', '4', '11'),
        ('positive', 'Oh! This was a popular song a few years ago. Iconic!', '2022-04-01', '7', '7'),
        ('negative', 'I guess some people just do not know what they are missing.','2022-04-05', '3', '6'),
        ('positive', 'This is totally unrelated, but I just wanted to say I was a HUGE fan of this song~!', '2022-04-27', '9', '5'),
        ('positive', 'Have you checked out their other albums?! I believe that they would have been in the top 3.','2022-04-27', '9', '8'),
        ('negative', 'I was hoping that comeback would be more of a dance title track, not a sad song.','2022-05-02', '10', '7'),
        ('positive', 'I was expecting something else, but this is good enough.','2022-05-03', '11', '5'),
        ('negative', 'Who? Did she really stayed single though? I remembered she dated someone else soon after this was released.', '2022-04-15', '5', '3');

-- Leader tuples
INSERT INTO Leader(id, leaderName, leaderId) 
VALUES 
        ('1', 'IU', '7'),
        ('2', 'Blackpink', '2'),
        ('3', 'Infinite', '5'),
        ('4', 'Carat','10'),
        ('5', 'EXO', '4'),
        ('6', 'IU', '7'),
        ('7', 'IKON', '3'),
        ('8', 'Inspirit', '6'),
        ('9', 'Blackpink','2'),
        ('10', 'WannaOne', '11'),
        ('11', 'Infinite', '5'),
        ('12', 'Carat', '10');

-- Followers
-- IKON and Inspirit follows IU
-- EXO follows Blackpink, Infinite, and Carat
-- Infinite follows EXO
-- Seventeen follows IKON and Inspirit
-- Carat follows Blackpink and WannaOne
-- WannaOne follows Infinite and Carat
INSERT INTO Follower(id, followerName, following)
VALUES
        ('1', 'IKON','7'),
        ('2', 'EXO', '2'),
        ('3', 'EXO', '5'),
        ('4', 'EXO', '10'),
        ('5', 'Infinite', '4'),
        ('6', 'Inspirit', '7'),
        ('7', 'Seventeen', '3'), 
        ('8', 'Seventeen', '6'),
        ('9', 'Carat', '2'),
        ('10', 'Carat', '11'),
        ('11', 'WannaOne', '5'),
        ('12', 'WannaOne', '10');

-- Hobbies
-- 'knitting': IKON
-- 'dancing': EXO, Seventeen
-- 'singing': Blackpink, Infinite, Carat
-- 'drawing': EXO, Seventeen, Carat
-- 'gaming': EXO, Carat, Inspirit
-- 'swimming': Blackpink, Inspirit, IU
-- 'photography': IKON, Seventeen, Carat, Blackpink
-- Stats query: inputting 'knitting' should result nothing, while the rest has a few rows
INSERT INTO Hobby(id, hobbyText, userId)
VALUES
        ('1', 'knitting', '3'),
        ('2', 'dancing', '9'),
        ('3', 'dancing', '4'),
        ('4', 'singing', '2'),
        ('5', 'drawing', '9'),
        ('6', 'singing', '6'),
        ('7', 'gaming', '6'),
        ('8', 'gaming', '10'),
        ('9', 'drawing', '4'),
        ('10', 'gaming', '4'),
        ('11', 'drawing', '10'),
        ('12', 'swimming', '2'),
        ('13', 'swimming', '7'),
        ('14', 'swimming', '10'),
        ('15', 'photography', '3'),
        ('16', 'photography', '9'),
        ('17', 'photography', '10'),
        ('18', 'photography', '2'),
        ('19', 'singing', '10'),
        ('20', 'drawing', '3');