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
-- EXO has >=2 posts
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
        (11, 'Voice of My Heart', 'I call out without sound. I call out remembering you.', '2022-05-01', 'Inspirit', '6');