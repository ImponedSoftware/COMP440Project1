Before Recording:
1) Drop the current 440_database on MYSQL Workbench (if any), by running the create_db.py file by itself
2) Create only ONE new user account, where username = 'comp440' and password = 'pass1234'. Since ids 2 through 11 will be taken already when we clicked the "Initialize DB" button
3) Initialize database first
4) Might need do the note on views.py, line 332 to be sure it doesn't cause issues during recording

Recording:
1) Login
2) Show each query in the Stats page
    NOTE: do not put a space after the input(s)
    a) Input tags options: (Return users that used the 2 tags in DIFFERENT posts)
        - 'healing' and 'calming' to return 'EXO'
        - 'OST' and 'calming' to return 'EXO'
        - 'pretty' and 'heartbreak' to return 'Seventeen'
        - 'pretty' and 'calming' to return 'Seventeen'
        - 'attacca' and 'heartbreak' to return 'Seventeen'
        - 'attacca' and 'calming' to return 'Seventeen'
        Any others should return a red flash message, especially 'heartbreak' and 'calming' since it is from the same post
    b) Postive Comments is self-generated
    c) Input Date: 2022-05-01 as stated in the Project PDF
        - Can try other dates after, like: '2022-05-03', '2022-04-02', '2022-03-06'
        - Some other dates should show errors, as it has not post
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
    a) Posts Tab:
        - Clicking on an username would display all posts that they have
        - Clicking on tags would display all posts with that tag
    b) Add Tab: To add input into the database
        - Add a hobby: will show error if the input has already been added by the user
        - Follow another account: check for dupes, cannot follow yourself
    c) Welcome Tab:
        - Can view own hobbies/following, and can delete each if wanted to
    d) Tables Tab:
        - Can view all the data of hobbies/following, group neatly
        - Might have to refresh page, if newest input is not displayed