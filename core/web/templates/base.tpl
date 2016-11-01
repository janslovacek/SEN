<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Required meta tags always come first -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta http-equiv="x-ua-compatible" content="ie=edge">

        <meta name="description" content="">
        <meta name="keywords" content=""/>
        <meta name="author" content="Jan Slováček, Michal Béder, Jan Paulovčák">
        <meta name="robots" content="noindex, nofollow"/>
        <link rel="shortcut icon" href="./static/img/favicon.png">

        <title>{{title}} | Weather Pi</title>

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="./static/css/bootstrap.min.css">
        <!-- Cover CSS -->
        <link rel="stylesheet" href="./static/css/cover.css">
        <!-- Custom CSS -->
        <link rel="stylesheet" href="./static/css/style.css">
    </head>

    <body>
        <div class="site-wrapper">
            <div class="site-wrapper-inner">
                <div class="cover-container">

                    <div class="masthead clearfix">
                        <div class="inner">
                            <h3 class="masthead-brand">Weather Pi</h3>
                            <nav class="nav nav-masthead">
                                <a class="nav-link {{'active' if page == 'home' else ''}}" href="./">Home</a>
                                <a class="nav-link {{'active' if page == 'weather' else ''}}" href="./weather">Current weather</a>
                                <a class="nav-link {{'active' if page == 'stats' else ''}}" href="./stats">Statistics</a>
                                <a class="nav-link {{'active' if page == 'db' else ''}}" href="./records">Records</a>
                            </nav>
                        </div>
                    </div>

                    <div class="inner cover container">
                        {{!base}}
                    </div>

                    <div class="mastfoot">
                        <div class="inner">
                            <p>Project in <a href="http://www.fit.vutbr.cz/study/course-l.php.cs?id=5976">Intelligent Sensors</a> subject, by <a href="mailto:xslova17@stud.fit.vutbr.cz">Jan Slováček</a>, <a href="mailto:xbeder00@stud.fit.vutbr.cz">Michal Béder</a> & <a href="mailto:xpaulo00@stud.fit.vutbr.cz">Ján Paulovčák</a>.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- jQuery first, then Tether, then Bootstrap JS. -->
        <script src="./static/js/jquery-3.1.1.min.js"></script>
        <script src="./static/js/tether.min.js"></script>
        <script src="./static/js/bootstrap.min.js"></script>
    </body>
</html>