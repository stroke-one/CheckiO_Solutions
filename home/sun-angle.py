def sun_angle(time):
    time = time.split(":")
    hour = int(time[0])
    mins = int(time[1]) / 60
    time = hour+mins

    if time < 6 or time > 18:
        return "I don't see the sun!"
    else:
        return (time - 6) * 15

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")