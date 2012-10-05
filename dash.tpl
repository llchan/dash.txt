<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" type="text/css" href="/static/css/foundation.min.css"/>
<link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
<meta http-equiv="refresh" content="10"/>
</head>
<body>
%for category, todos in data:
    <div class="row">
        <div class="twelve columns">
            <h4>{{ category }}</h4>
        </div>
<div class="twelve columns">
<dl class="nice vertical tabs">
        %for done, t in todos:
        <!--<div class="twelve columns">-->
            %if done:
            <dd class="done">{{ t }}</dd>
            %else:
            <dd class="pending">{{ t }}</dd>
            %end
        <!--</div>-->
        %end
</dl>
</div>
    </div>
%end
</body>
</html>
