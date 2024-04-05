# NASA Random Image Generator

API Used:
* [NASA (Astronomy Picture of the Day)](https://api.nasa.gov/)

`python nasa.py`

![example](https://i.imgur.com/4y5DqfH.png)

**Image generated** (Click for full size):

[<img src="https://i.imgur.com/NC9fFFl.png">](https://i.imgur.com/JYf8oCL.png)

Program will try to fetch the HD version of the image. If the JSON response does not contain an HD version of the image, it will fetch the standard version.

## Python program assigns "title" field in the JSON response to the "Title" field in the EXIF data:

URL: https://api.nasa.gov/planetary/apod?api_key=NASA_API_KEY&date=2023-11-10
```JSON
{
  "date": "2023-11-10",
  "explanation": "Dominated by dark matter, massive cluster of galaxies Abell 2744 is known to some as Pandora's Cluster. It lies 3.5 billion light-years away toward the constellation Sculptor. Using the galaxy cluster's enormous mass as a gravitational lens to warp spacetime and magnify even more distant objects directly behind it, astronomers have found a background galaxy, UHZ1, at a remarkable redshift of Z=10.1. That puts UHZ1 far beyond Abell 2744, at a distance of 13.2 billion light-years, seen when our universe was about 3 percent of its current age. UHZ1 is identified in the insets of this composited image combining X-rays (purple hues) from the spacebased Chandra X-ray Observatory and infrared light from the James Webb Space Telescope. The X-ray emission from UHZ1 detected in the Chandra data is the telltale signature of a growing supermassive black hole at the center of the ultra high redshift galaxy.  That makes UHZ1's growing black hole the most distant black hole ever detected in X-rays, a result that now hints at how and when the first supermassive black holes in the universe formed.",
  "hdurl": "https://apod.nasa.gov/apod/image/2311/uhz1.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "UHZ1: Distant Galaxy and Black Hole",
  "url": "https://apod.nasa.gov/apod/image/2311/uhz1_1024.jpg"
}
```

EXIF Data in Image Properties:

![EXIF Data](https://i.imgur.com/RavMPYy.png)

.env Variables:
* [NASA_API_KEY](https://api.nasa.gov/)
