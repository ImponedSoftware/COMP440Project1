-- Random users being added to show the intialize DB
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
INSERT INTO post(id, subject, description, dateCreatedOn, createdBy, author)
VALUES
        (2, 'Hello World!', 'Hi everyone, this is my first blog!!!', '2022-05-01', '7'),
        (3, '4')
        (4, '5'),
        (5, '2'),
        (6, '10'),
        (7, '3'),
        (8, '4'), 
        (9, '11'),
        (10, '9'),
        (11, '6')