// script tag for message timeout
function timeMsg(){
      window.setTimeout("clearMsg()",5000);//10secs

    }
function clearMsg(){
    document.getElementById("hideMsg").innerHTML = null;

}
