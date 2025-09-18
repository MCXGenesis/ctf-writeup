# atadatem

> look there are data that seperated!! you should combine them!

## The challenge

Given a `hcs.png` file as follows
![hcs.png](hcs.png)

## How to solve?

At first glance, there is nothing wrong with the picture. Let's try to analyze with `exiftool`.

```zsh
➜ exiftool hcs.png        
ExifTool Version Number         : 13.25
File Name                       : hcs.png
Directory                       : .
File Size                       : 139 kB
File Modification Date/Time     : 2025:09:14 10:35:38+07:00
File Access Date/Time           : 2025:09:18 10:56:06+07:00
File Inode Change Date/Time     : 2025:09:18 10:56:01+07:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 3000
Image Height                    : 3000
Bit Depth                       : 8
Color Type                      : Palette
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Pixels Per Unit X               : 2835
Pixels Per Unit Y               : 2835
Pixel Units                     : meters
Palette                         : (Binary data 66 bytes, use -b option to extract)
Transparency                    : 0 61 142 189 221
Comment                         : UUF6NjZDdXEvb
Description                     : 2FwLy86c3B0dGg=
Title                           : Comments - Keywords - Description
Keywords                        : W9jLm5pYmV0c
Application Record Version      : 4
Image Size                      : 3000x3000
Megapixels                      : 9.0
```

We got something a bit sus on the Comment, Description, Title, and Keywords of the metadata. Let me highlight it.

```
Comment                         : UUF6NjZDdXEvb
Description                     : 2FwLy86c3B0dGg=
Title                           : Comments - Keywords - Description
Keywords                        : W9jLm5pYmV0c
```

The Title shows the pattern is: Comments -> Keywords -> Description. So, combining the pattern will return a text.

```
UUF6NjZDdXEvbW9jLm5pYmV0c2FwLy86c3B0dGg=
```

This text is most likely to be base64 encoded. So, let's decode the text using an online base64 decoder.

![](images/Pasted%20image.png)

The base64 encoded text results in a text again ...

```
QAz66Cuq/moc.nibetsap//:sptth
```

Do you notice something? The text is reversed, and it seems to be a url! Let's reverse the text again using an online text reverser.

![](images/Pasted%20image%20(2).png)

It results a url

```
https://pastebin.com/quC66zAQ
```

Let's visit the link ...

![](images/Pasted%20image%20(3).png)

There is a text ... again.

```
SENTe21ldGFkYXRhX2Nhbl9iZV91c2VmdWxfc29tZXdoZXJlX3NvbWVob3dfc29tZXRpbWV9
```

It seems it is a base64 encoded text again. So let's use the online base64 decoder again to decode the text.

![](images/Pasted%20image%20(4).png)

And it shows the flag.

## The flag
```
HCS{metadata_can_be_useful_somewhere_somehow_sometime}
```