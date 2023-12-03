class Html:
    def __init__(self):
        pass

    @property
    def prefix(self):
        string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>

        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
                           img {
                        max-width: 100%;
                        height: auto;
                    } 
                    
                    #fullscreen-overlay {
                        display: none;
                        position: fixed;
                        top: 0;
                        left: 0;
                        width: 100%;
                        height: 100%;
                        background-color: rgba(0, 0, 0, 0.9);
                        justify-content: center;
                        align-items: center;
                        z-index: 1;
                    }

                    #fullscreen-image {
                        max-width: 100%;
                        max-height: 100%;
                    } 

        .menu-toggle {
            position: fixed;
            top: 20px;
            left: 20px;
            cursor: pointer;
        }

        .bar {
            width: 30px;
            height: 3px;
            background-color: #333;
            margin: 6px 0;
        }

        .menu {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #fff;
            z-index: 1;
            overflow-y: auto; /* 添加滚动条 */
        }

        .menu ul {
            list-style: none;
            padding: 0;
            margin: 100px 0 0 0;
            text-align: center;
            max-height: calc(100% - 100px); /* 设置最大高度，超出部分会出现滚动条 */
            overflow-y: auto; /* 添加滚动条 */

        }

        .menu li {
            margin: 20px 0;
        }

        .menu a {
            text-decoration: none;
            color: #333;
            font-size: 18px;
        }

        .content {
            /* 为了让页面内容不被菜单遮挡 */
            margin-top: 25px;
            margin-left: 85px;
        }

    </style>
    <title>Card Page</title>
</head>
<body>
            <div id="fullscreen-overlay">
                <img id="fullscreen-image" src="" alt="Fullscreen Image">
            </div>
            
<div class="menu-toggle" onclick="toggleMenu()">
    <div class="bar" id="bar1"></div>
    <div class="bar" id="bar2"></div>
    <div class="bar" id="bar3"></div>
</div>

<div class="menu">
    <ul>
        """
        return string

    @property
    def medium(self):
        string = """
    </ul>
</div>

<!-- 页面内容 -->
<div class="content">
        """
        return string

    @property
    def suffix(self):
        string = """
</div>

<script>

    function toggleMenu() {
        var menu = document.querySelector('.menu');
        menu.style.display = (menu.style.display === 'none' || menu.style.display === '') ? 'block' : 'none';
    }

    function closeMenu() {
        var menu = document.querySelector('.menu');
        menu.style.display = 'none';
    }
    
    
    function showFullscreen(imageSrc) {
        // 显示全屏覆盖层
        document.getElementById('fullscreen-image').src = imageSrc;
        document.getElementById('fullscreen-overlay').style.display = 'flex';
        // 隐藏页面滚动条
        document.body.style.overflow = 'hidden';
    }

    function hideFullscreen() {
        // 隐藏全屏覆盖层
        document.getElementById('fullscreen-overlay').style.display = 'none';
        // 恢复页面滚动条
        document.body.style.overflow = 'auto';
    }

    // 点击全屏覆盖层也可以退出全屏显示
    document.getElementById('fullscreen-overlay').onclick = hideFullscreen;

    
    
</script>
</body>
</html>
        """
        return string