var resetTimer = function (intervals) {
    for (var i = 0; i < intervals.length; i++) {
        intervals[i].curTime = intervals[i].startTime;
    } //i hope js is pass by value lmao
}

var alertMessage = function (intervals, curInterval_index) {
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

var startTimer = function (curInterval_index, intervals, display) {
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

var setupTimer = function (intervals) {
    var parsedIntervals = [];
    var curInterval_index = -1;

    if (intervals !== undefined) {
        for (var i = 0; i < intervals.length; i++) {
            parsedIntervals.push(new Interval(intervals[i][0], intervals[i][1], intervals[i][2]));
        }

        for (var i = 0; i < parsedIntervals.length; i++) {
            if (parsedIntervals[i].curTime != 0) {
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
        parsedIntervals.push(work);
        parsedIntervals.push(rest);
        curInterval_index = 0;
    }

    display = document.querySelector('#time');
    startTimer(curInterval_index, parsedIntervals, display);
};