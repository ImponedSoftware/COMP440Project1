-- Random users being added to show the intialize DB
-- Quick ID checks: Blackpink = 3, Infinite = 6, IU = 8, Carat = 11
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
        (2, 'Lilac', 'Could this last goodbye be any more perfect? ', '2022-03-01', 'IU', '8'),
        (3, 'Stay with Me', 'The truth hidden in me.', '2022-03-06', 'EXO', '5'),
        (4, 'Walk to Remember', 'When I look back on my past self, the more I look, I have lost my way.', '2022-03-10', 'Infinite', '6'),
        (5, 'Solo', 'From now on, I am going solo.', '2022-03-14', 'Blackpink', '3'),
        (6, 'Beautiful', 'When I think about you. Whenever paradise. Paradise beautiful', '2022-03-26', 'Carat', '11'),
        (7, 'Love Scenario', 'We were in love. We met and became a memory that cannot be erased. It was a commendable melodrama.', '2022-03-31', 'IKON', '4'),
        (8, 'With You', 'If this is a dream, please let me wake up.', '2022-04-02', 'EXO', '5'), 
        (9, 'Beautiful', 'I was young, I did not know I would be like this. I thought it was a given back then.', '2022-04-26', 'WannaOne', '12'),
        (10, "Don't Wanna Cry", 'The path that used to be familiar, it is now unfamiliar. Is this the path I know? I ask myself.', '2022-05-01', 'Seventeen', '10'),
        (11, 'Voice of My Heart', 'I call out without sound. I call out remembering you.', '2022-05-01', 'Inspirit', '7'),
        (12, 'To You', 'You have placed all of the smiles in the world in my hands.', '2022-05-03', 'Seventeen', '10');

-- Random tags being added to different posts
-- Dupe Tags: 
--    'ballad' on post_id 4
--    'OST' on post_id 3, 8
--    'healing' on post_id 4, 8, 9
INSERT INTO tag(text, author, post_id)
VALUES
        ('29', '8', '2'),
        ('calming', '5', '3'),
        ('heartbreak', '5', '3'),
        ('OST', '5', '3'),
        ('ballad', '6', '4'),
        ('healing', '6', '4'),
        ('single', '3', '5'),
        ('snowdrop', '3', '5'),
        ('new_era', '11', '6'),
        ('concert', '11', '6'),
        ('heartbreak', '4', '7'),
        ('calming', '4', '7'),
        ('OST', '5', '8'),
        ('healing', '5', '8'),
        ('healing', '12', '9'),
        ('youth', '12', '9'),
        ('farewell', '12', '9'),
        ('heartbreak', '10', '10'),
        ('calming', '10', '10'),
        ('memories', '7', '11'),
        ('pretty', '10', '12'),
        ('attacca', '10', '12');

-- Random comments being added to different posts
-- Post_id with comments: 3, 4, 5, 7, 9, 10, 11
-- Post with only negative commemts: 3, 5, 10
-- Never commented: Blackpink, EXO, Seventeen, Carat
-- Users that only posted negative comments: 4, 7 (IKON and Inspirit)
-- Posts with NO negative comments: 2, 4, 6, 7, 9, 11 (author: IU, Infinite, Carat, IKON, WannaOne, Inspirit)
INSERT INTO comment(sentiment, text, dateCreatedOn, post_id, author)
VALUES
        ('negative', 'Is this from that drama?! What is all the hype about?', '2022-03-06', '3', '6'),
        ('negative', 'It is actually better than a lot of recent fantasy dramas.', '2022-03-26', '3', '8'),
        ('positive', 'Nice lyrics.','2022-03-12', '4', '12'),
        ('positive', 'Oh! This was a popular song a few years ago. Iconic!', '2022-04-01', '7', '8'),
        ('negative', 'I guess some people just do not know what they are missing.','2022-04-05', '3', '7'),
        ('positive', 'This is totally unrelated, but I just wanted to say I was a HUGE fan of this song~!', '2022-04-27', '9', '6'),
        ('positive', 'Have you checked out their other albums?! I believe that they would have been in the top 3.','2022-04-27', '9', '9'),
        ('negative', 'I was hoping that comeback would be more of a dance title track, not a sad song.','2022-05-02', '10', '8'),
        ('positive', 'I was expecting something else, but this is good enough.','2022-05-03', '11', '6'),
        ('negative', 'Who? Did she really stayed single though? I remembered she dated someone else soon after this was released.', '2022-04-15', '5', '4');

-- Leader tuples
INSERT INTO Leader(id, leaderName, leaderId) 
VALUES 
        ('3', 'Blackpink', '3'),
        ('4', 'IKON', '4'),
        ('5', 'EXO', '5'),
        ('6', 'Infinite', '6'),
        ('7', 'Inspirit', '7'),
        ('8', 'IU', '8'),
        ('9', 'Ueana', '9'),
        ('10', 'Seventeen', '10'),
        ('11', 'Carat', '11'),
        ('12', 'WannaOne', '12');

-- Followers
-- IKON and Inspirit follows IU
-- EXO follows Blackpink, Infinite, and Carat
-- Infinite follows EXO
-- Seventeen follows IKON and Inspirit
-- Carat follows Blackpink and WannaOne
-- WannaOne follows Infinite and Carat
INSERT INTO Follower(id, followerName, following)
VALUES
        ('1', 'IKON','8'),
        ('2', 'EXO', '3'),
        ('3', 'EXO', '6'),
        ('4', 'EXO', '11'),
        ('5', 'Infinite', '5'),
        ('6', 'Inspirit', '8'),
        ('7', 'Seventeen', '4'), 
        ('8', 'Seventeen', '7'),
        ('9', 'Carat', '3'),
        ('10', 'Carat', '12'),
        ('11', 'WannaOne', '6'),
        ('12', 'WannaOne', '11');

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
        ('1', 'knitting', '4'),
        ('2', 'dancing', '10'),
        ('3', 'dancing', '5'),
        ('4', 'singing', '3'),
        ('5', 'drawing', '10'),
        ('6', 'singing', '7'),
        ('7', 'gaming', '7'),
        ('8', 'gaming', '11'),
        ('9', 'drawing', '5'),
        ('10', 'gaming', '5'),
        ('11', 'drawing', '11'),
        ('12', 'swimming', '3'),
        ('13', 'swimming', '8'),
        ('14', 'swimming', '11'),
        ('15', 'photography', '4'),
        ('16', 'photography', '10'),
        ('17', 'photography', '11'),
        ('18', 'photography', '3'),
        ('19', 'singing', '11'),
        ('20', 'drawing', '4');