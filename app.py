from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# 模拟数据库
posts = [
    {
        'id': 1,
        'title': '我的第一篇博客文章',
        'content': '这是我的第一篇博客文章的内容...',
        'image': 'https://example.com/image1.jpg',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'category': '生活',
        'tags': ['博客', '初次尝试']
    },
    # 可以添加更多文章...
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return '文章未找到', 404

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    results = [p for p in posts if query.lower() in p['title'].lower() or query.lower() in p['content'].lower()]
    return render_template('search.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)