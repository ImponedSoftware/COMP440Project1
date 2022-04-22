Before Recording:
1) Drop the current 440_database on MYSQL Workbench (if any), by running the create_db.py file by itself
2) Create only ONE new user account, where username = 'comp440' and password = 'pass1234'. Since ids 2 through 11 will be taken already when we clicked the "Initialize DB" button
3) Initialize database first
4) Might need do the note on views.py, line 334 to be sure it doesn't cause issues during recording

Recording:
1) Login
2) Show each query in the Stats page
    a) Input tags: 'heartbreak' and 'calming' to return actual results. 
        Any others should return a red flash message
    b) Postive Comments is self-generated
    c) Input Date: 2022-05-01 as stated in the Project PDF
    d) Choose from any of these:
        -- EXO and WannaOne (follows Infinite and Carat)
        -- EXO and Carat (follows Blackpink)
        -- IKON and Inspirit (follows IU)
        Any others should return a red flash message
    e) Two Methods:
            Input Method can be any of these inputs:
                - singing, dancing, gaming, photography, swimming
            'Show All Possible Pairs' method is self-generated
    f) The last 4 queries are self-generated
3) Extras:
    a) Add Tab: To add input into the database
        - Add a hobby: will show error if the input has already been added by the user
        - Follow another account: check for dupes, cannot follow yourself
    b) Welcome Tab:
        - Can view own hobbies/following, and can delete each if wanted to
    c) Tables Tab:
        - Can view all the data of hobbies/following, group neatly
        - Might have to refresh page, if newest input is not displayed