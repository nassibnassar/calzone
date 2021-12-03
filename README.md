Python script to generate spreadsheets for scheduling

```
$ cat sample.txt
||CET:|ET:|PT:

JAN 10|MON|16:00|10:00 a.m.|7:00 a.m.
JAN 10|MON|19:30|1:30 p.m.|10:30 a.m.
JAN 10|MON|22:00|4:00 p.m.|1:00 p.m.

JAN 11|TUE|16:00|10:00 a.m.|7:00 a.m.
JAN 11|TUE|19:30|1:30 p.m.|10:30 a.m.
JAN 11|TUE|22:00|4:00 p.m.|1:00 p.m.
```

```
$ python calzone.py sample.txt
```

![Calzone example](https://github.com/nassibnassar/calzone/blob/main/sample.png "Calzone example")
