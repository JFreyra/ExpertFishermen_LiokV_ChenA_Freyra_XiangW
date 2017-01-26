$("#editable.li").addEventListener("click", function() {
    
}



$.post("/sessionPush", input,
        function (data, success) {
            if (!success) {
                return "Saving timer went wrong, exit anyway?";
            }
            //nothing needs to be done lmao
        }
    );