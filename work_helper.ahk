
#SingleInstance Force

#Hotstring EndChars `t


multiStr := "
(
1
{1}
2
)"

::dh::
{
    currentTime := FormatTime(A_Now, "yyyy-MM-dd hh:mm:ss")
    multiStrWithTime := Format(multiStr, currentTime)
    SendInput multiStrWithTime
    return
}


