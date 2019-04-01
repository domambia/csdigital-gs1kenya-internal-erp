var lazyLoad=function(jsWithPath, callback) {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    if (typeof callback != 'undefined') {
      if (script.readyState) {
        script.onreadystatechange = function() {
          if (script.readyState == 'loaded' || script.readyState == 'complete') {
            callback();
          }
        }
      } else {
        script.onload = function() {
        callback();
        }
      }
    }
    script.src = jsWithPath;
    document.getElementsByTagName('head')[0].appendChild(script);
  }

  if (window.addEventListener){
    window.addEventListener("load", function(){
       lazyLoad('js/bootstrap-accessibility.min.js');
    }, false);
  }else if (window.attachEvent) {
    window.attachEvent("onload", function(){
       lazyLoad('js/bootstrap-accessibility.min.js');
    });
  }
  // lazyLoad('js/bootstrap-accessibility.min.js');