# Drive Capacity program by Nicholas 

#Use this to design a multi-terrabyte drive.
# Note that current drives in the 8TB capacity range typically have six platters. So it's not about platter count.

#Remember to prompt for inputs! Don't just do "platters=input()"

platters = int(input("Enter number of platters: "))
surfaces = int(input("Enter number of surfaces per platter: "))
tracks = int(input("Enter number of tracks per surface: "))
sectors = int(input("Enter number of sectors per track: "))
bytes_per_sector = int(input("Enter number of bytes per sector: "))

#Calculate the size of the drive in kb (kilobytes), mb (megabytes), gb (gigabytes), and tb (terrabytes).
total_bytes = platters * surfaces * tracks * sectors * bytes_per_sector

# 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB, 1 TB = 1024 GB
kb = total_bytes / 1024
mb = kb / 1024
gb = mb / 1024
tb = gb / 1024

#Print out the smallest of these that is greater than 1.0, with one fractional digit. 
#For example, 14,333,406,112 would print out as 14.3 GB
# We check from the largest unit (TB) downward.
if tb >= 1.0:
    value = tb
    unit = "TB"
elif gb >= 1.0:
    value = gb
    unit = "GB"
elif mb >= 1.0:
    value = mb
    unit = "MB"
else:
    value = kb
    unit = "KB"

# Print the result with one decimal place which is the .1f
print(f"{value:.1f} {unit}")

