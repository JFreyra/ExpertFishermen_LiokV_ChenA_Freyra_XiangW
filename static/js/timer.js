var intervals = [];


var Interval = function (name, startTime, curTime) {
    //timer units in seconds
    this.name = name;
    this.startTime = startTime;
    if (curTime !== undefined) { //if given a curTime
        this.curTime = curTime;
    } else {
        this.curTime = startTime;
    }
};


window.onbeforeunload = function () {
    if (intervals.length == 0) { //might happen
        //just shove in a basic pomodoro lmao
        var work = new Interval("work", 25 * 60); //25 min
        var rest = new Interval("break", 5 * 60); //5 min
        intervals.push(work);
        intervals.push(rest);
    }
    
    var input = {
        name: "intervals",
        data: JSON.stringify(intervals)
    };
    
    //save the current intervals in session
    $.post("/sessionPush", input,
        function (data, success) {
            if (!success) {
                return "Saving timer went wrong, exit anyway?";
            }
            //nothing needs to be done lmao
        }
    );
};


var setupTimer = function (input_intervals) {
    var curInterval_index = -1;
    if (input_intervals !== undefined) {
        console.log(input_intervals);
        intervals = input_intervals;
        
        for (var i = 0; i < intervals.length; i++) {
            if (intervals[i].curTime != 0) {
                curInterval_index = i;
                break;
            }
        }
        if (curInterval_index == -1) { //still invalid
            resetTimer();
            curInterval_index = 0;
        }

    } else { //no intervals given
        //default pomodoro
        var work = new Interval("work", 25 * 60); //25 min
        var rest = new Interval("break", 5 * 60); //5 min
        intervals.push(work);
        intervals.push(rest);
        curInterval_index = 0;
    }

    display = document.querySelector('#time');
    setTimeout( function() {
        startTimer(curInterval_index, display);
    }, 500 );
};


var resetTimer = function () {
    for (var i = 0; i < intervals.length; i++) {
        intervals[i].curTime = intervals[i].startTime;
    } //i hope js is pass by value lmao
};


var alertMessage = function (curInterval_index) {
    var name = intervals[curInterval_index].name;
    switch (name) {
    case "work":
        alert("Get back to work!");
        break;
    case "break":
        alert("You've earned yourself a break!");
        break;
    default:
        alert("Moving onto the next interval: " + name);
    }
};


var startTimer = function (curInterval_index, display) {
    var minutes, seconds;

    setInterval(function () {
        var curInterval_time = intervals[curInterval_index].curTime;
        if (curInterval_time <= 0) {
            curInterval_index++; //assume no finished intervals later in array
            if (curInterval_index == intervals.length) { //reached the end
                alert("A new era has begun! Timer resetting...");
                resetTimer(intervals);
                curInterval_index = 0;
            }
            alertMessage(intervals, curInterval_index);
            console.log(intervals[curInterval_index]);
        }

        minutes = parseInt(curInterval_time / 60, 10);
        seconds = parseInt(curInterval_time % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;
        intervals[curInterval_index].curTime--;
    }, 1000);
}