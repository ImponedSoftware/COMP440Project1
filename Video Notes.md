Before Recording:
1) Drop the current 440_database on MYSQL Workbench (if any), by running the create_db.py file by itself
2) Create only ONE new user account, where username = 'comp440' and password = 'pass1234'. Since ids 2 through 11 will be taken already when we clicked the "Initialize DB" button
3) Might need do the note on views.py, line 175 to be sure it doesn't cause issues during recording

Recording:
1) Login
2) Show that the post page is blank originally
3) Go to the "Initialize Database" and clicked on it ONCE only
4) Go to the post page and show that the database has been initialized 
    (should be seeing a bunch of posts, as it reads from the projectDB.sql file)
5) Create 2 random posts. 
    And show that there's an error message when we try creating the 3rd post
6) Comments on 3 different posts with different sentiments (positive/negative)
    And in between the 3 comments, show that we cannot comment on our own post and cannot comment on the same post twice, error messages
7) Show that users can view comments under each posts by clicking on the 'Show X' messages. And hiding it by clicking the same thing