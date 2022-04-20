from crypt import methods
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Users, Post, Comment, Tag, Leader, Follower, Hobby
from . import db
import mysql.connector

views = Blueprint('views', __name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="440_database"
)


# Must be logged in successfully to access the home page
@views.route('/')
@views.route('/welcome')
@login_required
def welcome():
    return render_template("welcome.html", users=current_user)

# ----------------------------------- Initialize DB Method -----------------------------------------------------------------------------------
# Initialize DB Function
# CANNOT click the button twice without the deleting the rows created first on the workbench
# Since it'll reread from projectDB.sql and get dupes usernames
# So, it'll cause an error when you click it continuously
@views.route("/initializeDB", methods=['GET','POST'])
@login_required
def initializeDB():
    cursor = mydb.cursor()
    if request.method == 'POST':
        flash("Initialized the database!", category='success')

        #Open the projectDB.sql to read it, and close after
        fd = open('projectDB.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        # Add information read to the table
        sqlCommands = sqlFile.split(';')
        for command in sqlCommands:
                if command.strip() != '':
                    print(command)
                    cursor.execute(command)
                    mydb.commit()
    return render_template('initializeDB.html', users=current_user)

# ----------------------------------- Post Methods -----------------------------------------------------------------------------------------

# Main posts page view
@views.route('/post_main')
@login_required
def post_main():
    posts = Post.query.all()
    return render_template("post_main.html", users=current_user, posts=posts)

# Create new post method
@views.route("/create_post", methods=['GET', 'POST'])
@login_required
def create_post():
    # Check the number of posts per day from the user
    cursor = mydb.cursor()
    query = "SELECT COUNT(post.author) FROM post WHERE post.dateCreatedOn = current_date AND post.author = %s"
    cursor.execute(query, [current_user.id])
    numOfPosts = cursor.fetchone()[0] + 1
    mydb.commit()
    cursor.close()

    print(current_user.id)
    print(numOfPosts)

    # Show message if user is exceeding the limit of post per day
    if(numOfPosts > 2):
        flash("Already reached limit. Can only create 2 post per day!", category='error')
        return redirect(url_for('views.post_main'))
    elif request.method == "POST":
        # Get post info if everything is filled out and limit is not reached
        print()
        subject = request.form.get('subject')
        description = request.form.get('description')
        tag_list = request.form.get('tag')
        # Seperate the tags by looking for ","
        tags = tag_list.split(",")

        # Show message if subject is empty
        if not subject:
            flash('Subject field cannot be empty.', category='error')
        else:
            # Match post to user's ID
            cursor = mydb.cursor()
            query2 = "SELECT username FROM users WHERE id = %s"
            currentUser = cursor.execute(query2, [current_user.id])
            currentUser = cursor.fetchone()[0]
            print(current_user.id)
            print(currentUser)
            cursor.close()

            # Add post info to the table
            post = Post(subject=subject, description=description, createdBy=currentUser, author=current_user.id)
            db.session.add(post)
            db.session.commit()

            # Adding the tags from the post to the table
            for tag in tags:
                tags = Tag(text=tag, author=current_user.id, post_id=post.id)
                db.session.add(tags)
                db.session.commit()

            # Show message and redirect back to posts_main, after successfully created
            flash('Post created!', category='success')
            return redirect(url_for('views.post_main'))

    return render_template('create_post.html', users=current_user)


# Delete post method
@views.route('/delete-post/<id>')
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    # Cannot delete post if it wasn't created by the user
    if current_user.id != post.author:
        flash('Post belongs to another user. You do not have permission to delete it.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')

    return redirect(url_for('views.post_main'))


# This will be use to look at post from specified users
@views.route('/posts/<username>')
@login_required
def posts(username):
    users = Users.query.filter_by(username=username).first()

    if not users:
        flash('No account with the username exists.', category='error')
        return redirect(url_for('views.post_main'))
    
    posts = users.posts

    return render_template("posts.html", users=current_user, posts=posts, username=username)

# This will be use to look at post from specific tag
@views.route('tags/<text>')
@login_required
def tags(text):
    tag1 = text
    posts = Post.query.all()
    pos = []
    cursor = mydb.cursor()
    query = "SELECT DISTINCT tag.post_id FROM tag WHERE text = (%s);"
    #query = "SELECT DISTINCT post.id FROM post JOIN tag ON tag.post_id = post.id WHERE post.id IN (SELECT tag.post_id FROM tag WHERE text = (%s));"
    positiveId = cursor.execute(query, (text, ))
    positiveId = cursor.fetchall()

    if not positiveId:
        flash("No post have this tag in it.", category='error')
    else:
        for id in positiveId:
            pos.append(id[0])

    mydb.commit()
    cursor.close()

    return render_template("tags.html", users=current_user, posts=posts, pos=pos, text=text)

# ----------------------------------- Comments Methods -------------------------------------------------------------------------------------

# Create comments on other posts
@views.route("/create-comment/<post_id>", methods=['GET', 'POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')
    sentiment = request.form.get('sentiment')
    cursor = mydb.cursor()

    # Query to count the comment made on that post from the user
    query = "SELECT COUNT(comment.id) FROM comment INNER JOIN post ON comment.post_id = post.id WHERE post.id = (%s) AND comment.author = (%s)"
    cursor.execute(query, (post_id, current_user.id))
    result = cursor.fetchone()[0] + 1

    # Query to count the number of comments made by the user on the current date
    query2 = "SELECT COUNT(*) FROM comment WHERE comment.dateCreatedOn = CURRENT_DATE AND comment.author = %s"
    cursor.execute(query2, [current_user.id])
    commented_today = cursor.fetchone()[0] + 1
    
    # Query to select DISTINCT author relating to the post.id
    query3 = "SELECT DISTINCT post.author FROM post WHERE post.id = %s"
    cursor.execute(query3, [post_id])
    # Note: If the line below is giving issues, just copy, delete, and paste it
    current_author = cursor.fetchone()[0]
    mydb.commit()
    cursor.close()

    print(current_user.id)
    print(result)

    # Checks to make sure the user is not commenting on their own posts, 
    # commenting on the same post twice, or exceeds the max limit per day
    if current_user.id == current_author:
        flash('Can not comment on your own post!', category='error')
    elif result > 1:
        flash('Can not comment more than once on the same post!', category='error')
    elif commented_today > 3:
        flash('Can not comment more than 3 times per day!', category='error')
    else:
        if not text:
            flash('Comment input cannot be empty!', category='error')
        else:
            # If everything is okay, add comment to table corresponding to the post
            post = Post.query.filter_by(id = post_id)

            if post:
                comment = Comment(text=text, sentiment=sentiment, author=current_user.id, post_id=post_id)
                db.session.add(comment)
                db.session.commit()
                flash('Comment created!', category='success')
            else:
                flash('Post does not exist', category='error')

    return redirect(url_for('views.post_main'))

# Delete comment made on a post
@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Comment does not exists.', category='error')
    elif (current_user.id != comment.author) and (current_user.id != comment.post.author):
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
    
    return redirect(url_for('views.post_main'))

# ----------------------------------- Stats Methods -------------------------------------------------------------------------------------------

# Basic layout of Stats page
@views.route("/stats", methods=['GET','POST'])
@login_required
def stats():
    if request.method == 'POST':
        if "TagsCheck" in request.form:
            return redirect(url_for('views.tags_check'))
        elif "Positive" in request.form:
            return redirect(url_for('views.allPositive'))
        elif "Date" in request.form:
            return redirect(url_for('views.blog_date'))
        elif "Follow" in request.form:
            return redirect(url_for('views.following_page'))
        elif "Hobby" in request.form:
           return redirect(url_for('views.hobby_check'))
        elif "NeverBlog" in request.form:
            # Display all the users who never posted a blog
            cursor = mydb.cursor()
            query = "SELECT users.username FROM users LEFT JOIN post ON post.author = users.id WHERE post.author IS NULL;"
            result = cursor.execute(query)
            result = cursor.fetchall()
            mydb.commit()
            cursor.close()

            if not result:
                flash("No users has never posted a blog.", category='error')
            else:
                return render_template("table_usernames.html", value=result)
                #for results in result:
                #    flash(results[0], category='success')
        elif "NeverComment" in request.form:
            # Display all the users who never posted a comment
            cursor = mydb.cursor()
            query = "SELECT users.username FROM users LEFT JOIN comment ON comment.author = users.id WHERE comment.author IS NULL;"
            result = cursor.execute(query)
            result = cursor.fetchall()
            mydb.commit()
            cursor.close()

            if not result:
                flash("No users have never posted a comment!", category='error')
            else:
                return render_template("table_usernames.html", value=result)
                #for results in result:
                #    flash(results[0], category='success')
        elif "Negative" in request.form:
            # Display those users who posted some comments, but each of them are negative
            cursor = mydb.cursor()
            query = "SELECT users.username FROM users JOIN comment a ON a.author = users.id WHERE a.author NOT IN (SELECT b.author FROM comment b WHERE b.sentiment = 'positive');"
            result = cursor.execute(query)
            result = cursor.fetchall()
            mydb.commit()
            cursor.close()

            if not result:
                flash("No users only posted negative comments.", category='error')
            else:
                return render_template("table_usernames.html", value=result)
                #for results in result:
                    #flash(results[0], category='success')
        elif "noNegative" in request.form:
            # Display those users such that all the blogs they posted so far never recieved any negative comments
            cursor = mydb.cursor()
            query = "SELECT DISTINCT post.createdBy FROM post WHERE post.createdBy NOT IN (SELECT post.createdBy FROM comment RIGHT JOIN post ON comment.post_id = post.id WHERE comment.sentiment LIKE 'negative' GROUP BY post.createdBy) OR post.id = NULL;"
            result = cursor.execute(query)
            result = cursor.fetchall()
            mydb.commit()
            cursor.close()

            print(result)

            if not result:
                flash("No blogs has only have positive comments.", category='error')
            else:
                return render_template("table_usernames.html", value=result)
                #for results in result:
                #    flash(results[0], category='success')
    return render_template('stats.html', users=current_user)

# List the users who post at least two blogs, one has a tag of “X”, and another has a tag of “Y”
# Demo: Should only display EXO and Seventeen for the tags (heartbreak and calming)
@views.route("/tags_check", methods=['GET','POST'])
@login_required
def tags_check():
    if request.method == 'POST':
        tag1 = request.form.get('tag1')
        tag2 = request.form.get('tag2')
        cursor = mydb.cursor()
        query = "SELECT DISTINCT username FROM users INNER JOIN tag a ON a.author = users.id INNER JOIN tag b ON b.author = users.id WHERE (a.author = b.author AND a.text = (%s) AND b.text = (%s)) AND EXISTS (SELECT COUNT(post.author) from post WHERE post.author = users.id GROUP BY author HAVING count(*) >= 2);"
        result = cursor.execute(query, (tag1, tag2))
        result = cursor.fetchall()
        mydb.commit()
        cursor.close()
        if not result:
            flash("No users has created 2 or more posts, and use those tags in a post.", category='error')
        else:
            #for results in result:
                return render_template("table_usernames.html", value=result)
                #flash(results[0], category='success')
    return render_template("tags_check.html", users=current_user)

# List all the blogs of user X, such that all the comments are positive for these blogs
@views.route("/allPositive", methods=['GET','POST'])
@login_required
def allPositive():
    posts = Post.query.all()
    pos = []
    cursor = mydb.cursor()
    query = "SELECT post.id FROM post JOIN comment ON comment.post_id = post.id WHERE post.id IN (SELECT comment.post_id FROM comment WHERE sentiment = 'positive');"
    positiveId = cursor.execute(query)
    positiveId = cursor.fetchall()

    if not positiveId:
            flash("No post has only positive comments",  category='error')
    else:
            for id in positiveId:
                pos.append(id[0])

    mydb.commit()
    cursor.close()

    return render_template("allPositive.html", users=current_user, posts=posts, pos=pos)

# List the users who posted the most number of blogs on (YYYY-MM-DD)
# Demo requires blogs on 2022-05-01, should print Seventeen, Inspirit, and Carat
@views.route("/blog_date", methods=['GET','POST'])
@login_required
def blog_date():
    if request.method == 'POST':
        date = request.form.get('date')
        print(date)
        cursor = mydb.cursor()
        query = "SELECT myTable.createdBy FROM (SELECT COUNT(post.id) AS counted, post.createdBy, RANK() OVER(ORDER BY COUNT(post.id) DESC) AS ranked FROM post WHERE dateCreatedOn = (%s) GROUP BY post.createdBy ORDER BY ranked) AS myTable WHERE ranked = 1;"
        params = [date]
        result = cursor.execute(query, params)
        result = cursor.fetchall()
        mydb.commit()
        cursor.close()
        print(result)

        if not result:
            flash("No posts created on that day", category='error')
        else:
            return render_template("table_usernames.html", value=result)

            # Or can just display as flash messages
            #for results in result:
             #   flash(results[0], category='success')
    return render_template("blog_date.html", users=current_user)

# List the users who are followed by both X and Y
@views.route("/following_page", methods=['GET','POST'])
@login_required
def following_page():
    if request.method == 'POST':
        followerone = request.form.get('followerone')
        followertwo = request.form.get('followertwo')
        cursor = mydb.cursor()
        query = "SELECT DISTINCT leader.leaderName FROM leader JOIN follower a ON a.following = leader.leaderId JOIN follower b ON b.following = leader.leaderId WHERE (a.following = b.following AND a.followername = (%s) AND b.followername = (%s)) AND (a.followername > b.followername OR a.followername < b.followername);"
        result = cursor.execute(query, (followerone, followertwo))
        result = cursor.fetchall()
        mydb.commit()
        cursor.close()

        if not result:
            flash("No common leader!", category='error')
        else:
            return render_template("table_usernames.html", value=result)
            #for results in result:
            #    flash(results[0], category='success')
    return render_template("following_page.html", users=current_user)

# (By input) List a user pair (A, B) such that they have at least one common hobby
@views.route("/hobby", methods=['GET','POST'])
@login_required
def hobby_check():
    if request.method == 'POST':
        hobbyText = request.form.get('hobbyText')
        cursor = mydb.cursor()
        query = "SELECT DISTINCT a.username, b.username, hobbyText FROM users a INNER JOIN users b, hobby WHERE a.id IN (SELECT DISTINCT userId FROM hobby WHERE hobbyText = (%s)) AND b.id IN (SELECT DISTINCT userId FROM hobby WHERE hobbyText = (%s)) AND hobbyText = (%s) AND a.id <> b.id AND a.username > b.username ORDER BY a.username ASC;"
        result = cursor.execute(query, (hobbyText, hobbyText, hobbyText))
        result = cursor.fetchall()
        mydb.commit()
        cursor.close()

        if not result:
            flash("No users has the same hobby.", category='error')
        else:
            return render_template("table_hobby_input.html", value=result)

    return render_template("hobby.html", users=current_user)

# (Automatically) List a user pair (A, B) such that they have at least one common hobby
@views.route("/hobby_pairs")
@login_required
def hobby_pairs():
    cursor = mydb.cursor()
    query = "WITH cte AS (SELECT a.username A, b.username B, h2.hobbyText AS same_hobby FROM users a INNER JOIN users b INNER JOIN hobby h1 INNER JOIN hobby h2 ON h2.userId > h1.userId AND h2.hobbyText = h1.hobbyText WHERE a.id=h1.userId AND b.id=h2.userId GROUP BY a.username, b.username, h2.hobbyText HAVING COUNT(*) >= 1 ORDER BY a.username ASC) SELECT A, B, GROUP_CONCAT(same_hobby SEPARATOR ', ') AS Common_hobby FROM cte GROUP BY A, B;"
    result = cursor.execute(query)
    result = cursor.fetchall()
    mydb.commit()
    cursor.close()

    if not result:
        flash("No pairs.", category='error')
    else:
        return render_template("table_hobby.html", value=result)

    return render_template("hobby.html", users=current_user)

# ----------------------------------- Display Table Methods -------------------------------------------------------------------------------------------

# Basic layout of Table page
@views.route("/table_page", methods=['GET','POST'])
@login_required
def tables_display():
    if request.method == 'POST':
        if "Hobby" in request.form:
            return redirect(url_for('views.hobby_table'))
        elif "Follow" in request.form:
            return redirect(url_for('views.follower_table'))
    return render_template('table_page.html', users=current_user)

# Display Table for Hobbies
@views.route("/display_hobby", methods=['GET','POST'])
@login_required
def hobby_table():
    cursor = mydb.cursor()
    query = "SELECT hobbyText, GROUP_CONCAT(users.username separator ', ') FROM users INNER JOIN hobby WHERE users.id = hobby.userId group by hobbyText;"
    # Basic display -> query = "SELECT username, hobbyText FROM users INNER JOIN hobby where hobby.userId = users.id order by username;"
    result = cursor.execute(query)
    result = cursor.fetchall()
    mydb.commit()
    cursor.close()

    if not result:
        flash("Nothing yet.", category='error')
    else:
        return render_template("display_hobby.html", value=result)

    return render_template("display_hobby.html", users=current_user)

# Display Table for Following
@views.route("/display_follower", methods=['GET','POST'])
@login_required
def follower_table():
    cursor = mydb.cursor()
    query = "SELECT followerName, GROUP_CONCAT(users.username separator ', ') FROM users INNER JOIN follower WHERE users.id = follower.following group by followerName;"
    # Basic display -> query = "SELECT followerName AS Users, username AS Following FROM users INNER JOIN follower where follower.following = users.id order by users;"
    result = cursor.execute(query)
    result = cursor.fetchall()
    mydb.commit()
    cursor.close()

    if not result:
        flash("Nothing yet.", category='error')
    else:
        return render_template("display_follower.html", value=result)

    return render_template("display_follower.html", users=current_user)